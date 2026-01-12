# BEAR Framework

**Break → Expand → Ascend → Rule**

A practitioner's model for attack progression when speed matters.

---

## What is BEAR?

BEAR is a simplified framework for understanding and communicating attacker progression during active incidents, red team debriefs, and executive briefings.

| Phase | Question | Transition |
|-------|----------|------------|
| **B**reak | Did they get in? | Outside → Inside |
| **E**xpand | How far did they move? | One → Many |
| **A**scend | Did they get real power? | User → Admin |
| **R**ule | What can they do now? | Access → Impact |

### Why BEAR?

MITRE ATT&CK is perfect for building detections. Lockheed Kill Chain is great for campaign analysis. But in the heat of an engagement or incident — they're overhead, not guidance. Too many boxes. Not enough focus.

> **BEAR is the "cut through the noise" layer — MITRE is where you go for comprehensive mapping.**
> 
> The framework's value is in the speed and focus, not exhaustive coverage.

---

## Interactive Tool

The included HTML file (`bear-framework.html`) is a single-page, offline-capable reference tool with:

- **Three View Modes**
  - *Tactical* — Attacker objectives (red team lens)
  - *Defensive* — Controls + detections (blue team lens)
  - *Executive* — Business risk questions (leadership lens)

- **Framework Overlays** — Toggle mappings to MITRE ATT&CK, NIST CSF 2.0, ISO 27001:2022, and CIS Controls v8

- **Keyboard Shortcuts** — `T/D/X` for modes, `1-4` for phases, `M/N/I/C` for overlays

No dependencies. No build step. Just open it in a browser.

---

## When to Use

| Scenario | How BEAR Helps |
|----------|----------------|
| 🔴 Active Incident | Quickly assess attacker position and risk |
| 🟡 Red Team Debrief | Structure findings by impact, not just technique |
| 🟢 Control Validation | Test defenses at each phase, find gaps |
| 🔵 Executive Briefing | Translate technical status to business risk |

---

## Credits

**BEAR Framework Concept:** Ivan Novikov ([Wallarm](https://www.wallarm.com))  
**Defensive Control Mapping & Tool:** Christopher Six

---

## License

MIT — Use it, fork it, make it yours.
