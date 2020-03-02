# Bonus 6a: een kans dat iets gebeurt

In bonus-3 hebben we al een dobbelsteen opgegooid voor een willekeurig resultaat. We kunnen nu ook die dobbelsteen laten bepalen wat er daarna in het verhaal gebeurd!

## Voorkennis

* Bonus 3: `random.randint`
* Les 6: `if`, `else`

## Leerdoelen

Aan het einde van deze bonus kun jij:

* Gebeurtenissen met een kans laten gebeuren.
* Meerdere verhaallijnen in hetzelfde programma programmeren.

****



## Dobbelsteen opgooien

In bonus-3 schreven we een code om een dobbelsteen op te gooien:

```python
import random

print('Je gooit een dobbelsteen op...'
worp = random.randint(1,6)
print('Het is een', worp)
```

Weet je deze nog? `random.randint(1,6)` geeft een willekeurig getal tussen 1 en 6!


## Reageren op een 6

In les-6 heb je geleerd om `if` en `else` te gebruiken om twee verschillende situaties te programmeren. Dit kunnen we gebruiken om te kijken wat er gegooid is.

Als we willen kijken of er 6 gegooid is, dan gebruiken we `if worp == 6:`:

```python
if worp == 6:
  print('Wow! Het was een 6!')
else:
  print('Geen geluk. Wellicht de volgende keer?')
```

## Opdracht bonus-6a-1\) 6 gooien

Deze opdracht wordt afgetekend als:

* Je een dobbelsteen opgooit en een bericht print als het een 6 is.
* Je een ander bericht print als het niet een 6 is.
* De speler op enter moet drukken om te gooien.
* Je in je schrift in eigen woorden schrijft hoe deze code werkt.

### Opdracht.

Maak het volgende:
- Print dat we een dobbelsteen opgooien.
- Wacht tot de speler op enter drukt. (Tip: gebruik `input`.)
- Gooi de dobbelsteen.
- Geef de speler een prijs als er 6 gegooid wordt.
- Als er geen 6 wordt gegooid, zeg dat de speler pech heeft.

****



## Dobbelsteen geeft een kans

In plaats van de dobbelsteen écht te gooien en dit te laten zien aan de lezer, kunnen we ook een dobbelsteen gooien om iets met een kans te laten gebeuren.

Stel dat je een kans van 1 op 6 wilt hebben... Dat is de kans dat er een 6 wordt gegooid!

Of stel dat je een kans van 1 op 3 wilt hebben... Dat is de kans dat er een 1 of een 2 wordt gegooid! Een 1 of een 2 zijn kleiner dan een 3. Dus we kunnen kijken of de worp kleiner is dan 3: `if worp < 3:`:

```python
if worp < 3:
  print('Dit gebeurt met een kans van 1 op 3!')
else:
  print('Dit gebeurt met een kans van 2 op 3!')
```


## Opdracht bonus-6a-2\) avondeten!

Deze opdracht wordt afgetekend als:

* Je print wat we vanavond gaan eten, met onderstaande kansen.
* Je in je schrift hebt geschreven hoe deze code werkt.

### Opdracht.

Je ouders twijfelen wat ze vanavond voor jullie avondeten zullen gaan klaarmaken. Je besluit om ze te helpen door Python te laten bepalen wat jullie vanavond zullen gaan eten!

Maak een programma dat voorspelt wat de lezer vanavond zal gaan eten:
- Met een kans van 5 op 6, eten we pasta.
- Met een kans van 1 op 6, eten we patat.

****



## Algemene kans

Maar met een dobbelsteen kunnen we alleen maar kansen van 1 op 6, 2 op 6, 3 op 6, etc. maken. Wat nu als we een kans van 1 op 4 zouden willen hebben? Oftewel, 25% kans?

Als we met procenten willen werken, kunnen we beter een getal tussen 0 en 100 maken. Dit kan het makkelijkste met:
```python
kans = random.random()*100
```
Dit maakt eerst een willekeurig getal tussen 0 en 1 (`random.random()`). Daarna doen we x100 om de getallen tussen 0 en 100 te maken.

Een kans van 25% is dan:
```python
if kans < 25: # 25% kans
  print('Dit gebeurt met een 25% kans.')
else: # 75% kans
  print('Dit is de overige kans van 75%.')
```

## Meer dan twee situaties

Met `if` en `else` programmeer je twee situaties. Maar je kunt ook meer dan twee situaties programmeren!

Als je in de `else` weer een `if` plaatst, ga je al van 2 naar 3 situaties. Hier heeft Python een handig commando voor: `elif`. Dat is een `else` en een `if` in één!

```python
if kans < 25: # 25% kans
  print('Dit gebeurt met een 25% kans.')
elif kans < 60: # 35% kans
  print('Deze kans is 35%, omdat 60 - 25 = 35!')
else: # 40% kans
  print('Deze kans is 40%, omdat 100 - 60 = 40!')
```

Door een `else` in `elif` te veranderen en een nieuwe `else` toe te voegen maak je dus steeds weer een situatie erbij: drie situaties, vier, vijf, zes, of zelfs twintig situaties. Het kan allemaal!



## Opdracht bonus-6a-3\) honger!!!

Deze opdracht wordt afgetekend als:

* Je print wat we vanavond gaan eten, met onderstaande kansen.
* Je in je schrift hebt geschreven hoe deze code werkt.

### Opdracht.

In de vorige opdracht waren er maar twee keuzes... Laten we daar nu drie opties van maken, met procentuele kansen.

Maak een programma dat voorspelt wat de lezer vanavond zal gaan eten:
- Met een 10% kans, eten we pasta bolognese.
- Met een 25% kans, eten we stampot boerenkool.
- Met een 65% kans, eten we pannenkoeken.
Merk op dat de kansen altijd tot 100% optellen!

## Opdracht bonus-6a-4\) meer variatie in het menu

Deze opdracht wordt afgetekend als:

* Je print wat we vanavond gaan eten, met onderstaande kansen.
* Je in je schrift hebt geschreven hoe deze code werkt.

### Opdracht.

Variatie is goed. Lekker, en gezond. We gaan meer opties programmeren.

Maak een programma dat voorspelt wat de lezer vanavond zal gaan eten:
- Met een 10% kans, eten we pasta bolognese.
- Met een 25% kans, eten we stampot boerenkool.
- Met een 15% kans, eten we patat met een kroket.
- Met een 30% kans, eten we pannenkoeken.
- Met een 20% kans, eten we soep met brood.
Merk op dat de kansen altijd tot 100% optellen!
