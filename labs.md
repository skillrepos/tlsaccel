# Enterprise Leader AI Accelerator — Labs
## Revision 1.0 - 12/02/26

These labs run in **any AI assistant** — Claude, ChatGPT, Microsoft Copilot, or Gemini — in a browser. A free account works. If your organization provides a sanctioned AI tool, use that one.

**One rule on data:** use the scenarios provided here or non-confidential examples from your own work. Treat today's tools as public.

Labs 5–8 also use the worksheets in the `worksheets/` folder (or your printed copies).

**Lab contents**

| Lab | Title | Time |
|-----|-------|------|
| 1 | Brief it like a chief of staff | 12 min |
| 2 | Ground it and verify | 12 min |
| 3 | The leadership writing suite | 12 min |
| 4 | Decision support and premortem | 12 min |
| 5 | Score your use cases | 15 min |
| 6 | Define pilot metrics | 12 min |
| 7 | Governance gut-check | 12 min |
| 8 | Your 90-day AI plan | 15 min |
| 9 | (Optional) See what your teams see | 15 min |

<br><br>

**Lab 1 — Brief it like a chief of staff**

**Purpose: See for yourself how much output quality depends on how you ask. (12 minutes)**

1. Open your AI assistant in a browser and start a new chat.

<br><br>

2. Send this deliberately lazy prompt:

```
Write a status update about the project.
```

Read the result. Notice how generic it is — the model had nothing to work with, so it predicted an average answer for an average asker.

<br><br>

