# Les 3b

**1) Open je bestand en laat de woorden één voor één zien**

Zoek nu jouw code van voor de vakantie op. Als het goed is had jij in je code al een functie `selecteren()` staan. Lees die code nu eens goed door en kijk of je nog weet wat alles doet.

In de functie `selecteren()` opende je een bestand en printte je de woorden daaruit één voor één.

{% hint style="info" %}
Heb je het bestand niet meer? [Download het dan hier](https://www.dropbox.com/s/vtez5spovavxrs7/words.csv?dl=0)
{% endhint %}

We gaan nu een stukje van het selecteren in jouw UI programma zetten, zo:

* Maak een nieuwe functie `selecteren()`
* Koppel die aan de selecteerknop. Weet je niet meer hoe het moet? Kijk bij je code van vorige week.
* Open het csv-bestand en zet iedere woord op het uitvoerveld. In jouw code was dat een `print()`, die moet je dus gaan veranderen.

Probeer je code nu weer uit.

**2) Even pauzeren!**

Als het goed is, doet je code het nu maar... alle woorden komen heel snel achter elkaar! Je ziet dus alleen het laatste woord. Zo ziet dat er waarschijnlijk uit (maar jij zou ook een ander woord kunnen hebben als je een andere versie van de woordenlijst gebruikt)

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

Wil je zeker weten dat inderdaad alle woorden langskomen? Zet dan eens een deze codes nadat je het uitvoerveld hebt aangepast:

```python
  root.update()
  time.sleep(1)
```

Dan komende de woorden wel één voor één.

We moeten dus wachten tot de gebruiker op een knop heeft kunnen klikken voor het volgende woord erbij komt! Daar is een tkinter een trucje voor met een variabele, dat gaat als volgt.

Zet bovenaan je code deze regels, die maken speciale tkinter variabeles aan die je kan gebruiken om te kijken of de ja of nee knop al is ingedrukt.

```python
ja_of_nee_knop_is_ingedrukt = IntVar() 
knop_gekozen = StringVar()

def ja_knop_ingedrukt():
  ja_of_nee_knop_is_ingedrukt.set(1)
  knop_gekozen.set("ja")
  
def nee_knop_ingedrukt():
  ja_of_nee_knop_is_ingedrukt.set(1)
  knop_gekozen.set("nee")
```

Nu moet je deze functie ingedrukt toevoegen als commando van de ja en de nee knop. Weet je nog hoe je een functie op een knop zet?&#x20;

Als dat gelukt is, moet je in **de loop waarin je de woorden inleest** een wacht commando zetten. Zet deze regel nadat je het woord in het uitvoerveld hebt geprint.

```python
jaknop.wait_variable(ja_of_nee_knop_is_ingedrukt)
```

Test je code nu uit! Druk steeds op de ja of nee knop en kijk of er steeds een nieuw woord in beeld komt.

**3) Ik ken dat woord al!**

In de selecteerfase van je programma gaat de gebruiker voor ieder woord aangeven of ze het al kennen. Dat deden we in de tekstversie met het intypen van ja of nee. In tkinter gaan we nu dus iets doen met de ingedrukte ja of nee knop.

We hebben de speciale variabele `knop_gekozen`gemaakt zodat we weten welke van de twee knoppen er gebruikt is. Staat deze variabele op "ja", dan is de jaknop indrukt, en staat hij op "nee" dan natuurlijk de neeknop. Dat kun jij in de code gebruiken!&#x20;

Pas je code die je al had aan zodat het netjes reageert op de knoppen.

Zorg er ook voor dat de ja en nee waardes opgeslagen worden in je csv-bestand.
