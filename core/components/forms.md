# Forms: Form Field · Input · Textarea · Select · Checkbox · Radio · Switch (Core)

> Gemeinsame Regeln stehen im **Form Field**. Alle Eingabeelemente werden innerhalb eines Form Fields verwendet.

---

## Form Field (Rahmen für jedes Eingabeelement)

**Zweck:** verbindet Label, Eingabe, Hilfetext und Fehlermeldung zu einer zugänglichen Einheit.

**Anatomie:** 1 Label (Pflicht, sichtbar) · 2 Kennzeichnung „Pflicht“ bzw. „optional“ · 3 Hilfetext (optional) · 4 Eingabeelement · 5 Fehlermeldung (bei `invalid`) · 6 Zeichenzähler (optional)

**Zustände:** default · focus · filled · disabled · read-only · invalid · (valid nur wenn hilfreich)

**Accessibility**
- `<label for>` mit dem Eingabeelement verbunden; **Platzhalter ersetzt nie das Label**
- Hilfetext und Fehler über `aria-describedby` verbunden, `aria-invalid="true"` bei Fehler
- Fehlertext sagt, was zu tun ist; Symbol + Text + Farbe
- Pflichtfelder: Text („Pflichtfeld“ oder „optional“ bei den anderen) und `required`; einheitlich im Projekt
- Beim Absenden mit Fehlern: Fokus auf das erste fehlerhafte Feld oder eine Fehlerzusammenfassung oben mit Links zu den Feldern
- `autocomplete` und passende `type`/`inputmode`

**Responsive:** Labels stehen über dem Feld (Standard). Nebeneinander stehende Labels erst ab ausreichender Breite. Felder nehmen mobil die volle Breite ein. Die Feldbreite darf den erwarteten Inhalt andeuten (PLZ schmal).

**Tokens:** `text.label.md` · `text.caption` · `color.text.secondary` · `color.feedback.error.*` · `space.stack.xs` (Label–Feld) · `space.stack.md` (Feld–Feld)

---

## Input

**Zweck:** einzeilige Texteingabe (Text, E-Mail, Telefon, Zahl, Suche, Passwort, Datum).
**Anatomie:** Container · Text · optional Präfix/Suffix (Icon, Einheit „€“) · optional Aktion (Passwort anzeigen, Suche leeren)
**Varianten:** Größe `sm` · `md` · `lg` · Typ (`text`, `email`, `tel`, `number`, `search`, `password`, `date` …)
**Zustände:** default · hover · focus · filled · disabled · read-only · invalid
**A11y:** passender `type`, Einheit als Text (nicht nur Icon), Passwortfeld erlaubt Einfügen, Anzeigen-Button mit `aria-pressed`
**Tokens:** `color.bg.surface` bzw. `bg.surface-sunken` · `color.border.strong` · `color.border.*` (focus/invalid über `color.focus.ring` / `color.feedback.error.border`) · `size.control.*` · `radius.control` · `text.body.md`

## Textarea

**Zweck:** mehrzeilige Texteingabe.
**Besonderheiten:** Höhe für den erwarteten Umfang (min. 3 Zeilen), vertikal vergrößerbar oder automatisch wachsend. Zeichenzähler bei Limit, per `aria-live="polite"` sparsam angesagt.
**Tokens:** wie Input, `size.control.*` gilt nur für die Mindesthöhe.

## Select

**Zweck:** eine Auswahl aus einer Liste (ab ca. 5 Optionen; bei 2–4 Optionen besser Radio).
**Varianten:** nativ (`<select>`, Standard und bevorzugt) · Custom Listbox (nur wenn nötig, z. B. mit Suche) · Multi-Select (Custom).
**Zustände:** default · hover · focus · expanded · disabled · invalid
**A11y:** nativ bevorzugen. Custom: Muster „Combobox“ bzw. „Listbox“ (WAI-ARIA APG) mit Pfeiltasten, Enter, Escape, Tippen zum Springen.
**Responsive:** mobil öffnet der native Picker des Systems. Custom-Listen auf Mobil als Bottom Sheet.
**Tokens:** wie Input + `elevation.floating` · `z.dropdown` · `color.selection.*`

## Checkbox

**Zweck:** eine oder mehrere unabhängige Optionen ein- oder ausschalten; Zustimmung.
**Zustände:** unchecked · checked · indeterminate (für Gruppen) · focus · disabled · invalid
**A11y:** `<input type="checkbox">`, das ganze Label ist klickbar, Gruppe in `<fieldset>` + `<legend>`, Space schaltet um.
**Tokens:** `color.action.primary.bg` (checked) · `color.border.strong` · `size.icon.md` · Zielgröße über das Label ≥ `size.target.min`

## Radio

**Zweck:** genau eine Option aus 2–7 sichtbaren Optionen.
**Zustände:** unselected · selected · focus · disabled · invalid
**A11y:** `<fieldset>` + `<legend>`, Pfeiltasten wechseln die Auswahl, Tab springt in die Gruppe bzw. aus ihr heraus. Keine vorausgewählte Option, wenn eine bewusste Wahl nötig ist.
**Varianten:** Liste · Karten-Auswahl (Radio Card, z. B. Tarifwahl), die Karte ist dann ganz klickbar.

## Switch

**Zweck:** eine Einstellung **sofort** ein- oder ausschalten (ohne Speichern-Button). Wenn erst gespeichert werden muss → Checkbox.
**Zustände:** off · on · focus · disabled · (loading, wenn die Umschaltung Zeit braucht)
**A11y:** `<button role="switch" aria-checked>` oder `<input type="checkbox" role="switch">`. Das Label beschreibt die Einstellung, nicht den Zustand („Newsletter“, nicht „Aus“). Der Zustand ist zusätzlich zur Farbe erkennbar (Position + ggf. Symbol oder Text).
**Tokens:** `color.action.primary.bg` (on) · `color.border.strong` (off) · `radius.pill` · `duration.fast`

---

## Do / Don't (alle Formularelemente)

| Do | Don't |
|---|---|
| Label immer sichtbar über dem Feld | Platzhalter als einziges Label |
| Fehler beim Feld, mit Lösung | Fehler nur als rote Umrandung |
| nur notwendige Felder | „Anrede“ und „Titel“ als Pflichtfelder ohne Grund |
| Validierung beim Verlassen bzw. Absenden | Fehlermeldung beim ersten Tastendruck |

**Erweiterung durch Projekte:** Aussehen frei (Umriss, Fläche, Unterstrich), Zusatztypen (Datumsauswahl, Datei-Upload, Adresssuche) als Projektkomponenten auf Basis von Form Field + Input.
