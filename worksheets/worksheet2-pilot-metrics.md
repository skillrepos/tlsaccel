# Worksheet 2 — Pilot Metrics Charter
*Enterprise Leader AI Accelerator · Lab 6*

**What this is:** a one-page plan for your pilot. It says who runs it, which one measurement should improve, what must not get worse, and when you would stop. Each box says what goes in it and gives an example from a made-up company. Boxes marked **Required** are the ones the lab asks for today; **Optional** ones are for back at work. Nothing has to be exact today: a best guess, marked "guess", is a good answer.

Fill it in on the worksheets page, which saves what you type on your own device: https://skillrepos.github.io/tlsaccel/#ws2

## Lab 6, step 2: Pilot header

| Box | Needed in the lab? | What goes in it | Example | Your answer |
|---|---|---|---|---|
| **Use case** | Required | The use case you picked as your winner on Worksheet 1 | Triage inbound support tickets | |
| **Workflow owner** | Required | The one person who will run the pilot day to day. One person, not a team: a name or a job title | Dana Ruiz, Support Operations | |
| **Sponsor** | Required | The one person who pays for the pilot and can clear roadblocks, often the workflow owner's manager: a name or a job title | Priya Shah, who runs Customer Service | |
| **Pilot team** | Required | The one group of people who will use the AI tool during the pilot, and about how many they are. No names needed | One support shift: 12 of the 45 agents, plus the helpdesk administrator | |
| **Start date** | Required | The first day the pilot team uses the AI tool in real work | January 5, 2027 | |
| **Day-90 date** | Required | The last day of the pilot: 89 days after the start date (the start date is day 1). On the worksheets page this is worked out for you; change it if your pilot must end on another day | March 31, 2027 (this team chose the end of the quarter, a few days short of 90) | |
| **Buy / partner / build** | Optional | How you will get the AI tool. Buy: a product that already does this job. Partner: a vendor fits a tool to your data and way of working. Build: your own engineers make it. Most first pilots buy | Buy: the add-on our helpdesk vendor sells | |

## Lab 6, steps 3–4: Primary metric (pick ONE)

| Family | Example metrics |
|---|---|
| Time | hours per task, cycle time, backlog age |
| Cost | cost per ticket/document/case, contractor spend |
| Quality | error/rework rate, first-pass acceptance |
| Adoption | weekly active users, % of volume through the tool |

| Box | Needed in the lab? | What goes in it | Example | Your answer |
|---|---|---|---|---|
| **My primary metric** | Required | The one measurement that should improve if the pilot works. Say what is measured and in what unit (minutes, dollars, percent or a count) | Median handling time per support ticket (minutes) | |
| **Baseline plan** | Required | How you will find out what your primary metric is today, before AI: who looks it up, from where, and for which two weeks | The helpdesk administrator pulls handling times for the pilot shift from the helpdesk, for two weeks in December | |
| **Baseline value** | Required | What your primary metric is today, before AI. Not sure? Write your best guess and add "guess": measuring it is the pilot's first job | 11 minutes (handling time per ticket today) | |
| **90-day target** | Required | What you want your primary metric to be by day 90, in the same unit as the baseline value. A number, not "better" | 8 minutes (down from 11) | |

## Lab 6, step 5: Quality guardrail

The number that must NOT get worse while the primary metric improves:

| Box | Needed in the lab? | What goes in it | Example | Your answer |
|---|---|---|---|---|
| **Guardrail** | Required | A second measurement, one that shows quality. It must not get worse while your primary metric improves | First-contact resolution (the share of tickets solved in one reply) | |
| **Current value** | Optional | What your guardrail is today. A guess is fine if you mark it | 72% (of tickets are solved in one reply today) | |

## Lab 6, step 6: Definition of done

> "By **[date]**, **[workflow]** handled with AI assistance shows **[metric]** moving from **[baseline]** to **[target]**, with **[guardrail]** maintained — or we stop and write down what we learned."

| Box | Needed in the lab? | What goes in it | Example | Your answer |
|---|---|---|---|---|
| **My definition of done** | Required | One sentence built from the boxes above: the day-90 date, the use case, the primary metric with its baseline value and 90-day target, and the guardrail | By March 31, 2027, support-ticket triage handled with AI assistance shows median handling time per support ticket moving from 11 minutes to 8 minutes, with first-contact resolution held at or above 72% — or we stop and write down what we learned. | |

