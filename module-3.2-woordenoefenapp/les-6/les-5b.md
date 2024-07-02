# Les 6b

De app die we gaan maken kent nu twee fases:&#x20;

1. Woorden selecteren
2. Woorden oefenen

In deze les gaan we een derde fases toevoegen: Uitvoer tonen.

In die fase gaan we jouw opgeslagen csv bestand uitlezen en netjes weergeven zodat je het kan tonen aan je docent, of aan je ouders!&#x20;

**Opdracht 1) Nieuwe fase toevoegen**

Maak een nieuwe functie en noem die `uitvoer_tonen()`. Weet je niet meer hoe je een funcite maakt? Kijkt dan in de code die je al hebt.

Vul de body van de functie nog even met:

`print('We gaan jouw woordenlijst nu tonen')`

Dat vullen we later verder in.

**Opdracht 2) Keuze voor de gebruiker uitbreiden.**

Eerst had de gebruiker 2 opties, en nu 3. Verander jij de if zelf? Vergeet niet ook de instructie aan te passen, dat is deze regel:

`input('Wil je woorden selecteren(s) of oefenen(o)?')`

Test je code! Wordt de funtion `uitvoer_tonen` goed aangeroepen?

**Opdracht 3) Data laten zien**

We gaan nu de functie ook invullen met code. Kijk goed in je bestaande code en volg deze stappen:

1. Lees het csv bestand words-selectie.csv uit
2. Print alleen de woorden waarvoor een antwoord is opgeslagen (doorvoor geldt: betekenis is niet leeg)
3. Zorg dat iedere regel zo geprint wordt:
4. Het woord `woord` betekent volgens jou `betekenis` Jij maakte er deze zin mee: `zin`

{% hint style="info" %}
Een handig manier om strings in Python mooi te maken is het gebruik van fstrings, die maak je zo:

f"Het woord {woord} betekent volgens jou {betekenis} Jij maakte er deze zin mee: {zin}.
{% endhint %}