3. Start a **new chat** (so the first attempt doesn't influence the second).

<br><br>

4. Send this structured brief — same request, done like you'd brief a new chief of staff:

```
You are an experienced program manager writing for a VP audience.

Context: Our team is migrating the customer billing system to a new vendor
platform. We are in week 6 of 12. Data migration is done. Integration testing
found 14 defects; 11 are fixed. The vendor's SSO module slipped two weeks,
which puts the go-live date at risk. The team is confident but tired.

Task: Write a status update for the VP of Engineering.

Format: Subject line, then three sections — Progress, Risks, Asks.
Under 200 words. Direct, no hype.
```

<br><br>

5. Compare the two outputs. Note the difference role, context, task, and format made.

<br><br>

6. Now iterate instead of accepting draft one. Send:

```
Critique this update as a skeptical VP would. What's unclear, missing, or buried?
```

<br><br>

7. Then send:

```
Rewrite the update fixing those issues. Keep it under 200 words.
```

<br><br>

8. Compare the final version to your lazy prompt result from step 2. Those two prompts — critique, then rewrite — cost 20 seconds.

<br><br>

**What just happened**

- Output quality tracked input quality: role + context + task + format beat one vague line.
- The model predicts a response for an *average* asker unless you make yourself specific.
- The critique → rewrite loop is the cheapest quality upgrade available — use it every time.
- This pattern (brief, draft, critique, final) repeats through every lab today.

<p align="center">**[END OF LAB]**</p></br></br>

**Lab 2 — Ground it and verify**

**Purpose: Watch a confident wrong answer happen, then fix it with grounding and citations. (12 minutes)**

1. Start a new chat and ask — without giving it any documents:

```
What is our company's parental leave policy?
```

Note what happens: a refusal, a generic answer, or a made-up policy. Whatever it answers, it cannot know — it has never seen your policy.

<br><br>

2. Now ask it about a specific company as if facts were on file:

```
What is the exact parental leave policy at Brightline Logistics Inc.?
Include the number of weeks and who qualifies.
```

If it produces specifics, be suspicious — Brightline Logistics is fictional. If it declines or hedges, that's the better behavior; models vary, which is itself a lesson.

<br><br>

3. Start a new chat. Paste this sample policy **plus** the grounded question below it:

```
POLICY DOC — Brightline Logistics Inc., HR-204 (excerpt)

Section 1: Eligibility. Employees with 12+ months of continuous service
qualify for paid parental leave.
Section 2: Duration. Birthing parents: 16 weeks paid. Non-birthing parents
and adoptive parents: 8 weeks paid.
Section 3: Scheduling. Leave may be split into two blocks within the first
12 months. Manager approval is needed only for the split, not the leave.
Section 4: Benefits. Health coverage continues; PTO does not accrue during
leave.

Using ONLY the document above, answer: an adoptive parent with 9 months of
service wants to take leave in two blocks. What are they entitled to, and
what approval do they need? Cite the section for each part of your answer.
```

<br><br>

4. Check the answer against the document. The right answer: **they are not yet eligible** (Section 1 — 12 months required). A good grounded answer catches this; a sloppy one jumps to "8 weeks, split allowed."

<br><br>

5. If the answer missed the eligibility trap, push back:

```
Re-check Section 1 against the employee's length of service.
```

Watch it correct itself — and note that *you* caught it because the citations made checking possible.

<br><br>

6. Run the 30-second spot-check drill. Ask:

```
List every specific claim in your answer (numbers, dates, section references)
as a checklist I can verify against the document.
```

<br><br>

7. Verify each claim against the policy text. This is the habit: every name, number, date, and citation gets 30 seconds.

<br><br>

**What just happened**

- Ungrounded questions about your organization produce guesses dressed as answers.
- Grounding ("using only this… cite the section") turned trust into verification.
- The eligibility trap shows why citations matter: checkable answers fail loudly instead of silently.
- Company-scale grounding is RAG — the same idea your teams automate across thousands of documents.

<p align="center">**[END OF LAB]**</p></br></br>

**Lab 3 — The leadership writing suite**

**Purpose: Produce three real pieces of leadership writing with the brief → draft → critique → final cycle. (12 minutes)**

1. Start a new chat. Turn messy notes into a status update — paste:

```
You are a director writing a weekly status note to senior leadership.

Raw notes: hiring req for data engineer still open 7 weeks... vendor demo
went well but pricing 30% over budget... Kim's team shipped the reporting
dashboard early... two customer escalations this week, both resolved, same
root cause (timeout config)... offsite planning eating too much team time.

Task: a status note with sections Wins / Watch items / Asks.
Format: under 150 words, scannable, no fluff.
```

<br><br>

2. Run the quality loop:

```
Critique it as a COO would, then rewrite it fixing the critique.
```

<br><br>

3. Next, the difficult message. In the same chat:

```
New task. I need to tell a peer director that my team cannot meet the
March 1 integration date she is counting on. Realistic date is March 22.
Reasons: the SSO slip from our vendor and one unfilled role. I want to
preserve the relationship, own the miss, and propose that her team starts
against our test environment on March 1 as a bridge.

Draft this as a short email: honest, no blame-shifting, specific ask at the end.
```

<br><br>

4. Make it sound like you. Give it your voice:

```
Rewrite it to match my style: [paste 3–5 sentences from an email YOU wrote —
any non-confidential one]. Keep the content, change the voice.
```

<br><br>

5. Now the re-tone drill. Send:

```
Take the final version and produce three variants of its core message:
(a) two sentences for a board update, (b) a short Slack message to my own
team, (c) a reassuring note to the affected customer. Label each.
```

<br><br>

6. Read all three variants. Same facts, three audiences — notice what the model kept, cut, and softened for each.

<br><br>

**What just happened**

- The brief → draft → critique → final cycle held up across three different writing jobs.
- A few sentences of your own writing is enough for a usable voice match.
- Re-toning one message for several audiences is a minutes-level task now — the judgment about *what* to say stays yours.
- For sensitive messages: AI drafts the structure, you write the heart.

<p align="center">**[END OF LAB]**</p></br></br>

**Lab 4 — Decision support and premortem**

**Purpose: Use AI to widen your options and stress-test a decision — without delegating the decision. (12 minutes)**

1. Start a new chat and paste the scenario:

```
You are an analytical advisor to a VP. Be direct and expose your assumptions.

Scenario: Our 300-person company needs AI-assisted summarization of customer
support tickets (8,000/month). Options on the table: (A) buy the add-on from
our existing helpdesk vendor at $18/agent/month for 45 agents, (B) have our
platform team build it with an LLM API (~2 engineers, 1 quarter, then upkeep),
(C) wait 6 months and re-evaluate.

Task: Compare A, B, and C with costs, risks, time to value, and the key
assumptions behind each. Then recommend one and justify it.
```

<br><br>

2. Read the comparison. Before accepting anything, make the assumptions explicit:

```
List every assumption your recommendation depends on, ranked by how much
the recommendation changes if the assumption is wrong.
```

<br><br>

3. Run the premortem on the recommendation:

```
It is six months later and we followed your recommendation. It failed badly.
Write the honest internal retrospective: what went wrong, in order of likelihood.
```

<br><br>

4. Turn the premortem into protection:

```
For the top three failure causes, give one concrete safeguard we could put
in place on day one of this decision.
```

<br><br>

5. Force the other side. Send:

```
Now argue for a DIFFERENT option than the one you recommended, as my
toughest board member would — no softening.
```

<br><br>

6. Decide. Write one sentence of your own — which option you'd pick and the single factor that decided it. (This step has no prompt. That's the point.)

