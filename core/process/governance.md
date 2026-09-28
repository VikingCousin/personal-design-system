# Governance und Versionierung (Core)

> Bewusst schlank: Das System wird von einer Person mit AI-Unterstützung gepflegt. Ziel ist Nachvollziehbarkeit, nicht Bürokratie.

## Rollen

| Rolle | Wer | Darf |
|---|---|---|
| **Owner** | der Nutzer | Core ändern, Projekte freigeben, Ausnahmen genehmigen, Versionen festlegen |
| **Assistenz** | Claude / AI Agents | Core-Änderungen **vorschlagen**, nach Freigabe umsetzen; in Projekten arbeiten gemäß Gates |

**Ownership:** `core/` gehört dem Owner, Änderungen nur nach ausdrücklicher Freigabe. `projects/<p>/` gehört zum jeweiligen Projekt; dort arbeitet Claude innerhalb der Gates selbstständig.

## Versionierung

Core folgt Semantic Versioning `MAJOR.MINOR.PATCH`. Die aktuelle Version steht im [CHANGELOG](../CHANGELOG.md) und in [core/README.md](../README.md).

| Stufe | Wann | Beispiele |
|---|---|---|
| **MAJOR** | bricht bestehende Projekte | Pflicht-Token umbenannt oder entfernt, Namensgrammatik geändert, Gate entfernt, Accessibility-Baseline geändert |
| **MINOR** | neue Möglichkeiten, rückwärtskompatibel | neue Komponente, neue optionale Token-Gruppe, neue bedingte Regel, neues Template |
| **PATCH** | Klarstellung, Korrektur | Tippfehler, Beispiel ergänzt, Link repariert, Formulierung präzisiert |

Projekte notieren ihre Core-Version im Projekt-README. Ein Projekt muss Core-Updates nicht sofort übernehmen.

## Änderungsregeln

1. Jede Änderung an `core/` steht im CHANGELOG (Datum, Version, was, warum).
2. Größere Änderungen (MAJOR, neue Prinzipien, Promotions) bekommen einen Eintrag in `core/decisions/NNNN-titel.md`.
3. Eine Regel steht an genau einer Stelle. Bei Änderungen werden alle Verweise geprüft.
4. Änderungen aus Projekten nur über den [Promotion-Prozess](promotion.md).

## Deprecation

- Veraltete Regeln oder Tokens werden **markiert, nicht sofort gelöscht**:
  `⚠️ DEPRECATED seit 1.3.0 · Ersatz: color.text.link · Entfernung frühestens in 2.0.0`
- Deprecated-Elemente bleiben mindestens bis zur nächsten MAJOR-Version erhalten.
- Claude weist bei Projektarbeit auf verwendete Deprecated-Elemente hin.

## Ausnahmen

Ein Projekt darf von einer Core-Regel abweichen, wenn es einen guten Grund gibt. Die Abweichung steht in der Projekt-`DECISIONS.md`:

```markdown
## D-007 · Ausnahme: Button-Radius
- Status: ENTSCHIEDEN · Ausnahme von core/components/actions.md
- Was: …   Warum: …   Geltungsbereich: …   Überprüfen am / bei: …
```

**Keine Ausnahmen** bei der Accessibility-Baseline. Ausnahme hiervon: Ein Medium kann eine Regel technisch nicht erfüllen (z. B. eine einfarbige Prägung hat keine Farbkontraste). Dann wird ein gleichwertiger Ersatz dokumentiert.

Wiederholt sich dieselbe Ausnahme in mehreren Projekten, ist das ein Hinweis, die Core-Regel zu überprüfen.

## Entscheidungsdokumentation

- Core: `core/decisions/NNNN-titel.md` (fortlaufend nummeriert)
- Projekt: `projects/<p>/DECISIONS.md`
- Format und Status: [documentation.md](../principles/documentation.md)
