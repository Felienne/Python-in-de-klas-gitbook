# Les 3b

#### 2**\) Laat je dier bewegen**

Deze opdracht wordt afgetekend als:

* Jouw dier over het scherm beweegt
* Je hiervoor time.sleep\(\) gebruikt.

**Uitleg**

Nu ga je je dier laten bewegen. Daarvoor gaan we 3 stappen zetten.

1\) Maak een variabele snelheid op regel 11, dat is boven de regel met `while True`:

Snelheid is een lijst met daarin 2 getallen zoals je hebt gezien in de slides. Zet de twee getallen op 1 en 0. Let op! Het zijn getallen, dus we gebruiken geen aanhalingstekens.

2\) Helemaal onderaan je code zet je nu deze regel: `muis_rechthoek = muis_rechthoek.move(snelheid)`

Let op! Deze regel staat in de lus van `while True`, dus die moet beginnen met 4 spaties.

3\) Onder de nieuwe regel zet je `time.sleep(0.1)` Dat zorgt ervoor dat het programma even wacht met bewegen. Anders gaat de muis veel te snel vooruit. Ook deze regel moet beginnen met 4 spaties.

**Tip: het is niet erg als je dier na een tijdje uit beeld verdwijnt! Dat lossen we later nog wel op.**

#### 

