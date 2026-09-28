---
name: personal-design-system
description: Arbeitsweise für das Personal Design System (PDS) des Nutzers. Verwenden, wenn der Nutzer ein neues Projekt „mit meinem Personal Design System“ anlegen, eine Marke, Website, App, Dokument oder Präsentation darin gestalten, Tokens oder Komponenten für ein Projekt erstellen oder das Core-System weiterentwickeln will. Das System ist der Ordner, der dieses Skill unter core/agent-skill/ enthält.
---

# Personal Design System · Agent Skill

> Core-Version: **1.0.0**. Dieses Skill beschreibt, **wie** Claude mit dem System arbeitet. **Was** gilt, steht in `core/`.
> Pfad des Systems: das Wurzelverzeichnis dieses Repositorys (im Folgenden `PDS/`).

## Grundhaltung

- **Core ist die Systematik, das Projekt ist die Marke.** Core schreibt keinen Stil vor. Farben, Schriften, Bildsprache und Tonalität entstehen im Projekt.
- **Claude bereitet vor, der Nutzer entscheidet.** Wesentliche Marken- und Geschäftsentscheidungen werden nie von Claude finalisiert ([approval-gates.md](rules/approval-gates.md)).
- **Core wird nie stillschweigend verändert**, auch nicht, wenn ein Projekt es nahelegt ([core-vs-project.md](rules/core-vs-project.md)).
- **Qualität vor Tempo:** Accessibility und Responsive sind Mindeststandards, keine Extras.

## Auslöser

- „Ich möchte ein neues Projekt X erstellen. Verwende mein Personal Design System.“
- „Erstelle für Projekt X eine Website / Präsentation / Brand-Guideline.“
- „Leite die Tokens für Projekt X ab.“
- „Nimm diese Regel in Core auf.“ / „Prüfe die Core-Kandidaten von Projekt X.“

## Ablauf für ein neues Projekt

| # | Schritt | Was Claude tut | Referenz |
|---|---|---|---|
| 1 | **Core lesen** | `PDS/README.md`, `core/README.md`, dieses Skill, die Principles und `process/project-workflow.md` lesen. Core-Version notieren. | `core/` |
| 2 | **Projekt anlegen** | `projects/<name>/` aus `core/process/project-template/` kopieren, README ausfüllen. Tiefe S/M/L, Accessibility-Profil und Einstieg (neue Marke / bestehende Marke / nur Anwendung) **vorschlagen**. | `process/project-bootstrap.md` |
| 3 | **Brief erfassen** | Brief des Nutzers unverändert in `brief/BRIEF.md` übernehmen oder mit dem Kurzbrief-Fragenkatalog erarbeiten. → **Gate G1** | Vorlage `brief/BRIEF.md` |
| 4 | **Lücken identifizieren** | Widersprüche, fehlende strategische Entscheidungen und Annahmen als OPEN in `DECISIONS.md`. Gebündelt fragen (A: vor der nächsten Phase nötig, B: bald, C: später), nicht 50 Einzelfragen. | `principles/documentation.md` |
| 5 | **Brand Foundation** | Idee, Positionierung, Zielgruppen, Persönlichkeit, Prinzipien, Voice inkl. Anrede-Regel. Kennzeichnung FAKT/ABLEITUNG/ANNAHME/OFFEN. → **Gate G2** | Vorlagen `brand/` |
| 6 | **Creative Directions** | Nur bei neuer Marke oder Redesign: Kriterien vorher festlegen, 2–3 echte Alternativen, Style-Tiles mit identischen Proben, Bewertung ohne Gewinner. Bei bestehender Marke: Brand-Import. | `process/creative-direction.md` |
| 7 | **Nutzer entscheiden lassen** | Richtung, Kombination oder Überarbeitung wählt der Nutzer. → **Gate G3** | `rules/approval-gates.md` |
| 8 | **Project Tokens** | Aus Core-Architektur ableiten: Primitives (Core-Defaults übernehmen oder begründet ändern), alle Pflicht-Tokens des Vertrags, Kontrastpaare prüfen und dokumentieren. → **Gate G4** | `tokens/architecture.md`, `contract.tokens.json` |
| 9 | **Components** | Core-Spezifikationen mit Projekt-Tokens umsetzen. Nur Abweichungen und Projektkomponenten bekommen eigene Specs. | `components/` |
| 10 | **Templates** | Core-Template-Strukturen gebranded umsetzen. → **Gate G5** | `templates/` |
| 11 | **Prüfen** | Accessibility und Responsive nach Checkliste prüfen, im Browser verifizieren, Ergebnis berichten. | `principles/quality-standards.md` |
| 12 | **Trennen** | Projektregeln nur im Projekt. Kein Projektwert in `core/`. | `rules/core-vs-project.md` |
| 13 | **Core-Kandidaten markieren** | Mögliche universelle Regeln als `[CORE-KANDIDAT]` am Fundort und in `DECISIONS.md` sammeln. | `process/promotion.md` |
| 14 | **Core nicht still ändern** | Promotion nur über Review und Freigabe durch den Nutzer, mit CHANGELOG und Version. | `process/governance.md` |

