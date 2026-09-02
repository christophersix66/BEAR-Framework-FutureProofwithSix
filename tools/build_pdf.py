#!/usr/bin/env python3
"""Build the BEAR Framework defensive control mapping PDF.

Maintainer: Christopher Six (@christophersix66)
Profile: https://github.com/christophersix66
"""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "BEAR-Framework-Defensive-Controls-v2.0.pdf"

INK = colors.HexColor("#18212B")
MUTED = colors.HexColor("#5A6775")
PAPER = colors.HexColor("#F5F7FA")
GRID = colors.HexColor("#D7DEE7")
ORANGE = colors.HexColor("#F36A2D")
GOLD = colors.HexColor("#D6A914")
TEAL = colors.HexColor("#1C9B96")
RED = colors.HexColor("#C93B48")
NAVY = colors.HexColor("#102A43")
WHITE = colors.white

PHASES = [
    {
        "name": "BREAK",
        "transition": "Outside -> Inside",
        "question": "Did the adversary get in?",
        "color": ORANGE,
        "tactics": "Initial Access (TA0001), Execution (TA0002)",
        "techniques": [
            "T1190 Exploit Public-Facing Application",
            "T1133 External Remote Services",
            "T1078 Valid Accounts",
            "T1566 Phishing",
            "T1204 User Execution",
        ],
        "objectives": [
            "Exploit public-facing applications or APIs",
            "Abuse external remote services or valid accounts",
            "Use phishing and user execution to establish a foothold",
            "Reach initial code execution inside the defended environment",
        ],
        "controls": [
            ("External asset inventory", "ID.AM-01/02/03", "A.5.9", "1.1, 1.3, 1.5, 2.1"),
            ("External vulnerability scanning and remediation", "ID.RA-01; PR.PS-02", "A.8.8", "7.6, 7.7"),
            ("MFA for exposed apps, remote access, and administrators", "PR.AA-03", "A.8.5", "6.3, 6.4, 6.5"),
            ("Edge and application configuration hardening", "PR.PS-01", "A.8.9", "4.1, 4.2"),
            ("WAF or application-layer gateway filtering", "PR.IR-01", "A.8.20", "13.10"),
            ("Authentication anomaly monitoring and analysis", "DE.CM-03; DE.AE-02", "A.8.16", "8.11, 13.1"),
            ("Email and browser attack-surface reduction", "PR.PS-01; PR.AT-01", "A.6.3; A.8.7; A.8.23", "9.1-9.7; 14.2"),
        ],
        "detections": [
            "Authentication failure spikes and impossible travel",
            "WAF, IDS, or gateway exploit indicators",
            "Unusual API patterns and newly exposed services",
            "Phishing delivery, link, attachment, and user-execution signals",
        ],
        "metrics": [
            "External asset inventory coverage",
            "Externally exposed vulnerability remediation time",
            "MFA coverage for exposed, remote, and administrative access",
            "Time from initial-access signal to triage",
        ],
    },
    {
        "name": "EXPAND",
        "transition": "One -> Many",
        "question": "How far did the adversary move?",
        "color": GOLD,
        "tactics": "Persistence (TA0003), Discovery (TA0007), Lateral Movement (TA0008), Command and Control (TA0011)",
        "techniques": [
            "T1053 Scheduled Task/Job",
            "T1018 Remote System Discovery",
            "T1083 File and Directory Discovery",
            "T1021 Remote Services",
            "T1071 Application Layer Protocol",
        ],
        "objectives": [
            "Discover identities, hosts, data stores, and trust relationships",
            "Move to internal, cloud, SaaS, or orchestration environments",
            "Establish persistence and command-and-control paths",
            "Turn one foothold into multiple reachable options",
        ],
        "controls": [
            ("Network segmentation and east-west filtering", "PR.IR-01", "A.8.22", "12.2, 13.4"),
            ("Zero-trust access and least privilege", "PR.AA-05; PR.IR-01", "A.5.15; A.5.18", "6.8, 13.5"),
            ("Endpoint detection and response", "DE.CM-09", "A.8.7; A.8.16", "13.2, 13.7"),
            ("Network traffic and flow monitoring", "DE.CM-01", "A.8.16", "13.3, 13.6"),
            ("Behavior analytics and event correlation", "DE.CM-03; DE.AE-02/03", "A.8.16", "8.11; 13.1, 13.11"),
            ("Application allowlisting", "PR.PS-05", "A.8.19", "2.5, 2.6, 2.7"),
            ("Cloud posture, workload, and provider monitoring", "PR.PS-01; DE.CM-06/09", "A.5.23; A.8.9; A.8.16", "4.1, 4.2, 15.6"),
        ],
        "detections": [
            "SMB, RDP, WinRM, SSH, or cloud lateral movement",
            "LDAP, DNS, service, host, and file-share discovery",
            "New scheduled tasks, services, tokens, or persistence objects",
            "First-time cloud API activity and behavior-baseline deviations",
        ],
        "metrics": [
            "Segmentation policy coverage and denied-path validation",
            "Endpoint monitoring coverage",
            "Mean time from lateral-movement signal to containment",
            "Behavior-alert investigation yield",
        ],
    },
    {
        "name": "ASCEND",
        "transition": "User -> Administrator",
        "question": "Did the adversary gain privileged control?",
        "color": TEAL,
        "tactics": "Privilege Escalation (TA0004), Credential Access (TA0006)",
        "techniques": [
            "T1068 Exploitation for Privilege Escalation",
            "T1548 Abuse Elevation Control Mechanism",
            "T1003 OS Credential Dumping",
            "T1558 Steal or Forge Kerberos Tickets",
        ],
        "objectives": [
            "Escalate to root, SYSTEM, tenant, domain, or cluster administration",
            "Dump, steal, forge, or replay privileged credentials",
            "Control identity, certificate, CI/CD, or management planes",
            "Convert ordinary access into durable administrative authority",
        ],
        "controls": [
            ("PAM and dedicated administration", "PR.AA-05", "A.8.2", "5.4, 12.8"),
            ("Just-in-time elevation and privileged-role governance", "PR.AA-05", "A.5.18; A.8.2", "6.1, 6.2, 6.8"),
            ("Credential vaulting and local admin password management", "PR.AA-01/04", "A.5.17; A.8.5", "5.2, 6.5"),
            ("Credential isolation and authentication hardening", "PR.AA-04; PR.PS-01", "A.8.5; A.8.9", "4.1, 4.2, 10.5"),
            ("Privileged directory and policy change monitoring", "DE.CM-03/09", "A.8.15; A.8.16", "8.5, 8.11"),
            ("Privileged behavior analytics and alert tuning", "DE.AE-02/03", "A.8.16", "13.1, 13.11"),
        ],
        "detections": [
            "Privilege escalation, token manipulation, and security-control bypass",
            "Sensitive group, role, policy, certificate, or trust changes",
            "Kerberoasting, DCSync, credential dumping, and abnormal ticket use",
            "First-time or out-of-pattern privileged activity",
        ],
        "metrics": [
            "Standing privileged identity count",
            "Administrative MFA and dedicated-workstation coverage",
            "Privileged-access review completion",
            "Mean time to detect and revoke unauthorized privilege",
        ],
    },
    {
        "name": "RULE",
        "transition": "Access -> Impact",
        "question": "What impact can the adversary create?",
        "color": RED,
        "tactics": "Collection (TA0009), Exfiltration (TA0010), Impact (TA0040)",
        "techniques": [
            "T1213 Data from Information Repositories",
            "T1567 Exfiltration Over Web Service",
            "T1486 Data Encrypted for Impact",
            "T1490 Inhibit System Recovery",
        ],
        "objectives": [
            "Collect and exfiltrate sensitive information",
            "Disrupt, alter, encrypt, or destroy systems and data",
            "Block recovery or retain leverage for extortion",
            "Create material operational, legal, financial, or safety impact",
        ],
        "controls": [
            ("Data inventory and classification", "ID.AM-05/07", "A.5.9; A.5.12", "3.2, 3.7"),
            ("DLP and egress control", "PR.DS-01/02/10", "A.8.12; A.8.20", "3.13, 13.10"),
            ("Sensitive-data access logging and analytics", "DE.CM-03/09; DE.AE-02", "A.8.15; A.8.16", "3.14; 8.5, 8.11"),
            ("Encryption at rest and in transit", "PR.DS-01/02", "A.8.24", "3.10, 3.11"),
            ("Protected, isolated backups", "PR.DS-11", "A.8.13", "11.2, 11.3, 11.4"),
            ("Restore testing and recovery integrity", "PR.DS-11; RC.RP-03/05", "A.8.13; A.5.30", "11.5"),
            ("Incident response execution and containment", "ID.IM-04; RS.MA-01; RS.MI-01/02", "A.5.24; A.5.25; A.5.26", "17.4, 17.7"),
            ("Incident communications", "RS.CO-02/03", "A.5.24; A.5.26", "17.2, 17.6"),
        ],
        "detections": [
            "Bulk access, archive creation, staging, and external transfers",
            "DNS tunneling and unusual egress paths",
            "Backup deletion, encryption, or retention-policy changes",
            "Mass file modification, service disruption, or destructive commands",
        ],
        "metrics": [
            "Sensitive-data inventory and DLP coverage",
            "Exfiltration alert investigation and confirmation rate",
            "Backup isolation and tested-restore success",
            "Recovery time and recovery point performance against objectives",
        ],
    },
]


