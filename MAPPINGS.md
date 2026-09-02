# BEAR Framework Mapping Register

Maintained by [Christopher Six (@christophersix66)](https://github.com/christophersix66).  
Reviewed: 2026-09-02 | Mapping register version: 2.0

## How to read these mappings

BEAR is a four-phase communication model. The references below are practitioner alignments that help teams pivot from a BEAR phase into established security vocabularies. They are not official crosswalks, certification evidence, or claims of one-to-one equivalence.

- **MITRE ATT&CK:** tactics and techniques are representative, not exhaustive. A technique can belong to more than one tactic and BEAR phase.
- **NIST CSF 2.0:** identifiers describe security outcomes, not individual products. A technology such as a WAF can support an outcome but is not itself a CSF subcategory.
- **ISO/IEC 27001:2022:** Annex A is a reference set. Control selection must follow the organization's risk assessment, risk treatment, and Statement of Applicability process.
- **CIS Controls v8.1:** identifiers refer to safeguards. Implementation Group applicability still depends on the organization and the safeguard.
- **Priority labels:** the interactive tool's Critical/High/Medium labels are a starting point for discussion, not a universal risk rating. Tailor them to asset criticality, threat exposure, legal obligations, and risk appetite.

## Phase-to-ATT&CK alignment

| BEAR phase | ATT&CK Enterprise tactics | Representative techniques |
|---|---|---|
| **Break** | Initial Access (TA0001), Execution (TA0002) | T1190 Exploit Public-Facing Application; T1133 External Remote Services; T1078 Valid Accounts; T1566 Phishing; T1204 User Execution |
| **Expand** | Persistence (TA0003), Discovery (TA0007), Lateral Movement (TA0008), Command and Control (TA0011) | T1053 Scheduled Task/Job; T1018 Remote System Discovery; T1083 File and Directory Discovery; T1021 Remote Services; T1071 Application Layer Protocol |
| **Ascend** | Privilege Escalation (TA0004), Credential Access (TA0006) | T1068 Exploitation for Privilege Escalation; T1548 Abuse Elevation Control Mechanism; T1003 OS Credential Dumping; T1558 Steal or Forge Kerberos Tickets |
| **Rule** | Collection (TA0009), Exfiltration (TA0010), Impact (TA0040) | T1213 Data from Information Repositories; T1567 Exfiltration Over Web Service; T1486 Data Encrypted for Impact; T1490 Inhibit System Recovery |

## Defensive control alignment

The tables map practical control capabilities to the closest framework outcomes or safeguards. Multiple references are shown where one capability spans more than one outcome.

### Break — outside to inside

| Defensive capability | NIST CSF 2.0 | ISO/IEC 27001:2022 Annex A | CIS Controls v8.1 |
|---|---|---|---|
| External asset inventory | ID.AM-01, ID.AM-02, ID.AM-03 | A.5.9 | 1.1, 1.3, 1.5, 2.1 |
| External vulnerability scanning and remediation | ID.RA-01, PR.PS-02 | A.8.8 | 7.6, 7.7 |
| MFA for exposed applications, remote access, and administrators | PR.AA-03 | A.8.5 | 6.3, 6.4, 6.5 |
| Edge and application configuration hardening | PR.PS-01 | A.8.9 | 4.1, 4.2 |
| WAF or application-layer gateway filtering | PR.IR-01 | A.8.20 | 13.10 |
| Authentication anomaly monitoring and analysis | DE.CM-03, DE.AE-02 | A.8.16 | 8.11, 13.1 |
| Email and browser attack-surface reduction | PR.PS-01, PR.AT-01 | A.6.3, A.8.7, A.8.23 | 9.1-9.7, 14.2 |

### Expand — one to many

| Defensive capability | NIST CSF 2.0 | ISO/IEC 27001:2022 Annex A | CIS Controls v8.1 |
|---|---|---|---|
| Network segmentation and east-west filtering | PR.IR-01 | A.8.22 | 12.2, 13.4 |
| Zero-trust access and least privilege | PR.AA-05, PR.IR-01 | A.5.15, A.5.18 | 6.8, 13.5 |
| Endpoint detection and response | DE.CM-09 | A.8.7, A.8.16 | 13.2, 13.7 |
| Network traffic and flow monitoring | DE.CM-01 | A.8.16 | 13.3, 13.6 |
| Behavior analytics and event correlation | DE.CM-03, DE.AE-02, DE.AE-03 | A.8.16 | 8.11, 13.1, 13.11 |
| Application allowlisting | PR.PS-05 | A.8.19 | 2.5, 2.6, 2.7 |
| Cloud posture, workload, and provider monitoring | PR.PS-01, DE.CM-06, DE.CM-09 | A.5.23, A.8.9, A.8.16 | 4.1, 4.2, 15.6 |

### Ascend — user to administrator

| Defensive capability | NIST CSF 2.0 | ISO/IEC 27001:2022 Annex A | CIS Controls v8.1 |
|---|---|---|---|
| Privileged access management and dedicated administration | PR.AA-05 | A.8.2 | 5.4, 12.8 |
| Just-in-time elevation and privileged role governance | PR.AA-05 | A.5.18, A.8.2 | 6.1, 6.2, 6.8 |
| Credential vaulting and local administrator password management | PR.AA-01, PR.AA-04 | A.5.17, A.8.5 | 5.2, 6.5 |
| Credential isolation and authentication hardening | PR.AA-04, PR.PS-01 | A.8.5, A.8.9 | 4.1, 4.2, 10.5 |
| Privileged directory and policy change monitoring | DE.CM-03, DE.CM-09 | A.8.15, A.8.16 | 8.5, 8.11 |
| Privileged behavior analytics and alert tuning | DE.AE-02, DE.AE-03 | A.8.16 | 13.1, 13.11 |

### Rule — access to impact

| Defensive capability | NIST CSF 2.0 | ISO/IEC 27001:2022 Annex A | CIS Controls v8.1 |
|---|---|---|---|
| Data inventory and classification | ID.AM-05, ID.AM-07 | A.5.9, A.5.12 | 3.2, 3.7 |
| Data loss prevention and egress control | PR.DS-01, PR.DS-02, PR.DS-10 | A.8.12, A.8.20 | 3.13, 13.10 |
| Sensitive-data access logging and analytics | DE.CM-03, DE.CM-09, DE.AE-02 | A.8.15, A.8.16 | 3.14, 8.5, 8.11 |
| Encryption at rest and in transit | PR.DS-01, PR.DS-02 | A.8.24 | 3.10, 3.11 |
| Protected, isolated backups | PR.DS-11 | A.8.13 | 11.2, 11.3, 11.4 |
| Restore testing and recovery integrity | PR.DS-11, RC.RP-03, RC.RP-05 | A.8.13, A.5.30 | 11.5 |
| Incident response execution and containment | ID.IM-04, RS.MA-01, RS.MI-01, RS.MI-02 | A.5.24, A.5.25, A.5.26 | 17.4, 17.7 |
| Incident communications | RS.CO-02, RS.CO-03 | A.5.24, A.5.26 | 17.2, 17.6 |

## Review notes

- The prior material used CSF 1.1 identifiers (`PR.AC`, `PR.IP`, and `PR.PT`) under a CSF 2.0 heading. These identifiers were replaced with the CSF 2.0 Core structure, including `PR.AA`, `PR.PS`, and `PR.IR`.
- NIST subcategory identifiers now use the official two-digit form, such as `ID.RA-01` and `RC.RP-03`.
- CIS mappings were narrowed to the safeguard actually described. Examples: external scanning is `7.6`; segment filtering is `13.4`; EDR is represented by `13.2`/`13.7`; dedicated administrative workstations are `12.8`.
- ATT&CK technique names and tactic membership were checked against Enterprise ATT&CK v19.2.
- The BEAR phases remain intentionally concise. They do not imply that real intrusions are linear or that every attacker performs every phase.

## Authoritative references

- [MITRE ATT&CK version history — current v19.2](https://attack.mitre.org/resources/versions/)
- [MITRE ATT&CK Enterprise techniques](https://attack.mitre.org/techniques/enterprise/)
- [NIST Cybersecurity Framework 2.0 (CSWP 29)](https://doi.org/10.6028/NIST.CSWP.29)
- [NIST CSF 2.0 Reference Tool](https://csrc.nist.gov/Projects/cybersecurity-framework/Filters#/csf/filters)
- [ISO/IEC 27001:2022](https://www.iso.org/standard/27001)
- [ISO guidance on the purpose and proper use of Annex A](https://committee.iso.org/files/live/sites/jtc1sc27/files/resources/ISO-IECJTC1-SC27-WG1_N3297_Auditing%20Practices%20Note%20-%20Annex%20A.pdf)
- [CIS Controls v8.1 Navigator](https://www.cisecurity.org/controls/cis-controls-navigator)
