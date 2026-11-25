# Enterprise Leader AI Accelerator — Labs
## Revision 1.22 - 11/25/26

These labs run in **any AI assistant** — Claude, ChatGPT, Microsoft Copilot, or Gemini — in a browser. A free account works. If your organization provides a sanctioned AI tool, use that one. Account setup is covered in the README's **Before you arrive** section.

The screenshots show Claude. Other assistants look different and word their answers differently — what matters is the pattern each step teaches, not an exact match.

**One rule on data:** use the scenarios provided here or non-confidential examples from your own work. Treat today's tools as public.

**Writing things down:** Labs 1–4 have no worksheet. Where a step asks you to write, mark or tick something, use paper or a notes app.

**Before Lab 1:** if your assistant is connected to your email, files, or calendar, turn those connections off for today. In Claude: click the **+** button under the chat box, then **Plugins**, and switch off Gmail, Google Drive and any other email or file apps. Otherwise some prompts will search your own mail and documents, even in an incognito chat.

**Also good to know:** if your assistant remembers your earlier chats, it may bring your own work into some answers. That is fine for today's labs. If you'd rather keep it out, use a chat that ignores your history: in ChatGPT, click **Temporary chat** (top right) and set the menu beside it to **Unpersonalized**; in Claude, click **Use incognito** (the ghost icon, top right).