class BearDocTemplate(SimpleDocTemplate):
    """Draw repeating document furniture after page content is laid out."""

    def afterPage(self):
        page_header_footer(self.canv, self)


def p(text, style):
    return Paragraph(text.replace("ATT&CK", "ATT&amp;CK"), style)


def bullet_list(items, style):
    return [Paragraph(f"- {item}", style) for item in items]


def page_header_footer(canvas, doc):
    canvas.saveState()
    canvas.setTitle("BEAR Framework Defensive Control Mapping v2.0")
    canvas.setAuthor("Christopher Six (@christophersix66)")
    canvas.setSubject("BEAR Framework practitioner mappings and defensive control reference")
    canvas.setCreator("Christopher Six (@christophersix66)")
    width, height = landscape(letter)
    if doc.page > 1:
        canvas.setStrokeColor(GRID)
        canvas.line(0.45 * inch, height - 0.34 * inch, width - 0.45 * inch, height - 0.34 * inch)
        canvas.setFont("Helvetica-Bold", 8)
        canvas.setFillColor(NAVY)
        canvas.drawString(0.45 * inch, height - 0.26 * inch, "BEAR Framework | Defensive Control Mapping v2.0")
        canvas.setFont("Helvetica", 7.5)
        canvas.setFillColor(MUTED)
        canvas.drawRightString(width - 0.45 * inch, height - 0.26 * inch, "Christopher Six | github.com/christophersix66")
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(0.45 * inch, 0.24 * inch, "Practitioner alignment - not an official crosswalk or certification artifact")
    canvas.drawRightString(width - 0.45 * inch, 0.24 * inch, f"Page {doc.page}")
    canvas.restoreState()


