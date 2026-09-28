# Core · Personal Design System

> **Version 1.0.0** · Stand 2026-09-28 · [CHANGELOG](CHANGELOG.md)
> Projektunabhängige Regeln, Systematik, Prozesse und Qualitätsstandards. **Keine** Markenwerte: Farben, Schriften, Logos und Bildsprache gehören in `projects/<name>/`.

## Inhalt

| Bereich | Einstieg | Worum es geht |
|---|---|---|
| **Principles** | [design-principles](principles/design-principles.md) · [accessibility](principles/accessibility.md) · [responsive](principles/responsive.md) · [interaction](principles/interaction.md) · [content-writing](principles/content-writing.md) · [quality-standards](principles/quality-standards.md) · [documentation](principles/documentation.md) · [visual-assets](principles/visual-assets.md) | Wie gestaltet, geschrieben, geprüft und dokumentiert wird; Logo, Icons, Bilder |
| **Tokens** | [README](tokens/README.md) · [architecture](tokens/architecture.md) · [contract.tokens.json](tokens/contract.tokens.json) | Ebenen, Namen, Rollen, Pflicht-Tokens, neutrale Default-Skalen |
| **Components** | [README](components/README.md) · [_spec-template](components/_spec-template.md) | Architektur, Zustände, Varianten und A11y von 24 Standardkomponenten |
| **Templates** | [README](templates/README.md) | Strukturen für Website, Marketingseite, Transaktionsablauf, App/Dashboard, Dokument, Präsentation, Brand-Guideline |
| **Process** | [project-workflow](process/project-workflow.md) · [project-bootstrap](process/project-bootstrap.md) · [creative-direction](process/creative-direction.md) · [promotion](process/promotion.md) · [governance](process/governance.md) · [project-template/](process/project-template/) | Wie Projekte entstehen, wie Core wächst und versioniert wird |
| **Agent Skill** | [SKILL.md](agent-skill/SKILL.md) · [approval-gates](agent-skill/rules/approval-gates.md) · [core-vs-project](agent-skill/rules/core-vs-project.md) · [examples](agent-skill/examples/prompts.md) | Wie Claude das System benutzt |
| **Patterns** | [README](patterns/README.md) | Unverbindliche, wiederverwendbare Muster |
| **Decisions** | [0001 Audit](decisions/0001-audit-core-kandidaten.md) · [0002 Grundentscheidungen](decisions/0002-core-v1-grundentscheidungen.md) · [0003 Smoke Test](decisions/0003-smoke-test-v1.md) | Warum Core so ist, wie er ist |

## Was Core festlegt, und was nicht

| Core legt fest | Core legt **nicht** fest |
|---|---|
| Accessibility-Baseline (WCAG 2.2 AA) und Profile | Zielgruppe |
| Token-Ebenen, Namen, Pflicht-Rollen, Skalenmethoden | Farben, Schriften, Radien, Schatten |
| neutrale Default-Skalen (Abstand, Zielgrößen, Z-Index, Breakpoints, Dauern) | Stil, Dichte, Charakter |
| Verhalten, Zustände und A11y von Komponenten | Aussehen von Komponenten |
| Pflichtbereiche und Qualitätsregeln von Templates | Layout und Gestaltung von Templates |
| Phasen, Gates, Promotion, Governance | Markenentscheidungen |
