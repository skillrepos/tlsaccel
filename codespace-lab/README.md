# Enterprise Leader AI Accelerator — Lab 9 environment

This repository backs **Lab 9 (optional): See what your teams see** from the
Enterprise Leader AI Accelerator workshop. It gives non-technical leaders a
one-click environment where a small AI agent runs visibly — THINK, ACT,
OBSERVE — on a local model.

## Run it

1. Sign in to GitHub (a free account works).
2. Click the green **Code** button → **Codespaces** tab → **Create codespace on main**.
3. Wait for setup to finish (3–5 minutes; a local AI model downloads automatically).
4. In the terminal at the bottom, run:

```
python codespace-lab/agent/leader_demo_agent.py
```

Follow the rest of the steps in the workshop's `labs.md` (Lab 9).

## What's in here

- `agent/leader_demo_agent.py` — the whole agent, one readable file
- `agent/tickets/` — three sample support tickets the agent works on
- `scripts/` — Codespace setup scripts (Python + Ollama with `llama3.2:3b`), run by the repo's top-level `.devcontainer/devcontainer.json`

## System requirements

Runs entirely inside GitHub Codespaces (4-core machine). Nothing to install
locally; the local model means no data leaves the environment.

## Troubleshooting

- **"connection refused" on port 11434** — Ollama isn't running yet:
  `bash codespace-lab/scripts/startOllama.sh`; retry when it prints "Ollama is running."
- **Model responses are slow** — normal; a 4-core Codespace takes a few seconds
  per THINK step (longer when busy). The wait is part of the lesson.
- **Agent makes an odd tool choice** — also part of the lesson; run it again
  and compare paths.

## License

For educational use only by the attendees of our workshops.
(c) 2026 Tech Skills Transformations and Brent C. Laster. All rights reserved.
