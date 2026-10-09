# Changelog · Personal Design System Core

Format: Version · Datum · Änderungen. Versionierung nach [governance.md](process/governance.md#versionierung).

## 1.1.0 · 2026-10-09 · PERSONAL DESIGN SYSTEM v1.1

Visual Brand Kit, Cross-Channel-Konsistenz und AI Brand Context Pack. Rückwärtskompatibel zu 1.0 (keine Pflicht-Tokens, Gates oder Namen geändert).

**Neu**
- Brand Kit (`core/brand-kit/`): Vertrag `brand-kit.json`, Generator `build_brand_kit.py` für `brand.css` (minimaler CSS-Adapter), `BRAND-KIT.html`, `BRAND-KIT.pdf`, Kanal-Ausgaben und QA-Bericht (Token-Vertrag, Kontraste, Assets, Freigabestatus, Konsistenz)
- 9 Kanal-Starter ohne feste Farben/Schriften: Website, Instagram Post und Story, Pinterest Pin, LinkedIn Post und Carousel, Newsletter, Präsentation, Angebot
- AI Brand Context Pack: `export_ai_context.py` (AI-BRAND-CONTEXT.md, brand-tokens.json, BRAND-KIT.pdf, freigegebene Assets, ChatGPT-Bildprompt, Manifest, Datenschutzprüfung)
- Templates: `cross-channel.md`, `social-media.md`, `newsletter-email.md`
- Automatisierte Tests: `core/brand-kit/tests/test_brand_kit.py` (15 Tests)
- Projektvorlage: `brand-kit/` (alles OPEN); Demo `demo/radhof-demo/` (fiktiv)
- Decisions: 0004 Gap Audit und Entscheidungen, 0005 Testprotokoll

**Geändert**
- Workflow: Phase 5 „Tokens & Brand Kit“, Phase 7 „Templates & Kanäle“; Gate **G4** gibt Tokens **und** Brand Kit frei (Gate-Nummern G0–G6 unverändert)
- Approval-Gates: Weitergabe eines AI Brand Context Packs an externe KI-Dienste gilt als Veröffentlichung (G6)
- Agent Skill: Schritt 8 und 10 erweitert, neuer Ablauf für Kanalaufträge und KI-Export
- Bootstrap: `brand-kit/` als Pflichtordner ab Phase 5; Assets nur in `assets/` (kein Duplikat)
- Qualitätsstandards: Checkliste Brand Kit
- Templates Website, Marketingseite, Dokument, Präsentation, Transaktionsablauf: Verweis auf Cross-Channel-Matrix bzw. Newsletter-Template; `brand-guideline.md` ist das Inhaltsmodell des Brand Kits
- Visuelle Assets: Logo-Schriften in Pfade umwandeln
- `.gitignore`: `ai-pack/` wird nie versioniert
- Quick Start: Block „Brand Kit für ChatGPT“, Ablauf mit Brand Kit und Kanälen

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
