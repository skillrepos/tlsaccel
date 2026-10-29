#!/usr/bin/env python3
"""
Leader demo agent — a minimal AI agent you can watch think.

The whole agent is one loop: THINK (the model plans) -> ACT (a tool runs)
-> OBSERVE (the result goes back to the model) -> repeat until done.

Tools the agent is ALLOWED to use (its entire blast radius):
  - list_tickets()        read the ticket folder
  - read_ticket(name)     read one support ticket
  - check_customer(id)    look up a customer in the mock database
  - draft_email(...)      DRAFT a reply (Tier 2: a human approves; it is never sent)

Run it:  python agent/leader_demo_agent.py
         python agent/leader_demo_agent.py --goal "Summarize all three tickets for an executive"
"""

import argparse
import json
import os
import re
import sys
import urllib.request

MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2:3b")
OLLAMA_URL = "http://localhost:11434/api/chat"
BASE = os.path.dirname(os.path.abspath(__file__))
TICKET_DIR = os.path.join(BASE, "tickets")
MAX_STEPS = 8

# ---------------------------------------------------------------- tools ----
# Mock customer database — in a real agent this is a CRM lookup.
CUSTOMERS = {
    "C-1001": {"name": "Harbor Freight Logistics", "tier": "Enterprise", "arr": "$480K", "status": "renewal in 45 days"},
    "C-1002": {"name": "Bluebird Bakery Chain", "tier": "Standard", "arr": "$18K", "status": "active"},
    "C-1003": {"name": "Northwind Medical Group", "tier": "Enterprise", "arr": "$310K", "status": "active, past escalation in Q2"},
}

DRAFTS = []


def list_tickets(_arg=""):
    return "Tickets available: " + ", ".join(sorted(f for f in os.listdir(TICKET_DIR) if f.endswith(".txt")))


def read_ticket(name):
    name = os.path.basename(name.strip())
    path = os.path.join(TICKET_DIR, name)
    if not os.path.exists(path):
        return f"No ticket named {name}. Use list_tickets to see valid names."
    with open(path) as f:
        return f.read()


def check_customer(cid):
    cid = cid.strip().upper()
    c = CUSTOMERS.get(cid)
    if not c:
        return f"No customer with id {cid}. Valid ids: {', '.join(CUSTOMERS)}."
    return json.dumps(c)


def draft_email(text):
    DRAFTS.append(text.strip())
    return ("DRAFT SAVED (not sent). Sending email is a Tier 2 action: "
            "a human must review and approve this draft.")


TOOLS = {
    "list_tickets": (list_tickets, "list_tickets() - list the support ticket files"),
    "read_ticket": (read_ticket, "read_ticket(filename) - read one ticket, e.g. read_ticket(ticket1.txt)"),
    "check_customer": (check_customer, "check_customer(customer_id) - look up a customer, e.g. check_customer(C-1001)"),
    "draft_email": (draft_email, "draft_email(text) - DRAFT a reply for human approval (never auto-sent)"),
}

SYSTEM = """You are a support-operations agent. Work toward the GOAL step by step.

On every turn reply with EXACTLY ONE of:
  ACTION: tool_name(argument)
  FINAL: <your finished answer to the goal>

Available tools:
{tools}

Rules: one action per turn. Read tickets before judging them. Check the
customer record for any ticket you consider urgent. Keep the FINAL answer
under 200 words.
""".format(tools="\n".join("  - " + d for _, d in TOOLS.values()))


# ---------------------------------------------------------------- model ----
def chat(messages):
    req = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps({"model": MODEL, "messages": messages, "stream": False,
                         "options": {"temperature": 0.2}}).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.loads(r.read())["message"]["content"]


def parse_action(text):
    m = re.search(r"ACTION:\s*(\w+)\s*\((.*?)\)\s*$", text, re.S | re.M)
    if m and m.group(1) in TOOLS:
        return m.group(1), m.group(2).strip().strip("'\"")
    return None, None


def banner(label, color):
    colors = {"think": "\033[94m", "act": "\033[91m", "observe": "\033[92m", "done": "\033[95m"}
    print(f"\n{colors[color]}{'=' * 8} {label} {'=' * 8}\033[0m")


# ----------------------------------------------------------------- main ----
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--goal", default="Find which of the three sample support tickets is most urgent and draft a response plan.")
    goal = ap.parse_args().goal

    print(f"\nGOAL: {goal}")
    print(f"MODEL: {MODEL} (local, via Ollama) — each THINK step may take 30s-2min on this hardware.\n")

    messages = [{"role": "system", "content": SYSTEM},
                {"role": "user", "content": "GOAL: " + goal}]

    for step in range(1, MAX_STEPS + 1):
        banner(f"THINK (step {step})", "think")
        print("(model is thinking...)", flush=True)
        reply = chat(messages)
        print(reply.strip())
        messages.append({"role": "assistant", "content": reply})

        if "FINAL:" in reply:
            banner("DONE — agent's final answer", "done")
            print(reply.split("FINAL:", 1)[1].strip())
            break

        tool, arg = parse_action(reply)
        if not tool:
            messages.append({"role": "user", "content":
                             "That was not a valid ACTION or FINAL. Reply with ACTION: tool(arg) or FINAL: answer."})
            continue

        banner(f"ACT — calling {tool}({arg})", "act")
        result = TOOLS[tool][0](arg)
        print(result[:600] + ("..." if len(result) > 600 else ""))

        banner("OBSERVE — result returned to the model", "observe")
        print("(feeding the result back into the loop)")
        messages.append({"role": "user", "content": f"RESULT of {tool}({arg}):\n{result}\n\nContinue toward the GOAL."})
    else:
        banner("DONE — step limit reached", "done")
        print("The agent hit its step budget (a guardrail every real agent needs).")

    # ---- governance summary ----
    print("\n" + "-" * 60)
    print("WHAT THIS AGENT COULD AND COULD NOT DO")
    print("-" * 60)
    print("Allowed tools (its entire blast radius):")
    for _, desc in TOOLS.values():
        print("  -", desc)
    print(f"\nEmail drafts awaiting HUMAN approval (Tier 2): {len(DRAFTS)}")
    for i, d in enumerate(DRAFTS, 1):
        print(f"\n--- Draft {i} ---\n{d[:400]}")
    print("\nNot allowed: sending email, changing records, reaching the internet.")
    print("That list was a one-line decision in this file — and it's the governance surface leaders control.")


if __name__ == "__main__":
    main()
