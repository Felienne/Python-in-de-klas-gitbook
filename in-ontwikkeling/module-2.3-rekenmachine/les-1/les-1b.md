# Les 1b

**Opdracht 1) Fork de startcode**&#x20;

Deze opdracht wordt afgetekend als:

* Je naar [https://replit.com/@mevrHermans/Pidk-K2-M3-L1a-start](https://replit.com/@mevrHermans/Pidk-K2-M3-L1a-start) bent gegaan
* Je dit programma 'geforkt' hebt met de fork knop

**Opdracht 2) Maak de code af!**

Deze opdracht wordt afgetekend als:

* Jouw code netjes op twee getallen vraagt
* Jouw code om een _operator_ vraagt (dat zijn symbolen van wiskunde: plus, min, keer, gedeeld door)
* Jouw code dan het antwoord print

**Uitleg.** Er staat al wat code voor jou klaar om mee te beginnen. Belangrijke codes om te gebruiken zijn deze:

* met `getal = input(tekst)` vraag je de gebruiker om een getal, dat komt in de variabele `getal`.&#x20;
* `int(tekst)` vertaalt de tekst tussen haakjes in een getal
* `if: elif: else:` gebruik je om een keuze te maken
* `round()` rond het getal netjes af voor we printen

{% hint style="info" %}
Vergeet niet dat Python voor een sterretje gebruikt, dat is deze \*. Python gebruikt voor gedeeld door de slash, deze /
{% endhint %}

**Opdracht 3) Verbeter de foutmelding**

Deze opdracht wordt afgetekend als:

* Je een nette foutmelding krijgt als je iets invoert dat geen getal is.

Als je een verkeerde operator invoert, krijg je een mooie foutmelding te zien:

![](<../../../.gitbook/assets/image (7).png>)

Maar misschien had je ook geprobeerd om iets in te voeren dat geen getal was. Dan gaat niet goed, dan krijg je dit:&#x20;

![](<../../../.gitbook/assets/image (5).png>)

Zorg dat je ook een mooie foutmelding krijgt als `getal1` of `getal2` geen getal is. Daarvoor hebben we een nieuwe code nodig: `is_getal(getal_1)`Met die code kun je kijken of een tekst die ingevoerd is, wel een getal is. De functie `is_getal` staat al voor jou klaar bovenin het programma.

Zet jij de code zelf in een `if`?
