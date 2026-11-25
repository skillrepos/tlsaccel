# Worksheet 2 — Pilot Metrics Charter
*Enterprise Leader AI Accelerator · Lab 6*

**What this is:** a short plan for your pilot: who runs it, which one measurement should improve, what must not get worse, and when you would stop. The sections follow Lab 6's steps in order. Where a number is asked for, a best guess, marked "guess", is a good answer. Boxes marked **Required** are the ones the lab asks for today; **Optional** ones are for back at work.

Fill it in on the worksheets page, which saves what you type on your own device, offers lists to pick from, and writes the step 6 boxes for you: https://skillrepos.github.io/tlsaccel/#ws2

## Lab 6, step 1: Your use case

| Box | Needed in the lab? | What goes in it | Example | Your answer |
|---|---|---|---|---|
| **Use case** | Required | The use case you picked as your winner on Worksheet 1. The worksheets page copies it here from Worksheet 1; change it if you want | Triage inbound support tickets | |

## Lab 6, step 2: Owner and sponsor

| Box | Needed in the lab? | What goes in it | Example | Your answer |
|---|---|---|---|---|
| **Workflow owner** | Required | The one person who will run the pilot day to day. One person, not a team: a job title, or a name (a made-up one is fine) | Dana Ruiz, Support Operations | |
| **Sponsor** | Required | The one person who pays for the pilot and can clear roadblocks, often the workflow owner's manager: a job title, or a name (a made-up one is fine) | Priya Shah, who runs Customer Service | |

## Lab 6, step 3: Primary metric (pick ONE)

The one measurement that should improve if the pilot works. First choose which kind it is:

| Family | Example metrics |
|---|---|
| Time | hours per task, cycle time, backlog age |
| Cost | cost per ticket/document/case, contractor spend |
| Quality | error/rework rate, first-pass acceptance |
| Adoption | weekly active users, % of volume through the tool |

| Box | Needed in the lab? | What goes in it | Example | Your answer |
|---|---|---|---|---|
| **My primary metric** | Required | The one measurement that should improve if the pilot works. Say what is measured and in what unit (minutes, dollars, percent or a count) | Median handling time per support ticket (minutes) | |

## Lab 6, step 4: Two numbers: today and day 90

Your primary metric as it is today, and where you want it after 90 days of the pilot. Nobody has exact numbers in the room: write your best guess and add "guess".

| Box | Needed in the lab? | What goes in it | Example | Your answer |
|---|---|---|---|---|
| **Baseline value** | Required | What your primary metric is today, before AI. Not sure? Write your best guess and add "guess": measuring it is the pilot's first job | 11 minutes (handling time per ticket today) | |
| **90-day target** | Required | What you want your primary metric to be by day 90, in the same unit as the baseline value. A number, not "better" | 8 minutes (down from 11) | |

## Lab 6, step 5: Quality guardrail

The number that must NOT get worse while the primary metric improves. Common ones: error or rework rate, customer satisfaction score, first-pass acceptance, complaints or escalations per month, first-contact resolution.

| Box | Needed in the lab? | What goes in it | Example | Your answer |
|---|---|---|---|---|
| **Guardrail** | Required | A second measurement, one that shows quality. It must not get worse while your primary metric improves | First-contact resolution (the share of tickets solved in one reply) | |

## Lab 6, step 6: Definition of done and stop rule

> "By **day 90**, **[workflow]** handled with AI assistance shows **[metric]** moving from **[baseline]** to **[target]**, with **[guardrail]** maintained — or we stop and write down what we learned."

| Box | Needed in the lab? | What goes in it | Example | Your answer |
|---|---|---|---|---|
| **My definition of done** | Required | One sentence built from your answers above: the use case, the primary metric with its baseline value and 90-day target, and the guardrail | By day 90, support-ticket triage handled with AI assistance shows median handling time per support ticket moving from 11 minutes to 8 minutes, with first-contact resolution held at or above 72% — or we stop and write down what we learned. | |

A stop rule is the result that would make you end the pilot early, decided before you start.

| Box | Needed in the lab? | What goes in it | Example | Your answer |
|---|---|---|---|---|
| **Stop check on day** | Required | The day of the pilot when you look at the primary metric and the guardrail and decide whether to carry on. The worksheets page suggests day 45, halfway through; any number from 1 to 89 works | 42 | |
| **We stop early if we see** | Required | What the primary metric or the guardrail would have to show on that day for you to stop the pilot early | Handling time is still 11 minutes or more, or fewer than 72% of tickets are solved in one reply for two weeks running | |

