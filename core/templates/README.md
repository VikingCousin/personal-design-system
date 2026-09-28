# Templates (Core)

> Core-Templates definieren **Struktur, Pflichtbereiche und Qualitätsregeln**, keine Gestaltung. Ein Projekt baut daraus seine gebrandeten Templates in `projects/<p>/templates/`.
> Die Wireframes sind schematisch und schreiben kein Layout vor. Reihenfolge und Anordnung dürfen Projekte begründet ändern, Pflichtbereiche und Qualitätsregeln nicht.

| Template | Datei | Typische Projekte |
|---|---|---|
| Website / Landingpage | [website-landingpage.md](website-landingpage.md) | lokales Unternehmen, Dienstleistung, Produkt, persönliche Marke |
| Marketingseite (Unterseite) | [marketing-page.md](marketing-page.md) | Leistungs-, Produkt-, Preis-, Über-uns-Seiten |
| Transaktionsablauf | [transaction-flow.md](transaction-flow.md) | Buchung, Anfrage, Checkout, Registrierung |
| App / Dashboard | [app-dashboard.md](app-dashboard.md) | SaaS, Kundenportal, interne Tools, Buchungsverwaltung |
| Dokument | [document.md](document.md) | Angebot, Bericht, Konzept, Rechnung, Brief |
| Präsentation | [presentation.md](presentation.md) | Pitch, Workshop, Report |
| Brand-Guideline | [brand-guideline.md](brand-guideline.md) | Kurzdokumentation einer Projektmarke |

## Aufbau jeder Template-Spezifikation

1. **Zweck** – welche Aufgabe das Template erfüllt
2. **Pflichtbereiche** und **optionale Bereiche**
3. **Struktur** (schematisch)
4. **Qualitätsregeln** (Inhalt, Accessibility, Responsive, Performance)
5. **Verwendete Core-Komponenten und Tokens**
6. **Was das Projekt festlegt**

## Allgemeine Regeln für alle Templates

- Eine **H1** pro Seite bzw. Dokument, logische Überschriftenhierarchie ohne Sprünge.
- Landmarks bei Webseiten: `header`, `nav`, `main`, `footer`; „Zum Inhalt springen“.
- Jede Seite hat **eine** Hauptaufgabe und **eine** Hauptaktion.
- Nur Tokens und Komponenten des Projekts; keine Sonderwerte ohne Begründung.
- Echte oder als Platzhalter gekennzeichnete Inhalte, keine erfundenen Belege (Bewertungen, Zahlen, Logos).
- Prüfung nach [quality-standards.md](../principles/quality-standards.md).
