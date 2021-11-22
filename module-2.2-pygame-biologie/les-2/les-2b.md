# Les 3b

**1) Verander de 'hongersnelheid'**

Deze opdracht wordt afgetekend als:

* Je `honger = honger + 1` verandert in `honger = honger + 0.1`

**Uitleg**. Als je dier je hard krimpt, dan zie je niet meer goed dat het dier beweegt. Daarom laten we de honger nu wat langzamer verlopen.

#### 2**) Laat je dier bewegen**

Deze opdracht wordt afgetekend als:

* Jouw dier over het scherm beweegt

**Uitleg. **Nu ga je je dier laten bewegen. Daarvoor gaan we twee stappen zetten.

1\) Maak een variabele snelheid, buiten de lus, dus boven de regel met `while dier_leeft`

Snelheid is een lijst met daarin twee getallen zoals je hebt gezien in de slides. Zet de twee getallen op 1 en 0.&#x20;

{% hint style="info" %}
Let op! Het zijn getallen, dus we gebruiken geen aanhalingstekens.
{% endhint %}

2\)  Onderaan in de lus je code zet je nu deze regel: `schildpad_rechthoek = schildpad_rechthoek.move(snelheid)`

Let op! Deze regel staat in de lus van `while`, dus die moet beginnen met spaties.

**Het is niet erg als je dier na een tijdje uit beeld verdwijnt! Dat lossen we op in opdracht 3.**

#### **3) Laat je dier rechts stuiteren**

Deze opdracht wordt afgetekend als:

* De dier aan de rechterkant omdraait&#x20;

**Uitleg.** Zorg dat de muis niet meer uit beeld verdwijnt, maar aan de **rechterkant** van het veld omdraait. In de les heb je deze code gezien:

```python
    if schildpad_rechthoek.bottom > 800:
        # draai om
        print("de muis draait om!")
        snelheid[0] = -snelheid[0]
```

Voeg deze code aan je eigen programma toe in de `while:`

#### **4) Laat je dier ook links stuiteren**

Deze opdracht wordt afgetekend als:

* De dier ook aan de linkerkant omdraait&#x20;

**Uitleg. **Zorg nu dat het dier ook aan de linkerkant omdraait. Welke waarde zou je daarvoor moeten gebruiken? Denk goed na, of probeer het uit. Je kunt de code van de rechterkant kopieren en aanpassen.

{% hint style="info" %}
verander de > in een < voor de linkerkant
{% endhint %}

#### 5) Stuiter door het veld (extra)

Deze opdracht wordt afgetekend als:

* Het dier schuin beweegt
* Het dier allebei aan alle vier de randen stuitert

**Uitleg.** Het dier stuitert nu allebei maar een richting op, maar ze kunnen ook schuin door het veld. Maak de snelheid dan bijv. \[1,2] en \[2,1].

Nu stuiteren ze niet helemaal goed want het dier loopt nu boven of ander het veld uit. Kan jij dat repareren?

#### 6) Begin op een willekeurige plek (extra)

Deze opdracht wordt afgetekend als:

* Het dier niet linksboven maar op een willekeurige plek begint

**Uitleg.** Het plaatje begint standaard links bovenin, maar dat kun je ook aanpassen. Denk aan deze vragen om je te helpen:

* Welke waardes moet je denk je aanpassen om de plaats in te stellen?
* Weet je nog hoe je een willekeurige waarde kiest?&#x20;