<br><br>

**What just happened**

- AI produced an options analysis, a premortem, safeguards, and a counter-argument in minutes — work that usually waits for a staff meeting.
- Asking for assumptions, failure modes, and the opposing case removes the model's agreeable default.
- Step 6 is the design: AI widened and stress-tested the thinking; the decision stayed with you.

<p align="center">**[END OF LAB]**</p></br></br>

**Lab 5 — Score your use cases**

**Purpose: Turn vague AI ideas from your organization into a scored, comparable shortlist. (15 minutes)**

1. Open **Worksheet 1: Use-Case Scorecard** (`worksheets/worksheet1-use-case-scorecard.md` or your printed copy).

<br><br>

2. On your own (no AI yet), list 3–5 candidate AI use cases from your organization. Use the green-flag pattern from the deck: high-volume, repetitive, verifiable work. One line each, named as a workflow: "triage inbound support tickets," not "use AI in support."

<br><br>

3. Score each candidate 1–5 on the five criteria — Value, Data readiness, Feasibility, Risk (5 = low risk), Measurability. Gut scores are fine; speed over precision.

<br><br>

4. Now stress-test with AI. Start a new chat:

```
You are a skeptical AI program reviewer. For the use case below, ask me the
five hardest questions you'd ask before funding it, covering: business value,
data readiness, buy-vs-build, risk, and measurability.

Use case: [paste your top-scored candidate — generic description only,
no confidential details]
```

<br><br>

5. Answer its questions honestly (to yourself or in the chat). Adjust any score the questions changed.

<br><br>

6. Repeat steps 4–5 for your #2 candidate.

<br><br>

7. Circle your winner on the worksheet and complete the bottom line: "**[Use case]** wins because **[one sentence]**."

<br><br>

8. Compare scorecards with a neighbor: one minute each. Where your scores differ on similar use cases, ask why — the disagreement is the insight.

<br><br>

**What just happened**

- Five scores forced the five conversations that decide pilot success — before any money moves.
- The AI's skeptical-reviewer questions exposed soft scores (data readiness is usually the one that drops).
- You now hold a ranked shortlist grounded in your own organization — the input for Lab 6.

<p align="center">**[END OF LAB]**</p></br></br>

**Lab 6 — Define pilot metrics**

**Purpose: Give your winning use case metrics a CFO would accept — baseline, target, guardrail, stop rule. (12 minutes)**

1. Open **Worksheet 2: Pilot Metrics Charter** (`worksheets/worksheet2-pilot-metrics.md`).

<br><br>

2. Fill in the header: your winning use case from Lab 5, a named owner (a real name), and the 90-day window.

<br><br>

3. Choose ONE primary metric from the four families (time, cost, quality, adoption). Write how you'll measure the baseline for two weeks before the pilot starts.

<br><br>

4. Add one quality guardrail — the number that must NOT get worse while the primary metric improves.

<br><br>