def control_table(rows, styles):
    data = [[
        p("Defensive capability", styles["table_header"]),
        p("NIST CSF 2.0", styles["table_header"]),
        p("ISO/IEC 27001:2022 Annex A", styles["table_header"]),
        p("CIS Controls v8.1", styles["table_header"]),
    ]]
    for capability, nist, iso, cis in rows:
        data.append([
            p(capability, styles["table_body"]),
            p(nist, styles["table_code"]),
            p(iso, styles["table_code"]),
            p(cis, styles["table_code"]),
        ])
    table = Table(data, colWidths=[3.55 * inch, 2.0 * inch, 2.15 * inch, 2.05 * inch], repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("GRID", (0, 0), (-1, -1), 0.45, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, PAPER]),
    ]))
    return table


def phase_page(phase, styles):
    story = []
    heading = Table([
        [
            p(phase["name"], ParagraphStyle("phase_name", parent=styles["h1"], textColor=WHITE, fontSize=21, leading=23)),
            p(phase["transition"], ParagraphStyle("phase_transition", parent=styles["body"], textColor=WHITE, alignment=TA_CENTER, fontName="Helvetica-Bold")),
            p(phase["question"], ParagraphStyle("phase_question", parent=styles["body"], textColor=WHITE, alignment=TA_LEFT, fontName="Helvetica-Bold")),
        ]
    ], colWidths=[2.0 * inch, 1.8 * inch, 5.95 * inch])
    heading.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), phase["color"]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ]))
    story.extend([heading, Spacer(1, 0.15 * inch)])

    context = Table([
        [p("Representative ATT&CK tactics", styles["label"]), p(phase["tactics"], styles["body"])],
        [p("Representative techniques", styles["label"]), p("; ".join(phase["techniques"]), styles["body_small"])],
    ], colWidths=[1.9 * inch, 7.85 * inch])
    context.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), PAPER),
        ("BOX", (0, 0), (-1, -1), 0.5, GRID),
        ("INNERGRID", (0, 0), (-1, -1), 0.35, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.extend([context, Spacer(1, 0.12 * inch)])

    top = Table([
        [p("Attacker objectives", styles["h3"]), p("Detection opportunities", styles["h3"]), p("Operational metrics", styles["h3"])],
        [
            p("<br/>".join(f"- {item}" for item in phase["objectives"]), styles["body_small"]),
            p("<br/>".join(f"- {item}" for item in phase["detections"]), styles["body_small"]),
            p("<br/>".join(f"- {item}" for item in phase["metrics"]), styles["body_small"]),
        ],
    ], colWidths=[3.25 * inch, 3.25 * inch, 3.25 * inch])
    top.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), PAPER),
        ("BOX", (0, 0), (-1, -1), 0.5, GRID),
        ("INNERGRID", (0, 0), (-1, -1), 0.35, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.extend([top, Spacer(1, 0.14 * inch), p("Defensive control alignment", styles["h2"]), Spacer(1, 0.05 * inch), control_table(phase["controls"], styles)])
    return story


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    base = getSampleStyleSheet()
    styles = {
        "title": ParagraphStyle("title", parent=base["Title"], fontName="Helvetica-Bold", fontSize=34, leading=38, textColor=WHITE, alignment=TA_LEFT, spaceAfter=8),
        "subtitle": ParagraphStyle("subtitle", parent=base["Normal"], fontName="Helvetica", fontSize=16, leading=20, textColor=colors.HexColor("#D7E3F0")),
        "h1": ParagraphStyle("h1", parent=base["Heading1"], fontName="Helvetica-Bold", fontSize=22, leading=25, textColor=NAVY, spaceAfter=8),
        "h2": ParagraphStyle("h2", parent=base["Heading2"], fontName="Helvetica-Bold", fontSize=14, leading=17, textColor=NAVY, spaceBefore=4, spaceAfter=5),
        "h3": ParagraphStyle("h3", parent=base["Heading3"], fontName="Helvetica-Bold", fontSize=9.5, leading=11, textColor=NAVY, spaceAfter=3),
        "body": ParagraphStyle("body", parent=base["BodyText"], fontName="Helvetica", fontSize=9, leading=12, textColor=INK, spaceAfter=5),
        "body_small": ParagraphStyle("body_small", parent=base["BodyText"], fontName="Helvetica", fontSize=8, leading=10.5, textColor=INK),
        "label": ParagraphStyle("label", parent=base["BodyText"], fontName="Helvetica-Bold", fontSize=8.5, leading=10.5, textColor=NAVY),
        "table_header": ParagraphStyle("table_header", parent=base["BodyText"], fontName="Helvetica-Bold", fontSize=8, leading=9.5, textColor=WHITE),
        "table_body": ParagraphStyle("table_body", parent=base["BodyText"], fontName="Helvetica", fontSize=7.8, leading=9.5, textColor=INK),
        "table_code": ParagraphStyle("table_code", parent=base["BodyText"], fontName="Courier", fontSize=7.4, leading=9.2, textColor=INK),
        "source": ParagraphStyle("source", parent=base["BodyText"], fontName="Helvetica", fontSize=8.2, leading=11, textColor=INK, leftIndent=12, firstLineIndent=-12, spaceAfter=5),
    }

    doc = BearDocTemplate(
        str(OUTPUT),
        pagesize=landscape(letter),
        rightMargin=0.45 * inch,
        leftMargin=0.45 * inch,
        topMargin=0.68 * inch,
        bottomMargin=0.56 * inch,
        title="BEAR Framework Defensive Control Mapping v2.0",
        author="Christopher Six (@christophersix66)",
        subject="BEAR Framework practitioner mappings and defensive control reference",
    )

    story = []
    cover = Table([
        [
            p("BEAR", styles["title"]),
            p("Defensive Control Mapping<br/><font size='15'>Break -> Expand -> Ascend -> Rule</font>", styles["subtitle"]),
        ]
    ], colWidths=[3.2 * inch, 6.55 * inch], rowHeights=[1.35 * inch])
    cover.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 20),
        ("RIGHTPADDING", (0, 0), (-1, -1), 20),
    ]))
    story.extend([Spacer(1, 0.32 * inch), cover, Spacer(1, 0.28 * inch)])

    phase_summary = [[p("Phase", styles["table_header"]), p("Operational question", styles["table_header"]), p("Transition", styles["table_header"]), p("Representative ATT&CK tactics", styles["table_header"])]]
    for phase in PHASES:
        phase_summary.append([
            p(phase["name"], styles["label"]),
            p(phase["question"], styles["body"]),
            p(phase["transition"], styles["body"]),
            p(phase["tactics"], styles["body_small"]),
        ])
    summary_table = Table(phase_summary, colWidths=[1.2 * inch, 3.2 * inch, 1.55 * inch, 3.8 * inch], repeatRows=1)
    summary_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, PAPER]),
        ("GRID", (0, 0), (-1, -1), 0.45, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.extend([
        p("A concise model for shared operational context", styles["h1"]),
        p("BEAR reduces an intrusion to four questions. It is a communication layer, not a replacement for ATT&CK, the Cyber Kill Chain, NIST CSF, ISO/IEC 27001, or CIS Controls. Real intrusions can revisit phases, run phases in parallel, or create impact without completing every phase.", styles["body"]),
        Spacer(1, 0.08 * inch),
        summary_table,
        Spacer(1, 0.2 * inch),
        p("Maintained by Christopher Six (@christophersix66)", styles["h2"]),
        p("Version 2.0 | 2026-09-02 | github.com/christophersix66<br/>BEAR Framework concept credited by the original project to Ivan Novikov (Wallarm).", styles["body"]),
        PageBreak(),
    ])

    story.extend([
        p("Mapping method and boundaries", styles["h1"]),
        p("The mappings in this document are practitioner alignments that help a team pivot from a BEAR phase into established security vocabularies. They are not official crosswalks, certification evidence, or claims of one-to-one equivalence.", styles["body"]),
    ])
    method_rows = [
        ("MITRE ATT&CK v19.2", "Tactics and techniques are representative, not exhaustive. ATT&CK objects are many-to-many and can span more than one BEAR phase."),
        ("NIST CSF 2.0", "The Core expresses outcomes, not products. Product examples are mapped to the closest supported outcome and retain the official two-digit subcategory form."),
        ("ISO/IEC 27001:2022", "Annex A is a reference set. Applicability is determined through organizational risk assessment, risk treatment, and the Statement of Applicability."),
        ("CIS Controls v8.1", "Entries point to the closest prescriptive safeguards. Implementation Group scope and organizational applicability still need to be evaluated."),
        ("BEAR priority labels", "Critical, High, and Medium labels are a starting point for discussion, not a universal risk rating. Tailor them to organizational risk."),
    ]
    method = Table([[p("Reference", styles["table_header"]), p("Use in BEAR", styles["table_header"])]] + [[p(a, styles["label"]), p(b, styles["body"])] for a, b in method_rows], colWidths=[2.1 * inch, 7.65 * inch], repeatRows=1)
    method.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, PAPER]),
        ("GRID", (0, 0), (-1, -1), 0.45, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    story.extend([
        method,
        Spacer(1, 0.18 * inch),
        p("Corrections from version 1.1", styles["h2"]),
        p("- Replaced CSF 1.1 categories PR.AC, PR.IP, and PR.PT that had been labeled as CSF 2.0.<br/>- Adopted the current CSF 2.0 categories PR.AA, PR.PS, and PR.IR and official two-digit subcategory identifiers.<br/>- Narrowed CIS mappings to the safeguards actually described, including 7.6 for external scanning, 13.4 for segment filtering, 13.2/13.7 for host detection and prevention, and 12.8 for dedicated administrative resources.<br/>- Updated ATT&CK technique names and tactic membership to Enterprise ATT&CK v19.2.<br/>- Removed claims of strict equivalence and documented the risk-based use of ISO Annex A.", styles["body"]),
        Spacer(1, 0.16 * inch),
        p("Perspective", styles["h2"]),
        p("The phase questions use neutral incident-response language ('the adversary') so tactical, defensive, and executive audiences can share the same status statement. Red-team operators may restate the questions in first person during an exercise.", styles["body"]),
        PageBreak(),
    ])

    for phase in PHASES:
        story.extend(phase_page(phase, styles))
        story.append(PageBreak())

    story.extend([
        p("Operational use", styles["h1"]),
        p("Use BEAR to establish position and decision urgency, then pivot to the detailed source framework for analysis, detection engineering, risk treatment, control implementation, or recovery planning.", styles["body"]),
    ])
    use_rows = [
        ("Active incident", "Identify the highest confirmed phase, evidence supporting it, reachable assets, business impact, and the next containment decision."),
        ("Red-team debrief", "Show the furthest demonstrated phase and distinguish observed capability from inferred or theoretical impact."),
        ("Control validation", "Test whether prevention, detection, containment, and recovery capabilities interrupt each phase; record evidence and gaps."),
        ("Executive briefing", "State what is confirmed, what remains uncertain, what impact is plausible, and which decision or resource is needed."),
    ]
    use_table = Table([[p("Scenario", styles["table_header"]), p("Recommended use", styles["table_header"])]] + [[p(a, styles["label"]), p(b, styles["body"])] for a, b in use_rows], colWidths=[1.9 * inch, 7.85 * inch], repeatRows=1)
    use_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, PAPER]),
        ("GRID", (0, 0), (-1, -1), 0.45, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    story.extend([
        use_table,
        Spacer(1, 0.18 * inch),
        p("Minimum incident status record", styles["h2"]),
        p("For each assessment, capture the timestamp, highest confirmed BEAR phase, confidence level, supporting evidence, affected identities and assets, containment status, plausible impact, decision owner, and next update time. Do not treat an unconfirmed capability as demonstrated impact.", styles["body"]),
        Spacer(1, 0.15 * inch),
        p("Maintenance rule", styles["h2"]),
        p("Review this mapping register when a referenced framework changes. Verify identifiers and titles against primary sources before publishing a new version. Keep the HTML tool, MAPPINGS.md, and PDF version labels synchronized.", styles["body"]),
        PageBreak(),
        p("Authoritative references", styles["h1"]),
        p("1. MITRE ATT&CK Version History (current v19.2): https://attack.mitre.org/resources/versions/", styles["source"]),
        p("2. MITRE ATT&CK Enterprise Techniques: https://attack.mitre.org/techniques/enterprise/", styles["source"]),
        p("3. NIST Cybersecurity Framework 2.0, NIST CSWP 29: https://doi.org/10.6028/NIST.CSWP.29", styles["source"]),
        p("4. NIST CSF 2.0 Reference Tool: https://csrc.nist.gov/Projects/cybersecurity-framework/Filters#/csf/filters", styles["source"]),
        p("5. ISO/IEC 27001:2022: https://www.iso.org/standard/27001", styles["source"]),
        p("6. ISO/IEC JTC 1/SC 27 guidance on Annex A: https://committee.iso.org/files/live/sites/jtc1sc27/files/resources/ISO-IECJTC1-SC27-WG1_N3297_Auditing%20Practices%20Note%20-%20Annex%20A.pdf", styles["source"]),
        p("7. CIS Controls v8.1 Navigator: https://www.cisecurity.org/controls/cis-controls-navigator", styles["source"]),
        Spacer(1, 0.18 * inch),
        p("Version record", styles["h2"]),
        p("v2.0 - 2026-09-02 - Framework alignment review, mapping corrections, accessibility and offline improvements. Maintained by Christopher Six (@christophersix66).<br/>v1.1 - Original repository PDF - Behavior drift content added.<br/>v1.0 - Original defensive control mapping.", styles["body"]),
        Spacer(1, 0.25 * inch),
        p("Credits", styles["h2"]),
        p("BEAR Framework concept: Ivan Novikov (Wallarm), as credited by the original project.<br/>Defensive control mapping, interactive tool, and repository maintenance: Christopher Six - github.com/christophersix66", styles["body"]),
    ])

    doc.build(story)
    print(OUTPUT)


if __name__ == "__main__":
    build()
