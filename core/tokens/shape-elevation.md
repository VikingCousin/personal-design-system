# Radius, Border, Shadow/Elevation, Opacity (Core)

> Core definiert die **Rollen**. Ob eine Marke eckig oder rund ist, mit Schatten oder mit Linien arbeitet, entscheidet das Projekt. `0` ist überall ein gültiger Wert.

## 1. Radius

| Semantisches Token | Verwendung |
|---|---|
| `radius.control` | Buttons, Inputs, Selects, Chips |
| `radius.container` | Karten, Panels, Tabellenrahmen |
| `radius.overlay` | Dialoge, Drawer, Popover, Toast |
| `radius.pill` | vollständig rund (Badges, Toggle), Wert 9999 px |
| `radius.focus` *(optional)* | Fokusring, folgt dem Radius des Elements (plus Offset) |

Primitive-Skala (Werte vom Projekt): `radius.none`, `radius.sm`, `radius.md`, `radius.lg`, `radius.xl`, `radius.full`.
**Regel:** Verschachtelte Rundungen: innerer Radius = äußerer Radius − Innenabstand, damit Kurven parallel laufen.

## 2. Border

| Token | Bedeutung | Default |
|---|---|---|
| `border.width.default` | Standardlinie | 1 px |
| `border.width.strong` | betonte Linie, Eingabefelder | 1–2 px (Projekt) |
| `border.width.focus` | Fokusring | ≥ 2 px |
| `border.offset.focus` | Abstand des Fokusrings zum Element | 2 px |

Farben der Rahmen: `color.border.*` ([color.md](color.md)). Eingabefelder brauchen einen Rahmen oder eine Fläche mit ≥ 3:1 Kontrast.

## 3. Elevation

Elevation beschreibt, **wie weit ein Element über der Fläche liegt**, nicht, wie es aussieht. Das Projekt entscheidet, ob Elevation über Schatten, Rahmen, Flächenhelligkeit oder eine Kombination dargestellt wird.

| Stufe | Token | Verwendung |
|---|---|---|
| 0 | `elevation.flat` | Seite, eingebettete Inhalte |
| 1 | `elevation.raised` | Karten, hervorgehobene Flächen |
| 2 | `elevation.floating` | Dropdown, Popover, Sticky Header |
| 3 | `elevation.overlay` | Dialog, Drawer |
| 4 | `elevation.toast` | Toasts, Benachrichtigungen |

Je Stufe definiert das Projekt `shadow.{stufe}` (auch `none` erlaubt) und ggf. die zugehörige Fläche (`color.bg.surface-raised`).
**Regel:** Elevation und [Z-Index](layout.md#3-z-index) passen zusammen: Eine höhere Elevation liegt nie unter einer niedrigeren. Im Dunkelmodus wird Elevation vor allem über hellere Flächen ausgedrückt.

## 4. Opacity

| Token | Verwendung |
|---|---|
| `opacity.scrim` | Hintergrundabdunkelung unter Dialogen (in Kombination mit `color.overlay.scrim`) |
| `opacity.disabled` | nur für nicht-textliche Elemente (Icons, Flächen). Text im Disabled-Zustand bekommt stattdessen `color.text.disabled` |
| `opacity.hover-overlay` | leichte Überlagerung als Hover-Zustand (optional) |
