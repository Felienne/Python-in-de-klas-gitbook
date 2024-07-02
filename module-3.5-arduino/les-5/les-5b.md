# Les 5b

**Opdracht 1) Mood Cue**

Bouw de schakeling van bladzijde 64 uit het boek. Let op hoe je de capacitors plaatst. De zijde met de zwarte streep moet worden verbonden met de aarde (ground -).
Als deze verkeerd om zijn kan de capacitor ontploffen.

**Opdracht 2) Programmeer je Arduino**

Schrijf de code om de Mood Cue aan te sturen. Stuur de code naar de Arduino en check of deze werkt. Dit is uitgelegd in het boek bldzd 66 t/m 68.

**Opdracht 3) Bouw de interface**

Vouw het bijgeleverde karton en plaats dit over je circuit zoals uitgelegd in het boek bldzd 69.

**Opdracht 4) Leg uit**

Leg in eigen woorden uit:
1. Wat doet de code `#include <Servo.h>`?
2. Wat doet de `map()` functie? Wat is het resultaat van onderstaande functie aanroepen
    - map(0, 0, 1023, 0, 179)
	- map(179, 0, 1023, 0, 179)
	- map(5, 0, 10, 0, 50)
3. Wat doet een capacitor?
4. WAt doet de functie `myServe.write()`? Waarom moet de waarden die je aan deze functie geeft kleiner zijn dan 180?

**Opdracht 5) There was light**

Vervang de potentiometer door een lichtsensor. Zorg dat de servo op "COME IN" staat als het licht is en op "STAY OUT" als het donker is

**Opdracht 6) Mysterious (X)**

Voeg een knop toe aan de opstelling van opdracht 5. Persoon 1 van het tweetal programmeert de knop en de lichtsensor op een bepaalde manier. Probeer voor ieder van deze 4 scenario's te bedenken wat de servo moet doen:
1. wel licht, knop niet ingedrukt
2. wel licht, knop ingedrukt
3. geen licht, knop niet ingedrukt
4. geen licht, knop ingedrukt

Persoon 2 van het tweetal leest het script en probeert uit de code te halen wat er gebeurt in elk van de 4 scenario's. Zowel persoon 1 als persoon 2 schrijft op wat hij/zij denkt dat er gebeurt. Controleer daarna of het klopt door de 4 scenario's te testen.

**Opdracht 7) Mastermind (X)**

Deze opdracht gaat hetzelfde als opdracht 6. Persoon 1 schrijft weer code voor de 4 scenario's. Deze keer leest persoon 2 niet het script maar gaat hij meteen testen wat er gebeurt. Hij schrijft de code (op papier of in een andere Arduino IDE) die hij denkt dat er hoort bij deze configuratie. Als persoon 2 voor alle 4 de scenario's code heeft geschreven vergelijkt hij dit met de code die persoon 1 had geschreven.