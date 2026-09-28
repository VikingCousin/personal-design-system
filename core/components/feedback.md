# Feedback: Alert · Toast · Tooltip · Badge · Empty / Loading / Error State (Core)

---

## Alert (Hinweis im Inhalt)

**Zweck:** dauerhaft sichtbarer Hinweis im Kontext (Formularfehler-Zusammenfassung, Wartungshinweis, Warnung vor einer Aktion).

**Anatomie:** 1 Container · 2 Icon · 3 Titel (optional) · 4 Text · 5 Aktion (optional) · 6 Schließen (optional)

**Varianten (Tone):** `info` · `success` · `warning` · `error`. Jede Variante hat **Icon + Text**, nicht nur Farbe.

**Accessibility:** `role="alert"` nur für dringende, neu erscheinende Fehler. Sonst `role="status"` oder statischer Inhalt. Nicht bei jedem Seitenaufruf ansagen lassen.

**Tokens:** `color.feedback.{tone}.{bg, text, border, icon}` · `radius.container` · `space.inset.md` · `size.icon.md`

---

## Toast

**Zweck:** kurze, vorübergehende Rückmeldung auf eine Aktion („Gespeichert“, „Link kopiert“). **Nicht** für Fehler, die eine Handlung verlangen (→ Alert beim Ort des Fehlers).

**Anatomie:** Container · Icon · Text · optional eine Aktion („Rückgängig“) · Schließen

**Verhalten**
- Standard: verschwindet nach ≥ 5 s. **Mit Aktion: bleibt**, bis sie geschlossen wird, oder deutlich länger. Pausiert bei Hover und Fokus
- höchstens 1–3 gleichzeitig, gestapelt
- Position im Projekt einheitlich; verdeckt keine Hauptaktion

**Accessibility:** Container mit `role="status"` (`aria-live="polite"`), bei Fehlern `role="alert"`. Aktionen im Toast sind per Tastatur erreichbar. Informationen stehen nicht **nur** im Toast.

**Tokens:** `color.bg.inverse` oder `color.bg.surface-raised` · `elevation.toast` · `z.toast` · `radius.overlay` · `duration.base` · `easing.enter|exit`

---

## Tooltip

**Zweck:** kurze **ergänzende** Beschreibung für ein Element, meist für Icon-Buttons. **Nicht** für wichtige Informationen, Links oder Formularhilfe (→ Hilfetext).

**Verhalten:** erscheint bei Hover **und** Fokus nach kurzer Verzögerung, bleibt beim Überfahren sichtbar, schließt mit Escape (WCAG 1.4.13).

**Accessibility:** `role="tooltip"`, verbunden über `aria-describedby` (bzw. als Name bei Icon-Buttons). Auf Touch-Geräten nicht die einzige Informationsquelle.

**Tokens:** `color.bg.inverse` · `color.text.inverse` · `text.caption` · `z.tooltip` · `radius.control` · `duration.fast`

---

## Badge

**Zweck:** kurzer Status oder eine Kategorie („Neu“, „Verfügbar“, „3“, „Entwurf“).

**Varianten:** Tone `neutral` · `info` · `success` · `warning` · `error` · `brand`; Form Text · Zahl · Punkt (nur mit Text daneben)

**Accessibility:** Der Text ist lesbar (Kontrast 4.5:1). Zahlen-Badges bekommen Kontext („3 ungelesene Nachrichten“). Badges sind nicht interaktiv. Wenn doch, dann Chip/Button.

**Tokens:** `color.feedback.*` bzw. `color.brand.*` · `radius.pill` · `text.label.sm` bzw. `text.caption` · `space.inset.xs`

---

## Empty State

**Zweck:** erklärt, warum hier nichts ist, und bietet den nächsten Schritt an.

**Arten:** erste Nutzung („Noch keine Buchungen“) · keine Ergebnisse (Suche, Filter) · alles erledigt · keine Berechtigung

**Anatomie:** Illustration oder Icon (optional, dekorativ) · Titel · Erklärung · Hauptaktion · ggf. Nebenaktion („Filter zurücksetzen“)

**Regeln:** konkret statt witzig; bei „keine Ergebnisse“ den Suchbegriff wiederholen und Auswege anbieten.

**Tokens:** `text.heading.sm` · `text.body.md` · `color.text.secondary` · `space.stack.md` · `size.container.sm`

---

## Loading State

**Zweck:** zeigt, dass etwas lädt, und vermeidet Layout-Sprünge.

**Varianten:** Skeleton (Struktur bekannt, bevorzugt für Seiten und Listen) · Spinner (kurze, unbestimmte Vorgänge in Buttons oder Bereichen) · Fortschrittsbalken (bestimmte Dauer, Uploads) · „Optimistic UI“ (Ergebnis sofort zeigen, bei Fehler zurücknehmen)

**Regeln:** unter 1 s nichts anzeigen (kein Flackern), über 10 s Fortschritt und Abbruch anbieten.

**Accessibility:** Bereich mit `aria-busy="true"`; Abschluss per `role="status"` ansagen („Ergebnisse geladen“); Skeleton-Animation respektiert reduzierte Bewegung.

**Tokens:** `color.bg.surface-sunken` (Skeleton) · `duration.deliberate` (Puls) · `easing.linear` (Fortschritt)

---

## Error State

**Zweck:** ein Bereich oder eine ganze Seite kann nicht angezeigt werden (Server-Fehler, keine Verbindung, 404, keine Berechtigung).

**Anatomie:** Titel (was ist passiert) · Erklärung (warum, falls bekannt) · Lösung (erneut versuchen, zurück, Kontakt) · ggf. Fehlercode für den Support (klein)

**Regeln:** Fehler auf der kleinstmöglichen Ebene zeigen (ein Widget statt der ganzen Seite). Eingaben nicht verlieren. Keine technische Sprache als Haupttext.

**Accessibility:** Fokus bzw. Ansage bei neu auftretenden Fehlern (`role="alert"`). Seiten-Titel (`<title>`) enthält den Fehler.

**Tokens:** `color.feedback.error.*` sparsam (eine ganze Seite in Rot ist zu viel) · `text.heading.*` · `space.stack.*`
