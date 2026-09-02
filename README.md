# BEAR Framework

**Break → Expand → Ascend → Rule**

A concise practitioner model for communicating attacker progression when speed and shared context matter.

## What is BEAR?

BEAR reduces an intrusion to four operational questions:

| Phase | Operational question | Transition | Representative ATT&CK tactics |
|---|---|---|---|
| **Break** | Did the adversary get in? | Outside → Inside | Initial Access, Execution |
| **Expand** | How far did the adversary move? | One → Many | Persistence, Discovery, Lateral Movement, Command and Control |
| **Ascend** | Did the adversary gain privileged control? | User → Administrator | Privilege Escalation, Credential Access |
| **Rule** | What impact can the adversary create? | Access → Impact | Collection, Exfiltration, Impact |

BEAR is a communication layer, not a replacement for MITRE ATT&CK, the Lockheed Martin Cyber Kill Chain, NIST CSF, ISO/IEC 27001, or CIS Controls. Intrusions are not always linear: attackers can revisit phases, pursue several phases in parallel, or achieve impact without completing every phase.

## Interactive tool

Open [`bear-framework.html`](./bear-framework.html) directly in a browser. It is a single-file, offline-capable reference with no build step and no runtime dependencies.

The printable reference is [`BEAR-Framework-Defensive-Controls-v2.0.pdf`](./output/pdf/BEAR-Framework-Defensive-Controls-v2.0.pdf).

- **Tactical view** — attacker objectives and representative behaviors
- **Defensive view** — objectives, priority controls, and detection opportunities
- **Executive view** — business-focused controls and questions
- **Framework overlays** — practitioner alignments to MITRE ATT&CK v19.2, NIST CSF 2.0, ISO/IEC 27001:2022 Annex A, and CIS Controls v8.1
- **Keyboard shortcuts** — `T`, `D`, or `X` for views; `1`–`4` for phases; `M`, `N`, `I`, or `C` for overlays; `Esc` to collapse a phase

The detailed alignment rationale and sources are maintained in [`MAPPINGS.md`](./MAPPINGS.md). The mappings are representative and non-authoritative; they are not one-to-one equivalences or certification evidence.

## When to use it

| Scenario | How BEAR helps |
|---|---|
| Active incident | Establish a fast, shared view of attacker position, reachable assets, and likely impact |
| Red-team debrief | Organize findings by operational progression and demonstrated impact |
| Control validation | Test whether prevention, detection, containment, and recovery capabilities interrupt each phase |
| Executive briefing | Translate technical observations into risk and decision points |

## Version 2.0 review

The September 2026 review:

- migrated stale NIST CSF 1.1 identifiers to the CSF 2.0 Core structure;
- updated MITRE ATT&CK names and mappings to Enterprise ATT&CK v19.2;
- tightened ISO/IEC 27001:2022 Annex A and CIS Controls v8.1 safeguard alignments;
- documented mapping scope, limitations, and authoritative sources;
- removed the remote font request so the HTML is genuinely offline-capable;
- improved keyboard and screen-reader behavior; and
- aligned repository and document attribution to Christopher Six's profiles.

## Credits and maintenance

- **BEAR Framework concept:** Ivan Novikov ([LinkedIn](https://www.linkedin.com/in/d0znpp/), Wallarm), as credited by the original project
- **Defensive control mapping, interactive tool, and repository maintenance:** [Christopher Six](https://github.com/christophersix66) ([LinkedIn](https://www.linkedin.com/in/christophersix-futureproofwithsix/))

## License

[MIT](./LICENSE) — use it, fork it, and adapt it subject to the license terms.
