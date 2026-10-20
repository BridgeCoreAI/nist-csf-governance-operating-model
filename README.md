# NIST CSF 2.0 GOVERN Operating Model

A public reference implementation for operationalizing the NIST CSF 2.0 GOVERN function through control records, evidence architecture, governance registers, review workflows, maturity assessments, and accountable remediation.

BridgeCore AI LLC | Governance Systems Engineering Lab

---

**This repository is a public reference implementation. All organizations, evidence records, stakeholders, risks, decisions, findings, and operational examples are fictional, synthetic, or sanitized for educational, research, and portfolio purposes.**

---

## 1. Repository Purpose

This repository demonstrates how the NIST Cybersecurity Framework 2.0 GOVERN function can be translated from a policy document into operational governance artifacts: control records, evidence structures, accountable workflows, control assessments, maturity evaluations, review processes, decision records, and remediation tracking, using GitHub itself as the version-controlled evidence and workflow layer.

## 2. Problem Statement

Most organizations can produce a governance policy. Far fewer can produce evidence that the policy is actually being followed, by whom, reviewed how often, and with what outcome. This repository is a working example of closing that specific gap for one GOVERN category, built to a standard that would hold up to a hiring manager, a GRC practitioner, an auditor, or a prospective client evaluating whether this approach is real or aspirational.

## 3. What This Repository Demonstrates

- Control records that separate control status from maturity, and design assessment from operating-effectiveness assessment
- An evidence model with explicit classification and stated limitations
- Governance registers (mission alignment, stakeholders, obligations, critical services, dependencies) with consistent identifiers
- A finding-and-recommendation model where every recommendation addresses a specific, evidenced gap
- A publication workflow separating private development from public release, with human review at every step
- GitHub-native governance workflow: issue templates, pull request review, validation workflows

## 4. Current Release Scope

**Current release (v0.1.0):** framework documentation and template set. GV.OC control instantiation planned — see CHANGELOG.

## Repository Structure

```
├── README.md
├── GOVERNANCE.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CITATION.cff
├── LICENSE
├── CHANGELOG.md
├── docs/
│   ├── operating-model.md
│   ├── evidence-model.md
│   ├── assessment-method.md
│   ├── maturity-model.md
│   ├── limitations.md
│   ├── repository-architecture.md
│   ├── implementation-guide.md
│   ├── future-roadmap.md
│   ├── glossary.md
│   └── portfolio-positioning.md
└── templates/
    ├── control-record-template.md
    ├── decision-record-template.md
    ├── dependency-review-template.md
    ├── evidence-record-template.md
    ├── finding-and-recommendation-template.md
    ├── operationalization-plan-template.md
    ├── regulatory-change-template.md
    ├── review-record-template.md
    └── stakeholder-review-template.md
 ```

The `docs/` directory contains the core operating model. The `templates/` directory contains the public template set.

## 5. GV.OC Controls Covered

- GV.OC-01 , Organizational mission understood and informing cybersecurity risk management
- GV.OC-02 , Internal and external stakeholder needs and expectations understood and considered
- GV.OC-03 , Legal, regulatory, and contractual cybersecurity requirements understood and managed
- GV.OC-04 , Critical objectives, capabilities, and services that external stakeholders depend on, understood and communicated
- GV.OC-05 , Outcomes, capabilities, and services the organization depends on, understood and communicated

## 6. Repository Architecture

See `docs/repository-architecture.md` for the full breakdown. In short: `govern/` holds control records organized by GOVERN category and control ID, `shared-registers/` holds the cross-control governance registers, `evidence/` holds evidence records, `templates/` holds reusable templates for every artifact type, and `examples/` holds the fictional organization used throughout.

## 7. How to Navigate This Repository

Start with `docs/operating-model.md` for the conceptual model, then `govern/GV.OC-organizational-context/README.md` for the control area itself, then any individual control folder for a worked example.

## 8. How to Use Control Records

