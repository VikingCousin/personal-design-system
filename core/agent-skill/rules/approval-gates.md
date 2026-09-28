# Approval-Gates (Core)

> An jedem Gate hält Claude an, legt das Ergebnis vor und wartet auf die ausdrückliche Freigabe des Nutzers. Ohne Freigabe geht Claude nicht in die nächste Phase. Die Freigabe wird in `DECISIONS.md` des Projekts dokumentiert.

## Gates

| Gate | Nach Phase | Claude legt vor | Nutzer entscheidet |
|---|---|---|---|
| **G0** | Setup | Projektordner, Vorschlag für Tiefe, Profil, Einstieg, Ergebnisliste | bestätigt oder korrigiert |
| **G1** | Brief | Brief + Analyse: Lücken, Widersprüche, gebündelte offene Fragen | Brief bestätigt, Fragen beantwortet oder bewusst offen |
| **G2** | Brand Foundation | Foundation + Voice mit Kennzeichnung, offene Entscheidungen (A/B/C) mit Optionen | Arbeitsfreigabe, Änderungen, offene Punkte |
| **G3** | Creative Direction bzw. Brand-Import | 2–3 Richtungen mit Style-Tiles und Bewertung, kein Gewinner. Bei bestehender Marke: Ergebnis des Brand-Imports mit gefundenen Problemen und Lösungsoptionen | wählt Richtung bzw. Kombination, verlangt Überarbeitung bzw. entscheidet über die Import-Befunde |
| **G4** | Tokens | Token-Dateien, Kontrastnachweis, Schriftlizenzen, Abweichungen von Core-Defaults | Freigabe der Werte |
| **G5** | Components / Templates | umgesetzte Komponenten bzw. Templates mit Prüfergebnis (A11y, Responsive) | Freigabe (einzeln oder gebündelt) |
| **G6** | Release | was veröffentlicht, deployt, gedruckt oder versendet wird | ausdrückliche Freigabe für genau diesen Schritt |

In Tiefe S dürfen G1+G2 und G4+G5 gebündelt werden. G3 und G6 werden nie übersprungen.

## Nie ohne Nutzer

Diese Punkte trifft **immer** der Nutzer. Claude darf Optionen vorbereiten, begründen und empfehlen, wenn der Nutzer danach fragt, aber nicht festlegen:

- Markenname, Produktnamen, Claims und Slogans
- Positionierung und Markenprinzipien (final)
- visuelle Richtung
- finale Farben, Schriften, Logo und Markenzeichen
- Anrede (du/Sie) und Grundtonalität
- Geschäftsmodell, Preise, Angebotsstufen, Rabatte
- rechtliche Aussagen, Garantien und Versprechen
- Umgang mit sensiblen Themen (z. B. KI-generierte Inhalte, Gesundheit, Tod, Finanzen)
- Änderungen an `core/`
- Veröffentlichung, Deployment, Versand, Druckfreigabe
- Löschen von Projektmaterial

## Was Claude ohne Gate tun darf

- Dateien im Projektordner anlegen und Arbeitsstände überarbeiten
- Recherchieren (mit Quellenangabe) und Research-Agenden erstellen
- Explorationen und Prototypen erstellen (klar als solche gekennzeichnet)
- Qualitätsprüfungen durchführen und Fehler in eigenen Arbeitsständen beheben
- Core-Kandidaten markieren
- nicht-strategische Details, die sich aus freigegebenen Entscheidungen ergeben (z. B. Hover-Farbe aus freigegebener Aktionsfarbe ableiten), dokumentiert entscheiden

## Wenn der Nutzer „einfach machen“ sagt

Auch bei weitgehender Autonomie gelten die „Nie ohne Nutzer“-Punkte. Claude arbeitet dann mit **Arbeitsständen und Vorschlägen**, markiert sie deutlich und legt die Entscheidungen gebündelt vor, statt sie selbst zu finalisieren.
