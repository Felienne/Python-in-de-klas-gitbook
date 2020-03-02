# Bonus 6: meerdere verhaallijnen

Deze bonus bestaat uit drie losse delen. In ieder deel gaan we gebruiken wat je in bonus-3, bonus-4 of bonus-5 hebt gemaakt. Het verhaal zal nu iedere keer dat iemand het leest héél anders gaan verlopen: je gaat *meerdere verhaallijnen* programmeren!

****











&nbsp;

&nbsp;

&nbsp;

****

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

****











&nbsp;

&nbsp;

&nbsp;

****

# Bonus 6b: gevalideerde input gebruiken

In bonus-5 valideerde we de input van de lezer met behulp van een lijst. Nu gaan we ervoor zorgen dat die input ook effect heeft!

## Voorkennis

* Bonus 5: input valideren
* Les 6: `if`, `else`
* Bonus 6a: `elif`

## Leerdoelen

Aan het einde van deze bonus kun jij:

* Aan de hand van de keuze van de lezer het verhaal anders laten verlopen.
* Meerdere verhaallijnen in hetzelfde programma programmeren.

****




## Recap bonus-5

In bonus-5 hadden we een lijst gemaakt van mogelijke keuzes, genaamd `keuzes`. De lezer kon vervolgens één van die keuzes kiezen. Het programma ging pas verder wanneer de lezer één van de mogelijke antwoorden koos. Deze staat nu opgeslagen in een variabele `antwoord`:

```python
print('Vertel hier een verhaal.')

print()
keuzes = [ 'ren weg', 'wacht af', 'ga kijken' ]
antwoord=''
while antwoord not in keuzes:
  print('Wat doe je? Kies tussen:', keuzes)
  antwoord = input()
print()

print('Verhaal gaat verder.')
```


## Het antwoord bepalen

Het antwoord van de lezer staat nu opgeslagen in de variabele `antwoord`, en we weten dat het één van de opties uit de lijst `keuzes` is. Voor iedere keuze willen we een ander scenario programmeren. We kunnen `if` gebruiken om te reageren op iedere keuze. Voor de eerste keuze ziet dit er als volgt uit:

```python
if antwoord == keuzes[0]:
  print("Het was keuze 1!")
```

Net zoals in bonus-6a, kunnen we `elif` gebruiken om alle opties af te lopen:

```python
if antwoord == keuzes[0]:
  print("Het was keuze 1!")
elif antwoord == keuzes[1]:
  print("Het was keuze 2!")
elif antwoord == keuzes[2]:
  print("Het was keuze 3!")
```

Als je meer dan drie keuzes hebt, dan kun je dit eenvoudig uitbreiden door steeds de laatste twee regels te kopiëren en daaronder te plakken, en 1 bij de index van de lijst op te tellen.



## Opdracht bonus-6b-1\) Drie verhaallijnen

Deze opdracht wordt afgetekend als:

* Je een verhaal hebt over een dier die zijn natuurlijke vijand tegen komt.
* De lezer drie keuzes krijgt.
* Het verhaal pas verder gaat wanneer de lezer een mogelijke keuze invoert.
* Voor iedere keuze wordt gezegd 'Het was keuze' met het nummer daarachter.

### Opdracht.

In opdrachten bonus-5-1 t/m bonus-5-4 schreef je een verhaal over een dier die zijn natuurlijke vijand tegen kwam. Nu ben je in staat om dit verhaal verder te schrijven.

Voeg de `if` en de twee `elif` uit bovenstaand voorbeeld toe aan jouw verhaal.

(We gaan hier in de volgende opdracht weer mee verder.)

****



## Het antwoord gebruiken

We kunnen nu een totaal ander bericht printen voor iedere andere keuze. In het vorige voorbeeld waren dit de keuzes:

```python
keuzes = [ 'ren weg', 'wacht af', 'ga kijken' ]
```

We kunnen dan `print` in de keuzebepaling met de `if` en de twee `elif` herschrijven tot een klein verhaaltje:

```python
if antwoord == keuzes[0]:    # ren weg
  print('Je probeert weg te rennen!')
  print('...')
  print('Je bent ontkomen.')
  print('Niets lijkt je te volgen.')
elif antwoord == keuzes[1]:    # wacht af
  print('Je wacht af.')
  print('Er springt een aap uit de bosjes.')
  # Vertel hier een lang verhaal
  print('Je loopt weg.')
elif antwoord == keuzes[2]:    # ga kijken
  print('Je loopt ernaar toe, en gaat kijken.')
  print('Er springt een aap uit de bosjes.')
  # Vertel hier een ander lang Verhaal
  # Het verhaal is anders dan bij keuze 2,
  # omdat je nu heeeel dichtbij staat!
  print('Je loopt weg.')

print()
# Hier kun je een verder verhaal programmeren.
# Wat de lezer hierboven ook gekozen heeft,
# uiteindelijk gaat het verhaal hier gewoon verder!
```

