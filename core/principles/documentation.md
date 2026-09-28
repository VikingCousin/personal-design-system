# Dokumentation und Entscheidungen (Core)

> Wie Projekte und Core dokumentiert werden, damit Menschen und AI Agents auch später nachvollziehen können, **was** gilt und **warum**.

## 1. Entscheidungsebenen

| Ebene | Bedeutung | Ort |
|---|---|---|
| **PDS** | Personal-Design-System-Entscheidung, gilt für alle Projekte | `core/decisions/` |
| **PROJ** | projektspezifische Entscheidung | `projects/<p>/DECISIONS.md` |
| **OPEN** | bewusst noch nicht entschieden | als OPEN im jeweiligen Log |

## 2. Entscheidungsstatus

| Status | Bedeutung |
|---|---|
| **OPEN** | nicht entschieden. Keine Phase darf die Entscheidung implizit vorwegnehmen. Kann **Leitplanken** haben (was unabhängig vom Ausgang gilt). |
| **ARBEITSFREIGABE** | gilt als Grundlage für die nächste Phase, ist aber nicht eingefroren |
| **ENTSCHIEDEN** | gilt, bis es ausdrücklich revidiert wird |
| **REVIDIERT / ABGELÖST** | ersetzt durch eine neuere Entscheidung (mit Verweis) |

Nur der Nutzer setzt ARBEITSFREIGABE oder ENTSCHIEDEN. Claude schlägt vor.

## 3. Aussagekennzeichnung in strategischen Dokumenten

Brief-Analysen, Brand Foundation, Strategie- und Research-Dokumente kennzeichnen jede wesentliche Aussage:

| Markierung | Bedeutung |
|---|---|
| **[FAKT]** | steht im Brief oder wurde vom Nutzer gesagt (mit Quelle, z. B. `§3`) |
| **[ABLEITUNG]** | daraus entwickelt, nicht festgelegt |
| **[ANNAHME]** | unbelegt, muss validiert werden (Verweis auf Research) |
| **[OFFEN]** | offene Entscheidung (Verweis auf ID) |
| **[CORE-KANDIDAT]** | könnte projektübergreifend gelten ([Promotion](../process/promotion.md)) |

Reine Spezifikationen (Tokens, Komponenten) brauchen diese Kennzeichnung nicht.

## 4. Format eines Entscheidungseintrags

```markdown
## D-012 · Anrede in der App
- Status: ENTSCHIEDEN · 2026-10-02 · Ebene: PROJ
- Kontext: Warum musste entschieden werden?
- Optionen: a) … b) … c) …
- Entscheidung: b
- Begründung: (bei Designentscheidungen: die 7 Prüffragen, knapp)
- Folgen: Was ändert sich, was ist jetzt ausgeschlossen?
- Ausnahmen / offene Punkte: …
```

Core-Entscheidungen liegen als eigene Dateien in `core/decisions/NNNN-titel.md`. Projektentscheidungen stehen gesammelt in `projects/<p>/DECISIONS.md`.

## 5. Dokumentregeln

- **Status-Kopf** in jedem Arbeitsdokument: Status, Datum, Bezug.
- **Source of Truth:** Der Brief des Projekts ist die strategische Grundlage. Widersprüche werden dokumentiert, nicht still aufgelöst. Den Brief ändert nur der Nutzer.
- **Arbeitsstände** heißen so, bis sie freigegeben sind.
- **Dateinamen:** englisch oder deutsch, kebab-case, ohne Leerzeichen. Reihenfolge-Präfixe (`01-`) nur, wenn die Reihenfolge Bedeutung hat.
- **Querverweise** mit relativen Pfaden.
- **Keine Dopplung:** Eine Regel steht an genau einer Stelle, alles andere verweist darauf.
