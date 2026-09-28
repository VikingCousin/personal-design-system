# Containers: Card · Modal/Dialog · Drawer · Accordion (Core)

---

## Card

**Zweck:** fasst zusammengehörige Inhalte zu einer Einheit zusammen (Produkt, Artikel, Kennzahl, Option). **Nicht** als Standardrahmen um alles.

**Anatomie:** 1 Container · 2 Medien (optional) · 3 Kopf (Titel, Metadaten) · 4 Inhalt · 5 Aktionen (optional)

**Varianten:** `static` (nur Inhalt) · `interactive` (ganze Karte klickbar) · `selectable` (Auswahl, siehe Radio Card) · Emphasis über `elevation.flat | raised` bzw. Rahmen

**Zustände:** default · hover und focus-visible (nur interactive) · selected · loading (Skeleton) · disabled

**Accessibility**
- Ganze Karte klickbar: **ein** Link im Titel, dessen Klickfläche per Pseudo-Element die Karte abdeckt; weitere Aktionen in der Karte bleiben eigenständig erreichbar
- Titel als Überschrift der passenden Ebene
- Medien mit Alt-Text oder `alt=""`, wenn dekorativ

**Responsive:** Karten-Raster über Container Queries, mobil 1 Spalte. Gleich hohe Karten nur, wenn die Inhalte vergleichbar sind.

**Tokens:** `color.bg.surface` · `elevation.*` · `radius.container` · `space.inset.md–lg` · `space.stack.sm` · `color.border.default|subtle`

---

## Modal / Dialog

**Zweck:** unterbricht den Ablauf für eine kurze, fokussierte Aufgabe oder eine notwendige Bestätigung. **Nicht** für lange Inhalte oder Formulare mit vielen Schritten → eigene Seite oder Drawer.

**Anatomie:** 1 Scrim · 2 Container · 3 Titel · 4 Inhalt (scrollbar) · 5 Aktionen · 6 Schließen-Button

**Varianten:** `dialog` (Standard) · `alertdialog` (Bestätigung einer folgenreichen Aktion) · Größe `sm` · `md` · `lg` · mobil ggf. `fullscreen`

**Zustände:** closed · opening · open · closing · loading (Aktion läuft)

**Accessibility**
- `<dialog>` bzw. `role="dialog"` + `aria-modal="true"`, `aria-labelledby` = Titel
- Beim Öffnen: Fokus auf das erste sinnvolle Element bzw. den Titel. Beim Schließen: Fokus zurück zum Auslöser
- Fokus bleibt im Dialog (Fokusfalle), Escape schließt (außer bei zwingender Entscheidung, dann sichtbar begründen)
- Hintergrund ist inert (`inert`)
- `alertdialog`: die sichere Option ist fokussiert, nicht die destruktive

**Responsive:** mobil volle Breite oder Vollbild; Aktionen bleiben sichtbar (Sticky-Fuß); der Inhalt scrollt, nicht die Seite.

**Tokens:** `color.overlay.scrim` · `opacity.scrim` · `color.bg.surface-raised` · `elevation.overlay` · `radius.overlay` · `z.overlay` / `z.modal` · `duration.slow` · `easing.enter|exit`

| Do | Don't |
|---|---|
| Titel sagt, worum es geht: „Buchung stornieren?“ | „Sind Sie sicher?“ |
| Buttons benennen das Ergebnis: „Stornieren“ / „Buchung behalten“ | „Ja“ / „Nein“ |
| Dialog im Dialog vermeiden | verschachtelte Modals |

---

## Drawer

**Zweck:** Seitenpanel für Zusatzinhalte, Filter, Details oder Navigation, ohne den Kontext zu verlassen.

**Varianten:** Position `start` · `end` · `bottom` (Bottom Sheet mobil) · modal (mit Scrim, Fokusfalle) · nicht-modal (Seite bleibt bedienbar)

**Accessibility:** modal wie Dialog. Nicht-modal: als `complementary` bzw. Region mit Überschrift; Schließen-Button; Escape schließt; Fokus zurück zum Auslöser.

**Responsive:** mobil als Bottom Sheet oder Vollbild; Breite auf Desktop über `size.container.sm`.

**Tokens:** wie Dialog, `radius.overlay` nur an den freien Kanten

---

## Accordion

**Zweck:** blendet Abschnitte ein und aus, um lange Inhalte übersichtlich zu machen (FAQ, Einstellungen). **Nicht** für Inhalte, die fast alle lesen müssen.

**Anatomie:** 1 Kopf (Button mit Titel + Indikator) · 2 Panel

**Varianten:** einzeln öffnend · mehrere gleichzeitig (Standard) · mit oder ohne Rahmen

**Zustände:** collapsed · expanded · focus-visible · disabled

**Accessibility**
- Kopf = `<button aria-expanded aria-controls>` in einer Überschrift passender Ebene, oder `<details>`/`<summary>`
- Indikator (Pfeil, Plus) zusätzlich zum Zustand, dreht bzw. wechselt ohne Bewegung bei reduzierter Bewegung
- Inhalte sind über die Seitensuche (Strg+F) auffindbar, wo möglich (`hidden="until-found"`)

**Tokens:** `color.border.default` · `space.inset.md` · `text.heading.sm` oder `text.label.md` · `duration.base`