5. Draft your definition-of-done sentence on the worksheet:

> "By [date], [workflow] handled with AI assistance shows [metric] moving from [baseline] to [target], with [guardrail] maintained — or we stop and write down what we learned."

<br><br>

6. Red-team it with AI. Start a new chat:

```
You are a skeptical CFO. Here is a pilot metrics plan:

[paste your definition-of-done sentence and your primary metric, baseline
plan, target, and guardrail]

Attack it: where is it gameable, unmeasurable, or likely to show a result
that isn't really caused by the AI? Then suggest the smallest fixes.
```

<br><br>

7. Apply the fixes that convinced you. Update the worksheet.

<br><br>

8. Read your final definition-of-done out loud once. If it names a workflow, a number, a date, an owner, and a stop rule — you are ahead of most funded AI pilots.

<br><br>

**What just happened**

- Baseline-first design makes the result provable either way — the missing piece in most failed pilots.
- The guardrail stops the classic trap: speed up, quality down, "success."
- The stop rule makes killing a failed pilot a planned outcome, not an embarrassment.
- The CFO red-team caught the gameable parts while fixing them was still free.

<p align="center">**[END OF LAB]**</p></br></br>

**Lab 7 — Governance gut-check**

**Purpose: Apply the injection questions and autonomy tiers to a realistic agent proposal — and start your governance playbook. (12 minutes)**

1. Read this proposal, which contains several planted red flags:

```
PROPOSAL: "InboxZero" support agent (from our platform team)

The agent monitors the shared support inbox, reads each incoming email and
any attachments, looks up the customer in our CRM and billing system using
an admin service account, drafts and SENDS replies automatically for
anything it classifies as routine, and files refunds up to $500 without
approval to reduce handling time. It can also browse vendor documentation
sites to research error messages. Logging to be added in phase 2. Pilot on
all customers for 6 months.
```

<br><br>

2. On your own, mark every red flag you see. Aim for at least five.

<br><br>

3. Apply the three injection questions from the deck: What untrusted content does it read? What private data can it reach? Can it send anything out? Count the trifecta legs.

<br><br>

4. Check your findings with AI:

```
Review this AI agent proposal as a security-minded AI governance reviewer.
List every risk, map each to (a) the prompt-injection "lethal trifecta" and
(b) an autonomy tier decision (assist / review / autonomous). Then propose
the minimal changes that would make a safe 90-day pilot.

[paste the proposal]
```

<br><br>

5. Compare its list with yours. Key flags: all three trifecta legs present (reads external email/attachments/web + CRM and billing access + sends email), admin service account instead of least privilege, auto-send and auto-refund at Tier 3 autonomy on day one, logging deferred, all customers instead of a scoped pilot, 6 months instead of 90 days.

<br><br>

6. Decide what a safe version looks like: which actions move to Tier 2 (human approves), what access gets narrowed, what gets logged from day one. Two or three bullets.

<br><br>

7. Open **Worksheet 3: Governance Playbook** (`worksheets/worksheet3-governance-playbook.md`). Fill in Box 1 (Inventory) with the AI already in use in your org — including shadow use you suspect — and Box 2 (Usage policy headlines): three rules you'd publish this week.

<br><br>

**What just happened**

- A proposal that sounds efficient held all three legs of the lethal trifecta plus Tier-3 autonomy, day one.
- The fix pattern is standard: narrow access, insert human approval on consequential actions, log everything, scope the pilot.
- Your playbook now has its first two boxes — the rest is homework with a deadline, not a mystery.

<p align="center">**[END OF LAB]**</p></br></br>

**Lab 8 — Your 90-day AI plan**

**Purpose: Leave with a concrete 30/60/90 plan and the paragraph you'll send your leadership team. (15 minutes)**

1. Open the 30/60/90 section of **Worksheet 3**. Have your Lab 5 scorecard and Lab 6 charter beside you.

<br><br>

2. Fill in Days 1–30 (SEE): your daily AI habit, who starts the inventory, when the one-page policy ships, and who sees your scored shortlist.

<br><br>

