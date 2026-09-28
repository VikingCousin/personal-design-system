# Template: Transaktionsablauf (Buchung, Anfrage, Checkout, Registrierung) (Core)

> Ergänzt nach dem Smoke Test v1.0 ([0003](../decisions/0003-smoke-test-v1.md)): Fast jedes Projekt hat einen Ablauf, an dessen Ende eine Verbindlichkeit steht (Reservierung, Kauf, Anfrage, Konto).

## Zweck
Nutzende führen eine Aufgabe mit mehreren Angaben sicher bis zum Abschluss und wissen danach genau, was passiert ist und was als Nächstes passiert.

## Bereiche

| Bereich | Pflicht? | Aufgabe |
|---|---|---|
| Einstieg | Pflicht | Worum geht es, was wird gebraucht (z. B. „Dauer ca. 2 Minuten, Führerschein bereithalten“) |
| Auswahl | je nach Ablauf | Produkt, Leistung, Termin, Zeitraum, Menge, mit Verfügbarkeit und Preis |
| Angaben | Pflicht | nur notwendige Felder, gruppiert ([forms.md](../components/forms.md)) |
| Fortschritt | ab 3 Schritten | Schrittanzeige mit Namen („2 von 4: Kontaktdaten“), Zurück möglich ohne Datenverlust |
| Zusammenfassung | Pflicht vor verbindlichem Abschluss | alle Angaben, Preis inkl. aller Kosten, Bedingungen, Ändern-Links |
| Abschluss-Aktion | Pflicht | eindeutig benannt nach Verbindlichkeit („Zahlungspflichtig bestellen“, „Reservierung anfragen“, „Konto erstellen“) |
| Bestätigung | Pflicht | Ergebnis, Referenznummer, nächste Schritte, Kontakt. Zusätzlich per E-Mail, wenn vorhanden |
| Fehler und Abbruch | Pflicht | Fehler beim Feld und als Zusammenfassung; Abbruch ohne Nachteil; Zwischenspeichern bei langen Abläufen |

## Struktur (schematisch)

```
[Einstieg] → [Auswahl] → [Angaben] → [Zusammenfassung] → [Abschluss] → [Bestätigung]
                 ↑______________ Ändern ohne Datenverlust ______________|
```

Kurze Abläufe (≤ 5 Felder) dürfen einseitig sein. Dann sind Zusammenfassung und Abschluss derselbe Bildschirm.

## Qualitätsregeln
- **Transparenz:** Preise, Gebühren, Kaution, Stornobedingungen **vor** dem Abschluss sichtbar; keine vorausgewählten kostenpflichtigen Extras.
- **Verfügbarkeit:** Nicht verfügbare Optionen sind erkennbar (Text + Symbol, nicht nur ausgegraut) und erklärt.
- **Termine und Zeiträume:** Datumseingabe per Tastatur und per Kalender möglich; Zeitzone bzw. Ort, falls relevant.
- **Keine Doppeleingaben** (WCAG 3.3.7), **zugängliche Anmeldung** (WCAG 3.3.8), **Fehlervermeidung** bei rechtlich oder finanziell verbindlichen Vorgängen: prüfen, korrigieren, bestätigen (WCAG 3.3.4).
- **Zeitlimits** (z. B. reservierter Warenkorb) werden angekündigt und lassen sich verlängern.
- **Mobil:** Hauptaktion immer erreichbar, passende Tastaturen (`inputmode`), `autocomplete` für Adresse und Zahlung.
- **Bestätigungs-E-Mail:** gleiche Begriffe wie im Ablauf, alle wichtigen Daten, als Text lesbar (nicht nur Bild).
- Rechtliche Anforderungen (z. B. Button-Beschriftung bei kostenpflichtigen Bestellungen, Widerruf) klärt das Projekt.

## Komponenten und Tokens
Form Field und alle Eingaben · Button · Radio Card · Alert · Toast · Loading State · Error State · Table bzw. Liste (Zusammenfassung) · optional Projektkomponenten (Datums- bzw. Zeitraumwahl, Warenkorb)

## Was das Projekt festlegt
Schritte und Reihenfolge, Pflichtangaben, Zahlungs- bzw. Anfragemodell, Texte der Abschluss-Aktion, Bestätigungsinhalte.
