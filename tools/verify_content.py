#!/usr/bin/env python3
"""Verify BEAR Framework version, mapping, accessibility, and authorship invariants.

Maintainer: Christopher Six (@christophersix66)
Profile: https://github.com/christophersix66
"""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = ROOT / "bear-framework.html"
README_PATH = ROOT / "README.md"
MAPPINGS_PATH = ROOT / "MAPPINGS.md"
PDF_PATH = ROOT / "output" / "pdf" / "BEAR-Framework-Defensive-Controls-v2.0.pdf"


class StructureParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.duplicate_ids = set()
        self.controls = []
        self.phase_cards = 0

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        element_id = values.get("id")
        if element_id:
            if element_id in self.ids:
                self.duplicate_ids.add(element_id)
            self.ids.add(element_id)
        if values.get("aria-controls"):
            self.controls.append(values["aria-controls"])
        if "phase-card" in values.get("class", "").split():
            self.phase_cards += 1
            if values.get("role") != "button" or values.get("tabindex") != "0":
                raise AssertionError("Every phase card must be keyboard operable")


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    html = HTML_PATH.read_text(encoding="utf-8")
    readme = README_PATH.read_text(encoding="utf-8")
    mappings = MAPPINGS_PATH.read_text(encoding="utf-8")
    combined = "\n".join((html, readme, mappings))

    for label in ("MITRE ATT&CK v19.2", "NIST CSF 2.0", "ISO/IEC 27001:2022", "CIS Controls v8.1"):
        require(label in combined, f"Missing version label: {label}")

    for stale in ("PR.AC-", "PR.IP-", "PR.PT-"):
        require(stale not in html, f"Stale CSF 1.1 identifier remains in HTML: {stale}")

    required_mappings = (
        "PR.AA-03",
        "PR.IR-01",
        "DE.CM-09",
        "PR.DS-11",
        "RC.RP-03",
        "13.4",
        "13.7",
        "12.8",
        "11.5",
        "T1204 User Execution",
        "T1213 Data from Information Repositories",
    )
    for mapping in required_mappings:
        require(mapping in combined, f"Required corrected mapping missing: {mapping}")

    require("fonts.googleapis.com" not in html, "Remote font dependency breaks offline operation")
    require("https://github.com/christophersix66" in combined, "Christopher Six GitHub profile attribution missing")
    require(not re.search(r"\b(Codex|OpenAI)\b", combined, flags=re.IGNORECASE), "Assistant attribution must not appear in published content")

    parser = StructureParser()
    parser.feed(html)
    require(parser.phase_cards == 4, "Expected exactly four BEAR phase cards")
    require(not parser.duplicate_ids, f"Duplicate HTML ids: {sorted(parser.duplicate_ids)}")
    require(all(target in parser.ids for target in parser.controls), "An aria-controls target is missing")
    require(html.count('class="overlay-btn"') == 4, "Expected four framework overlay buttons")
    require(html.count('aria-pressed="false"') >= 6, "Toggle buttons must expose their state")

    require(PDF_PATH.exists(), "Version 2.0 PDF is missing")
    pdf = PdfReader(str(PDF_PATH))
    require(len(pdf.pages) == 8, "Version 2.0 PDF should contain eight pages")
    metadata = pdf.metadata or {}
    require(metadata.get("/Author") == "Christopher Six (@christophersix66)", "PDF author metadata is incorrect")
    require(metadata.get("/Creator") == "Christopher Six (@christophersix66)", "PDF creator metadata is incorrect")
    require("./output/pdf/BEAR-Framework-Defensive-Controls-v2.0.pdf" in readme, "README PDF link is missing")

    print("BEAR Framework content verification passed")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"verification failed: {exc}", file=sys.stderr)
        raise SystemExit(1)

