# Farbe (Core)

> Core definiert **Rollen und Regeln**, keine Farben. Welche Farben eine Marke hat, entscheidet das Projekt.

## 1. Vier Farbebenen

| Ebene | Frage | Beispiele | Pflicht? |
|---|---|---|---|
| **Brand** | Welche Farben tragen die Marke? | Markenfarbe, Sekundärfarbe, Akzent | Pflicht (mindestens eine) |
| **UI** | Wie ist die Oberfläche aufgebaut? | Hintergründe, Flächen, Text, Rahmen, Aktionen, Fokus | Pflicht |
| **Semantic Feedback** | Was bedeutet ein Zustand? | Erfolg, Warnung, Fehler, Info | Pflicht |
| **Material** | Welche physischen Materialien gehören zur Marke? | Metall, Holz, Lack, Stoff, Fahrzeugfolie | **optional**, nur bei physischen Produkten |

Die Brand-Farbe muss **nicht** die Aktionsfarbe sein. Material-Farben werden nie als UI-Farben verwendet.

## 2. Pflicht-Rollen

Die vollständige Liste steht im [Vertrag](contract.tokens.json). Zusammengefasst:

| Gruppe | Rollen |
|---|---|
| Hintergrund | `color.bg.canvas` · `color.bg.surface` · `color.bg.surface-raised` · `color.bg.surface-sunken` · `color.bg.inverse` |
| Text | `color.text.primary` · `color.text.secondary` · `color.text.disabled` · `color.text.inverse` · `color.text.link` · `color.text.link-hover` · `color.text.on-action` |
| Rahmen | `color.border.default` · `color.border.strong` · `color.border.subtle` |
| Aktion | `color.action.primary.{bg, bg-hover, bg-active, text}` · `color.action.secondary.{bg, bg-hover, bg-active, text, border}` · `color.action.danger.{bg, bg-hover, bg-active, text}` |
| Auswahl | `color.selection.bg` · `color.selection.text` |
| Feedback | `color.feedback.{success, warning, error, info}.{bg, text, border, icon}` |
| Fokus | `color.focus.ring` |
| Überlagerung | `color.overlay.scrim` |
| Marke | `color.brand.primary` · `color.brand.secondary` (optional) · `color.brand.accent` (optional) |

**Optionale Gruppen:** `color.data.*` (Diagramme: kategoriale Reihe `series-1…n`, sequenziell, divergierend), `color.material.*` (physisch), projektspezifische Status (`color.status.*`).

## 3. Kontrastregeln

| Paar | Mindestkontrast (Profil Standard) |
|---|---|
| `text.primary` auf `bg.canvas`, `bg.surface`, `bg.surface-raised` | 4.5:1 (Ziel 7:1) |
| `text.secondary` auf allen Flächen | 4.5:1 |
| `text.on-action` auf `action.*.bg` (alle Zustände) | 4.5:1 |
| `feedback.*.text` auf `feedback.*.bg` und auf `bg.surface` | 4.5:1 |
| `border.strong` (Eingabefelder) gegen Fläche | 3:1 |
| `focus.ring` gegen angrenzende Farben | 3:1 |
| `feedback.*.icon`, bedeutungstragende Icons | 3:1 |
| `text.disabled` | keine Pflicht, muss aber lesbar bleiben (Richtwert ≥ 3:1) |

Im Profil „Erweitert“ gilt für Fließtext 7:1. Das Projekt dokumentiert alle Pflichtpaare mit Messwert in `tokens/README.md`.

## 4. Regeln

1. **Genau eine primäre Aktionsfarbe.** Sie wird nicht für Dekoration verwendet, damit Aktionen erkennbar bleiben.
2. **Feedbackfarben sind reserviert.** Rot, Grün, Gelb (oder die Entsprechungen des Projekts) werden nicht dekorativ eingesetzt, wenn sie als Fehler, Erfolg oder Warnung gelesen werden könnten.
3. **Nie nur Farbe** ([accessibility.md](../principles/accessibility.md)).
4. **Neutrale Skala mit mindestens 9 Stufen**, damit Flächen, Rahmen und Text abgestuft werden können.
5. **Paletten in OKLCH aufbauen** (empfohlen), weil dort gleiche Helligkeitsstufen auch gleich hell wirken. Ausgabe als HEX.
6. **Disabled nicht über Transparenz** des ganzen Elements lösen, wenn dadurch Text unlesbar wird.

## 5. Hell und Dunkel

- Ob ein Projekt einen **Dunkelmodus** anbietet, entscheidet das Projekt (Zielgruppe, Nutzungssituation, Aufwand).
- **Wenn** es einen gibt, wird er als eigener Entwurf gestaltet, nicht invertiert: Flächen werden über Helligkeit gestaffelt statt über Schatten, gesättigte Farben werden entsättigt bzw. aufgehellt, und alle Kontrastpaare werden neu geprüft.
- Der Dunkelmodus überschreibt nur semantische Tokens (`semantic.dark.tokens.json`).
- Standard ist `prefers-color-scheme` mit manueller Umschaltung, sofern das Projekt nichts anderes festlegt.

## 6. Farbdokumentation

| Angabe | Wann |
|---|---|
| HEX | immer (`$value`) |
| OKLCH | immer (`$extensions.pds.oklch`) |
| RGB | bei Bedarf ableitbar |
| CMYK-Näherung | wenn das Projekt Print hat |
| RAL / Pantone / Materialbezeichnung | wenn das Projekt physische Produkte, Lack, Folie oder Textil hat |

**Keine falsche Gleichheit:** Bildschirmfarben (RGB) und Druck- bzw. Materialfarben (CMYK, RAL, Pantone) sind verschiedene Farbsysteme. Umrechnungen werden als **Näherung** gekennzeichnet und am echten Muster geprüft.

Beispiel für das Format (Werte nur zur Veranschaulichung, nicht berechnet):

```json
"brand": {
  "primary": {
    "$type": "color", "$value": "#1F4E79",
    "$extensions": { "pds": { "oklch": "oklch(0.42 0.09 250)", "cmyk": "~ 90/60/20/10 (Näherung)", "ral": "~ RAL 5009 (Näherung, am Muster prüfen)" } }
  }
}
```

## 7. Datenvisualisierung

Für Projekte mit Diagrammen, Dashboards oder Karten (optionale Gruppe `color.data.*`):

| Skala | Einsatz | Regel |
|---|---|---|
| **kategorial** `color.data.series-1…n` | unterschiedliche Gruppen ohne Rangfolge | höchstens ca. 8 Farben; darüber Gruppen zusammenfassen. Benachbarte Reihen unterscheiden sich deutlich in Helligkeit, nicht nur im Farbton |
| **sequenziell** `color.data.seq-1…n` | Mengen von wenig bis viel | eine Farbe von hell nach dunkel, gleichmäßige Helligkeitsstufen (OKLCH) |
| **divergierend** `color.data.div-*` | Abweichung von einem Mittelwert | zwei Farben mit neutraler Mitte |

1. Datenfarben sind **nicht** die Feedbackfarben. Rot bzw. Grün nur, wenn sie wirklich schlecht bzw. gut bedeuten.
2. Reihen werden zusätzlich über **direkte Beschriftung**, Muster, Form oder Linienart unterschieden. Die Legende ist nicht das einzige Mittel.
3. Farben müssen für die häufigsten Farbsehschwächen unterscheidbar sein (mit Simulator prüfen).
4. Jedes Diagramm hat eine Textalternative: Kernaussage als Text und bei Bedarf eine Datentabelle.
5. Linien und Flächen in Diagrammen haben ≥ 3:1 Kontrast zum Hintergrund.
