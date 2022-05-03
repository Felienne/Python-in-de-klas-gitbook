# Les 4b

De app die we gaan maken kent straks twee fases:&#x20;

1. Woorden selecteren
2. Woorden oefenen

In deze les gaan we het oefenen om orde maken. Dat doen we meteen in een functie.

**Opdracht 1) Oefenfunctie aanroepen**

Vorige les hebben we alleen nog de code `print('We gaan oefenen')`in de code gezet. Dat gaan we nu veranderen in het aanroepen van de oefenfunctie. Vervang de regel door`oefenen()`.

**Opdracht 2) De functie aanmaken**

De code werkt nu niet want er is nog geen functie oefenen! Die ga jij nu zelf maken en invullen. Scroll naar boven in je code en maak een functie. Je mag in de body (de inhoud) van je functie `print('We gaan oefenen')`zetten.&#x20;

Test je code nu uit. Krijg je inderdaad de tekst in beeld als je o typt? Dan is de functie goed aangemaakt.

Tip: Klap de functie `selecteren()`even dicht met het driehoekje:

****![](<../../.gitbook/assets/image (12).png>)****

**Opdracht 3) De functie invullen**

Nu ga jij de functie invullen. Zorg dat er het volgende gebeurt:

1. Lees het csv-bestand weer in
2. Kijk per regel of het woord bekend is. Doe alleen iets voor onbekende woorden, dus als `rij['bekend'] == 'nee'`
3. Voor onbekende woorden, vraag de gebruiker om **twee** invoeren!
   1. De betekenis
   2. Een zin met het woord erin

Voor nu slaan we de twee antwoorden op in twee variabelen: `betekenis` en `zin`. Volgende les schrijven we die variabelen teurg in de csv file zodat je die aan je leraar Engels kan laten zien!&#x20;

****

