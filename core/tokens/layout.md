# Layout: Breakpoints, Raster, Z-Index (Core)

## 1. Breakpoints

Mobile first: Ein Breakpoint beschreibt die **Mindestbreite**, ab der eine Regel gilt. Die Defaults sind überschreibbar.

| Token | Default | Typisch |
|---|---|---|
| `breakpoint.sm` | 480 px | große Smartphones quer |
| `breakpoint.md` | 768 px | Tablet hoch |
| `breakpoint.lg` | 1024 px | Tablet quer, kleiner Laptop |
| `breakpoint.xl` | 1280 px | Desktop |
| `breakpoint.2xl` | 1536 px | großer Desktop |

Die Regeln dazu stehen in [principles/responsive.md](../principles/responsive.md). Komponenten verwenden bevorzugt **Container Queries** statt dieser Viewport-Breakpoints.

## 2. Raster und Container

| Token | Bedeutung |
|---|---|
| `layout.columns.{mobile, tablet, desktop}` | Spaltenzahl (Empfehlung 4 / 8 / 12) |
| `space.layout.gutter` | Seitenrand bzw. Spaltenabstand |
| `size.container.*` | maximale Inhaltsbreite (siehe [spacing-sizing.md](spacing-sizing.md)) |

## 3. Z-Index

Z-Werte werden nie frei vergeben, sondern nur über diese Ebenen. Die Defaults sind überschreibbar, die **Reihenfolge nicht**.

| Token | Default | Verwendung |
|---|---|---|
| `z.base` | 0 | normaler Inhalt |
| `z.raised` | 10 | hervorgehobene Karten, Sticky-Tabellenköpfe |
| `z.dropdown` | 100 | Dropdown, Autocomplete |
| `z.sticky` | 200 | Sticky Header, Tab-Bar |
| `z.overlay` | 300 | Scrim unter Dialogen |
| `z.modal` | 400 | Dialog, Drawer |
| `z.popover` | 500 | Popover in Dialogen, Menüs |
| `z.toast` | 600 | Toasts, Benachrichtigungen |
| `z.tooltip` | 700 | Tooltips (immer oben) |

Zwischenwerte werden nur **innerhalb** einer Komponente verwendet (lokaler Stacking-Kontext).
