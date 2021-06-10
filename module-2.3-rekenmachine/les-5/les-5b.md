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

We gaan daarvoor een nieuwe variabele `begin` maken. Die begint op 0 als er geen keer is, en op de plek voor de keer als er wel een keer is.

Maak jij deze code af?

```python
  #zoek naar de eerste * in de lijst:
  if '*' in som_onderdelen:
    index_keer = som_onderdelen.index('*')
    #is er een keer? Dan beginnen we daar!
    begin = index_keer-1
  else:
    #geen keer? We beginnen aan het begin
    begin = 0

  getal_1 = __  <- zet hier som_onderdelen op de plek van begin
  operator = __  <- zet hier som_onderdelen op de plek van begin + 1
  getal_2 = __  <- zet hier som_onderdelen op de plek van begin + 2

  __ #hier komt de rest van jouw code
```

Test je code nu uit. Werkt het al goed?

**Opdracht 4\) De goede getallen weghalen!**

Deze opdracht wordt afgetekend als:

* Je **de goede getallen uit de lijst haalt**
* Je daardoor iedere som met \* en - en + netjes uitrekent

De code werkt niet goed. Dat komt omdat we nu nog altijd de eerste drie dingen uit de lijst halen, en niet de getallen en operator die we net gedaan hebben. Dat werkt natuurlijk niet goed.

We hadden deze codes:

```python
      som_onderdelen.pop(0)
      som_onderdelen.pop(0)
      som_onderdelen.pop(0)
      som_onderdelen.insert(0, str(antwoord))
```

Maar in plaats van weghalen en invoegen bij 0 willen we dat nu natuurlijk bij `begin` doen. Dat is of 0 of de plek van de keer. Past jij de code aan?

{% hint style="info" %}
Kijk goed of al deze sommen het doen:

* 5 + 4 \* 10 -&gt; 45
* 2 + 2 + 2  -&gt; 6
* 2 + 2 \* 2  -&gt; ook 6
{% endhint %}

**Opdracht 5\) Ook de gedeeld door heeft voorrang \(extra\)**

Deze opdracht wordt afgetekend als:

* Je ook sommen met een / kan uitrekenen. Gedeeld door komt ook voor + en -

**Uitleg.** Ook delen gaat voor plus en min. Kun jij zorgen dat dat ook werkt in je rekenmachine? Dat is een pittige klus, maar wel heel leuk als het lukt. Weet je al hoe je dat gaat doen? Ga er dan maar voor! 

