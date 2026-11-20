# Enterprise Leader AI Accelerator — Labs
## Revision 1.10 - 11/20/26

These labs run in **any AI assistant** — Claude, ChatGPT, Microsoft Copilot, or Gemini — in a browser. A free account works. If your organization provides a sanctioned AI tool, use that one. Account setup is covered in the README's **Before you arrive** section.

The screenshots show Claude. Other assistants look different and word their answers differently — what matters is the pattern each step teaches, not an exact match.

**One rule on data:** use the scenarios provided here or non-confidential examples from your own work. Treat today's tools as public.

**Before Lab 1:** if your assistant is connected to your email, files, or calendar, turn those connections off for today (in Claude: the **+** button under the chat box → **Connectors**). Otherwise some prompts will search your own mail and documents.

**Also before Lab 1:** if your assistant remembers your earlier chats, switch that off for today, or use a chat that ignores it — **Temporary Chat** in ChatGPT and Gemini, an **incognito chat** in Claude (the ghost icon), the memory setting in Copilot. Otherwise it may answer from what it remembers about you and your work instead of from the lab's scenario. A temporary or incognito chat has to be chosen again each time a step says "start a new chat"; switching memory off in settings covers the whole day.

Labs 5–8 also use the worksheets in the `worksheets/` folder (or your printed copies). The same folder has a one-page reference sheet to keep.

**Lab contents**

