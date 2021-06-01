# Les 5b

**Opdracht 1\) Zoek de keer in een lijst**

Deze opdracht wordt afgetekend als:

* Je de positie van de eerste keer kan printen

**Uitleg.** We gaan in de lijst kijken of er een \* in zit. Dat doen we met een `index()`. Index vertelt op welke plek een bepaald element in een lijst zit. Wij gaan 'm zo gebruiken: `som_onderdelen.index('*')`

Zoek de positie op met deze code en sla die op een in een variable. Die variabele noemen we `index_keer`. We doen het zoeken nu alleen nog eventjes naar de keer, de gedeeld door die komt later!

Print de variabele uit en kijk of het klopt. 

{% hint style="info" %}
Denk eraan dat de lijst altijd op 0 begint, dus als er staat dat een \* op plek 1 staat, dan staat die op de tweede plek!
{% endhint %}

**Opdracht 2\) Is er wel een keer?**

Deze opdracht wordt afgetekend als:

* Je de positie van de eerste keer kan printen**, als deze in de lijst zit**
* Je de som gewoon uitrekent als er geen keer in de lijst zit 

**Uitleg.** Heb je al eens geprobeerd de code uit te voeren als er geen keer in de som zit? Zo niet, probeer dat nu eens. Bijv. 5 + 3. Dan krijg je dit:

![](../../.gitbook/assets/image%20%2810%29.png)

Omdat er geen \* in de som zit, komt er een foutmelding. Dat gaan we nu oplossen. We mogen `index()` alleen gebruiken als we weten dat er een keer in de lijst zit. Dat kunnen we testen met de code `in`. Dat gaat zo:

```python
if '*' in som_onderdelen:
    index_keer = som_onderdelen.index('*')
    print(index_keer)
```

**Opdracht 3\) De getallen ophalen**

Deze opdracht wordt afgetekend als:

* Je het getal vóór en na de keer ophaalt
* Je die getallen gaat gebruiken in je som, als er een keer in de som zit
* Je, als er geen keer in de som zit, gewoon de eerste twee getallen gebruikt

**Uitleg.** Er kunnen nu twee situaties aan de hand zijn:

* Of er zit een keer in de som, en dan willen we die keer pakken en de getallen voor en na de keer. 
* Of er zit geen keer in de som, en dan willen we gewoon de eerste twee getallen en de eerste operator \(zoals we het eerst deden\)

Maak jij deze code af?

```python
  if '*' in som_onderdelen:
    #vind de eerste plek van een keer
    index_keer = som_onderdelen.index('*')

    #haal de getallen voor en na de keer op
    getal_1 = __  <- zet hier som_onderdelen op de plek voor de keer 
    operator = __ <- zet hier som_onderdelen op de plek van de keer 
    getal_2 = __  <- zet hier som_onderdelen op de plek na de keer 
  else:
    #haal de eerste drie elementen uit de lijst, zoals we al deden
    getal_1 = som_onderdelen[0]
    operator = som_onderdelen[1]
    getal_2 = som_onderdelen[2]
```

\*\*\*\*