Tiefe S darf Schritte verdichten (z. B. Foundation auf einer Seite, G1+G2 zusammen), **überspringt aber keine Gates**.

## Harte Regeln

1. Nie einen Markennamen, ein Logo, eine visuelle Richtung, finale Farben oder Schriften, Preise oder Geschäftsmodell-Entscheidungen ohne Freigabe als final festlegen. Ohne Freigabe heißt alles „Entwurf“, „Exploration“ oder „Vorschlag“.
2. Nie offene Entscheidungen implizit schließen (z. B. durch eine Gestaltung, die eine Zielgruppe bevorzugt).
3. Nie Rohwerte in Komponenten; nie Primitives direkt in Komponenten.
4. Nie Werte aus Explorationen ungeprüft in Tokens übernehmen.
5. Nie den Brief des Nutzers verändern. Widersprüche werden dokumentiert.
6. Nie etwas veröffentlichen, deployen oder versenden ohne ausdrückliche Freigabe (G6).
7. Nie Belege erfinden (Kundenstimmen, Zahlen, Auszeichnungen, Zertifikate). Platzhalter kennzeichnen.
8. Nie Projektmarken, Projektbegriffe oder Projektwerte in `core/` schreiben.

## Wie Claude berichtet

- Kurz, was erledigt ist, was offen ist und was der Nutzer als Nächstes entscheiden muss (gebündelt, mit Optionen).
- Dateien als Links. Prototypen mit Anleitung zum Öffnen.
- Ehrlich über Grenzen: Was geprüft wurde, was nur Hypothese ist.

## Dateikarte

```
PDS/
├── README.md                    Einstieg
├── AGENTS.md / CLAUDE.md        Agent-Einstieg (verweist hierher)
├── core/
│   ├── README.md                Inhaltsverzeichnis Core, Version
│   ├── CHANGELOG.md
│   ├── principles/              design-principles, accessibility, responsive, interaction, content-writing, quality-standards, documentation, visual-assets
│   ├── tokens/                  architecture, naming, color, typography, spacing-sizing, shape-elevation, motion, layout, contract/defaults.tokens.json
│   ├── components/              README (Architektur, Zustände, Varianten), actions, forms, containers, navigation, feedback, data, _spec-template
│   ├── templates/               website-landingpage, marketing-page, transaction-flow, app-dashboard, document, presentation, brand-guideline
│   ├── process/                 project-workflow, project-bootstrap, creative-direction, promotion, governance, project-template/
│   ├── patterns/                unverbindliche Muster
│   ├── decisions/               Core-Entscheidungen
│   └── agent-skill/             dieses Skill, rules/, examples/
└── projects/<name>/             ein Ordner je Projekt
```
