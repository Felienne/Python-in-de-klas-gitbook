# Les 4b

**Opdracht 1\) Maak een variabele antwoord**

Deze opdracht wordt afgetekend als:

* Je een variabele `antwoord` hebt gemaakt om het antwoord van een som in op te slaan. 

**Uitleg.** Als eerste stap gaan we een variabele toevoegen. In plaats van het antwoord meteen te printen met `print(getal1 + getal2)` gaan we de waarde eerst in een variabele zetten.  
  
Vervang alle vier regels voor operatoren door toewijzingen, bijvoorbeeld:

`print(getal1 + getal2)`

wordt ****

`antwoord  = getal1 + getal2   
print (antwoord)`

Test je code nu uit. Als het goed is, werkt alles nog precies hetzelfde!

**Opdracht 2\) Pas je if aan**

Deze opdracht wordt afgetekend als:

* Je nog maar een keer **** `print(antwoord)` in je code hebt staan.

**Uitleg.** We hebben nu vier keer dezelfde regen in de code staan. Dat is niet zo handig, dus dat gaan we eerst netjes maken voor we verder gaan.

We gaan eerst kijken of de operator wel in het lijstjes operatoren zit. Dat doen we met de regel `if operator in operatoren:`Die if gaan we combineren met de else die we al hadden, zoals in de code hier onder. Op de \_\_\_\_ staart de code die jij al had, met 4 if's.

```python
  if operator in operatoren:
    _____
  else:
    print('deze operator ken ik niet!')
```

Nu mag je de regel print\(antwoord\) bij alle vier de regels weghalen en alleen op het einde printen, zoals in deze code. Op de streepjes staan dan de andere drie operatoren, zonder `print(antwoord)`

```python
  if operator in operatoren:
    if operator == '+':
      antwoord = getal1 + getal2
    ____
      
    print (antwoord)
  else:
    print('deze operator ken ik niet!')
```

{% hint style="info" %}
Test je code nu weer goed, met een kloppende som en een foute som! Bijv:   
3 + 5 -&gt; dat wordt natuurlijk 8  
hallo dit is een som -&gt; dat moet een nette foutmelding geven
{% endhint %}

**Opdracht 3\) Zet het antwoord weer in de lijst**

Deze opdracht wordt afgetekend als:

* Je het antwoord op de som terug in de lijst hebt gezet.

**Uitleg.** Je hoeft vanaf deze les de code niet meer te forken, je mag steeds aan je eigen rekenmachine doorwerken.

**Opdracht 4\) Voeg een while lus toe**

Deze opdracht wordt afgetekend als:

* Je een while lus aan je code hebt toegevoegd 