Je ziet dat bij iedere keuze die de lezer maakt een heel ander verhaal gaat gebeuren. Uiteraard moet je nog wel even je fantasie loslaten om het verhaal af te schrijven...

Ook is even commentaar (`#`) toegevoegd achter iedere keuze. Dat maakt de code veel makkelijker om te lezen!



## Opdracht bonus-6b-2\) Drie verhaallijnen

Deze opdracht wordt afgetekend als:

* Je een verhaal hebt over een dier die zijn natuurlijke vijand tegen komt.
* De lezer drie keuzes krijgt.
* Het verhaal pas verder gaat wanneer de lezer een mogelijke keuze invoert.
* Voor iedere keuze een _ander_ verhaal van minstens twee zinnen vertelt wordt.

### Opdracht.

Ga verder met je code uit de vorige opdracht. Schrijf voor iedere keuze die de lezer in jouw verhaal heeft, een verhaal van minstens twee zinnen.

****













&nbsp;

&nbsp;

&nbsp;

****

# Bonus 6c: willekeurige dingen, willekeurige verhalen

## Voorkennis

* Bonus 4: random dingen
* Les 6: `if`, `else`
* Bonus 6a: `elif`

## Leerdoelen

Aan het einde van deze bonus kun jij:

* Willekeurige dingen de verhaallijn laten veranderen.
* Meerdere verhaallijnen in hetzelfde programma programmeren.

****



## Recap bonus-4

In bonus-4 gebruikten we lijsten om willekeurige dingen in ons verhaal te laten verschijnen. De lijst schudde we met `random.shuffle(lijstnaam)`.

We combineerden ook twee lijsten: een lijst met bijvoeglijk naamwoorden (`voorstukje`) en een lijst met zelfstandig naamwoorden (`vervoer`).

```python
import random

print('Hoe','ga','ik','vandaag','naar','school?')
voorstukjes = [ 'grote', 'snelle', 'mooie' ]
vervoer = [ 'auto', 'fiets', 'bus' ]
random.shuffle(voorstukjes)
random.shuffle(vervoer)
print('Ik','neem','vandaag','de',voorstukjes[0],vervoer[0],'!')
```

## Bijvoeglijk naamwoord gebruiken

We kunnen het bijvoeglijk naamwoord gebruiken om te veranderen wat er geprint wordt. Hiervoor lopen we weer alle opties af met `elif`, net zoals in bonus-6a. Voor de laatste optie kunnen we ook gewoon `else` gebruiken.

```python
voorstukje = voorstukjes[0] # Kies een willekeurig bijv. naamwoord
if voorstukje == 'grote': # groot
  print('Wow, die', vervoer[0], 'is echt gigantisch!')
elif voorstukje == 'snelle': # snel
  print('Daarmee zijn we snel op school!')
else: # mooi
  print('Het is niet de grootste of de snelste, maar hij is wel super mooi!!!')
```



## Opdracht bonus-6c-1\) Jouw vervoer

Deze opdracht wordt afgetekend als:

* Je vijf bijvoeglijk naamwoorden hebt waar willekeurig uit gekozen wordt, en een ander bericht print voor elk.
* Je in je schrift hebt geschreven hoe deze code werkt.

### Opdracht.

In opdracht bonus-4-2 programmeerde je vijf bijvoeglijke naamwoorden als `voorstukjes`. Print nu één heel andere zin voor ieder van die bijvoeglijke naamwoorden, net zoals in bovenstaand voorbeeld.

****

## Opdracht bonus-6c-2\) Emotionele dieren, deel 2

Deze opdracht wordt afgetekend als:

* Je vijf verschillende emoties hebt als bijvoeglijk naamwoord, waar willekeurig uit gekozen wordt.
* Je voer ieder van die emoties een klein verhaaltje hebt geprogrammeerd.
* Je in je schrift hebt geschreven hoe deze code werkt.

### Opdracht.

In opdracht bonus-4-3 programmeerde je willekeurige emoties ('boze', 'vrolijke', ...) voor willekeurige dieren. Deze werden willekeurig uit twee lijsten gekozen.

Programmeer nu voor iedere emotie een ander verhaaltje.

Bijvoorbeeld, wanneer er een 'boos' dier te voorschijn springt, dan moet je jezelf verdedigen. Of als er een 'vrolijk' dier te voorschijn springt, dan maak je van hem je huisdier.

