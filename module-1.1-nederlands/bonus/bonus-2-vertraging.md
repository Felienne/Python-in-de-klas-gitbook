# Bonus 2: vertraging

Nu verschijnt jouw verhaal in één keer. Wellicht vind je dat prettig, maar wellicht ook niet. We kunnen ook een vertraging tussen zinnen inbouwen, zodat het verhaal zich langzaam zal ontvouwen!

## Voorkennis

* Les 2: meerdere regels printen

## Leerdoelen

Aan het einde van deze bonus kun jij:

* Een library importeren.
* Een vertraging gebruiken om je verhaal langzaam te laten verschijnen.

****



## De 'time' library

Helaas kan standaard Python geen vertraging gebruiken. Standaard Python kan eigenlijk vrij weinig...

Gelukkig is het mogelijk om héél véél méér met Python te doen door een 'library' te 'importeren'. 'Library' is Engels voor 'bibliotheek', en een bibliotheek is een plek waar je heel veel dingen kunt opzoeken. In een library kan Python stukjes code opzoeken, die jij in jouw programma kunt gebruiken!

In de 'time' library vinden we alles wat we nodig hebben wat met tijd te maken heeft. 'Time' is Engels voor 'tijd'. Deze kun je zo in jouw code importeren:

```python
import time
```

****




## Vertraging inbouwen

In de time library staat het commando 'sleep'. 'Sleep' is Engels voor 'slapen'. Daarmee doet jouw code eventjes helemaal niets, waardoor we dus een vertraging kunnen inbouwen.

Deze gebruik je in je code door eerst de naam van de library te typen (`time`), daarna een punt (`.`), en daarna het commando (`sleep`): `time.sleep`.

De punt betekent dus 'gebruik ... van ...': "*gebruik* het commando `sleep` *van* de library `time`".

Na `sleep` heb je net zoals bij `print` een rond haakje openen (`(`) en een rond haakje sluiten (`)`) nodig. Daartussen zet je hoeveel seconden je wilt wachten. Bijvoorbeeld, een vertraging van twee seconden ziet er zo uit:

```python
time.sleep(2)
```

Als je dit commando tussen twee print commando's zet, dan wacht Python na het printen van het eerste voordat hij het tweede print:

```python
import time

print('Hallo.')
time.sleep(2)
print('Doei.')
```


## Opdracht bonus-2-1\) Een vertraagde zin

Deze opdracht wordt afgetekend als:

* Je bovenaan je code hebt geschreven `import time`
* Je twee zinnen print, waarvan de tweede pas na drie seconden verschijnt
* Je in je schrift in eigen woorden schrijft hoe deze code werkt

### Opdracht.

Schrijf een verhaal van slechts twee zinnen over jouw lievelingseten. Laat de eerste zin direct verschijnen, maar de tweede zin pas na drie seconden.




****

## Meerdere vertragingen

Een verhaal van maar twee zinnen is nogal kort. Maar we kunnen eenvoudig `time.sleep(2)` meerdere keren gebruiken om zo meerdere vertraagde zinnen te printen! Bijvoorbeeld met drie zinnen:


```python
import time

print('Yo!')
time.sleep(1)
print('Hoe','gaat','het','met','jou?')
time.sleep(2)
print('Met','mij','gaat','het','goed.')
```

**Let op:** we gebruiken `import time` slechts één keer, helemaal bovenaan de code!

Ook kun je zien dat we twee verschillende wachttijden hebben gekozen: eerst 1 seconde, en daarna 2 seconden.

## Korter dan een seconde wachten

Je kunt ook korter wachten dan 1 seconde door een kommagetal in te vullen. Om bijvoorbeeld een halve seconde te wachten, programmeer je:

```python
time.sleep(0.5)
```

**Let op: gebruik een punt in plaats van een komma in Python code!** Wij Nederlanders gebruiken een komma, maar Engelsen gebruiken een punt. Python is Engelstalig, en dus moet je een punt gebruiken in een kommagetal.




## Opdracht bonus-2-2\) Een verhaal met vertragingen

Deze opdracht wordt afgetekend als:

* Je helemaal bovenaan je code hebt geschreven `import time` (en _nergens anders_ in je code!)
* Je vijf zinnen print, elke zin met vertraging er tussen
* Je in je schrift in eigen woorden schrijft hoe deze code werkt

### Opdracht.

Schrijf een verhaal van vijf zinnen over hoe jij vandaag naar school bent gekomen. Zorg dat er tussen alle zinnen een vertraging zit: een lange vertraging na lange zinnen, en een korte vertraging na een kort zinnetje.


