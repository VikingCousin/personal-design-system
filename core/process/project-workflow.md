# Projekt-Workflow: Phasen und Gates (Core)

> Wie ein Projekt vom Brief bis zu Templates entsteht. Gilt für jedes Projekt. Die **Tiefe** passt sich der Projektgröße an, die **Gates** bleiben.

## 1. Phasen im Überblick

| # | Phase | Ergebnis | Gate danach |
|---|---|---|---|
| 0 | **Setup** | Projektordner aus der [Vorlage](project-template/), `README.md` ausgefüllt | G0 · Setup bestätigt |
| 1 | **Brief** | `brief/BRIEF.md` + Brief-Analyse (Lücken, Widersprüche, OPEN) | G1 · Brief bestätigt |
| 2 | **Brand Foundation** | `brand/foundation.md`, `brand/voice.md` | G2 · Arbeitsfreigabe Foundation |
| 3 | **Research** *(bei Bedarf, auch parallel)* | `research/RESEARCH-AGENDA.md`, Befunde | — |
| 4 | **Creative Direction** | 2–3 Richtungen + Style-Tiles in `prototypes/`, Bewertung | G3 · Richtung gewählt |
| 5 | **Tokens** | `tokens/*.tokens.json` + `tokens/README.md` (Kontraste, Lizenzen) | G4 · Tokens freigegeben |
| 6 | **Components** | Umsetzung der Core-Komponenten + Projektkomponenten | G5 · Komponenten freigegeben |
| 7 | **Templates** | gebrandete Templates (Web, App, Dokument, Präsentation …) | G5 · Templates freigegeben |
| 8 | **Anwendung / Release** | Website, App, Dokumente, Brand-Guideline | G6 · Veröffentlichung |

Die Gates sind in [agent-skill/rules/approval-gates.md](../agent-skill/rules/approval-gates.md) genau beschrieben.

## 2. Prozess-Tiefe

Im Setup wählt der Nutzer (Claude schlägt vor) eine Tiefe:

| | **S · Kompakt** | **M · Standard** | **L · Umfassend** |
|---|---|---|---|
| Typisch | Landingpage für lokales Unternehmen, persönliche Seite, Event, einfaches Tool | neues Produkt, Dienstleistungsmarke, SaaS-MVP | neue Marke mit großer Tragweite, viele Medien, physische Produkte, sensible Themen |
| Brief | Kurzbrief (Fragenkatalog §1 der Vorlage) | vollständiger Brief | vollständiger Brief + Analyse |
| Brand Foundation | 1 Seite: Idee, Zielgruppe, 3 Prinzipien, Tonalität, Anrede | vollständig | vollständig, mit FAKT/ABLEITUNG/ANNAHME |
| Research | Desk: 3–5 Wettbewerber bzw. Vorbilder | gezielt für offene Fragen | Research-Agenda (Desk, User, Partner, Legal, Tech) |
| Creative Direction | 2 Richtungen **oder** 1 Richtung mit 2 Varianten | 2–3 Richtungen | 3 Richtungen + Tests mit Nutzenden |
| Tokens | Pflichtvertrag | Pflichtvertrag + Ergänzungen | + Modi, Themes, Material, Print |
| Components | Core-Komponenten ohne eigene Specs | + Projekt-Specs für Abweichungen | + projektspezifische Komponenten-Bibliothek |
| Templates | 1–2 | nach Bedarf | vollständiges Set + Brand-Guideline |
| Gates | G1+G2 und G4+G5 dürfen gebündelt werden | alle | alle, schriftlich im Log |

## 3. Einstiegsvarianten

| Variante | Vorgehen |
|---|---|
| **Neue Marke** | Phasen 0–8 wie oben |
| **Bestehende Marke** (Logo, Farben, Schriften vorhanden) | Phase 4 wird zu **Brand-Import**: Vorhandenes erfassen, gegen Core prüfen (Kontraste, Lesbarkeit, Lizenzen), Probleme und Lösungsoptionen vorlegen. Keine neuen Richtungen, außer der Nutzer wünscht ein Redesign. |
| **Nur Anwendung** (z. B. „baue eine Präsentation im Stil von Projekt X“) | Direkt Phase 7/8 mit den vorhandenen Tokens und Templates des Projekts |

## 4. Wann was passiert

| Frage | Regel |
|---|---|
| **Wann ist Research nötig?** | Wenn eine offene Entscheidung ohne Evidenz nur geraten wäre (Zielgruppe unklar, Wettbewerb unbekannt, Recht oder Technik betroffen, sensible Themen). In Tiefe S genügt kurze Desk-Recherche. Behauptungen ohne Quelle werden als ANNAHME markiert. |
| **Wann Creative Directions?** | Wenn die visuelle Identität neu entsteht oder grundlegend geändert wird, und erst **nach G2** (Foundation). Bei bestehender Marke: Brand-Import. |
| **Wann Tokens?** | Erst **nach G3** (Richtung gewählt). Werte aus Explorationen sind nur Arbeitswerte. |
| **Wann Components?** | Nach G4. Zuerst die Core-Komponenten, die die Templates brauchen, dann Projektkomponenten. |
| **Wann Templates?** | Wenn die benötigten Komponenten stehen. In Tiefe S dürfen Komponenten direkt im ersten Template entstehen, müssen aber Core-Regeln erfüllen. |
| **Wann ist ein Projekt „fertig“?** | Wenn die im Setup vereinbarten Ergebnisse vorliegen und die [Qualitätsprüfung](../principles/quality-standards.md) bestanden ist. |

## 5. Grundsätze während aller Phasen

- Der Brief ist Source of Truth. Widersprüche werden dokumentiert (`DECISIONS.md` → OPEN), nicht still aufgelöst.
- Projektregeln stehen im Projekt, Core-Regeln im Core. Eine Projektregel, die allgemein gelten könnte, wird als `[CORE-KANDIDAT]` markiert ([promotion.md](promotion.md)).
- Offene strategische Entscheidungen werden von späteren Phasen nicht implizit entschieden. Sie werden mit Leitplanken offen gehalten ([documentation.md](../principles/documentation.md)).
