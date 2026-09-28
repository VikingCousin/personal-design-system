# Navigation: Navigation · Tabs · Breadcrumb · Pagination (Core)

---

## Navigation (Haupt- und Bereichsnavigation)

**Zweck:** Orientierung und Wechsel zwischen Hauptbereichen.

**Anatomie:** 1 Container (`<nav>` mit Label) · 2 Marke bzw. Logo (Link zur Startseite) · 3 Einträge · 4 aktiver Eintrag · 5 Nebenaktionen (Suche, Konto, Warenkorb, CTA) · 6 Menü-Button (mobil)

**Varianten**

| Variante | Einsatz |
|---|---|
| Top-Bar | Websites, einfache Apps |
| Seitennavigation (Sidebar) | Apps und Dashboards mit vielen Bereichen, einklappbar |
| Tab-Bar unten (mobil) | Apps mit 3–5 Hauptbereichen |
| Menü mit Unterebenen | große Websites; höchstens 2 Ebenen im Menü |

**Zustände:** default · hover · focus-visible · current (aktive Seite) · expanded (Untermenü, mobiles Menü)

**Accessibility**
- `<nav aria-label="Hauptnavigation">`; mehrere Navigationen eindeutig beschriftet
- aktive Seite: `aria-current="page"` + sichtbares Merkmal über die Farbe hinaus (Unterstrich, Balken, Fettung)
- Menü-Button: `aria-expanded`, `aria-controls`, Label „Menü“; mobiles Menü schließt mit Escape
- Untermenüs öffnen per Klick bzw. Tastatur, nicht nur per Hover
- „Zum Inhalt springen“-Link als erstes fokussierbares Element

**Responsive:** Mehr als ca. 4–5 Einträge auf Mobil kommen in ein Menü; die wichtigste Aktion (z. B. „Jetzt buchen“) bleibt sichtbar.

**Tokens:** `color.bg.surface|canvas` · `color.text.*` · `text.label.md` · `space.inline.*` · `size.target.min` · `z.sticky` · `elevation.floating` (wenn sticky)

---

## Tabs

**Zweck:** wechselt zwischen gleichrangigen Ansichten **desselben** Kontexts. **Nicht** als Hauptnavigation zwischen Seiten (→ Navigation mit Links).

**Anatomie:** 1 Tab-Liste · 2 Tabs · 3 aktiver Indikator · 4 Panel

**Zustände:** default · hover · focus-visible · selected · disabled

**Accessibility:** `role="tablist"`, `tab` (`aria-selected`, `aria-controls`), `tabpanel`. Pfeiltasten wechseln zwischen Tabs, Tab springt ins Panel. Der ausgewählte Tab ist nicht nur farblich markiert.

**Responsive:** Tab-Liste scrollt horizontal mit sichtbarem Hinweis, oder wird mobil zu Select/Segmented Control. Kein Umbruch auf mehrere Zeilen.

**Tokens:** `text.label.md` · `color.text.secondary` → `color.text.primary` (selected) · `color.action.primary.bg` bzw. `color.brand.primary` (Indikator) · `border.width.strong`

---

## Breadcrumb

**Zweck:** zeigt die Position in einer Hierarchie ab 3 Ebenen und erlaubt den Sprung zurück.

**Anatomie:** `<nav aria-label="Brotkrumen">` · geordnete Liste von Links · Trenner (dekorativ, `aria-hidden`) · aktuelle Seite (kein Link, `aria-current="page"`)

**Responsive:** mobil nur die übergeordnete Ebene („← Kategorie“) oder mittlere Ebenen gekürzt (`…` als Button zum Ausklappen).

**Tokens:** `text.caption` bzw. `text.body.sm` · `color.text.secondary` · `color.text.link`

---

## Pagination

**Zweck:** teilt lange Listen in Seiten, wenn Nutzende gezielt zurückfinden wollen (Suchergebnisse, Tabellen). Alternativen: „Mehr laden“ (Feeds), virtuelles Scrollen (sehr große Tabellen).

**Anatomie:** `<nav aria-label="Seitennavigation">` · Zurück · Seitenzahlen (mit Auslassungen) · Weiter · optional „Einträge pro Seite“ und „x–y von z“

**Zustände:** default · hover · focus-visible · current (`aria-current="page"`) · disabled (Zurück auf Seite 1)

**Accessibility:** Links oder Buttons mit zugänglichem Namen („Seite 3“, „Nächste Seite“). Nach dem Seitenwechsel landet der Fokus am Anfang der Liste bzw. die Änderung wird angesagt.

**Responsive:** mobil nur Zurück / „Seite 3 von 12“ / Weiter.

**Tokens:** `size.target.min` · `text.label.md` · `color.action.secondary.*` · `color.selection.*` (current)
