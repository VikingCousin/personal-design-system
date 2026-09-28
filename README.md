# Personal Design System

> **PERSONAL DESIGN SYSTEM v1.0** · Core 1.0.0 · Stand 2026-09-28 · [Changelog](core/CHANGELOG.md)

Ein persönliches, projektunabhängiges Design-System. Es liefert die **Regeln, Systematik, Prozesse und Qualitätsstandards**, mit denen jedes neue Projekt eine eigene Marke und eigene Oberflächen bekommt: SaaS, lokales Unternehmen, E-Commerce, Dienstleistung, App, persönliche Marke oder etwas ganz anderes.

Es liefert **keine** fertige Optik. Jedes Projekt hat seine eigene Marke.

> **English summary:** A reusable, AI-assisted personal design system. `core/` holds brand-neutral rules (accessibility, responsive design, token architecture, component behavior, template structures, project workflow with approval gates). Each project in `projects/` builds its own brand and design system on top of it. Claude Code follows [`core/agent-skill/SKILL.md`](core/agent-skill/SKILL.md). Documentation is in German.

> **Schnellstart auf einer Seite:** [PERSONAL-DESIGN-SYSTEM-QUICKSTART.pdf](PERSONAL-DESIGN-SYSTEM-QUICKSTART.pdf) · Quelldatei zum Aktualisieren: [quickstart/PERSONAL-DESIGN-SYSTEM-QUICKSTART.html](quickstart/PERSONAL-DESIGN-SYSTEM-QUICKSTART.html)

---

## In 30 Sekunden

| Frage | Antwort |
|---|---|
| **Was gehört in Core?** | Alles, was für *jedes* Projekt gilt: Accessibility, Responsive, Token-Architektur und -Namen, Farbrollen (nicht Farben), Typo-Systematik (nicht Schriften), Spacing, Komponenten-Verhalten, Template-Strukturen, Prozesse, Gates, Qualitätsprüfungen. → [`core/`](core/README.md) |
| **Was gehört in Projects?** | Alles, was eine Marke ausmacht: Brief, Positionierung, Tonalität, Farben, Schriften, Logo, Bildsprache, Creative Direction, eigene Komponenten und Templates. → `projects/<name>/` |
| **Wie starte ich ein neues Projekt?** | Claude sagen: *„Ich möchte ein neues Projekt X erstellen. Verwende mein Personal Design System.“* Oder von Hand: [`core/process/project-template/`](core/process/project-template/) nach `projects/<name>/` kopieren und [Bootstrap](core/process/project-bootstrap.md) folgen. |
| **Wie arbeitet Claude damit?** | nach dem [Agent Skill](core/agent-skill/SKILL.md): Core lesen → Projekt anlegen → Brief → Brand Foundation → Creative Directions → **du entscheidest** → Tokens → Components → Templates → Prüfung. An jedem [Gate](core/agent-skill/rules/approval-gates.md) wartet Claude auf deine Freigabe. |
| **Wo liegen Tokens?** | Systematik und Pflicht-Tokens: [`core/tokens/`](core/tokens/README.md). Werte eines Projekts: `projects/<name>/tokens/`. |
| **Wo liegen Components?** | Verhalten, Zustände, Accessibility: [`core/components/`](core/components/README.md). Aussehen und Projektkomponenten: `projects/<name>/components/`. |
| **Wie wird Core weiterentwickelt?** | Nur über [Promotion](core/process/promotion.md): Projekte markieren `[CORE-KANDIDAT]`, du entscheidest, dann Eintrag im Changelog und neue Version ([Governance](core/process/governance.md)). Core wird nie stillschweigend geändert. |

---

## Struktur

```
personal-design-system/
├── README.md              ← du bist hier
├── AGENTS.md              Einstieg für AI Agents (verweist auf den Agent Skill)
├── CLAUDE.md              lädt AGENTS.md für Claude Code
│
├── core/                  PROJEKTUNABHÄNGIG · Version 1.0.0
│   ├── README.md          Inhaltsverzeichnis
│   ├── CHANGELOG.md
│   ├── principles/        Designprinzipien, Accessibility, Responsive, Interaction, Content, Qualität, Doku, Assets
│   ├── tokens/            Architektur, Namen, Rollen, Skalen, contract.tokens.json, defaults.tokens.json
│   ├── components/        24 Komponenten-Spezifikationen + Spec-Vorlage
│   ├── templates/         Website, Marketingseite, Transaktionsablauf, App/Dashboard, Dokument, Präsentation, Brand-Guideline
│   ├── process/           Workflow & Gates, Bootstrap, Creative Direction, Promotion, Governance, project-template/
│   ├── patterns/          unverbindliche Muster
│   ├── decisions/         warum Core so ist, wie er ist
│   └── agent-skill/       SKILL.md, rules/, examples/
│
└── projects/              EIN ORDNER JE PROJEKT (siehe projects/README.md)
```

## Ein neues Projekt: der Ablauf

```
0 Setup → 1 Brief → 2 Brand Foundation → (3 Research) → 4 Creative Direction → 5 Tokens → 6 Components → 7 Templates → 8 Release
      G0        G1                 G2                                     G3            G4             G5             G5          G6
```

- **Prozess-Tiefe** S (klein, z. B. Landingpage eines Handwerksbetriebs), M (Standard) oder L (große neue Marke). Details in [project-workflow.md](core/process/project-workflow.md).
- **Bestehende Marke?** Dann Brand-Import statt neuer Creative Directions.
- **Nie ohne dich:** Name, Richtung, Farben, Schriften, Logo, Anrede, Preise, Veröffentlichung.

## Wichtigste Regeln auf einen Blick

1. Accessibility-Baseline **WCAG 2.2 AA** in jedem Projekt, verschärfbar, nie absenkbar.
2. **Token-first:** primitive → semantic → component; Komponenten nutzen nie Rohwerte.
3. **Core schreibt keinen Stil vor.** Keine Farben, Schriften, Radien oder Schatten im Core.
4. **Mobile first**, lauffähig ab 320 px und mit 200 % Zoom.
5. **Nie nur Farbe** für Bedeutung.
6. **Claude bereitet vor, du entscheidest** (Gates G0–G6).
7. **Projekt → Core nur über Promotion.**

## Pilotprojekt Digital Legacy

Das Pilotprojekt war der Stresstest, an dem dieses System entwickelt wurde (Brief, Brand Foundation, drei Creative-Direction-Explorationen). Es ist **unfertig, pausiert und privat**, deshalb nicht Teil dieses öffentlichen Repositorys. Keine Richtung ist gewählt, offene Geschäftsentscheidungen bleiben offen. Seine visuelle Identität ist **nicht** Teil von Core. Welche Erkenntnisse übernommen wurden, steht in [core/decisions/0001](core/decisions/0001-audit-core-kandidaten.md).

## Grenzen von v1.0

Noch nicht enthalten: Build-Adapter (Tokens → CSS/Tailwind/PPTX/DOCX), weitere Komponenten (Dropdown-Menü, Combobox, Datumsauswahl, Avatar, Fortschritt, Chip, Datei-Upload), E-Mail-Template, Figma-Bibliothek. Details in [core/decisions/0003](core/decisions/0003-smoke-test-v1.md).
