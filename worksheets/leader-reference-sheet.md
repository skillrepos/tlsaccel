# Leader's AI Reference Sheet
*Enterprise Leader AI Accelerator · one page to keep on your desk*

## Nine terms

| What you buy | How AI connects to your business | Limits to know |
|---|---|---|
| **Model** — the trained engine | **Agent** — AI given a goal and tools; it plans and acts | **Context window** — the model's working memory per conversation |
| **Assistant** — a chat product built on a model | **RAG** — retrieving your documents so answers use your data | **Token** — the word-chunks AI reads, writes, and bills by |
| **Copilot** — AI built into a tool you already use | **Fine-tuning** — extra training to specialize a model | **Hallucination** — fluent, confident, and wrong |

Also: **Inference** — running the model: each question or task you send it. Training is done once by the vendor; inference is what you pay for every time it is used.

## Brief it like a capable new hire

**Role** (who it should be) · **Context** (what it needs to know) · **Task** (exactly what you want) · **Format** (what good looks like).
Then: "Critique this draft." → "Rewrite it fixing those issues. Don't invent facts — mark anything missing as [NEED: …]."

## Four checking habits

1. Decide the stakes first: brainstorm → use freely · internal draft → skim · external or a decision → check line by line.
2. Check every name, number, date, quote, and link against a source.
3. Ask it to argue against itself: "What's weakest here? What did you assume?"
4. Whoever ships it owns it. "The AI said so" is never a defense.

## Before you sign AI-drafted work

Ask: "What did the AI write, and what did you check?" · Redo one number yourself · Ask where each figure came from · Look for what is missing: costs, risks, the other side · Then sign it, send it back, or reject it.

*Writing tips:* for a hard message, let AI draft the structure and write the heart yourself. To sound like you, paste 3–5 sentences of your own writing and ask it to match that voice.

## Does this need AI?

| Situation | Likely approach |
|---|---|
| Fixed rules, predictable inputs | Plain automation — no AI needed |
| Summarizing, drafting, interpreting language | AI assistant, with a person reviewing |
| Answers that depend on your own documents | Grounded AI (RAG), with citations |
| Multi-step tasks that need tools and choices | AI agent, with a person approving what matters |
| High-stakes decisions about people, money, safety | A person leads; AI assists under tight controls |

## Seven questions to ask your technical team before you fund a pilot

1. What business problem are we solving — and who has it?
2. Why does this need AI? Would simpler automation do?
3. What data does it need — does it exist, is it accurate, may we use it, and do we agree what the numbers mean?
4. What happens when the AI is wrong — who notices, who fixes it?
5. How much can it do on its own — what needs a person to approve?
6. How will we know it worked — baseline, target, guardrail?
7. What will it cost to run and to scale — not just to pilot?

*On question 7:* ask what one task costs — measured, not estimated — and ask again whenever the model changes. The price list is not the bill.

## Working with your technical team

**What they need from you:** a named problem in one workflow · access to the data and to the people who do the work today · one owner who can decide · the yardstick (baseline, target, guardrail, stop rule) agreed before the build · room to say "it doesn't need AI".
**Who decides what:** you decide the problem, the metric, the risk you accept, and whether to scale or stop. They decide how it is built and tested, and which model and tools. Decide together: buy, partner or build; what it may do alone; what it costs to run.

## A pilot that can prove value

One workflow · one team · 90 days · one owner (plus a sponsor) · one primary metric · one guardrail · a stop rule written before you start.

## Before you scale — all four must be true

The technology works on real cases · people use it in their daily work · the metric moved and the guardrail held · someone owns it and the cost at full volume is known.

## Any AI agent proposal: three questions and three tiers

- What untrusted content does it read? What private data can it reach? Can it send anything out? (All three together is the danger zone.)
- **Tier 1 — Assist:** AI drafts, a person does. **Tier 2 — Review:** AI prepares the action, a named person approves. **Tier 3 — Autonomous:** low-risk, reversible actions only, with logs and spot checks — earned per use case.
- **Four limits before any agent runs:** a step limit per task · a dollar cap per task · a monthly cap with an alert · a named person who gets the alert.

---
*(c) 2026 Tech Skills Transformations and Brent C. Laster. All rights reserved.*
