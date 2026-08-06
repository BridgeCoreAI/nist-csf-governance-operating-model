# Implementation Guide

How another organization could adapt this GV.OC reference implementation to its own environment.

1. Define organizational scope: decide which business units, systems, or services this governance model will cover.
2. Review the GV.OC requirements: read each control's description and assessment questions before customizing anything.
3. Assign control owners: a named individual per control, not a team or role.
4. Assign evidence owners: may be the same person as the control owner, or a distinct evidence-focused role.
5. Customize registers: replace the synthetic Edjobe Financial Group entries with your organization's real objectives, stakeholders, obligations, services, and dependencies.
6. Replace synthetic examples: every fictional evidence record should be replaced with a real equivalent before this model is used for anything beyond reference.
7. Establish review cadences: set a realistic recurring review frequency per control and per register, tied to actual risk and change velocity.
8. Configure GitHub teams: set up the collaborator groups referenced in CODEOWNERS.
9. Configure branch protections: require review before changes to control records and registers.
10. Configure GitHub Projects: see `.github/project-guidance.md` for recommended fields and views.
11. Run validation workflows: confirm control records and evidence metadata meet the structural requirements before relying on them.
12. Conduct the first assessment: walk through each control's assessment questions honestly, including where the answer is "not yet."
13. Record findings: tied to specific evidence, not general impressions.
14. Create remediation actions: for every gap identified, with an owner and a due date.
15. Review evidence: on the cadence you set, not only when convenient.
16. Approve changes: through the same review discipline this repository itself uses.
17. Revalidate periodically: governance evidence expires; a control assessed as passing a year ago is not automatically still passing today.

**Sensitive organizational evidence should never be placed in a public repository.** If you adapt this model for your own organization, keep your real registers, evidence, and control records private.
