# Core vs. Project: Zuordnungsregeln (Core)

## Entscheidungsbaum

```
Ist es ein Wert, eine Farbe, eine Schrift, ein Motiv, ein Logo oder ein Tonfall?
  └─ ja  → PROJEKT
  └─ nein → Ist es eine Regel, Methode, Struktur, Rolle, Skala oder Mindestanforderung?
             └─ nein → PROJEKT (Inhalt)
             └─ ja  → Gilt sie auch für ein Projekt ganz anderer Art
                      (z. B. Handwerksbetrieb UND B2B-SaaS UND persönliche Marke)?
                       └─ nein / unsicher → PROJEKT, als [CORE-KANDIDAT] markieren
                       └─ ja → Steht sie schon in Core?
                                └─ ja  → Core-Regel anwenden, ggf. Verweis
                                └─ nein → [CORE-KANDIDAT], Promotion-Prozess
```

## Beispiele

| Aussage | Zuordnung |
|---|---|
| „Unsere Aktionsfarbe ist Orange.“ | Projekt (`tokens/`) |
| „Jede Aktion hat genau eine primäre Aktionsfarbe.“ | Core (`tokens/color.md`) |
| „Wir duzen.“ | Projekt (`brand/voice.md`) |
| „Jedes Projekt legt eine Anrede-Regel fest.“ | Core (`principles/content-writing.md`) |
| „Buchungskalender zeigt freie Tage grün mit Häkchen.“ | Projekt (Komponente), die Regel „Status nie nur über Farbe“ ist Core |
| „Fehlermeldungen nennen die Lösung.“ | Core |
| „Unsere Karten haben 24 px Radius.“ | Projekt |
| „Radien verschachtelter Elemente laufen parallel.“ | Core (`tokens/shape-elevation.md`) |

## Beim Arbeiten in einem Projekt

- Core-Dateien werden **gelesen, nicht geändert**.
- Abweichungen von Core werden als **Ausnahme** in `DECISIONS.md` dokumentiert ([governance.md](../../process/governance.md#ausnahmen)).
- Regeln, die nur in diesem Projekt gelten, stehen in `brand/`, `tokens/README.md` oder `components/`.
- Wenn eine Core-Regel im Projekt stört: nicht umgehen, sondern Ausnahme dokumentieren und ggf. Core-Kandidat für eine Anpassung melden.

## Beim Arbeiten an Core

- Nur nach Freigabe durch den Nutzer.
- Formulierungen verallgemeinern, keine Projektbegriffe (Projektnamen, Branchenbegriffe, Markenwerte) in Core-Regeln. Beispiele dürfen Projekttypen nennen, aber keine konkreten Marken.
- CHANGELOG und Version pflegen.
