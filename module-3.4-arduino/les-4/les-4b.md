# Les 4b

**Opdracht 1) Color mixing lamp**

Bouw de schakeling van bldzd 54 in je boek. Lees de uitleg bij de schakeling op bladzijde 55. Let goed op dat je ook de gekleurde doorschijnende stroken gebruikt.

**Opdracht 2) Programmeer je Arduino**

Schrijf de code om de color mixing lamp aan te sturen. Stuur de code naar de Arduino en check of deze werkt. Dit is uitgelegd in het boek bldzd 56 t/m 60.

**Opdracht 3) Leg uit**

Leg in eigen woorden uit:
- In het script worden de variabelen `redValue` en `redSensorValue` aangemaakt. Geef voor beide variabelen aan welke mogelijke waarden die kan hebben en waarvoor de variabele wordt gebruikt.
- In de code staat `redValue = redSensorValue / 4;` waarom is het nodig om de `redSensorValue` te delen door 4?.
- Wat gebeurt er als we de draadjes die naar de pinnen A0 en A1 gaan omwisselen?
- Wat doet de functie `analogWrite`?

**Opdracht 4) Stoplicht**

Zorg dat de RGB LED blauw gaat branden. Op het moment dat de sensoren voornamelijk rood licht binnenkrijgen moet de RGB LED uitgaan. 
Als de sensoren daarna weer voornamelijk groen licht binnenkrijgen moet de RGB LED weer blauw gaan branden.

**Opdracht 5) Lichtsignalen (X)**

Splits het tweetal. Één van de twee schrijft de code om de RGB LED aan te sturen op basis van de lichtsensors. 
De code mag alleen geverifieerd worden en nog niet naar de Arduino worden gestuurd. 
Vervolgens schrijven beiden op welke kleur de RGB LED geeft als er:
1. alleen rood licht op de sensoren valt
2. alleen blauw licht op de sensoren valt
3. alleen groen licht op de sensoren valt

Wie de meeste goede antwoorden heeft gegeven heeft gewonnen.

**Opdracht 6) Rainbow road (X)**

Voor deze opdracht hoef je de sensoren niet te gebruiken. Je kan ze wel gewoon in de schakeling laten zitten. Zorg dat de
kleur van de RGB LED geleidelijk veranderd van kleur. Gebruik deze volgorde: rood,oranje,geel,groen,blauw,paars,rood. Zorg dat de totale cyclus ca. 10 seconden duurt.
Het is handig om hiervoor een loop (lus) te maken met `for`. Weet je niet hoe dit moet kijk dan even naar je code van les 3b. Daarin heb je al een loop met `for` gemaakt.