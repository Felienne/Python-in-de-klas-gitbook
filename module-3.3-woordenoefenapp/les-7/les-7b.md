# Les 7b

Er mist nog een belangrijke functie in ons programma... Kijken of wat de gebruiker invoert eigenlijk wel klopt! We gaan dat op twee plekken controleren, bij het invoeren van het antwoord in `oefenen()` om meteen feedback te geven, en bij het maken van het overzicht in `uitvoer_tonen()`.

**Opdracht 1) Controleren bij het invoeren**

Ga naar de functie oefenen() en voeg daar een if toe. Controleer of de ingevoerde betekenis hetzelfde is als de beschrijving uit het bestand. Zo ja, zeg dan iets positiefs tegen de gebruiker. Zo nee, vertel dan wat de betekenis wel is. Je kan daar weer een fstring voor gebruiken!

**Opdracht 2) Opslaan bij het invoeren**

We willen ook in de tabel opslaan of de gebruiker het antwoord wist zodat we dat later kunnen printen. Maak dus een nieuwe rij in de tabel, noem die "Goed" en sla daar "goed" of "fout" in op.

Weet je niet meer goed hoe dat moet? Kijk in je code of zoek eens op Google op "save csv file in Python". &#x20;

**Opdracht 3) Goed of fout weergeven in de uitvoer**

Ga nu weer naar je nieuwe functie  `uitvoer_tonen()`. Je las daarin het csv bestand al uit natuurlijk, maar nu is er een nieuwe kolom! Pas je code zo aan dat `rij['Goed']` wordt opgeslagen in een variabele en netjes geprint.





