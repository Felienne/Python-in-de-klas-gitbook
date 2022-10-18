# Les 7b

**1) Tonen**

Als je vorige les nog niet aan je tonen veld hebt gewerkt, is het daar nu tijd voor! Volg deze stappen:

1. Maak een functie `tonen().`
2. Koppel die functie aan de tonen knop.
3. Maak het hele veld weer leeg met de functie die je daarvoor hebt gemaakt.
4. Voeg een label toe voor je statistieken, laat die in beeld komen en zet er wat leuks in. Je kan beginnen met bijv "Hier zijn jouw statistieken!"

**2) Statistieken voor tonen**

Nu het label voor tonen goed in beeld komt, mag jij zelf kiezen welke statistieken je gaat tonen. Hier zijn een aantal ideeën die je zou kunnen laten zien:

* Hoeveel woorden er al geselecteerd zijn
* Hoeveel woorden er _nog niet_ geselecteerd zijn
* Hoeveel woorden al goed beantwoord zijn
* Hoeveel woorden er fout beantwoord zijn tot nu toe
* Hoeveel zinnen er al zijn ingevoerd

**3) Sla ook een datum op bij ieder antwoord (extra)**

We kunnen het tonen-venster _nog_ uitgebreider maken. Dat doen we door ook de datum van vandaag op te slaan als iemand een antwoord invoert. Daarmee kan je nog veel meer statistieken maken zoals:

* Aantal antwoorden goed vandaag, deze week, deze maand
* Aantal antwoorden fout vandaag, deze week, deze maand
* Welk woord het allerlangst geleden fout beantwoord is&#x20;

Volg deze stappen om de datum in te voeren:

1. Zet boven aan je code `import time`
2. Voeg nu bij het antwoorden de code `datum = date.today()` in
3. Sla de variabele ook op in je csv file door de rij aan te passen
4. Sla de variabele ook op in je csv file door de headers aan te passen
