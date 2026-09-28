# Project Bootstrap: ein neues Projekt anlegen (Core)

## 1. Kurzfassung

1. Projektnamen als Ordnernamen festlegen: `projects/<projekt-name>/` (kebab-case, Arbeitsname genügt).
2. Den Inhalt von [`project-template/`](project-template/) in den neuen Ordner kopieren.
3. `README.md` des Projekts mit den Startinformationen füllen (§3).
4. Brief in `brief/BRIEF.md` erfassen (vom Nutzer geliefert oder im Gespräch erarbeitet).
5. Prozess-Tiefe und Accessibility-Profil vorschlagen, Nutzer bestätigt (Gate G0).
6. Weiter mit Phase 1 ([project-workflow.md](project-workflow.md)).

## 2. Ordner

```
projects/<projekt-name>/
├── README.md          PFLICHT · Steckbrief: Status, Phase, Core-Version, Profil, Tiefe
├── DECISIONS.md       PFLICHT · Entscheidungslog (OPEN / ARBEITSFREIGABE / ENTSCHIEDEN)
├── brief/             PFLICHT · BRIEF.md (Source of Truth)
├── brand/             PFLICHT ab Phase 2 · foundation.md, voice.md, visual-direction.md
├── tokens/            PFLICHT ab Phase 5 · *.tokens.json + README.md
├── components/        PFLICHT ab Phase 6 · Projekt-Specs, Abweichungen von Core
├── templates/         PFLICHT ab Phase 7 · gebrandete Templates
├── assets/            PFLICHT ab Phase 5 · logos/, icons/, fonts/, images/
├── research/          OPTIONAL · RESEARCH-AGENDA.md, findings/
├── prototypes/        OPTIONAL · Explorationen, Style-Tiles (nie Produktionscode)
├── examples/          OPTIONAL · angewandte Beispiele (Website, Dokument …)
└── build/             OPTIONAL · generierte Ausgaben (CSS, Tailwind …), nie von Hand bearbeiten
```

Die Vorlage enthält alle Pflichtordner mit einer kurzen `README.md` bzw. Startdatei, damit klar ist, was hineingehört, und zusätzlich `research/` mit einer leeren Research-Agenda. Wird keine Research gebraucht, darf `research/` gelöscht werden. Die übrigen optionalen Ordner (`prototypes/`, `examples/`, `build/`) werden erst angelegt, wenn sie gebraucht werden.

## 3. Startinformationen vom Nutzer

Mindestens (kann im Gespräch erfragt werden, fehlende Punkte werden OPEN):

| # | Information | Warum |
|---|---|---|
| 1 | Was ist das Projekt, was wird angeboten? | Grundlage |
| 2 | Für wen (Zielgruppen, Nutzungssituation)? | Accessibility-Profil, Tonalität |
| 3 | Ziel (verkaufen, buchen lassen, informieren, Leads, intern nutzen …) | Hauptaktion, Templates |
| 4 | Welche Medien bzw. Ergebnisse werden gebraucht (Website, App, Dokumente, Präsentation, Print, Fahrzeug, Produkt …)? | Umfang, restriktivstes Medium, Farbdokumentation |
| 5 | Gibt es schon eine Marke (Name, Logo, Farben, Schriften)? | Neue Marke oder Brand-Import |
| 6 | Sprache(n), Markt, Anrede-Wunsch | Content-Regeln |
| 7 | Vorbilder, Abneigungen, Wettbewerber | Creative Direction |
| 8 | Rahmen: Zeit, Budget, Technik (z. B. WordPress, React, Shopify) | Tiefe, Umsetzung |
| 9 | Was ist bereits entschieden, was bewusst offen? | Entscheidungslog |

## 4. Was Claude beim Bootstrap vorschlagen darf, der Nutzer aber bestätigt

- Projektname als **Arbeitsname** (nie als finaler Markenname)
- Prozess-Tiefe S / M / L
- Accessibility-Profil Standard / Erweitert
- Liste der benötigten Ergebnisse (Medien, Templates)
- ob Research vor der Foundation nötig ist

## 5. Was Claude NICHT selbst entscheidet

Siehe [approval-gates.md](../agent-skill/rules/approval-gates.md#nie-ohne-nutzer). Kurz: Markenname, Positionierung, Markenprinzipien, visuelle Richtung, finale Farben und Schriften, Logo, Anrede, Geschäftsmodell und Preise, rechtliche Aussagen, Veröffentlichung.

## 6. Core-Version festhalten

In `README.md` des Projekts steht, auf welcher Core-Version das Projekt aufbaut (z. B. `Core 1.0.0`). Bei Core-Updates prüft Claude die Auswirkungen anhand des [CHANGELOG](../CHANGELOG.md) und schlägt ein Update des Projekts vor, statt es stillschweigend umzustellen.