## Lab 6, step 7: Stop rule

A stop rule is the result that would make you end the pilot early, decided before you start.

| Box | Needed in the lab? | What goes in it | Example | Your answer |
|---|---|---|---|---|
| **Stop check on day** | Required | The day of the pilot, about halfway through, when you look at the primary metric and the guardrail and decide whether to carry on. A number from 1 to 89 | 42 | |
| **We stop early if we see** | Required | What the primary metric or the guardrail would have to show on that day for you to stop the pilot early | Handling time is still 11 minutes or more, or fewer than 72% of tickets are solved in one reply for two weeks running | |

## Lab 6, steps 8–9: Finance red-team findings

A red-team is a deliberate attack on your own plan, to find its weak spots before someone else does. In step 8 an AI reviewer plays a skeptic from finance and names three weak spots, each with a fix. In step 9 you write down the two that matter most.

| Box | Needed in the lab? | What goes in it | Example | Your answer |
|---|---|---|---|---|
| **Most gameable part and the fix** | Required | "Gameable" means the primary metric could look better without the work getting better. Write the weak spot the AI reviewer found in your plan, and how you will close it | Agents can look faster by splitting one problem into two tickets. Fix: also count reopened tickets and tickets per customer problem. | |
| **Attribution risk and the fix** | Required | Would the primary metric have improved anyway, without the AI? Write why it might, and how you will tell the difference | Ticket volume dips every January, so handling times fall anyway. Fix: compare the pilot shift with a shift that does not use the tool. | |

## Lab 6, step 10: What the pilot needs

**For step 10 of Lab 6, after the AI review.** What it will take to run the pilot for 90 days: money, people, and a limit on what the AI tool may spend. Rough answers are fine.

| Box | Needed in the lab? | What goes in it | Example | Your answer |
|---|---|---|---|---|
| **Money** | Required | What the pilot will cost in money over the 90 days: licenses, usage fees, vendor help. A rough figure is fine | $18 per agent per month × 12 agents = $216 a month | |
| **People and time** | Required | Who will work on the pilot, and about how many hours a week each | Dana, 4 hours a week; each pilot agent, one hour of training | |
| **AI running cost per task** | Optional | What the AI tool charges to do the job once, for example one ticket or one document. "Not measured yet" is a fine answer today: it is your first question for the team | Not measured yet: first question for the vendor | |
| **Monthly cap** | Optional | The most you will let the AI tool spend in one month | $500 | |
| **Who gets the alert** | Optional | The one person who is told when the month's spending gets close to the cap | Dana Ruiz | |

## Lab 6, step 10: If it succeeds

**Also for step 10 of Lab 6.** What happens after day 90 if the pilot works: who keeps it going, and what it costs once everyone uses it.

| Box | Needed in the lab? | What goes in it | Example | Your answer |
|---|---|---|---|---|
| **Who runs it after day 90** | Required | Who keeps the AI tool running once the pilot is over | Support Operations, under Dana Ruiz | |
| **Rough cost at full volume, and who pays** | Required | What the AI tool will cost when everyone who should use it does, and whose budget covers it | $18 × 45 agents = $810 a month, about $9,700 a year, from the Customer Service budget | |

## Seven questions for the team proposing the pilot (take-home)

Tick each one you already have a clear answer to. The unticked ones are your next conversation.

- ☐ 1. What business problem are we solving — and who has it?
- ☐ 2. Why does this need AI? Would simpler, rule-based automation do?
- ☐ 3. What data does it need — does it exist, is it accurate, may we use it, and do we agree what the numbers mean?
- ☐ 4. What happens when the AI is wrong — who notices, who fixes it?
- ☐ 5. How much can it do on its own — what needs a person to approve?
- ☐ 6. How will we know it worked — baseline, target, guardrail?
- ☐ 7. What will it cost to run and to scale — not just to pilot?

---
*(c) 2026 Tech Skills Transformations and Brent C. Laster. All rights reserved.*