3. Fill in Days 31–60 (SCOPE): your pilot's owner, baseline collection dates, and the buy/partner/build lean.

<br><br>

4. Fill in Days 61–90 (SHIP): the weekly review slot and the day-90 decision meeting — put a real date on it.

<br><br>

5. Draft the announcement. Start a new chat:

```
Turn these notes into one tight paragraph (under 120 words) I can send my
leadership team: we are piloting AI deliberately. Include: the use case,
the owner, the 90-day window with baseline and metric, the stop rule, and
one sentence on governance (approved tools + usage policy shipping now).
Confident, no hype.

Notes: [paste the key lines from your worksheets]
```

<br><br>

6. Run the loop once: `Critique this paragraph as a skeptical CTO, then rewrite it.`

<br><br>

7. Copy the final paragraph onto the worksheet (or email it to yourself right now — that's better).

<br><br>

8. If you're willing: share your pilot one-liner with the room when asked. Thirty seconds, and the feedback is free.

<br><br>

**What just happened**

- The 30/60/90 turned today's material into named owners and dated commitments.
- The announcement paragraph is the real test: if it names a workflow, metric, owner, and stop rule in 120 words, your plan is coherent.
- Booking the day-30 checkpoint is the single step that predicts whether the rest happens.

<p align="center">**[END OF LAB]**</p></br></br>

**Lab 9 (Optional) — See what your teams see**

**Purpose: Watch a real AI agent run its think → act → observe loop in a live dev environment — no coding. (15 minutes)**

> Note: this lab uses GitHub Codespaces — a complete development environment that runs in your browser. You need a free GitHub account (github.com/signup). The environment takes 3–5 minutes to start; read ahead while it builds.

1. Open the lab repository in your browser:

```
<CODESPACE-REPO-URL>
```

<br><br>

2. Click the green **Code** button, select the **Codespaces** tab, and click **Create codespace on main**. A VS Code environment opens in your browser. Wait for setup to finish — the terminal at the bottom shows progress, and a local AI model downloads automatically (3–5 minutes).

<br><br>

3. When the terminal shows a prompt, type (or copy) this and press Enter:

```
python agent/leader_demo_agent.py
```

<br><br>

4. The agent receives a goal: *"Find which of the three sample support tickets is most urgent and draft a response plan."* Watch the loop scroll by, labeled at each step:

- **THINK** — the model's plan for the next step
- **ACT** — a tool call: reading a ticket file, checking the (mock) customer database
- **OBSERVE** — the tool's result feeding back in

The local model thinks slowly — 30 seconds to 2 minutes per step on this hardware is normal. That wait is itself informative: this is what "AI compute" means physically.

<br><br>

5. When it finishes, read the agent's final plan in the terminal. Then look at the one-screen summary it prints: which tools it was ALLOWED to use, and which actions it drafted but did NOT take (sending email is Tier 2 — a human approves).

<br><br>

6. Run it once more with a different goal:

```
python agent/leader_demo_agent.py --goal "Summarize all three tickets for an executive"
```

Notice the same loop, different tool choices — the agent decided its own path.

<br><br>

7. Connect it back: this loop — with real tools, real credentials, and real autonomy decisions — is exactly what your teams propose when they say "agent." The tool list and the Tier-2 approval you just saw are the governance surface you control.

<br><br>

8. When done, close the browser tab. (Codespaces auto-stop when idle; nothing to clean up.)

<br><br>

**What just happened**

- You ran an AI agent: a model in a loop with tools, exactly as drawn on the deck's agent slide.
- The agent chose its own steps toward the goal — that's agency, and why the tool list matters.
- The email step waited for human approval: autonomy Tier 2, visible in running code.
- Everything ran on a local open-weight model in the environment — no data left the machine.

<p align="center">**[END OF LAB]**</p></br></br>

<p align="center">
<b>For educational use only by the attendees of our workshops.</b>
</p>
<p align="center">
<b>(c) 2026 Tech Skills Transformations and Brent C. Laster. All rights reserved.</b>
</p>
