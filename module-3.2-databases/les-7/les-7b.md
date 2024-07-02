# Les 7b

**Opdracht** **1) Invoeren vanuit Python**

Maak het programma van de slides zelf ook: zorg dat de gebruiker naam en geslacht kan invoeren. Begin met [deze repl](https://replit.com/@OnnoEbbens/Pidk-K3-M2-L7a-2#main.py).

De database heeft al een autoincrement, dat hoef jij (nog) niet in te stellen.

**Opdracht 2) Tabel maken en invoeren vanuit Python**

Maak het programma van de slides zelf ook: zorg dat de gebruiker naam en geslacht kan invoeren.

In opdracht 2 is er nog geen tabel aangemaakt in de database. Dat moet jij zelf doen, en je moet daar ook de autoincrement voor gebruiken, zodat de id vanzelf opgehoogd wordt.\
\
Begin met [deze repl](https://replit.com/@mevrHermans/Pidk-K3-M2-L7b-2).

1. Voer eerst de `create` uit, dat hoeft maar een keer (daarna is de tabel aangemaakt) \`
2. Maak dan de rest van de code af, die moet je nog wel even 'aan' zetten, door de # eraf te halen.

**Opdracht** **3) Alle metroreizen(X)**

Maak een nieuw Pythonprogramma aan in repl.it. Zet op de eerste regel deze code: `import sqlite3`

Nu kun je vanuit Python ook database codes aanspreken zoals in opdracht 1 en 2.

{% hint style="info" %}
Met de code `sqlite3 database.db` kan je je database testen via de shell
{% endhint %}

Maak nu alle drie de tabellen van de metroreizendataset. De gebruiker moet personen en stations kunnen invoeren. Ook moet de gebruiker de tabel reizen kunnen vullen met reizen van een persoon van en naar een station.

Tip: Print alle namen en stations uit met Python. Zoek zelf uit hoe dat moet. Dan kan de gebruiker gewoon de nummers invoeren.

**Opdracht 4) PyGame & Invoeren (X)**

WErk verder in je replit van opdracht 3, maar voeg bovenaan deze code in:

`import pygame`

Nu kan je SQL en Pygame allebei gebruiken in een programma!

Maak nu een mooie 'user interface' in PyGame waarin de data kan worden ingevoerd. Maak bijv:

* een knop Invoeren
* een knop Aanpassen
* Een knop Laat alle data zien

Schrijf dan bijbehorende queries. Je mag de queries laten zien met print, of, extra moeilijk op het PyGame scherm zelf met een blit.
