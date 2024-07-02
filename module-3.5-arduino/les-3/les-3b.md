# Les 3b

**Opdracht 1) Maak een Love-o-Meter**

Maak het circuit met temperatuursensor en 3 led lampen (zie boek bldzd 44). Let op de verschillende pinnen van de tempeartuursensor. Als je de temperatuursensor verkeerd zet heb je kans dat deze gevaarlijk heet wordt.

**Opdracht 2) Bouw de interface**

Vouw het bijgeleverde karton en plaats dit over je circuit zodat je een echte Love-o-Meter hebt.

**Opdracht 3) Programmeer je Arduino**

Schrijf de code om je Love-o-Meter circuit van opdracht 1 aan te  sturen. Stuur de code naar de Arduino en check of deze werkt. Dit is uitgelegd in het boek bldzd 47 t/m 51.

**Opdracht 4) Leg uit**

Leg in eigen woorden uit:
- Wat doet de `serial.Begin()` functie en welke input geef je mee aan deze functie?
- Welke functie gebruik je om de waarde van een sensor weer te geven?
- Wat doet de `analogRead` functie? Wat is het verschil met de `digitalRead()` functie?
- Waarom wordt bij het printen van de tempeartuur de functie `serial.Println()` gebruikt en niet `serial.Print()`?
- Gerda denkt dat ze koorts heeft. Ze heeft geen thermometer maar wel de Arduino. Kan ze deze opstelling gebruiken om te meten hoeveel graden koorts ze heeft?

**Opdracht 5) Andersom**

Nu gaan er steeds meer lampjes branden als de temperatuursensor warmer wordt. Pas de code aan zodat bij de start alle lampjes branden en er steeds meer lampjes uitgaan als het warmer wordt.

**Opdracht 6) Gevoelig**

Er gaat nu iedere keer een lampje aan (of uit bij opdracht 5) als de temperatuur 2 graden stijgt. Pas de code aan zodat dit al gebeurd bij een stijging van 1 graden.

**Opdracht 7) Lichtshow**

Programmeer de lampjes zo dat bij een bepaalde temperatuur de lampjes gaan knipperen. Kies zelf de temperatuur en hoe snel ze knipperen.

**Opdracht 8) baselineTemp**

We geven nu aan de Arduino op dat de standaardtemperatuur (`baselineTemp`) 20 graden is. Stel je gebruikt de Love-o-Meter op een plek waar het geen 20 graden is. Wat kan je doen om automatisch de `baselineTemp` te bepalen. Pas de code zo aan zodat deze werkt bij iedere temperatuur.

**Opdracht 9) DJ Love (X)**

Voeg een knop (button) toe aan de schakeling. Pas als je deze knop indrukt werkt de schakeling. Zorg dat de staat van de knop (aan/uit) wordt weergegeven op de computer, gebruik hiervoor de functie `serial.Print()`.

**Opdracht 10) DIY (X)**

Bedenk zelf nog iets om je schakeling of code uit te breiden. Bedenk eerst goed wat je wil dat er gebeurd. Dan hoe je dat moet maken en ga het dan pas uitvoeren.