## Lab 6, step 7: Finance red-team finding

A red-team is a deliberate attack on your own plan, to find its weak spots before someone else does. In step 7 an AI reviewer plays a skeptic from finance and names three weak spots, each with a fix. You write down the one that matters most.

| Box | Needed in the lab? | What goes in it | Example | Your answer |
|---|---|---|---|---|
| **Biggest weak spot and the fix** | Required | Of the three weak spots the AI reviewer named, the one that worries you most, and what you will change to close it | Agents can look faster by splitting one problem into two tickets. Fix: also count reopened tickets and tickets per customer problem. | |

## Back at work: the rest of the charter

No lab step asks you to fill these in today. They finish the charter: fill them in back at work, with the people who have the numbers.

### Pilot team and dates

| Box | Needed in the lab? | What goes in it | Example | Your answer |
|---|---|---|---|---|
| **Pilot team** | Optional | The one group of people who will use the AI tool during the pilot, and about how many they are. No names needed | One support shift: 12 of the 45 agents, plus the helpdesk administrator | |
| **Start date** | Optional | The first day the pilot team uses the AI tool in real work | January 5, 2027 | |
| **Day-90 date** | Optional | The last day of the pilot: 89 days after the start date (the start date is day 1). On the worksheets page this is worked out for you; change it if your pilot must end on another day | March 31, 2027 (this team chose the end of the quarter, a few days short of 90) | |
| **Buy / partner / build** | Optional | How you will get the AI tool. Buy: a product that already does this job. Partner: a vendor fits a tool to your data and way of working. Build: your own engineers make it. Most first pilots buy | Buy: the add-on our helpdesk vendor sells | |

### Measuring it

| Box | Needed in the lab? | What goes in it | Example | Your answer |
|---|---|---|---|---|
| **Baseline plan** | Optional | How you will find out what your primary metric is today, before AI: who looks it up, from where, and for which two weeks | The helpdesk administrator pulls handling times for the pilot shift from the helpdesk, for two weeks in December | |
| **Guardrail's current value** | Optional | What your guardrail is today. A guess is fine if you mark it | 72% (of tickets are solved in one reply today) | |

### A second weak spot

| Box | Needed in the lab? | What goes in it | Example | Your answer |
|---|---|---|---|---|
| **Attribution risk and the fix** | Optional | Would the primary metric have improved anyway, without the AI? Write why it might, and how you will tell the difference | Ticket volume dips every January, so handling times fall anyway. Fix: compare the pilot shift with a shift that does not use the tool. | |

### What the pilot needs

What it will take to run the pilot for 90 days: money, people, and a limit on what the AI tool may spend. Rough answers are fine.

| Box | Needed in the lab? | What goes in it | Example | Your answer |
|---|---|---|---|---|
| **Money** | Optional | What the pilot will cost in money over the 90 days: licenses, usage fees, vendor help. A rough figure is fine | $18 per agent per month × 12 agents = $216 a month | |
| **People and time** | Optional | Who will work on the pilot, and about how many hours a week each | Dana, 4 hours a week; each pilot agent, one hour of training | |
| **AI running cost per task** | Optional | What the AI tool charges to do the job once, for example one ticket or one document. "Not measured yet" is a fine answer today: it is your first question for the team | Not measured yet: first question for the vendor | |
| **Monthly cap** | Optional | The most you will let the AI tool spend in one month | $500 | |
| **Who gets the alert** | Optional | The one person who is told when the month's spending gets close to the cap | Dana Ruiz | |

### If it succeeds

What happens after day 90 if the pilot works: who keeps it going, and what it costs once everyone uses it.

| Box | Needed in the lab? | What goes in it | Example | Your answer |
|---|---|---|---|---|
| **Who runs it after day 90** | Optional | Who keeps the AI tool running once the pilot is over | Support Operations, under Dana Ruiz | |
| **Rough cost at full volume, and who pays** | Optional | What the AI tool will cost when everyone who should use it does, and whose budget covers it | $18 × 45 agents = $810 a month, about $9,700 a year, from the Customer Service budget | |

### Seven questions for the team proposing the pilot

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
