# Enterprise Leader AI Accelerator
**Tech Leader Summit · Wednesday, December 2, 2026 · Workshop (4 × 90 min) · Revision 1.2**

The essential one-day leader's playbook for understanding and applying AI — for managers, project leaders, and business stakeholders who make AI decisions without doing the implementation.

## What's here

| File / folder | What it is |
|---|---|
| `labs.md` | All 9 hands-on labs, step by step, with prompts to copy and screenshots |
| `worksheets/` | 3 fill-in worksheets: use-case scorecard, pilot metrics charter, governance playbook + 30/60/90 |
| `codespace-lab/` | Files for the optional Lab 9 (runs in GitHub Codespaces) |
| `images/` | Screenshots used in labs.md |

---

## Before you arrive (about 10 minutes)

You need **one free account** for Labs 1–8, and a second free account **only if** you want to do the optional Lab 9. **No API keys, credit cards, or software installs are needed.**

### 1. An AI assistant account (required, Labs 1–8)

The screenshots in labs.md use **Claude**, so that's the simplest choice. ChatGPT, Microsoft Copilot, or Gemini work too. If your company provides an approved AI tool, use that one.

To set up a free Claude account:

1. Go to **https://claude.com** in your browser.
2. Click **Continue with Google** (fastest if you have a Google account) or **Continue with email**.

   ![Claude sign-up page](./images/setup1.png?raw=true "claude.com: Continue with Google or Continue with email")

3. If you chose email: enter your address, then open the sign-in email Claude sends you and follow its link or code.
4. Complete the short profile questions Claude asks. It may also ask you to verify a phone number.
5. You're in when you see a chat box. Send `Hello` to confirm it answers.

**About the free plan:** there is no fixed message count; usage limits reset in 5-hour windows. A full day of labs may hit the limit. If it does, switch to a different assistant for the rest of that lab — every lab works in any of them.

### 2. A GitHub account (optional, Lab 9 only)

Lab 9 lets you watch a real AI agent run in a browser-based workspace called a Codespace. Skip this if you don't plan to do Lab 9.

1. Go to **https://github.com/signup**.
2. Enter your email, a password, and a username when prompted.
3. Enter the verification code GitHub emails you.
4. Done. Free accounts include 120 Codespaces "core hours" a month; Lab 9 uses about 1 of them.

If you already have a GitHub account, sign in and you're ready.

### 3. Check your laptop (2 minutes)

Company laptops sometimes block AI sites or Codespaces. Before the workshop, make sure these load on the laptop you'll bring:

- **https://claude.ai** (or your chosen assistant)
- **https://github.com/codespaces** (Lab 9 only)

If either is blocked, bring a personal laptop or tablet, or ask your IT team before the event.

---

## During the workshop

- Open **labs.md** in this repo (or the printed copy) and follow along. Every prompt is written out for you to copy.
- Keep the **worksheets** open — Labs 5–8 fill them in. Copy the files or print them; they're yours to keep.
- **One rule on data:** use the sample scenarios in the labs, or non-confidential examples from your own work. Treat the tools as public for the day.

## Troubleshooting

| Problem | What to do |
|---|---|
| "You've reached your usage limit" | Switch to another assistant (ChatGPT, Gemini, Copilot) for the rest of the lab |
| The assistant uses your files or email in an answer | Turn off connected apps in the chat menu for the workshop, or use a new chat |
| Your answers look different from the screenshots | Normal — AI answers vary. Check that the *pattern* the step describes is there |
| Lab 9: VS Code asks "Do you trust the authors…?" | Click **Trust Folder & Continue** |
| Lab 9: "connection refused" when running the agent | Run `bash codespace-lab/scripts/startOllama.sh`. When it prints **Ollama is running.**, try again. If it says Ollama is not installed, run the command it shows (about 2 minutes) |

## License

For educational use only by the attendees of our workshops.
(c) 2026 Tech Skills Transformations and Brent C. Laster. All rights reserved.
