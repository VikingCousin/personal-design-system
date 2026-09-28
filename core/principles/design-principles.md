# Designprinzipien (Core)

> Gilt für jedes Projekt. Projekte ergänzen eigene **Markenprinzipien** in `projects/<p>/brand/`. Diese Core-Prinzipien sind keine Markenwerte, sondern Arbeitsregeln.
> Bei Konflikt zwischen einem Markenprinzip und einem Core-Prinzip gilt Core, außer die Abweichung ist als Ausnahme dokumentiert ([Governance](../process/governance.md#ausnahmen)).

## Die sieben Core-Prinzipien

1. **Nutzbarkeit vor Wirkung.** Eine Gestaltung, die beeindruckt, aber schwer zu bedienen ist, ist nicht fertig. Accessibility ist eine Mindestanforderung, kein Feature ([accessibility.md](accessibility.md)).
2. **System vor Einzelfall.** Jeder wiederkehrende Wert ist ein Token, jedes wiederkehrende Muster eine Komponente. Einmalige Werte brauchen eine Begründung ([Tokens](../tokens/architecture.md)).
3. **Rolle vor Wert.** Gestaltet und benannt wird nach Funktion (`color.action.primary`), nicht nach Aussehen (`blue-500` im Komponentencode).
4. **Inhalt vor Dekoration.** Struktur, Hierarchie und Gestaltungselemente müssen etwas über den Inhalt aussagen. Was nichts aussagt, wird entfernt.
5. **Marke im Projekt, Qualität im Core.** Core schreibt keinen Stil vor. Jede Marke darf laut, leise, bunt, schlicht, rund oder eckig sein, solange sie die Qualitätsregeln erfüllt.
6. **Begründet statt beliebig.** Wesentliche Designentscheidungen werden mit den sieben Prüffragen (unten) begründet und dokumentiert.
7. **Menschen entscheiden, AI bereitet vor.** Wesentliche Marken- und Geschäftsentscheidungen trifft der Mensch. Claude entwickelt Optionen, begründet und dokumentiert ([Approval-Gates](../agent-skill/rules/approval-gates.md)).

## Die sieben Prüffragen für wichtige Designentscheidungen

Für jede wichtige Entscheidung (Farbe, Schrift, Layoutprinzip, Komponentenlogik, Markenzeichen):

1. Welches Problem löst sie?
2. Für welche Zielgruppe bzw. Nutzungssituation?
3. Warum passt sie zur Marke des Projekts?
4. Funktioniert sie in **allen Medien des Projekts** (Screen, Print, Beschilderung, Produkt …)?
5. Ist sie in 5–10 Jahren noch vertretbar, oder ist sie ein Trend?
6. Ist sie barrierefrei?
7. Kann sie als Token oder Regel abgebildet werden?

Nicht jede Kleinigkeit braucht alle sieben Antworten. Pflicht sind sie für Entscheidungen, die in `DECISIONS.md` landen.

## Was Core bewusst NICHT vorschreibt

- keine Farbpalette, keine Schriftart, keine Bildsprache
- keinen Stil (minimalistisch, verspielt, editorial, technisch …)
- keine Rundungen, keine Schatten, keine Dichte. Core definiert nur die **Skalen und Rollen**, die Werte setzt das Projekt.
- keinen Dark Mode als Pflicht (siehe [color.md](../tokens/color.md#5-hell-und-dunkel))
- keine Zielgruppe
