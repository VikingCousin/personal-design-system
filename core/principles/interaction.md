# Interaction (Core)

> Regeln für Verhalten, Zustände und Rückmeldungen. Gilt unabhängig vom visuellen Stil.

## 1. Zustände

Jedes interaktive Element definiert die Zustände, die es haben kann. Das vollständige Zustandsmodell steht in [components/README.md](../components/README.md#3-zustandsmodell). Mindestens:

| Zustand | Muss erkennbar sein durch |
|---|---|
| Default | — |
| Hover (nur Zeiger) | leichte Veränderung; nie einzige Information |
| Focus-visible | Fokusring (Token `color.focus.ring`, `border.width.focus`) |
| Active / Pressed | kurze Rückmeldung beim Auslösen |
| Selected / Checked | Form oder Symbol **und** Farbe |
| Disabled | reduziert, aber lesbar; Grund erklären, wenn nicht offensichtlich |
| Loading / Busy | Fortschritt oder Aktivitätsanzeige; Element nicht doppelt auslösbar |
| Error / Invalid | Text + Symbol + Farbe |

## 2. Rückmeldung

1. **Jede Aktion hat eine Reaktion.** Unter 100 ms direkt, bis 1 s ohne Anzeige, 1–10 s mit Aktivitätsanzeige, über 10 s mit Fortschritt und Abbruchmöglichkeit.
2. **Erfolg bestätigen, wo er nicht sichtbar ist** (z. B. „Gespeichert“). Was sichtbar ist, braucht keine zusätzliche Meldung.
3. **Fehler dort zeigen, wo sie entstehen**, und sagen, wie man sie behebt ([content-writing.md](content-writing.md#3-fehler-und-leere-zustände)).
4. **Nichts geht verloren.** Eingaben bleiben bei Fehlern erhalten. Beim Verlassen mit ungespeicherten Änderungen wird nachgefragt.

## 3. Destruktive und folgenreiche Aktionen

- Löschen, Kündigen, Senden, Bezahlen und Veröffentlichen sind klar benannt („Rechnung löschen“, nicht „OK“).
- Nicht umkehrbare Aktionen brauchen eine Bestätigung. Umkehrbare Aktionen besser mit „Rückgängig“ statt Bestätigungsdialog.
- Destruktive Aktionen sind visuell unterscheidbar (Variante `danger`), aber nie die hervorgehobene Standardaktion.

## 4. Bewegung

- Bewegung erklärt Veränderungen (woher kommt etwas, wohin geht es). Sie ist nie dekorativer Selbstzweck in Abläufen.
- Keine Information nur durch Bewegung.
- `prefers-reduced-motion: reduce`: Bewegungen werden durch Überblenden ersetzt oder entfallen.
- Dauer und Kurven kommen aus [tokens/motion.md](../tokens/motion.md).
- Autoplay-Bewegung (Karussell, Video) muss sich pausieren lassen und startet ohne Ton.

## 5. Formulare

- So wenige Felder wie möglich. Optionale Felder kennzeichnen oder weglassen.
- Validierung: beim Verlassen des Feldes bzw. beim Absenden, nicht bei jedem Tastendruck mit Fehlermeldung.
- Passende Eingabetypen (`email`, `tel`, `inputmode`), `autocomplete` setzen.
- Die Hauptaktion steht am Ende des Formulars und ist eindeutig benannt.

## 6. Navigation und Orientierung

- Die aktuelle Position ist immer erkennbar (aktive Navigation, Breadcrumb, Titel).
- Zurück funktioniert erwartungsgemäß (Browser-Zurück und URL-Zustand).
- Überlagerungen (Dialog, Drawer) lassen sich mit Escape und sichtbarem Schließen-Button verlassen und geben den Fokus an den Auslöser zurück.
