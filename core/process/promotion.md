# Promotion: Project → Core (Core)

> Wie eine Erkenntnis aus einem Projekt zu einer Core-Regel wird. Grundsatz: **Core wird nie stillschweigend aufgrund eines einzelnen Projekts verändert.**

## 1. Markieren

Während der Projektarbeit markiert Claude (oder der Nutzer) mögliche universelle Regeln direkt am Fundort:

```markdown
[CORE-KANDIDAT] Fehlermeldungen nennen immer die Lösung, nicht nur das Problem.
```

und sammelt sie in der Projekt-`DECISIONS.md` im Abschnitt „Core-Kandidaten“ mit ID, Quelle und Kurzbegründung.

## 2. Kriterien

Ein Kandidat wird nur übernommen, wenn **alle Pflichtkriterien** erfüllt sind:

| # | Kriterium | Pflicht? | Prüffrage |
|---|---|---|---|
| 1 | markenunabhängig | Pflicht | Enthält die Regel Farbe, Form, Schrift, Tonalität oder Motive einer Marke? Dann nein. |
| 2 | in mehreren Projekttypen sinnvoll | Pflicht | Stimmt die Regel für mindestens zwei sehr unterschiedliche Projekttypen (z. B. lokaler Handwerker **und** B2B-SaaS)? |
| 3 | Nutzen | Pflicht | Verbessert sie Accessibility, Usability, Qualität oder Systemkonsistenz? |
| 4 | keine unnötige Einschränkung | Pflicht | Verbietet sie künftigen Marken einen legitimen Stil? |
| 5 | dokumentierbar bzw. tokenisierbar | Pflicht | Lässt sie sich klar als Regel, Token, Spezifikation oder Checkliste formulieren? |
| 6 | bewährt | empfohlen | Wurde sie in einem Projekt tatsächlich angewendet und hat sich bewährt? |
| 7 | kein Widerspruch | Pflicht | Widerspricht sie keiner bestehenden Core-Regel, oder wird die bestehende Regel bewusst ersetzt? |

**Ergebnisse:**
- **A · übernehmen** → Core-Regel (ggf. als bedingte Regel: „Wenn … dann …“)
- **B · Muster** → [`core/patterns/`](../patterns/README.md), unverbindlich
- **C · projektspezifisch** → bleibt im Projekt
- **zurückgestellt** → erneut prüfen, wenn ein zweites Projekt die Regel bestätigt

## 3. Review-Prozess (leichtgewichtig)

1. **Sammeln:** Kandidaten stehen in der Projekt-`DECISIONS.md`.
2. **Prüfen:** Claude prüft sie gegen die Kriterien und simuliert kurz zwei andere Projekttypen. Das Ergebnis ist eine Tabelle mit A/B/C und Begründung.
3. **Entscheiden:** Der Nutzer entscheidet (einzeln oder gesammelt).
4. **Umsetzen:** Claude schreibt die Regel an **eine** passende Stelle in `core/`, verallgemeinert die Formulierung, entfernt Projektbezüge und ergänzt Querverweise.
5. **Dokumentieren:** Eintrag in `core/decisions/` (bei größeren Änderungen) und immer im [CHANGELOG](../CHANGELOG.md), Versionsnummer nach [Governance](governance.md#versionierung) erhöhen.
6. **Rückmelden:** Im Projekt wird der Kandidat als „übernommen in Core x.y“ bzw. „Muster“ oder „projektspezifisch“ markiert.

**Wann:** am Ende einer Projektphase oder spätestens bei Projektabschluss, nicht mitten in einer Aufgabe.
