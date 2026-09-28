# Template: Website / Landingpage (Core)

## Zweck
Einstiegsseite, die in wenigen Sekunden klärt: **Was ist das? Für wen? Warum hier? Was tue ich als Nächstes?**

## Bereiche

| Bereich | Pflicht? | Aufgabe |
|---|---|---|
| Header mit Navigation | Pflicht | Marke, Hauptbereiche, Hauptaktion |
| Hero | Pflicht | Angebot in einem Satz, Nutzen, Hauptaktion. Zeigt das Charakteristischste des Projekts, nicht zwingend „Headline + Bild + Button“ |
| Nutzen / Leistungen | Pflicht | 3–6 konkrete Leistungen oder Vorteile |
| Vertrauen | Pflicht, sobald echte Belege vorliegen | echte Referenzen, Bewertungen, Zertifikate, Zahlen, Team. **Nie erfunden** |
| So funktioniert es | optional | Ablauf in Schritten, wenn der Ablauf erklärungsbedürftig ist |
| Angebot / Preise | optional | Preise oder Preisrahmen, wenn für die Entscheidung wichtig |
| FAQ | optional | echte Einwände beantworten (Accordion) |
| Abschluss-CTA | Pflicht | Hauptaktion wiederholen, ggf. Kontaktalternative |
| Footer | Pflicht | Kontakt, Pflichtangaben (Impressum, Datenschutz), sekundäre Links |
| Lokales (bei lokalen Unternehmen) | Pflicht bei Ortsbezug | Adresse, Öffnungszeiten, Karte bzw. Anfahrt, Einzugsgebiet |

## Struktur (schematisch)

```
[Header: Marke · Navigation · Hauptaktion]
[Hero: Angebot · Nutzen · Hauptaktion · charakteristisches Element]
[Nutzen/Leistungen]
[Vertrauen]
[optional: Ablauf · Preise · FAQ]
[Abschluss-CTA]
[Footer]
```

## Qualitätsregeln
- **Hauptaktion** ist überall dieselbe und gleich benannt (z. B. „Anhänger reservieren“).
- Der Hero-Text wirkt auch ohne Bild; Bilder haben Alt-Text oder sind dekorativ.
- **Performance:** größtes Bild optimiert und mit Maßen, Schriften ≤ 2 Familien, Ladezeit mobil ohne blockierende Skripte, kein Autoplay-Video mit Ton.
- Kontaktwege (Telefon als `tel:`-Link, E-Mail, Formular) sind mobil mit einem Tap erreichbar.
- SEO-Grundlagen: aussagekräftiger `<title>`, Meta-Description, strukturierte Daten bei lokalen Unternehmen (optional).
- Cookie- bzw. Consent-Hinweise nur, wenn nötig, und datensparsam voreingestellt.

## Komponenten und Tokens
Navigation · Button · Link · Card · Accordion · Form Field (Kontakt) · Alert · `space.layout.section` · `size.container.*` · `text.display|heading|body.*`

## Was das Projekt festlegt
Reihenfolge der optionalen Bereiche, Hero-Konzept, Bildsprache, Tonalität, ob eine Hauptaktion in der mobilen Navigation dauerhaft sichtbar ist.
