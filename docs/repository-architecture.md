# Repository Architecture

```
nist-csf-governance-operating-model/
|-- govern/                     Control records organized by GOVERN category and control ID
|-- shared-registers/           Cross-control governance registers (mission, stakeholders, obligations, services, dependencies, decisions, actions)
|-- evidence/                   Evidence records, organized by type
|-- templates/                  Reusable templates for every artifact type in this repository
|-- examples/                   The fictional organization (Edjobe Financial Group) and its supporting synthetic materials
|-- docs/                       This documentation set
`-- .github/                    Issue templates, pull request template, validation workflows
```

## How the Pieces Connect

A control record in `govern/` references specific rows in `shared-registers/` (via identifiers like STK-001, OBL-001) and specific evidence records in `evidence/` (via identifiers like EVD-001). This cross-referencing is what makes the repository navigable as a connected system rather than a collection of disconnected documents.

## Identifier Convention

Three-digit sequential identifiers, prefixed by type: OBJ (objectives), STK (stakeholders), OBL (obligations), SVC (services), DEP (dependencies), DEC (decisions), ACT (actions), EVD (evidence), PUB (publication records, private repository only).