| Lab | Title | Time |
|-----|-------|------|
| 1 | [Giving AI the context it needs](#lab1) | 12 min |
| 2 | [Ground it and verify](#lab2) | 12 min |
| 3 | [Review AI work before you sign it](#lab3) | 12 min |
| 4 | [Decision support and premortem](#lab4) | 12 min |
| 5 | [Score your use cases](#lab5) | 12 min |
| 6 | [Define pilot metrics](#lab6) | 12 min |
| 7 | [Governance gut-check](#lab7) | 12 min |
| 8 | [Your 90-day AI plan](#lab8) | 12 min |
| 9 | [(Optional — for after the workshop) See what your teams see](#lab9) | 12 min |

<br><br>

<a name="lab1"></a>

**Lab 1 — Giving AI the context it needs**

**Purpose: See for yourself how much output quality depends on how you ask. (12 minutes)**

1. Open your AI assistant in a browser and start a new chat.

<br><br>

2. Send this deliberately lazy prompt:

```
Write a status update about the project.
```

Read the result. What you get depends on what your assistant already knows about you:

- **If you use it regularly** (memory on, past chats, or a project with files in it), it may pick one of your real projects and write a decent update. It had context; it just came from what it has stored about you, not from your prompt. Notice that *it* chose the project and the facts. If it picked the wrong one, or used something out of date, you would not know unless you checked.
- **If it knows nothing about you** (a new account, or a temporary or incognito chat), it will either write a generic, fill-in-the-blanks update or ask what the project is.

Either way, the update is only as good as the context the model has. The rest of this lab is about supplying that context yourself, on purpose.

![Lazy prompt result](./images/acc1.png?raw=true "Lazy prompt: Claude asks for the missing context")

<br><br>

3. Start a **new chat** (so the first attempt doesn't influence the second).

<br><br>

4. Send this structured brief — same request, done the way you'd brief a capable new hire:

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

![Structured brief result](./images/acc2.png?raw=true "Structured brief: a usable VP status update")

<br><br>

5. Compare the two outputs. Note the difference role, context, task, and format made. Also look for any detail that wasn't in your brief (in the run above, "validated against production records" was invented).

<br><br>

6. Now iterate instead of accepting draft one. Send:

```
Critique this update as a skeptical VP would. List the five biggest things
that are unclear, missing, or buried, one line each.
```

![Skeptical VP critique](./images/acc3.png?raw=true "The critique flags vague and missing items")

<br><br>

7. Then send:

```
Rewrite the update fixing those issues. Keep it under 200 words. Do not invent facts: wherever information is missing, write [NEED: what's missing] instead.
```

![Rewrite with NEED markers](./images/acc4.png?raw=true "The rewrite marks missing facts instead of inventing them")

<br><br>

8. Read the final version. Every [NEED: …] is a question only you can answer. Without that last sentence in the prompt, models fill the gaps the critique found with made-up specifics — dates, percentages, names — that read as fact. Also check that nothing invented in the first draft survived into this one. Then pick the one [NEED] whose answer would improve the update most — that is business context only you can supply.

<br><br>

**What just happened**

- Output quality tracked input quality: role + context + task + format beat one vague line.
- Without your context, the model either guesses (from what it has stored about you, or from what an average asker would want) or asks. A brief puts you in control of what it works from.
- The critique → rewrite loop is the cheapest quality upgrade available — use it every time.
- Asked to "fix" missing information, a model will invent it. "Don't invent facts — mark what's missing" turns that risk into a to-do list.
- This pattern (brief, draft, critique, final) comes back several times today.

<p align="center">**[END OF LAB]**</p></br></br>

<a name="lab2"></a>

**Lab 2 — Ground it and verify**

**Purpose: See what an assistant does when it doesn't have the facts, then fix it with grounding and citations. (12 minutes)**

1. Start a new chat and ask — without giving it any documents:

```
What is our company's parental leave policy?
```

Note what happens: a refusal, a generic answer, or a made-up policy. Whatever it answers, it cannot know — it has never seen your policy. (If it answers with your real employer's policy, memory or a connection is still switched on — see the top of this page.)

<br><br>

2. Now ask it about a specific company as if facts were on file:

```
What is the exact parental leave policy at Brightline Logistics Inc.?
Include the number of weeks and who qualifies.
```

If it produces specifics, be suspicious — Brightline Logistics is fictional. If it declines or hedges, as Claude does here, that's the better behavior; models vary, which is itself a lesson.

![Ungrounded question about a fictional company](./images/acc5.png?raw=true "Claude searches, finds nothing, and declines to guess")

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

![Grounded answer with citations](./images/acc6.png?raw=true "Grounded answer catches the eligibility trap and cites each section")

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

![Claim checklist](./images/acc7.png?raw=true "A checklist of every claim to verify against the document")

<br><br>

7. Verify each claim against the policy text. This is the habit: every name, number, date, and citation gets 30 seconds.

<br><br>

**What just happened**

- Ungrounded questions about your organization produce guesses dressed as answers.
- Grounding ("using only this… cite the section") turned trust into verification.
- The eligibility trap shows why citations matter: checkable answers fail loudly instead of silently.
- Company-scale grounding is RAG — the same idea your teams automate across thousands of documents.

<p align="center">**[END OF LAB]**</p></br></br>

<a name="lab3"></a>

**Lab 3 — Review AI work before you sign it**

**Purpose: Check an AI-drafted recommendation the way you check any work that goes out under your name. (12 minutes)**

1. Read this memo. Someone on your team drafted it with AI and wants you to forward it to the executive team under your name.

```
TO: You        FROM: Jordan, Sales Operations
RE: Roll out DraftPilot to all 400 sales reps

Recommendation: approve a company-wide rollout this month.

Results: Our pilot ran for six weeks with 40 volunteer reps. All 12
pilot participants said DraftPilot saved them about 3 hours a week on
emails and proposals. Industry research shows 73% of sales teams win
more deals with AI drafting.

Value: 400 reps x 3 hours x 48 weeks x $60 an hour = $5.2 million a
year in time saved.

Cost: $30 per rep per month, or $144,000 a year. There are no other
costs.

Risk: There is no data risk, because the vendor has passed a security
audit.

The vendor's 20% discount ends Friday, so we need a decision this week.
```

<br><br>

2. On your own, before any AI: take two minutes and mark everything you would check or question before signing. Aim for at least four.

<br><br>

3. Start a new chat. Send the prompt below with the memo pasted under it:

```
I am about to forward the recommendation below to our executive team
under my name. Someone on my team drafted it with AI. Review it for me
before I sign. In a table of at most 8 rows, short phrases only, list
each number or claim I should check, what looks wrong or unsupported,
and how to check it. Check the arithmetic yourself and show it in one
line. Then list what is missing that a CFO would ask for, three lines
at most. Do not invent facts: if you cannot tell, say so. Under 250
words in total.

[paste the memo here]
```

<br><br>

4. Compare its list with yours. Tick what it found that you missed, and what you found that it missed.

<br><br>

5. Check one number yourself on your phone's calculator: 400 × 3 × 48 × $60. Compare your answer with the memo's.

<br><br>

6. Ask about the statistic:

```
Where does the 73% figure come from? Name the source only if you can
point me to it; otherwise say plainly that you cannot.
```

A good answer says it cannot find one. If your assistant names a study, ask yourself whether you would forward that without opening it.

<br><br>

7. Make the call: **sign, send back, or reject.** Write it down with one sentence on why. (This step has no prompt.)

<br><br>

8. Draft the note back:

```
Write a short note from me to Jordan, under 120 words. Thank them, then
list the three things that must be fixed before I can sign, each with
what I need to see. Direct and respectful. No lecture.
```

<br><br>

9. Read the note and change one line so it sounds like you.

<br><br>

10. Write one rule you will set for your team about AI-drafted work that comes to you.

<br><br>

11. (Optional — if you finish early.) Ask for an honest version:

```
Rewrite Jordan's memo using only what the pilot actually supports. Do
not invent facts — mark anything missing as [NEED: ...]. Under 150 words.
```

Compare it with the original: less impressive, and far more useful.

<br><br>

**What just happened**

- The memo read well and had at least six problems: 40 volunteers but "all 12 participants"; time savings people estimated for themselves; a statistic with no source; $5.2 million that is really $3,456,000; "no other costs"; and "no data risk". The Friday deadline is pressure, not evidence.
- AI makes weak work look finished. Polish no longer tells you anything about quality.
- The assistant was a useful second reviewer — after you looked first. Looking first keeps your own judgment in practice.
- It could check the arithmetic and the logic. It could not tell you what happened in the pilot. Only asking Jordan can.
- Your rule from step 10 is the start of a team habit: "tell me what the AI wrote and what you checked."

<p align="center">**[END OF LAB]**</p></br></br>

<a name="lab4"></a>

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
Keep it under 250 words: bottom line first, then a short comparison table,
then the three assumptions that matter most.
```

![Options analysis](./images/acc11.png?raw=true "Bottom line first, then costs and assumptions for each option")

<br><br>

2. Read the comparison. Spot-check one number yourself (45 agents × $18 × 12 months = $9,720 a year). Then look at the three assumptions: which one, if wrong, would flip the recommendation?

<br><br>

3. Run the premortem on the recommendation:

```
It is six months later and we followed your recommendation. It failed badly.
Write the honest internal retrospective: the top three causes, in order of
likelihood, two sentences each.
```

![Premortem retrospective](./images/acc12.png?raw=true "The premortem ranks likely failure causes")

<br><br>

4. Turn the premortem into protection:

```
For each of those three causes, give one concrete safeguard we could put
in place on day one of this decision. One line each.
```

<br><br>

5. Force the other side. Send:

```
Now argue for a DIFFERENT option than the one you recommended, as my
toughest board member would — no softening. Under 150 words.
```

<br><br>

6. Decide. Write one sentence of your own — which option you'd pick and the single factor that decided it. (This step has no prompt. That's the point.)

<br><br>

**What just happened**

- AI produced an options analysis, a premortem, safeguards, and a counter-argument in minutes — work that usually waits for a staff meeting.
- Asking for assumptions, failure modes, and the opposing case removes the model's agreeable default.
- Length limits ("under 250 words," "one line each") keep the output short enough to actually read — without them, this lab produces several thousand words.
- The comparison still left costs out. "2 engineers, 1 quarter, then upkeep" hides the other work those engineers won't do, security review, training, usage fees, and support. Ask "what costs are missing?" of every AI business case.
- Step 6 is the design: AI widened and stress-tested the thinking; the decision stayed with you.

<p align="center">**[END OF LAB]**</p></br></br>

<a name="lab5"></a>

**Lab 5 — Score your use cases**

**Purpose: Turn vague AI ideas from your organization into a scored, comparable shortlist. (12 minutes)**

1. Open **Worksheet 1: Use-Case Scorecard** (`worksheets/worksheet1-use-case-scorecard.md` or your printed copy).

<br><br>

2. On your own (no AI yet), list 3 candidate AI use cases from your organization. Use the green-flag pattern from the deck: high-volume, repetitive, verifiable work. One line each, named as a workflow: "triage inbound support tickets," not "use AI in support."

<br><br>

3. Score each candidate 1–5 on the five criteria — Value, Data readiness, Feasibility, Risk (5 = low risk), Measurability. Gut scores are fine; speed over precision.

<br><br>

4. Now stress-test with AI. Start a new chat:

```
You are a skeptical AI program reviewer. For the use case below, ask me the
five hardest questions you'd ask before funding it, one line each, covering:
business value, data readiness, buy-vs-build, risk, and measurability.

Use case: [paste your top-scored candidate — generic description only,
no confidential details]
```

The screenshot uses a sample use case ("triage inbound support tickets"); yours will differ.

![Skeptical reviewer questions](./images/acc13.png?raw=true "Five hard funding questions for a sample use case")

<br><br>

5. Answer its questions honestly (to yourself or in the chat). Adjust any score the questions changed.

<br><br>

6. Run the **blocker check** on the worksheet for your top-scored candidate. A high score never overrides a blocker: if any box is ticked, move to your next candidate.

<br><br>

7. Circle your winner on the worksheet and complete the bottom line: "**[Use case]** wins because **[one sentence]**."

<br><br>

8. Look back at your winner's five scores. Mark the one you are least sure of, and write down what you would need to find out to settle it. The instructor will ask for a show of hands on which of the five it was.

<br><br>

**What just happened**

- Five scores forced the five conversations that decide pilot success — before any money moves.
- The AI's skeptical-reviewer questions exposed soft scores (data readiness is usually the one that drops).
- The blocker check catches what a total hides: one unusable data source or one missing owner outweighs four good scores.
- You now hold a ranked shortlist grounded in your own organization — the input for Lab 6.

<p align="center">**[END OF LAB]**</p></br></br>

<a name="lab6"></a>

**Lab 6 — Define pilot metrics**

**Purpose: Give your winning use case metrics a CFO would accept — baseline, target, guardrail, stop rule. (12 minutes)**

1. Open **Worksheet 2: Pilot Metrics Charter** (`worksheets/worksheet2-pilot-metrics.md`).

<br><br>

2. Fill in the header: your winning use case from Lab 5, the workflow owner and the executive sponsor (real names — often two different people), and the 90-day window.

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

Attack it: name the three biggest ways it is gameable, unmeasurable, or
likely to show a result the AI didn't cause. Give the smallest fix for each.
Under 150 words.
```

The screenshot uses a sample plan (median handling time 11 → 8 minutes, first-contact resolution as the guardrail).

![CFO red-team](./images/acc14.png?raw=true "The CFO finds where the sample plan is gameable")

<br><br>

7. Apply the fixes that convinced you. Update the worksheet.

<br><br>

8. Fill in the two short boxes near the bottom of the worksheet: **What the pilot needs** and **If it succeeds**. Rough answers are fine.

<br><br>

9. Read your final definition-of-done out loud once. If it names a workflow, a number, a date, an owner, and a stop rule — you are ahead of most funded AI pilots.

<br><br>

**What just happened**

- Baseline-first design makes the result provable either way — the missing piece in most failed pilots.
- The guardrail stops the classic trap: speed up, quality down, "success."
- The stop rule makes killing a failed pilot a planned outcome, not an embarrassment.
- The CFO red-team caught the gameable parts while fixing them was still free.
- A sponsor, a resource estimate, and a plan for success are what separate a pilot from an experiment nobody picks up afterward.

<p align="center">**[END OF LAB]**</p></br></br>

<a name="lab7"></a>

**Lab 7 — Governance gut-check**

**Purpose: Apply the injection questions and autonomy tiers to a realistic agent proposal, make the approval call, and start your governance playbook. (12 minutes)**

1. Read this proposal, which contains several planted red flags:

```
PROPOSAL: "PayFast" invoice agent (from our finance systems team)

The agent monitors the shared accounts-payable inbox, reads each incoming
email and any attached invoice, looks up the supplier in our purchasing and
accounting systems using an admin service account, SENDS emails to
suppliers automatically about anything it classifies as routine, and pays
invoices up to $5,000 without approval to shorten payment time. It can also
browse supplier websites to confirm bank and contact details. Logging to be
added in phase 2. Pilot on all suppliers for 6 months.
```

<br><br>

2. On your own, take 90 seconds to mark every red flag you see. Aim for at least five.

<br><br>

3. Apply the three injection questions from the deck: What untrusted content does it read? What private data can it reach? Can it send anything out? Count the trifecta legs.

<br><br>

4. Check your findings with AI:

```
Review this AI agent proposal as a security-minded AI governance reviewer.
List every risk, map each to (a) the prompt-injection "lethal trifecta" and
(b) an autonomy tier decision (assist / review / autonomous). Answer as a
table (risk | trifecta leg | tier), at most 6 rows. Then list the three
changes that matter most for a safe 90-day pilot, one line each.

[paste the proposal]
```

![Governance review of PayFast](./images/acc15.png?raw=true "The review finds all three trifecta legs and maps each risk")

<br><br>

5. Compare its list with yours. Key flags: all three trifecta legs present (reads external email/attachments/web + purchasing and accounting access + sends email and payments), admin service account instead of least privilege, auto-send and auto-pay at Tier 3 autonomy on day one, bank details taken from websites an outsider controls, logging deferred, all suppliers instead of a scoped pilot, 6 months instead of 90 days.

<br><br>

6. Make the call: **approve, approve with conditions, or reject**. Write it on Worksheet 3 with two sentences on why. If you chose conditions, name them — for example which actions move to Tier 2 (human approves), what access gets narrowed, what gets logged from day one.

<br><br>

7. Hold your call for the re-run of the poll. When the room splits, listen for what the other side weighted that you did not.

<br><br>

8. Open **Worksheet 3: Governance Playbook** (`worksheets/worksheet3-governance-playbook.md`). In Box 1 (Inventory), list two or three AI tools already in use in your org — including shadow use you suspect. In Box 2 (Usage policy headlines), write three rules you'd publish this week.

<br><br>

**What just happened**

- A proposal that sounds efficient held all three legs of the lethal trifecta plus Tier-3 autonomy, day one.
- The fix pattern is standard: narrow access, insert human approval on consequential actions, log everything, scope the pilot.
- You made a decision, not just a list of risks — and others in the room made a different one. That is what an approval meeting is.
- Your playbook now has its first two boxes — the other four get decide-by dates in Lab 8.

<p align="center">**[END OF LAB]**</p></br></br>

<a name="lab8"></a>

**Lab 8 — Your 90-day AI plan**

**Purpose: Leave with a concrete 30/60/90 plan and the paragraph you'll send your leadership team. (12 minutes)**

1. Open the 30/60/90 section of **Worksheet 3**. Have your Lab 5 scorecard and Lab 6 charter beside you.

<br><br>

2. Fill in two lines of Days 1–30 (SEE): your daily AI habit and the date the one-page policy ships.

<br><br>

3. Fill in two lines of Days 31–60 (SCOPE): your pilot's owner and the baseline collection dates.

<br><br>

4. Fill in one line of Days 61–90 (SHIP): the day-90 decision meeting — put a real date on it.

<br><br>

5. Turn back to the six boxes at the top of Worksheet 3. Beside Boxes 3–6, write the date you will decide each one by.

<br><br>

6. Draft the announcement. Start a new chat:

```
Turn these notes into one tight paragraph (under 120 words) I can send my
leadership team: we are piloting AI deliberately. Include: the use case,
the owner, the 90-day window with baseline and metric, the stop rule, and
one sentence on governance (approved tools + usage policy shipping now).
Confident, no hype.

Notes: [paste the key lines from your worksheets]
```

![Announcement paragraph](./images/acc16.png?raw=true "Worksheet notes turned into a leadership-ready paragraph (sample notes)")

<br><br>

7. Run the loop once:

```
Critique this paragraph as a skeptical CTO in three bullets, then rewrite it. Don't invent facts — mark anything missing as [NEED: ...].
```

<br><br>

8. Copy the final paragraph onto the worksheet (or email it to yourself right now — that's better).

<br><br>

9. If you're willing: pitch your pilot in the review round that follows — thirty seconds covering the workflow, owner, metric, and stop rule. The room gives one strength and one concern.

<br><br>

**What just happened**

- The 30/60/90 turned today's material into named owners and dated commitments.
- The announcement paragraph is the real test: if it names a workflow, metric, owner, and stop rule in 120 words, your plan is coherent.
- Putting the day-90 decision meeting on calendars now is what turns the plan into a commitment.
- Every open box of your governance playbook now has a date: a started playbook, not a blank one.

<p align="center">**[END OF LAB]**</p></br></br>

<a name="lab9"></a>

**Lab 9 (Optional) — See what your teams see**

**Purpose: Watch a real AI agent run its think → act → observe loop in a live dev environment — no coding. (12 minutes)**

> This lab is for after the workshop. In the session your instructor shows a different agent live, just before Lab 7. To watch one run step by step in real code, follow the steps below in your own time.

> Note: this lab uses GitHub Codespaces — a complete development environment that runs in your browser. You need a free GitHub account (see the README's **Before you arrive** section). The first startup takes 3–5 minutes; read ahead while it builds.

1. Open the lab repository in your browser:

```
https://github.com/skillrepos/tlsaccel
```

<br><br>

2. Click the green **Code** button, select the **Codespaces** tab, and click **Create codespace on main**. A VS Code window opens in your browser tab.

![Create a codespace](./images/acc17.png?raw=true "Code button, Codespaces tab, Create codespace on main")

<br><br>

3. If VS Code asks **"Do you trust the authors of the files in this folder?"**, click **Trust Folder & Continue**. Then wait for setup to finish: the terminal at the bottom shows **Running postCreateCommand…** while a small AI model downloads (3–5 minutes).

<br><br>

4. When setup is done (the terminal shows **Ollama is running.**), click into the terminal, type (or copy) this, and press Enter:

```
python codespace-lab/agent/leader_demo_agent.py
```

<br><br>

5. The agent's goal: *find the most urgent of three sample support tickets, check that customer's record, and draft a reply.* Watch the loop scroll by:

- **THINK** — the model decides its next step
- **ACT** — a tool call: reading a ticket, looking up the (sample) customer database
- **OBSERVE** — the tool's result goes back to the model

Each step takes a few seconds — longer on a busy machine. That wait is what "AI compute" means physically.

![The agent loop](./images/acc18.png?raw=true "THINK, ACT, OBSERVE repeating as the agent reads tickets")

<br><br>

6. When it finishes, read the summary at the bottom: the tools the agent was ALLOWED to use, and the email draft waiting for a human to approve (sending is a Tier 2 action). Read the draft closely — does it promise anything nobody approved, such as a fix by a certain time?

![Governance summary and draft](./images/acc19.png?raw=true "Allowed tools, one draft awaiting human approval")

<br><br>

7. Run it once more with a different goal:

```
python codespace-lab/agent/leader_demo_agent.py --goal "Summarize all three tickets for an executive"
```

Same loop, different tool choices — this time it has no reason to look up a customer or draft an email. The agent chose its own path.

<br><br>

8. Connect it back: this loop — with real tools, real credentials, and real autonomy decisions — is what your teams propose when they say "agent." The tool list and the Tier 2 approval you just saw are the governance surface you control.

<br><br>

9. Answer four questions as the sponsor: What was the agent allowed to touch? Which action needed approval? What could have gone wrong? Would you authorize this agent in your organization?

<br><br>

10. When done, close the browser tab. Codespaces stop on their own when idle.

<br><br>

**What just happened**

- You ran an AI agent: a model in a loop with tools, as drawn on the deck's agent slide.
- The agent chose its own steps toward the goal — that's agency, and why the tool list matters.
- The email waited for human approval: autonomy Tier 2, visible in running code. Its draft can still promise things on your behalf — which is exactly why a person reviews it.
- Everything ran on a small open-weight model inside the environment; no ticket data left it.

<p align="center">**[END OF LAB]**</p></br></br>

<p align="center">
<b>For educational use only by the attendees of our workshops.</b>
</p>
<p align="center">
<b>(c) 2026 Tech Skills Transformations and Brent C. Laster. All rights reserved.</b>
</p>
