# Worksheet 1 — AI Use-Case Scorecard
*Enterprise Leader AI Accelerator · Lab 5*

**Before we start (write this first):** How confident am I today that I could sponsor an AI pilot and defend it to finance? (1 = not at all, 5 = fully) → **Start of day: ____**  **End of day: ____**

---

List **three** candidates, then score each **1–5** on every criterion. Higher is better. **Risk is scored in reverse: 5 = low risk.**

| Criterion | What it means | What a 5 looks like | What a 1 looks like |
|---|---|---|---|
| **Value** | Which business number it improves (time, cost, quality or revenue), and whether the budget owner cares about that number | A number the budget owner is measured on moves | "It would be innovative" |
| **Data readiness** | Whether the data it needs exists, is clean, and is yours to use | Data exists, is clean, and we may use it | Data is scattered, dirty, or legally unclear |
| **Feasibility** | How easy it is to put in place: can a bought tool do it, and can one team own it? | A bought tool does it, or one team can own it end to end | Needs custom build + three teams + new data pipelines |
| **Risk** (5 = low) | What happens when it is wrong, and what sensitive data it touches | Internal, human-reviewed, reversible | Customer-facing, regulated, irreversible |
| **Measurability** | Whether there is a "before" number today, and a result you can see within 90 days | Baseline exists; result visible in 90 days | No baseline; benefits "strategic" |

## Candidates

| # | Use case (name it as a workflow) | Value | Data | Feas. | Risk | Meas. | **Total** |
|---|----------------------------------|:-----:|:----:|:-----:|:----:|:-----:|:---------:|
| 1 |                                  |       |      |       |      |       |           |
| 2 |                                  |       |      |       |      |       |           |
| 3 |                                  |       |      |       |      |       |           |

*Example row: Triage inbound support tickets — Value 4, Data 4, Feas. 5, Risk 4, Meas. 5, Total 22.*

**First-pilot rule:** a first pilot needs **4+ on Risk and 4+ on Measurability**, whatever its total.

**Quick version, for judging one proposal someone brings you:** ask four questions instead of five (fold Data readiness into Feasibility). The rule is the same: Risk and Measurability must pass, however good the Value story is.

## Blocker check (Lab 5, step 6)

A blocker is something that rules a use case out for now, however well it scores. **A high score never overrides a blocker.** For your top-scored candidate, tick anything that is true:

- ☐ We cannot legally or contractually use the data it needs
- ☐ Nobody in the business would be accountable for it
- ☐ It would make decisions on its own that a person should make
- ☐ We have no way to measure the result
- ☐ Plain automation (fixed rules, no AI) would do the job

Any box ticked → fix that first, or move to your next candidate.

## The winner (Lab 5, step 7)

| Box | What goes in it | Example | Your answer |
|---|---|---|---|
| **My winner** | The candidate you choose as your first pilot | Triage inbound support tickets | |
| **…wins because (one sentence)** | Why this use case should be your first pilot: one sentence that says what makes it a safe bet | It is high-volume, an agent checks every draft, and handling time is already measured. | |

## Notes from the AI stress-test (Lab 5, steps 4–5 and 8)

The AI reviewer in step 4 asks five hard questions about your top candidate. These boxes hold what you learned from them.

| Box | What goes in it | Example | Your answer |
|---|---|---|---|
| **Score I changed and why** | If the AI's questions made you change one of your five scores: which score, from what to what, and why. Nothing changed? Write "none" | Data readiness, 4 down to 3: agents do not all label tickets the same way. | |
| **Hardest question I couldn't answer yet** | The one question from the AI reviewer that you could not answer today | What does one AI-drafted reply cost at 8,000 tickets a month? | |
| **Who in my org can answer it** | The person who could answer that question: a name or a job title | The helpdesk administrator, and the vendor's account manager. | |
| **Score I am least sure of** | Of your winner's five scores, the one you trust least. You will enter this one in the poll on your phone | Data readiness | |
| **What I would need to find out to settle it** | What you would have to check or measure to be sure of that score | Pull 200 past tickets and count how many carry the right label. | |

---
*(c) 2026 Tech Skills Transformations and Brent C. Laster. All rights reserved.*
