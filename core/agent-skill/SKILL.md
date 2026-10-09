---
name: personal-design-system
description: Arbeitsweise für das Personal Design System (PDS) des Nutzers. Verwenden, wenn der Nutzer ein neues Projekt „mit meinem Personal Design System“ anlegen, eine Marke, Website, App, Dokument oder Präsentation darin gestalten, Tokens oder Komponenten für ein Projekt erstellen oder das Core-System weiterentwickeln will. Das System ist der Ordner, der dieses Skill unter core/agent-skill/ enthält.
---

# Personal Design System · Agent Skill

> Core-Version: **1.1.0**. Dieses Skill beschreibt, **wie** Claude mit dem System arbeitet. **Was** gilt, steht in `core/`.
> Pfad des Systems: das Wurzelverzeichnis dieses Repositorys (im Folgenden `PDS/`).

## Grundhaltung

- **Core ist die Systematik, das Projekt ist die Marke.** Core schreibt keinen Stil vor. Farben, Schriften, Bildsprache und Tonalität entstehen im Projekt.
- **Claude bereitet vor, der Nutzer entscheidet.** Wesentliche Marken- und Geschäftsentscheidungen werden nie von Claude finalisiert ([approval-gates.md](rules/approval-gates.md)).
- **Core wird nie stillschweigend verändert**, auch nicht, wenn ein Projekt es nahelegt ([core-vs-project.md](rules/core-vs-project.md)).
- **Qualität vor Tempo:** Accessibility und Responsive sind Mindeststandards, keine Extras.

## Auslöser

- „Ich möchte ein neues Projekt X erstellen. Verwende mein Personal Design System.“
- „Erstelle für Projekt X eine Website / Präsentation / Brand-Guideline.“
- „Leite die Tokens für Projekt X ab.“ / „Erstelle das Brand Kit für Projekt X.“
- „Erstelle einen Pinterest Pin / Instagram Post / Newsletter für Projekt X gemäß meinem Design System.“
- „Exportiere das AI Brand Context Pack für Projekt X.“
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
| 8 | **Project Tokens & Brand Kit** | Tokens aus der Core-Architektur ableiten (Primitives, alle Pflicht-Tokens, Kontraste). Dann `brand-kit/brand-kit.json` füllen (Verweise auf Tokens, nichts kopieren, Offenes bleibt OPEN), `build_brand_kit.py` ausführen, QA-Bericht prüfen. → **Gate G4** (Tokens und Brand Kit) | `tokens/architecture.md`, `brand-kit/README.md` |
| 9 | **Components** | Core-Spezifikationen mit Projekt-Tokens umsetzen. Nur Abweichungen und Projektkomponenten bekommen eigene Specs. | `components/` |
| 10 | **Templates & Kanäle** | Core-Template-Strukturen und Kanal-Starter mit Brand Kit und Tokens umsetzen. → **Gate G5** | `templates/`, `templates/cross-channel.md` |
| 11 | **Prüfen** | Accessibility und Responsive nach Checkliste prüfen, im Browser verifizieren, Ergebnis berichten. | `principles/quality-standards.md` |
| 12 | **Trennen** | Projektregeln nur im Projekt. Kein Projektwert in `core/`. | `rules/core-vs-project.md` |
| 13 | **Core-Kandidaten markieren** | Mögliche universelle Regeln als `[CORE-KANDIDAT]` am Fundort und in `DECISIONS.md` sammeln. | `process/promotion.md` |
| 14 | **Core nicht still ändern** | Promotion nur über Review und Freigabe durch den Nutzer, mit CHANGELOG und Version. | `process/governance.md` |

Tiefe S darf Schritte verdichten (z. B. Foundation auf einer Seite, G1+G2 zusammen), **überspringt aber keine Gates**.

## Kanalaufträge (z. B. „Erstelle einen Pinterest Pin für Projekt X“)

1. **Projekt finden** (`projects/<x>/`). Unklar welches → nachfragen.
2. **Brand Kit lesen** (`brand-kit/brand-kit.json`): Version und Status notieren. Kanal muss in `channels` stehen.
3. **Kanalvorlage anwenden**: Regeln aus [templates/cross-channel.md](../templates/cross-channel.md) und dem Kanal-Template, Starter aus `brand-kit/generator/starters/`.
4. **Nur freigegebene Assets und Tokens** verwenden (Logos mit `ENTSCHIEDEN`, Werte aus den Token-Dateien).
5. **Fehlende Informationen erfragen** (Inhalt, Ziel-URL, Bild, Kennzeichnung). Nicht Erfragtes bleibt sichtbar `[OFFEN: …]`.
6. **Keine neue visuelle Identität erfinden.** Kein Brand Kit → anbieten: Brand Kit aufbauen bzw. bestehende Marke importieren, oder ein klar als „Entwurf ohne Markenidentität“ gekennzeichneter Strukturentwurf.
7. **Konsistent erzeugen und prüfen**: Inhalte in `channels.<kanal>.sample` eintragen, `build_brand_kit.py` ausführen, QA-Konsistenzprüfung muss bestehen; Pre-Production-Check aus cross-channel.md; Veröffentlichung nur nach G6.

Ist das Kit nur `ENTWURF`, wird das Ergebnis als Entwurf gekennzeichnet.

## Export für externe KI-Tools (AI Brand Context Pack, Core 1.1)

Bei „Exportiere das AI Brand Context Pack für Projekt X“ oder „Brand Kit für ChatGPT“:
1. Projekt finden, `projects/<x>/brand-kit/brand-kit.json` lesen. Fehlt es: nur die Entwurfsvorlage erzeugen und anbieten, ein Brand Kit aufzubauen oder zu importieren. Nichts erfinden.
2. `build_brand_kit.py` und danach `export_ai_context.py` ausführen ([brand-kit/README.md](../brand-kit/README.md#7-ai-brand-context-pack-export-für-chatgpt-claude-gemini-)).
3. `EXPORT-CHECK.md` lesen und berichten: Status (FREIGEGEBEN / ENTWURF / DEMO), offene Punkte, ausgeschlossene Dateien, Funde.
4. **Nichts selbst hochladen oder veröffentlichen.** Die Weitergabe an externe Dienste gibt der Nutzer frei (G6).

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
│   ├── templates/               website-landingpage, marketing-page, transaction-flow, app-dashboard, document, presentation, brand-guideline, cross-channel, social-media, newsletter-email
│   ├── brand-kit/               Brand-Kit-Vertrag, generator/ (build_brand_kit.py, export_ai_context.py, starters/), tests/
│   ├── process/                 project-workflow, project-bootstrap, creative-direction, promotion, governance, project-template/
│   ├── patterns/                unverbindliche Muster
│   ├── decisions/               Core-Entscheidungen
│   └── agent-skill/             dieses Skill, rules/, examples/
├── projects/<name>/             ein Ordner je Projekt
└── demo/                        fiktive Demo-Marken zum Testen (nie als reale Marke verwenden)
```
