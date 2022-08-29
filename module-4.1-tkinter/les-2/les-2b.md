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

**3) Maak ook een invoerveld en een uitvoerveld**

We hebben ook weer in- en uitvoer nodig. Een tekstbox om een woord te laten zien en een invoer om in te typen. Voeg die ook toe aan je programma, zodat het er zo uit ziet:

<img src="../../.gitbook/assets/image.png" alt="" data-size="original">

**4) Koppel de functie voor woorden selecteren**

Zoek nu jouw code van voor de vakantie op. Als het goed is had jij in je code al een functie `selecteren()` staan. Kopieer alleen die functie naar je nieuwe programma.

Koppel nu de functie aan de selecteerknop, dat doe je door `["command"]` in te stellen op selecteren (zonder aanhalingstekens!)

Probeer je code nu uit. Als het goed is krijg je deze foutmelding:

**FileNotFoundError: \[Errno 2] No such file or directory: 'words-selectie.csv'**

Dat komt omdat je je bestand nog niet hebt ingeladen. Download [dit bestand](https://replit.com/@mevrHermans/pidk-k3-m3-l7-einde#words.csv) en voeg het aan je programma toe.

Zorg nu dat het selecteren van woorden goed werkt! Daarvoor moet je soms code omzetten zoals vorige week.