Each control folder contains a `control-record.md` (the assessment itself), an `evidence-log.md`, `findings.md`, `action-plan.md`, and `review-history.md`. See `docs/assessment-method.md` for how these fit together.

## 9. How to Use the Evidence Model

See `docs/evidence-model.md`. Every evidence record states what it demonstrates, its limitations, and its classification. Public examples are always marked `Synthetic Example: Yes`.

## 10. How Findings Are Developed

See `docs/assessment-method.md` and `templates/finding-and-recommendation-template.md`. Every finding traces back to specific evidence; no finding is asserted without a cited basis.

## 11. How Recommendations Are Developed

Every recommendation addresses the exact gap identified in its paired finding, includes a practical operationalization plan (owner, process, cadence, tracking method, completion measure), and does not introduce unrelated requirements.

## 12. How Maturity Is Assessed

See `docs/maturity-model.md` for the five-level model (Non-Existent through Optimized and Continuously Improved). Maturity is scored only after control status (Pass, Partial Pass, Fail, Not Assessed) is determined, never combined with it.

## 13. How GitHub Supports Governance Operations

Version control, pull request review, issue tracking, and scheduled workflows provide traceability, review history, and accountability structure. See Section 14 below for what this does not prove.

## 14. What GitHub Does Not Prove

GitHub does not, by itself, satisfy NIST CSF requirements. It serves as a version-controlled evidence, workflow, and accountability layer in this reference implementation. The existence of an artifact does not prove a control is operating effectively; operating effectiveness must be supported by appropriate evidence over time. See `docs/limitations.md`.

## 15. Synthetic Data Notice

All organizations, stakeholders, evidence, registers, findings, and examples in this repository are fictional or synthetic. The example organization, Edjobe Financial Group, does not exist and is not modeled on any real company.

## 16. Confidentiality Notice

This repository contains no real client information, employer information, credentials, or confidential material of any kind. Everything here is safe for public, unrestricted viewing.

## 17. Limitations

This repository does not provide legal advice, regulatory approval, certification, audit assurance, or compliance guarantees, and is not a replacement for organizational judgment, the NIST Cybersecurity Framework itself, an RMF or ATO tool, or an AI governance framework. See `docs/limitations.md` for the complete statement.

## 18. Contribution Guidance

See `CONTRIBUTING.md`. Issues and pull requests are welcome for corrections, clarifications, and template improvements. This repository does not accept contributions containing real organizational data of any kind.

## 19. Release Roadmap

- v0.1.0 , GV.OC Organizational Context complete (current)
- v0.2.0 , GV.RM Risk Management Strategy (planned)
- v0.3.0 , GV.RR Roles, Responsibilities, and Authorities (planned)
- v0.4.0 , GV.PO Policy (planned)
- v0.5.0 , GV.OV Oversight (planned)
- v0.6.0 , GV.SC Cybersecurity Supply Chain Risk Management (planned)
- v1.0.0 , Complete NIST CSF 2.0 GOVERN operating model (planned)

See `docs/future-roadmap.md`.

## 20. Related BridgeCore AI Work

This project is conceptually related to other BridgeCore AI governance engineering work, without claiming technical integration that has not actually been built:

- `rmf-ato-accelerator`: NIST SP 800-37 RMF lifecycle accelerator with CNSSI 1253 control tailoring and evidence generation
- `ai-grc-engineering`: hands-on AI GRC engineering portfolio translating NIST AI RMF, ISO/IEC 42001, and the EU AI Act into working governance systems
- `accountability-layer-framework`: the organizational accountability architecture above the technical enforcement layer

## 21. Author Attribution

Designed and developed by Grace M. Adjeli.

## 22. Organization Attribution

BridgeCore AI LLC, Governance Systems Engineering Lab.

## 23. License

Licensed under the Apache License, Version 2.0. See `LICENSE`.

## 24. Citation

See `CITATION.cff`.

---

*"Governance is not what is defined. It is what is enforced at execution."*
