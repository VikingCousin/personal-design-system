# Data: Table (Core)

## Table

**Zweck:** strukturierte Daten zum Vergleichen, Sortieren und Bearbeiten. **Nicht** für Layout. Für wenige Datenpunkte pro Objekt besser Liste oder Karten.

**Anatomie:** 1 Beschriftung (`<caption>` oder Überschrift) · 2 Toolbar (Suche, Filter, Aktionen, optional) · 3 Kopfzeile · 4 Zeilen · 5 Zellen · 6 Auswahl-Checkboxen (optional) · 7 Zeilenaktionen (optional) · 8 Fuß mit Summen oder Pagination (optional)

**Varianten:** Dichte `comfortable` · `compact` (nur Zeiger-Geräte, siehe [Dichte](../tokens/spacing-sizing.md#4-dichte)) · Zeilentrennung per Linie oder abwechselnder Fläche · sticky Kopf bzw. erste Spalte

**Zustände:** default · row-hover · row-selected · sorted (`aria-sort`) · loading (Skeleton-Zeilen) · empty (Empty State in der Tabelle) · error · editing (bei Inline-Bearbeitung)

**Accessibility**
- echtes `<table>` mit `<th scope="col|row">`; komplexe Köpfe mit `headers`
- Sortierung: Button im Spaltenkopf, `aria-sort` am `th`, Sortierrichtung sichtbar (Symbol)
- Auswahl: Checkbox je Zeile mit Namen („Zeile Anhänger 3 auswählen“), „Alle auswählen“ im Kopf
- Zeilenaktionen erreichbar per Tastatur; nicht nur bei Hover sichtbar
- Zahlen rechtsbündig mit `tabular-nums`, Einheiten im Kopf oder in der Zelle

**Responsive** (je Tabelle entscheiden und dokumentieren)

| Strategie | Wann |
|---|---|
| horizontaler Scrollbereich mit sticky erster Spalte | viele Spalten, Vergleich wichtig |
| gestapelte Zeilen (jede Zeile als Karte mit Label: Wert) | wenige Zeilen, Details wichtig |
| Spaltenauswahl bzw. Priorisierung | Dashboards |

Der Scrollbereich ist fokussierbar (`tabindex="0"`, Name) und zeigt, dass es weitergeht.

**Tokens:** `color.bg.surface` · `color.border.subtle|default` · `color.selection.*` · `text.body.sm` / `text.label.sm` (Kopf) · `text.numeric` (optional) · `space.inset.sm` (Zellen) · `z.raised` (sticky)

| Do | Don't |
|---|---|
| Spalten nach Wichtigkeit von links nach rechts | 15 gleichwertige Spalten ohne Priorität |
| Leerzustand mit Erklärung in der Tabelle | leere Tabelle ohne Hinweis |
| Summen und Einheiten klar | Zahlen linksbündig ohne Einheit |

**Erweiterung durch Projekte:** Datenvisualisierung, Inline-Bearbeitung, Gruppierung und Virtualisierung sind Projektkomponenten auf Basis dieser Spezifikation. Diagrammfarben über die optionale Gruppe `color.data.*`.
