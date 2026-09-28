# Template: Dokument (Core)

## Zweck
Schriftliche Dokumente, die gelesen, gedruckt oder weitergegeben werden: Angebot, Bericht, Konzept, Rechnung, Brief, Handout. Ausgabe als DOCX, PDF oder Online-Dokument.

## Pflichtbereiche nach Dokumenttyp

| Typ | Pflichtbereiche |
|---|---|
| **Alle** | Titel · Datum · Absender bzw. Verfasser · Seitenzahlen (ab 2 Seiten) · Kontakt |
| Bericht / Konzept | Titelseite oder Titelblock · Zusammenfassung (≤ 1 Seite, zuerst) · Inhaltsverzeichnis (ab ca. 6 Seiten) · Kapitel mit nummerierten Überschriften · Quellen bzw. Anhang |
| Angebot | Empfänger · Leistungsbeschreibung · Preise (netto/brutto klar) · Gültigkeit · Bedingungen · nächster Schritt |
| Rechnung | rechtliche Pflichtangaben laut Projekt bzw. Land klären · Positionen · Summen · Zahlungsziel |
| Brief | Briefkopf · Anschrift · Betreff · Anrede (nach Anrede-Regel des Projekts) · Gruß · Unterschrift |

## Struktur (schematisch)

```
[Kopf: Marke · Dokumenttitel · Datum]
[Zusammenfassung / Kernaussage]
[Inhalt: H1 → H2 → H3, Absätze, Listen, Tabellen, Abbildungen mit Unterschrift]
[Anhang / Quellen]
[Fuß: Seitenzahl · Kontakt · Vertraulichkeitsvermerk (falls nötig)]
```

## Qualitätsregeln
- **Formatvorlagen statt manueller Formatierung** (Überschrift 1–3, Standard, Zitat, Beschriftung). Nur so bleiben Inhaltsverzeichnis, Barrierefreiheit (getaggtes PDF) und Konsistenz erhalten.
- **Typografie:** Fließtext 10–12 pt im Druck, Zeilenabstand 1.3–1.5, Zeilenlänge ≤ ca. 80 Zeichen; Ersatzschrift für Office festgelegt ([typography.md](../tokens/typography.md#5-schriftwahl-prüfliste-für-das-projekt)).
- **Farbe:** Markenfarben für Akzente, nicht für Fließtext; S/W-Druck bleibt verständlich.
- **Tabellen** mit Kopfzeile, die sich auf Folgeseiten wiederholt.
- **Barrierefreies PDF:** Tags, Lesereihenfolge, Alt-Texte, Dokumentsprache, Titel in den Metadaten.
- **Ränder** so bemessen, dass das Dokument auch gelocht bzw. gebunden lesbar bleibt.

## Komponenten und Tokens
Farb- und Typo-Tokens des Projekts, übersetzt in Formatvorlagen (Print: pt statt px; Umrechnung dokumentieren). Tabellen nach [data.md](../components/data.md), Hinweisboxen nach Alert.

## Was das Projekt festlegt
Briefkopf, Titelseite, Farbeinsatz, Schriften für Office, Dokumenttypen, Vorlagendateien (DOCX, Google Docs).
