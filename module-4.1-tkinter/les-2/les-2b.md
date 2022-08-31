# Les 2b

**1) Maak een nieuw programma op replit**

Maak een vers programma op replit en zet er deze code in:

```python
from tkinter import *

root = Tk()

root.title("Mijn woordenoefenapp")
root.geometry("600x400")
```

Test je code uit en kijk of je weer een mooie UI in beeld krijgt.

**2) Maak drie knoppen**

In je oefenapp had je, als het goed is, die verschillende _modi_ (het meervoud van modus):

1. Woorden selecteren om te oefenen met de functie `selecteren()`
2. Woorden oefenen met de functie `oefenen()`
3. Een print maken van jouw woordenkennis met de functie `uitvoer_tonen()`

Maak nu drie knoppen en zet daar op:

1. Selecteren
2. Oefenen
3. Uitvoer tonen

Weet je niet meer hoe je knoppen maakt? Spiek bij jouw code van vorige week.&#x20;

Hier zijn belangrijke tips!!

* Iedere knop moet een eigen variabele worden! (bijv: `knop1` en `knop2` of, nog beter: `selecteerknop` en `oefenknop`)
* `.place(x=0, y=120)` geeft de (x,y) coördinaat van de knop aan
* Iedere knop moet op een andere plaats komen
* Je hoeft nog geen codes te koppelen aan de knoppen. Dus `["command"]`mag je nog even weglaten

Test nu je code en kijk of het er goed uit ziet!&#x20;

**3) Maak ook een invoerveld, een uitvoerveld en een okknop**

We hebben ook weer in- en uitvoer nodig. Een tekstbox om een woord te laten zien en een invoer om in te typen. Voeg die ook toe aan je programma, zodat het er zo uit ziet:

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

**4) Open je bestand en laat de woorden één voor één zien**

Zoek nu jouw code van voor de vakantie op. Als het goed is had jij in je code al een functie `selecteren()` staan. Lees die code nu eens goed door en kijk of je nog weet wat alles doet.

In de functie `selecteren()` opende je een bestand en printte je de woorden daaruit één voor één.

Dat stukje gaan we nu in jouw UI programma zetten, zo:

* Maak een nieuwe functie `selecteren()`
* Koppel die aan de selecteerknop. Weet je niet meer hoe het moet? Kijk bij je code van vorige week.
* Open het csv-bestand en zet iedere woord op het uitvoerveld. In jouw code was dat een `print()`, die moet je dus gaan veranderen.

Probeer je code nu weer uit.

**5) Even pauzeren!**

Als het goed is, doet je code het nu maar... alle woorden komen heel snel achter elkaar! Je ziet dus alleen het laatste woord. Wil je zeker weten dat dat zo is? Zet dan eens een deze codes nadat je het uitvoerveld hebt aangepast:

```python
  root.update()
  time.sleep(1)
```

Dan komende de woorden wel een voor een.

We moeten dus wachten tot de gebruiker op een knop heeft kunnen klikken voor het volgende woord erbij komt! Daar is een tkinter een trucje voor met een variabele, dat gaat zo:

```python
 okknop.wait_variable(okknop_ingedrukt)



okknop_ingedrukt = IntVar()

okknop["command"] = lambda: okknop_ingedrukt.set(1)
```
