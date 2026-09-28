# Template: App / Dashboard (Core)

## Zweck
Arbeitsoberfläche für wiederkehrende Aufgaben: Überblick, Listen, Details, Bearbeitung, Einstellungen.

## Grundlayouts

| Layout | Pflichtbereiche | Einsatz |
|---|---|---|
| **App-Shell** | Navigation (Sidebar oder Top-Bar; mobil Tab-Bar oder Menü) · Seitentitel · Hauptbereich · Konto/Hilfe | Rahmen aller App-Seiten |
| **Übersicht (Dashboard)** | Titel · 3–6 wichtigste Kennzahlen oder Aufgaben · nächste Handlungen · Einstieg in die Listen | Startseite nach Login |
| **Liste** | Titel + Hauptaktion („Neue Buchung“) · Suche und Filter · Tabelle bzw. Liste · Empty, Loading, Error · Pagination | Datensätze verwalten |
| **Detail** | Titel + Status · Hauptinformationen · Aktionen · Verlauf bzw. Aktivität (optional) · Zurück | einzelner Datensatz |
| **Formular / Bearbeiten** | Titel · Gruppen (Fieldsets) · Speichern / Abbrechen · Fehlerzusammenfassung | Anlegen, Ändern |
| **Einstellungen** | Kategorien (Tabs oder Seitennavigation) · Switches bzw. Formulare · Speichern-Logik einheitlich | Konto, Organisation |
| **Onboarding / Leerzustand** | Erklärung · erster Schritt · Beispiel oder Vorlage | erste Nutzung |

## Struktur App-Shell (schematisch)

```
Desktop                                     Mobil
┌──────────┬──────────────────────────┐     ┌──────────────────────┐
│ Marke    │ Seitentitel · Aktionen   │     │ Titel · Menü         │
│ Nav      ├──────────────────────────┤     ├──────────────────────┤
│ …        │ Inhalt                   │     │ Inhalt               │
│ Konto    │                          │     ├──────────────────────┤
└──────────┴──────────────────────────┘     │ Tab-Bar (3–5)        │
                                            └──────────────────────┘
```

## Qualitätsregeln
- **Kennzahlen mit Kontext:** Zeitraum, Vergleich und Einheit. Keine Zahl ohne Bedeutung.
- **Zustände vollständig:** Jede Liste und jedes Widget hat Empty, Loading und Error ([feedback.md](../components/feedback.md)).
- **Speichern einheitlich:** entweder automatisch (mit Rückmeldung) oder explizit, nicht gemischt ohne Kennzeichnung.
- **Tastaturbedienung** für häufige Aufgaben; optional Tastenkürzel (dokumentiert, abschaltbar).
- **Datenschutz:** personenbezogene Daten nur so viel wie nötig anzeigen.
- **Dichte:** komfortabel als Standard, kompakt optional nur für Zeiger-Geräte ([spacing-sizing.md](../tokens/spacing-sizing.md#4-dichte)).
- **Diagramme** haben eine Textalternative bzw. Datentabelle und unterscheiden Reihen nicht nur über Farbe (`color.data.*` + Muster bzw. direkte Beschriftung).
- Rollen und Rechte: Nicht verfügbare Aktionen werden erklärt oder ausgeblendet, einheitlich im Projekt.

## Komponenten und Tokens
Navigation · Tabs · Table · Pagination · Form Field und Eingaben · Button · Dialog · Drawer · Toast · Alert · Badge · Empty, Loading und Error State · `z.*` · `elevation.*` · optional Dichte-Modus

## Was das Projekt festlegt
Navigationstyp, Informationsarchitektur, Kennzahlen, Rollenmodell, Dichte, Dunkelmodus ja oder nein.
