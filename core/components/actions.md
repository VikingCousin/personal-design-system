# Actions: Button · Link (Core)

---

## Button

**Zweck:** löst eine Aktion aus (speichern, senden, öffnen, löschen). **Nicht** für Navigation zu einer anderen Seite → [Link](#link).

**Anatomie:** 1 Container · 2 Label · 3 optionales Icon (vor oder nach dem Label) · 4 optionaler Ladeindikator

**Varianten**

| Achse | Werte | Regel |
|---|---|---|
| Emphasis | `primary` · `secondary` · `tertiary` | höchstens eine `primary` pro Ansicht bzw. Formular |
| Tone | `neutral` · `danger` | `danger` nur für destruktive Aktionen, nie als Standardaktion vorausgewählt |
| Größe | `sm` · `md` · `lg` | `sm` nur auf Zeiger-UIs oder mit erweiterter Klickfläche |
| Form | Text · Text + Icon · nur Icon | nur Icon → `aria-label` und Tooltip |
| Breite | inhaltsbreit · volle Breite | volle Breite auf Mobil für Hauptaktionen erlaubt |

**Zustände:** default · hover · focus-visible · active · disabled · loading (Label bleibt oder wird ersetzt durch „Wird gespeichert …“, Button ist währenddessen nicht erneut auslösbar, `aria-busy="true"`).

**Accessibility**
- `<button type="button|submit">`, nie `div`
- Name = sichtbares Label; bei reinem Icon `aria-label`
- Tastatur: Enter und Space lösen aus
- `disabled`: Wenn der Grund nicht offensichtlich ist, lieber aktiv lassen und beim Klick erklären, oder den Grund daneben nennen
- Umschalt-Buttons: `aria-pressed`

**Responsive:** Label bricht nicht ab (kein `…`), Button darf umbrechen oder volle Breite annehmen. Buttongruppen stapeln sich mobil, die Hauptaktion steht dann zuerst oder unten, aber einheitlich im Projekt.

**Tokens:** `color.action.{primary|secondary|danger}.*` · `color.text.on-action` · `text.label.md` · `size.control.{sm|md|lg}` · `space.inset.*` · `space.inline.sm` (Icon-Abstand) · `radius.control` · `border.width.*` · `color.focus.ring` · `duration.fast`

**Inhalt:** Verb (+ Objekt): „Anhänger buchen“, „Rechnung senden“. Nie „OK“, „Absenden“, „Hier klicken“.

| Do | Don't |
|---|---|
| eine klare Hauptaktion | drei gleich laute Buttons nebeneinander |
| „Löschen“ als `danger` + Bestätigung bzw. Rückgängig | destruktive Aktion als `primary` vorausgewählt |

**Erweiterung:** Projekte gestalten Form, Farbe und Typo frei über Tokens und dürfen Varianten mit eigener Bedeutung ergänzen. Nicht erlaubt: Fokus entfernen, Zielgröße unterschreiten, Zustände nur über Farbe.

---

## Link

**Zweck:** Navigation zu einer anderen Seite, einem Abschnitt oder einer Datei. **Nicht** für Aktionen → Button.

**Varianten:** `inline` (im Fließtext) · `standalone` (eigenständig, z. B. „Alle Artikel ansehen“) · `external` (öffnet andere Website: Kennzeichnung durch Icon + zugänglicher Hinweis) · `download` (Dateityp und Größe nennen).

**Zustände:** default · hover · focus-visible · active · visited (optional).

**Accessibility**
- `<a href>`. Ohne `href` ist es kein Link.
- Inline-Links sind nicht nur farblich vom Text unterschieden (Unterstreichung oder gleichwertiges Merkmal)
- Linktext ist ohne Kontext verständlich
- Neues Fenster nur mit Hinweis („öffnet in neuem Tab“)

**Tokens:** `color.text.link` · `color.text.link-hover` · `color.focus.ring` · Textstil des Umfelds

| Do | Don't |
|---|---|
| „Preisliste als PDF (240 KB)“ | „hier“, „mehr“ |
| Unterstreichung im Fließtext | Link nur über Farbe erkennbar |
