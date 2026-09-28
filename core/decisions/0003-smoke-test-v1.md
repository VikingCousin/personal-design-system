# 0003 · Smoke Test Core v1.0

- **Status:** accepted · **Ebene:** PDS · **Datum:** 2026-09-28 · **Core-Version:** 1.0.0
- **Art:** theoretischer Test. Zwei stark unterschiedliche Projekte wurden gedanklich gegen Core durchgespielt. Es wurden **keine** Projekte angelegt.

## Testprojekte

| | **A · Lokaler Anhängerverleih** | **B · Modernes B2B-SaaS** |
|---|---|---|
| Ziel | Reservierungen und Anrufe aus der Region | Trials, Aktivierung, tägliche Nutzung |
| Ergebnisse | Landingpage, Preisliste, Reservierungsanfrage, Fahrzeug- bzw. Anhängerbeschriftung, Visitenkarte, Angebot/Rechnung | Marketing-Website, Preisseite, Registrierung, App mit Dashboard, Tabellen, Diagrammen, Einstellungen, Dokumentation, Pitch-Deck |
| Zielgruppe | Privatkunden und Handwerker vor Ort, oft mobil, wenig Zeit | Fachanwender im Büro, Desktop, täglich mehrere Stunden |
| Restriktivstes Medium | Anhängerbeschriftung aus 20 m Entfernung, Favicon | dichte Tabelle bei 1280 px, Favicon |
| Wahrscheinliche Tiefe | S, evtl. Brand-Import (Logo vorhanden) | M |

## Prüfung

| Prüffrage | A · Anhängerverleih | B · B2B-SaaS |
|---|---|---|
| **Bootstrap und Workflow** | trägt mit Tiefe S (Kurzbrief, Foundation auf einer Seite, 2 Richtungen oder Brand-Import, gebündelte Gates) | trägt mit Tiefe M |
| **Principles** | trägt; Accessibility Standard-Profil; Content-Regeln (konkret, Sprache der Nutzenden) passen gut | trägt; „Sprache der Nutzenden“ erlaubt Fachsprache; Tastatur- und Dichte-Regeln vorhanden |
| **Tokens** | Pflichtvertrag vollständig belegbar; Material- bzw. RAL-Angaben für Folie über die optionale Gruppe `color.material` | Pflichtvertrag vollständig belegbar; Dunkelmodus und Dichte „kompakt“ als Modi; Themes für White-Label |
| **Components** | Button, Form, Card, Accordion, Alert decken die Landingpage ab. Datums-/Zeitraumwahl als Projektkomponente | Table, Tabs, Dialog, Drawer, Toast, Pagination, Empty/Loading/Error decken die App-Grundlagen ab |
| **Templates** | Landingpage (inkl. Lokales), Marketingseite (Preise), Dokument (Angebot, Rechnung) | Website, Marketingseite (Preise), App/Dashboard, Dokument, Präsentation |
| **Erzwingt Core einen Stil?** | nein: keine Farben, Schriften, Radien oder Schatten; Dichte, Tonalität und Anrede sind frei | nein: kompakte Dichte und Dunkelmodus erlaubt, beides nicht Pflicht |
| **Versehentlich Digital-Legacy-spezifisch?** | Beispielwerte gefunden (s. u.) | wie A |

## Gefundene Probleme und Korrekturen

| # | Problem | Betroffen | Korrektur in Core 1.0.0 |
|---|---|---|---|
| 1 | Kein Template für Abläufe mit Verbindlichkeit (Reservierung, Checkout, Registrierung). Beide Projekte (und E-Commerce) brauchen es. | A, B | neu: [templates/transaction-flow.md](../templates/transaction-flow.md) |
| 2 | Keine Regeln für Logo, Icons, Fotografie und Bildrechte | A, B | neu: [principles/visual-assets.md](../principles/visual-assets.md) |
| 3 | Diagrammfarben nur als optionale Token-Gruppe erwähnt, ohne Regeln | B | neu: Abschnitt Datenvisualisierung in [tokens/color.md](../tokens/color.md#7-datenvisualisierung) |
| 4 | Beispiel-Hexwert aus einer Pilot-Richtung in `tokens/architecture.md`; Material- und Zahlenbeispiele mit Pilotbezug | — | durch neutrale Beispiele ersetzt |
| 5 | Pflicht-Dunkelmodus wäre für A Überlast | A | war bereits bedingt formuliert, bestätigt |
| 6 | 44-px-Zielgröße kollidiert mit dichten SaaS-Tabellen | B | war bereits geregelt: `size.target.min-pointer` (24 px) nur für Zeiger-UIs, bestätigt |
| 7 | Schwerer Prozess für kleine Projekte | A | war bereits geregelt über Tiefe S, bestätigt |

## Bewusst nicht korrigiert (Grenzen, siehe README)

- Weitere Komponenten (Dropdown-Menü, Combobox mit Suche, Datumsauswahl, Avatar, Fortschritt, Chip, Datei-Upload) sind in v1.0 nicht spezifiziert. Projekte bauen sie nach der Spec-Vorlage. Kandidaten für 1.1.
- Kein E-Mail-Template (Bestätigungs-E-Mails sind im Transaktionsablauf geregelt). Kandidat für 1.1.
- Keine Adapter bzw. kein Build (Tokens → CSS/Tailwind/PPTX). Kandidat für 1.1.

## Ergebnis

**Bestanden.** Core v1.0 ist für beide Projekttypen verwendbar, erzwingt keinen Stil und enthält nach den Korrekturen keine Digital-Legacy-Visuals. Die Lücken 1–3 wurden vor der Freigabe von 1.0.0 geschlossen.
