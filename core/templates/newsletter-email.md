# Template: Newsletter und E-Mail (Core)

> Neu in Core **1.1.0**. Gemeinsame Regeln: [cross-channel.md](cross-channel.md). Transaktions-E-Mails (Bestätigungen) zusätzlich nach [transaction-flow.md](transaction-flow.md).
> E-Mail-Clients unterstützen CSS nur eingeschränkt (z. B. CSS-Variablen, Webfonts, moderne Layouts). Deshalb setzt der Starter **aufgelöste Token-Werte inline** ein. Unterstützung vor Versand mit aktuellen Testwerkzeugen bzw. echten Clients prüfen.

## Arten

| Art | Zweck | Pflicht |
|---|---|---|
| Newsletter | regelmäßige Information, Angebote | Einwilligung, Abmeldelink, Absenderangaben |
| Kampagne | ein Anlass, eine Aktion | wie Newsletter |
| Transaktion | Bestätigung, Rechnung, Passwort | keine Werbung als Hauptinhalt, Referenznummer |

## Struktur

```
[Preheader: 1 Satz, ergänzt den Betreff]
[Kopf: Logo (verlinkt zur Website)]
[Eyebrow · Headline · Text]
[CTA-Button (Tabellen-Button, nicht nur Bild)]
[optional: weitere Module, je eine Aussage]
[Fuß: Absender, Grund des Empfangs, Abmelden, Datenschutz]
```

## Regeln

- **Breite** ca. 600 px als einspaltiger Standard, mobil fließend. Einspaltig bevorzugen.
- **Betreff und Preheader** sind Teil der Gestaltung: konkret, ehrlich, keine Irreführung.
- **Schriften:** Webfonts werden nicht überall geladen. Fallback-Stack aus dem Token (`font.family.*`) ist Pflicht und muss gut aussehen.
- **Farben** als Inline-Werte aus den Tokens. Dunkelmodus der Clients kann Farben invertieren: Logo mit Rand oder transparenter Variante testen.
- **Bilder** mit `alt`, Breite/Höhe, nie wichtige Information nur im Bild. Die Mail muss mit ausgeschalteten Bildern verständlich sein.
- **CTA** als HTML-Button (Tabellenzelle + Link), mindestens 44 px hoch, gleicher Begriff wie auf der Website.
- **Links** eindeutig benannt, Abmeldelink sichtbar und funktionsfähig.
- **Textversion** (Plain Text) mit gleichem Inhalt bereitstellen.

## Token-Zuordnung

| Element | Token |
|---|---|
| Hintergrund außen / innen | `color.bg.surface-sunken` / `color.bg.canvas` |
| Text, Sekundärtext | `color.text.primary`, `color.text.secondary` |
| CTA | `color.action.primary.bg`, `color.action.primary.text`, `radius.control` |
| Links | `color.text.link` |
| Fuß | `color.bg.surface`, `text.caption` |

## Compliance-Prüfpunkte (vor Versand fachkundig verifizieren)

- [ ] nachweisbare Einwilligung (z. B. Double-Opt-in), sofern erforderlich
- [ ] Absender eindeutig, Pflichtangaben im Fuß
- [ ] Abmeldung jederzeit und einfach möglich
- [ ] Datenschutzhinweis verlinkt
- [ ] Werbung als Werbung erkennbar
- [ ] Tracking (Öffnungs-/Klickmessung) nur im zulässigen Rahmen und transparent

## Qualitätsprüfung

- [ ] Rendering in mehreren Clients bzw. mit Testwerkzeug geprüft (hell, dunkel, mobil)
- [ ] Bilder aus: Inhalt verständlich
- [ ] alle Links und Abmeldelink getestet
- [ ] keine `[OFFEN: …]`-Platzhalter
- [ ] Testversand an interne Adresse, Freigabe **G6** vor Versand
