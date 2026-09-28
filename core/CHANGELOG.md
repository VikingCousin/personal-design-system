# Changelog · Personal Design System Core

Format: Version · Datum · Änderungen. Versionierung nach [governance.md](process/governance.md#versionierung).

## 1.0.0 · 2026-09-28 · PERSONAL DESIGN SYSTEM v1.0

Erste nutzbare Version. Entwickelt am Pilotprojekt Digital Legacy, bewusst ohne dessen visuelle Identität.

**Neu**
- Principles: Designprinzipien mit 7 Prüffragen, Accessibility (WCAG 2.2 AA, Profile Standard/Erweitert), Responsive, Interaction, Content & UX Writing, Qualitätsstandards, Dokumentation und Entscheidungen, Visuelle Assets (Logo, Icons, Bilder, Illustration)
- Tokens: Architektur (primitive → semantic → component), Namensgrammatik, semantischer Vertrag (`contract.tokens.json`), neutrale Defaults (`defaults.tokens.json`), Regeln für Farbe, Typografie, Spacing und Sizing, Radius, Border, Elevation, Opacity, Motion, Breakpoints, Z-Index
- Components: Architektur, Zustandsmodell, Variantenlogik, Erweiterungsregeln, Spec-Vorlage und Spezifikationen für Button, Link, Form Field, Input, Textarea, Select, Checkbox, Radio, Switch, Card, Modal/Dialog, Drawer, Accordion, Navigation, Tabs, Breadcrumb, Pagination, Alert, Toast, Tooltip, Badge, Empty/Loading/Error State, Table
- Templates: Website/Landingpage, Marketingseite, Transaktionsablauf, App/Dashboard, Dokument, Präsentation, Brand-Guideline
- Process: Projekt-Workflow mit Phasen, Gates G0–G6 und Prozess-Tiefe S/M/L, Project Bootstrap mit Projektvorlage, Creative-Direction-Methode, Promotion Project → Core, Governance und Versionierung
- Agent Skill: `SKILL.md`, Approval-Gates, Core-vs-Project-Regeln, Beispiel-Prompts
- Patterns: 4 unverbindliche Muster aus dem Pilotprojekt
- Decisions: 0001 Audit der Core-Kandidaten, 0002 Grundentscheidungen, 0003 Smoke Test

**Korrekturen aus dem Smoke Test (vor Freigabe von 1.0.0)**
- neu: `templates/transaction-flow.md`, `principles/visual-assets.md`, Abschnitt Datenvisualisierung in `tokens/color.md`
- Beispielwerte aus dem Pilotprojekt in Core-Beispielen durch neutrale Beispiele ersetzt