Labs 5–8 each use a worksheet: Worksheet 1 for Lab 5, 2 for Lab 6, 3 for Lab 7 and 4 for Lab 8. Fill them in on the **[worksheets page](https://skillrepos.github.io/tlsaccel/)**, which shows one worksheet at a time: you type into the boxes on your phone or laptop, and your answers are saved on your own device. Boxes marked **Required** are the ones the labs ask you to fill in; boxes marked **Optional** are for back at work. At any point, press **Check for required info** on a worksheet to see which Required boxes are still empty, listed by lab step. No use case of your own ready? Each worksheet there has examples you can use instead. The `worksheets/` folder has a one-page reference sheet to keep.

**Lab contents**

| Lab | Title |
|-----|-------|
| 1 | [Giving AI the context it needs](#lab1) |
| 2 | [Ground it and verify](#lab2) |
| 3 | [Review AI work before you sign it](#lab3) |
| 4 | [Decision support and premortem](#lab4) |
| 5 | [Score your use cases](#lab5) |
| 6 | [Define pilot metrics](#lab6) |
| 7 | [Governance gut-check](#lab7) |
| 8 | [Your 90-day AI plan](#lab8) |
| 9 | [(Optional — for after the workshop) See an agent run in real code](#lab9) |

<br><br>

<a name="lab1"></a>

**Lab 1 — Giving AI the context it needs**

**Purpose: See for yourself how much output quality depends on how you ask.**

1. Open your AI assistant in a browser and start a new chat.

<br><br>

2. Send this deliberately lazy prompt. Project Kestrelmoor is made up for this lab, so your assistant knows nothing about it:

```
Write a status update about Project Kestrelmoor.
```

Read the result. You will probably see one of these:

- **Questions back:** it asks what the project is and who the update is for.
- **A fill-in-the-blanks template.**
- **A finished-looking update** with progress, dates and risks. Look closely: it made all of it up.

Some assistants first search your past chats or connected files for the name, or suggest apps you could connect, and then come up empty. Whatever you get, the model can't do the job without context.

![Lazy prompt result](./images/acc1.png?raw=true "Lazy prompt: Claude asks for the missing context")

<br><br>

3. Start a **new chat** (so the first attempt doesn't influence the second).

<br><br>

4. Send this structured brief — same request, done the way you'd brief a capable new hire:

```
You are an experienced program manager writing for a leadership audience.

Context: Project Kestrelmoor is migrating our customer billing system to a
new vendor platform. We are in week 6 of 12. Data migration is done.
Integration testing found 14 defects; 11 are fixed. The vendor's SSO module
slipped two weeks, which puts the go-live date at risk. The team is
confident but tired.

Task: Write a status update for the head of engineering.

Format: Subject line, then three sections — Progress, Risks, Asks.
Under 200 words. Direct, no hype.
```

![Structured brief result](./images/acc2.png?raw=true "Structured brief: a usable status update")

<br><br>

5. Compare the two outputs. Note the difference role, context, task, and format made. Also look for any detail that wasn't in your brief (in the run above, "I'm working with the vendor on a recovery plan" was invented).

<br><br>

6. Now iterate instead of accepting draft one. Send:

```
Critique this update as a skeptical head of engineering would. List the five biggest things
that are unclear, missing, or buried, one line each.
```

![Skeptical critique](./images/acc3.png?raw=true "The critique flags vague and missing items")

<br><br>

7. Then send:

```
Rewrite the update fixing those issues. Keep it under 200 words. Do not invent facts: wherever information is missing, write [NEED: what's missing] instead.
```

![Rewrite with NEED markers](./images/acc4.png?raw=true "The rewrite marks missing facts instead of inventing them")

<br><br>

8. Read the final version. Every [NEED: …] marks a fact the AI does not have, which a person (you, a team lead, the vendor) has to supply. Without the last sentence of that prompt, models fill those gaps with made-up dates, percentages and names that read as fact. Also check that nothing invented in the first draft survived into this one.

<br><br>

9. Pick the one [NEED] whose answer would improve the update most, and note who you would ask for it.

<br><br>

**What just happened**

- Output quality tracked the context the model had. With one vague line it could only ask, hand back a template, or make things up. Role + context + task + format gave it what it needed.
- Ask about one of your real projects in an assistant that remembers your chats, and a vague prompt can come back as a confident update built from what it remembers — possibly the wrong project, or out of date. A brief puts you in control of what it works from.
- The critique → rewrite loop is the cheapest quality upgrade available — use it every time.
- Asked to "fix" missing information, a model will invent it. "Don't invent facts — mark what's missing" turns that risk into a to-do list.
- This pattern (brief, draft, critique, final) comes back several times today.

<p align="center">**[END OF LAB]**</p></br></br>

<a name="lab2"></a>

**Lab 2 — Ground it and verify**

**Purpose: See what an assistant does when it doesn't have the facts, then fix it by giving it the source document ("grounding") and asking it to cite the section for each claim.**

1. Start a new chat and ask about a specific company's policy without giving it any documents, as if it already had them:

```
What is the exact parental leave policy at Brightline Logistics Inc.?
Include the number of weeks and who qualifies.
```

If it produces specifics, be suspicious — Brightline Logistics is fictional. If it declines or hedges, as Claude does here, that's the better behavior; models vary, which is itself a lesson.

![Ungrounded question about a fictional company](./images/acc5.png?raw=true "Claude searches, finds nothing, and declines to guess")

<br><br>

2. Start a new chat. Paste this sample policy **plus** the grounded question below it:

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

3. Check the answer against the document. The right answer: **they are not yet eligible** (Section 1 — 12 months required). A good grounded answer catches this; a sloppy one jumps to "8 weeks, split allowed."

![Grounded answer with citations](./images/acc6.png?raw=true "Grounded answer catches the eligibility trap and cites each section")

<br><br>

4. If the answer missed the eligibility trap, push back:

```
Re-check Section 1 against the employee's length of service.
```

Watch it correct itself — and note that *you* caught it because the citations made checking possible.

<br><br>

5. Run the 30-second spot-check drill. Ask:

```
List every specific claim in your answer (numbers, dates, section references)
as a checklist I can verify against the document.
```

![Claim checklist](./images/acc7.png?raw=true "A checklist of every claim to verify against the document")

<br><br>

6. Verify each claim against the policy text. This is the habit: every name, number, date, and citation gets 30 seconds.

<br><br>

**What just happened**

- Ungrounded questions about your organization produce guesses dressed as answers.
- Grounding ("using only this… cite the section") turned trust into verification.
- The eligibility trap shows why citations matter: checkable answers fail loudly instead of silently.
- At company scale this is called RAG: software finds the right passages among thousands of documents and hands them to the AI, the way you pasted the policy here.

<p align="center">**[END OF LAB]**</p></br></br>

<a name="lab3"></a>

**Lab 3 — Review AI work before you sign it**

**Purpose: Check an AI-drafted recommendation the way you check any work that goes out under your name.**

1. Read this memo. Someone on your team drafted it with AI and wants you to forward it to leadership under your name.

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

3. Start a new chat and send the prompt below. The memo is already in it, so it is one copy and paste:

```
I am about to forward the recommendation below to our leadership
under my name. Someone on my team drafted it with AI. Review it for me
before I sign. In a table of at most 8 rows, short phrases only, list
each number or claim I should check, what looks wrong or unsupported,
and how to check it. Check the arithmetic yourself and show it in one
line. Then list what is missing that finance would ask for, three lines
at most. Do not invent facts: if you cannot tell, say so. Under 250
words in total.

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

9. (Optional — if you have time.) Read the note and change one line so it sounds like you.

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

**Purpose: Use AI to widen your options and stress-test a decision — without delegating the decision.**

1. Start a new chat and paste the scenario:

```
You are an analytical advisor to a department head. Be direct and expose your assumptions.

Scenario: Our 300-person company needs AI-assisted summarization of customer
support tickets (8,000/month). Options on the table: (A) buy the add-on from
our existing helpdesk vendor at $18/agent/month for 45 agents, (B) have our
platform team build it on an AI model rented from a vendor (~2 engineers,
1 quarter, then upkeep),
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

3. Run a premortem on the recommendation: imagine it has already failed, and ask why. Send:

```
It is six months later and we followed your recommendation. It failed badly.
Write the honest internal retrospective: the top three causes, in order of
likelihood, two sentences each.
```

![Premortem retrospective](./images/acc12.png?raw=true "The premortem ranks likely failure causes")

<br><br>

4. Turn the premortem into a plan:

```
Turn those three causes into a plan for the first 30 days of this
decision. As a table of at most 8 rows: the step, the cause it guards
against, who does it (a role, not a name), and the week. Under 150 words.
```

Check the plan the way you would check one from your team: does every cause have at least one step, and does every step have one owner and a week?

<br><br>

5. Force the other side. Send:

```
Now argue for a DIFFERENT option than the one you recommended, as my
toughest critic would — no softening. Under 150 words.
```

<br><br>

6. Decide. Write one sentence of your own — which option you'd pick and the single factor that decided it. (This step has no prompt. That's the point.)

<br><br>

**What just happened**

- AI produced an options analysis, a premortem, a 30-day plan, and a counter-argument in minutes — work that usually waits for a staff meeting.
- Step 4 is AI as a planner: a fast first draft of steps, owners and weeks. Whether each step has one owner and a real date is still your check.
- Asking for assumptions, failure modes, and the opposing case removes the model's agreeable default.
- Length limits ("under 250 words," "one line each") keep the output short enough to actually read — without them, this lab produces several thousand words.
- The comparison still left costs out. "2 engineers, 1 quarter, then upkeep" hides the other work those engineers won't do, security review, training, usage fees, and support. Ask "what costs are missing?" of every AI business case.
- Step 6 is the design: AI widened and stress-tested the thinking; the decision stayed with you.

<p align="center">**[END OF LAB]**</p></br></br>

<a name="lab5"></a>

**Lab 5 — Score your use cases**

**Purpose: Turn vague AI ideas from your organization into a scored, comparable shortlist.**

1. Open **[Worksheet 1: Use-Case Scorecard](https://skillrepos.github.io/tlsaccel/#ws1)**. Keep this page open too — you will switch between the two. The worksheet's sections are in the same order as the steps below, and each section is labelled with its step: **Lab 5, step 2**, **Lab 5, step 3**, and so on.

<br><br>

2. On your own (no AI yet), think of two or three candidate AI use cases from your organization. Two is enough. Type one into each box under **Lab 5, step 2: Your candidates** on the worksheet. Look for the green-flag pattern: high-volume, repetitive work whose results are easy to check. Name each one as a workflow: "triage inbound support tickets," not "use AI in support." Nothing comes to mind, or nothing you can share? Open the yellow **Need an example for step 2?** box just under those three boxes and tap an idea: it goes into your next empty box.

<br><br>

3. Under **Lab 5, step 3: Score each candidate** on the worksheet, give each of your candidates a score from 1 to 5 on each of the five criteria below. Higher is better, including for Risk: **for Risk, 5 means low risk and 1 means high risk.** Gut scores are fine; speed over precision.

| Criterion | What it means |
|---|---|
| **Value** | Which business number it improves (time, cost, quality or revenue), and whether the budget owner cares about that number |
| **Data readiness** | Whether the data it needs exists, is clean, and is yours to use |
| **Feasibility** | How easy it is to put in place: can a bought tool do it, and can one team own it? |
| **Risk** | What happens when it is wrong, and what sensitive data it touches. **Scored in reverse: 5 = low risk** |
| **Measurability** | Whether there is a "before" number today, and a result you can see within 90 days |

<br><br>

4. Now stress-test with AI. Start a new chat:

```
You are a skeptical AI program reviewer. For the use case below, ask me the
five hardest questions you'd ask before funding it, one line each, covering:
business value, data readiness, buy-vs-build, risk, and measurability.

Use case: [paste your top-scored candidate — generic description only,
no confidential details]
```

You do not have to type this prompt. The worksheet writes it for you under **Lab 5, step 4: Stress-test with AI**, as soon as one candidate has a name and all five scores. (Until then, that section says what is still missing.) Check the description there for confidential details, press **Copy the step 4 prompt with my use case in it**, and paste it into the new chat.

The screenshot uses a sample use case ("triage inbound support tickets"); yours will differ.

![Skeptical reviewer questions](./images/acc13.png?raw=true "Five hard funding questions for a sample use case")

<br><br>

5. Think through an honest answer to each question. You do not need to type your answers into the chat. Adjust any score the questions changed, then fill in the boxes under **Lab 5, step 5: Notes from the AI's questions** on the worksheet: the score you changed, the hardest question you could not answer, and (if you know) who could answer it.

<br><br>

6. Run the **blocker check** on the worksheet (under **Lab 5, step 6**) for your top-scored candidate. A blocker rules a use case out for now, however well it scores: if any box is ticked, move to your next candidate.

<br><br>

7. Under **Lab 5, step 7: The winner** on the worksheet, choose your winner from the list of your candidates, and complete the line below it: "**[Use case]** wins because **[one sentence]**."

<br><br>

8. Look back at your winner's five scores. Under **Lab 5, step 8** on the worksheet, choose the one you are least sure of, and write down what you would need to find out to settle it. You will enter which of the five it was in a poll on your phone.

<br><br>

**What just happened**

- Five scores forced the five conversations that decide pilot success — before any money moves.
- The AI's skeptical-reviewer questions exposed soft scores (data readiness is usually the one that drops).
- The blocker check catches what a total hides: one unusable data source or one missing owner outweighs four good scores.
- You now have a ranked shortlist — the input for Lab 6.
- Other scorecards may ask four questions instead of five, or score from 1 to 3 (the worksheet's quick version folds Data readiness into Feasibility). The conversations underneath are the same, and Risk and Measurability still have to pass.

<p align="center">**[END OF LAB]**</p></br></br>

<a name="lab6"></a>

**Lab 6 — Define pilot metrics**

**Purpose: Give your winning use case metrics built for a finance review — baseline, target, guardrail, stop rule.**

1. Open **[Worksheet 2: Pilot Metrics Charter](https://skillrepos.github.io/tlsaccel/#ws2)**. Its sections follow the steps below, each labelled with its step. Under **Lab 6, step 1**, your winning use case from Lab 5 is already filled in. Nothing of your own to work with? Open the yellow **Stuck?** box on the worksheet and press **Fill my empty boxes with the example**.

<br><br>

2. Under **Lab 6, step 2**, name the workflow owner and the sponsor: one person each. A job title or a made-up name is fine.

<br><br>

3. Under **Lab 6, step 3**, pick ONE primary metric — the one number that should improve if the pilot works. Choose which kind it is (time, cost, quality or adoption), then tap the measurement closest to yours.

<br><br>

4. Under **Lab 6, step 4**, write two numbers for that metric, in the same unit: what it is today (the baseline) and your 90-day target. No exact numbers? Write your best guess and add "guess".

<br><br>

5. Under **Lab 6, step 5**, tap one quality guardrail — the number that must NOT get worse while the primary metric improves.

<br><br>

6. Under **Lab 6, step 6**, read the two things the worksheet has written from your answers, and change anything that does not fit: your **definition of done** (one sentence that says what success looks like on day 90) and your **stop rule** (a check on day 45, and what you would have to see that day to stop early). The definition of done has this shape:

> "By day 90, [workflow] handled with AI assistance shows [metric] moving from [baseline] to [target], with [guardrail] maintained — or we stop and write down what we learned."

<br><br>

7. Now have an AI reviewer attack your plan the way a skeptic in finance would (a "red-team": a deliberate attack on your own plan, to find its weak spots first). Under **Lab 6, step 7**, press **Show my plan for the step 7 prompt**, take out anything confidential, then press **Copy the step 7 prompt with my plan in it**. Paste it into a new chat. This is what it copies:

```
You are a skeptical finance reviewer. Here is a pilot metrics plan:

[the worksheet puts your plan here]

Attack it: name the three biggest ways it could look good without real
improvement, be impossible to measure, or show a result the AI didn't cause. Give the smallest fix for each.
Under 150 words.
```

The reviewer names three weak spots, each with a fix. Where you agree, change the matching box. Then write the one that worries you most in **Biggest weak spot and the fix**. (The screenshot uses a sample plan.)

![Finance red-team](./images/acc14.png?raw=true "The reviewer finds where the sample plan could look good without real improvement")

<br><br>

**What just happened**

- Baseline-first design makes the result provable either way — the missing piece in most failed pilots.
- The guardrail stops the classic trap: speed up, quality down, "success."
- The stop rule makes killing a failed pilot a planned outcome, not an embarrassment.
- The AI reviewer looks for the parts that could look good without real improvement, while fixing them is still free.
- **The rest of the charter**, folded at the bottom of the worksheet (team, dates, costs, what happens if it succeeds), is for back at work.

<p align="center">**[END OF LAB]**</p></br></br>

<a name="lab7"></a>

**Lab 7 — Governance gut-check**

**Purpose: Apply the injection questions and autonomy tiers to a realistic agent proposal, make the approval call, and start your governance playbook.**

1. Open **[Worksheet 3: Governance Playbook](https://skillrepos.github.io/tlsaccel/#ws3)** and keep it open beside these steps. It is a one-page governance playbook: seven boxes that say how AI is used where you work. In this lab you write one decision on it (step 6) and its usage-policy headlines (step 8). Then read this proposal, which contains several planted red flags:

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

3. Apply the three injection questions from the deck: What untrusted content does it read? What private data can it reach? Can it send anything out? Count how many of the three you answer "yes" to. An agent with a yes to all three has what the deck calls the **lethal trifecta**: instructions hidden in something it reads can make it send your private data out.

<br><br>

4. Check your findings with AI. Start a new chat and send the prompt below. It explains its own terms and the proposal is already in it, so it is one copy and paste:

```
Review the AI agent proposal below as a security-minded AI governance
reviewer. Check it against two things:

(a) The prompt-injection "lethal trifecta". An AI agent is dangerous when
it has all three of these: it reads untrusted content (such as outside
email, attachments or web pages), it can reach private data, and it can
send things out.

(b) Three autonomy tiers. Tier 1, Assist: the AI drafts and a person does
the action. Tier 2, Review: the AI prepares the action and a named person
approves it. Tier 3, Autonomous: the AI acts on its own and people audit
afterward.

List every risk in the proposal. For each one say which part of the
trifecta it belongs to (if any) and which tier that action should run at.
Answer as a table (risk | trifecta part | tier), at most 6 rows. Then list
the three changes that matter most for a safe 90-day pilot, one line each.

PROPOSAL: "PayFast" invoice agent (from our finance systems team)

The agent monitors the shared accounts-payable inbox, reads each incoming
email and any attached invoice, looks up the supplier in our purchasing and
accounting systems using an admin service account, SENDS emails to
suppliers automatically about anything it classifies as routine, and pays
invoices up to $5,000 without approval to shorten payment time. It can also
browse supplier websites to confirm bank and contact details. Logging to be
added in phase 2. Pilot on all suppliers for 6 months.
```

![Governance review of PayFast](./images/acc15.png?raw=true "The review finds all three parts of the lethal trifecta and maps each risk")

<br><br>

5. Compare its list with yours. Key flags: a yes to all three injection questions, so the lethal trifecta is complete (it reads outside email, attachments and web pages; it can reach the purchasing and accounting systems; it sends email and payments), an admin account that can reach everything instead of only the access it needs, auto-send and auto-pay at Tier 3 (autonomous) on day one, bank details taken from websites an outsider controls, logging deferred, all suppliers instead of a scoped pilot, 6 months instead of 90 days.

<br><br>

6. Make the call: **approve, approve with conditions, or reject**. On **[Worksheet 3](https://skillrepos.github.io/tlsaccel/#ws3)**, under **Lab 7, step 6**, choose your call and write two sentences on why. If you chose conditions, name them — for example which actions move to Tier 2 (review: a named person approves), what access gets narrowed, what gets logged from day one.

<br><br>

7. When the instructor opens the new poll (Vote 2), vote on the same question as Vote 1 (the poll at the start of this part of the day): should an AI agent pay supplier invoices up to $5,000 with no person approving each one? Enter your decision from step 6. Your first vote stays as it was. If others chose differently, listen for one reason you had not thought of.

<br><br>

8. Stay on **Worksheet 3**. In Box 2 (Usage policy headlines), write three rules you'd publish this week, one line each.

Box 1 (Inventory: the AI tools already in use where you work, including shadow AI, meaning tools people use for work without approval) is for back at work.

<br><br>

**What just happened**

- A proposal that sounds efficient held all three parts of the lethal trifecta plus Tier 3 (autonomous) actions, day one.
- The fix pattern is standard: narrow access, insert human approval on consequential actions, log everything, scope the pilot.
- This is how you work with a technical team without being technical: you did not need to know how PayFast is built to ask what it reads, what it can reach, what it can do alone, and what gets logged.
- You made a decision, not just a list of risks, and saw how the room decided on the same facts. That comparison is what an approval meeting is.
- Your playbook now has its usage-policy headlines (Box 2). The inventory (Box 1) and Boxes 3–7 are for back at work; Lab 8 lets you put dates on them.

<p align="center">**[END OF LAB]**</p></br></br>

<a name="lab8"></a>

**Lab 8 — Your 90-day AI plan**

**Purpose: Leave with a concrete 30/60/90 plan and the paragraph you'll send your manager or team.**

1. Open **[Worksheet 4](https://skillrepos.github.io/tlsaccel/#ws4)**. Its first section shows what you already wrote on Worksheets 2 and 3, so you do not need them beside you. Every box says what goes in it; this lab asks for the ones marked **Required**.

<br><br>

2. Fill in two lines of Days 1–30 (SEE: find out what AI is already doing): your daily AI habit (one task you will do with AI every working day) and the date the one-page policy ships.

<br><br>

3. Fill in two lines of Days 31–60 (SCOPE: pick and plan one pilot): your pilot's owner (already filled in from Worksheet 2; change it if you need to) and the baseline collection dates (the two weeks in which you measure your primary metric before AI).

<br><br>

4. Fill in one line of Days 61–90 (SHIP: start the pilot in real work): the date of your **day-90 decision meeting**, where you decide whether to scale the pilot up, change it, or stop it, using the four tests on Worksheet 4. Pick a date about 90 days after the pilot starts (on or just after the day-90 date on Worksheet 2, if you set one). That is after this 90-day plan ends, which is fine. Book it now.

<br><br>

5. (Optional — if you have time; otherwise back at work.) Go to **A date for each open box of your playbook**, further down Worksheet 4, and give each of Boxes 3–7 a **decide by** date: the date by which you will have settled that box.

<br><br>

6. Draft the announcement. On the worksheet, under **Lab 8, steps 6–8**, press **Show my notes for the step 6 prompt**, take out names and anything confidential, then press **Copy the step 6 prompt with my notes in it**. Start a new chat and paste. This is the prompt it copies:

```
Turn these notes into one tight paragraph (under 120 words) I can send my
manager and team: we are piloting AI deliberately. Include: the use case,
the owner, the 90-day window with baseline and metric, the stop rule, the
weekly check on use, metric and guardrail, and one sentence on governance
(approved tools + usage policy shipping now).
Confident, no hype.

Notes: [the key lines from your worksheets: the worksheet puts them here]
```

![Announcement paragraph](./images/acc16.png?raw=true "Worksheet notes turned into a ready-to-send paragraph (sample notes)")

<br><br>

7. Now have the AI criticize the paragraph and then rewrite it, once:

```
Critique this paragraph as a skeptical reader in three bullets, then rewrite it. Don't invent facts — mark anything missing as [NEED: ...].
```

<br><br>

8. Copy the final paragraph onto the worksheet (or email it to yourself right now — that's better).

<br><br>

9. Save your work before you leave. Your answers are kept only in this browser on this device. At the bottom of Worksheet 4, press **Save all four as one PDF, or print**, and save the PDF (or press **Copy my answers** and email them to yourself).

<br><br>

10. If you're willing: pitch your pilot in the review round that follows — thirty seconds covering the workflow, owner, metric, and stop rule. The room gives one strength and one concern.

<br><br>

**What just happened**

- The 30/60/90 turned today's material into named owners and dated commitments.
- The announcement paragraph is the real test: if it names a workflow, metric, owner, and stop rule in 120 words, your plan is coherent.
- Putting the day-90 decision meeting on calendars now is what turns the plan into a commitment. At that meeting the four tests on Worksheet 4 decide: scale, change, or stop.
- If you dated the open boxes of your governance playbook, it is a started playbook, not a blank one. If not, dating them is your first job back at work.

<p align="center">**[END OF LAB]**</p></br></br>

<a name="lab9"></a>

**Lab 9 (Optional) — See an agent run in real code**

**Purpose: Watch a real AI agent run its think → act → observe loop in a live dev environment — no coding.**

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

4. While setup runs, read what you are about to start: one small program (`codespace-lab/agent/leader_demo_agent.py`) that gives an AI model a goal and four tools, then lets the model choose each next step until it is done.

- **The model:** Llama 3.2, a small open model running inside your Codespace. Nothing goes to an outside AI service.
- **The data:** all made up: three short support tickets (in `codespace-lab/agent/tickets/`; click one in the file list on the left to read it) and three sample customer records.
- **The four tools, all it can do:** list the tickets, read one, look up a customer, save a draft email. It cannot send email, change records or reach the internet.
- **Two built-in limits:** it reads all three tickets before answering, and it stops after 8 steps.

<br><br>

5. When setup is done (the terminal shows **Ollama is running.**), click into the terminal, type (or copy) this, and press Enter:

```
python codespace-lab/agent/leader_demo_agent.py
```

<br><br>

6. The agent's goal: *find the most urgent of three sample support tickets, check that customer's record, and draft a reply.* Watch the loop scroll by:

- **THINK** — the model decides its next step
- **ACT** — a tool call: reading a ticket, looking up the (sample) customer database
- **OBSERVE** — the tool's result goes back to the model

Each step takes a few seconds — longer on a busy machine. That wait is what "AI compute" means physically.

![The agent loop](./images/acc18.png?raw=true "THINK, ACT, OBSERVE repeating as the agent reads tickets")

<br><br>

7. When it finishes, read the summary at the bottom: the tools the agent was ALLOWED to use, and the email draft waiting for a human to approve (sending is a Tier 2, review, action). Read the draft closely — does it promise anything nobody approved, such as a fix by a certain time?

![Governance summary and draft](./images/acc19.png?raw=true "Allowed tools, one draft awaiting human approval")

<br><br>

8. Run it once more with a different goal:

```
python codespace-lab/agent/leader_demo_agent.py --goal "Summarize all three tickets for an executive"
```

Same loop, different tool choices — this time it has no reason to look up a customer or draft an email. The agent chose its own path.

<br><br>

9. Connect it back: this loop — with real tools, real credentials, and real autonomy decisions — is what a technical team means when it says "agent." The tool list and the Tier 2 approval you just saw are the controls a leader can ask about.

<br><br>

10. Answer four questions as the sponsor: What was the agent allowed to touch? Which action needed approval? What could have gone wrong? Would you authorize this agent in your organization?

<br><br>

11. When done, close the browser tab. Codespaces stop on their own when idle.

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
