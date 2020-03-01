# Bonus 6: meerdere verhaallijnen

Deze bonus bestaat uit drie losse delen. In ieder deel gaan we gebruiken wat je in bonus-3, bonus-4 of bonus-5 hebt gemaakt. Het verhaal zal nu iedere keer dat iemand het leest héél anders gaan verlopen: je gaat *meerdere verhaallijnen* programmeren!

****




# Bonus 6a: gevalideerde input gebruiken

In bonus-5 valideerde we de input van de lezer met behulp van een lijst. Nu gaan we ervoor zorgen dat die input ook effect heeft!

## Voorkennis

* Bonus 5: input valideren
* Les 6: `if`, `else`

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

Als het niet de eerste keuze is, dan moeten we controleren of de tweede keuze is gekozen. Dit doe je in de `else`:

```python
if antwoord == keuzes[0]:
  print("Het was keuze 1!")
else:
  if antwoord == keuzes[1]:
    print("Het was keuze 2!")
```

En als het niet de eerste keuze is, en ook niet de tweede keuze, dan moeten we controleren of het de derde keuze is. Dit doe je in een tweede `else`:

```python
if antwoord == keuzes[0]:
  print("Het was keuze 1!")
else:
  if antwoord == keuzes[1]:
    print("Het was keuze 2!")
  else:
    if antwoord == keuzes[2]:
      print("Het was keuze 3!")
```

Merk op dat iedere volgende `if` een grotere inspringing nodig heeft. Je code gaat dus steeds schuiner lopen. Dat werkt... maar het kan veel netter! Als je een `if` in de `else` wilt zetten, zoals we hierboven deden, kun je dit combineren tot één commando: `elif`. Dat is tegelijkertijd `else` en `if`:

```python
if antwoord == keuzes[0]:
  print("Het was keuze 1!")
elif antwoord == keuzes[1]:
  print("Het was keuze 2!")
elif antwoord == keuzes[2]:
  print("Het was keuze 3!")
```

Als je meer dan drie keuzes hebt, dan kun je dit eenvoudig uitbreiden door steeds de laatste twee regels te kopiëren en daaronder te plakken, en 1 bij de index van de lijst op te tellen.



## Opdracht bonus-6a-1\) Drie verhaallijnen

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



## Opdracht bonus-6a-2\) Drie verhaallijnen

Deze opdracht wordt afgetekend als:

* Je een verhaal hebt over een dier die zijn natuurlijke vijand tegen komt.
* De lezer drie keuzes krijgt.
* Het verhaal pas verder gaat wanneer de lezer een mogelijke keuze invoert.
* Voor iedere keuze een _ander_ verhaal van minstens twee zinnen vertelt wordt.

### Opdracht.

Ga verder met je code uit de vorige opdracht. Schrijf voor iedere keuze die de lezer in jouw verhaal heeft een verhaal van minstens twee zinnen.

****













&nbsp;

&nbsp;

&nbsp;

****

# Bonus 6b: een kans dat iets gebeurt

TODO schrijven

```python
import random


# Dobbelsteen:

worp = random.randint(1,6)
print(worp)

if worp < 3:
  print("Dit bericht heeft slechts een 2/6 kans!")
  print("Want je moet 1 of 2 gooien met de dobbelsteen.")


# Algemene kans:

kans = random.random()*100
print(kans)

if kans < 20:
  print('Je ziet dit bericht met een 20% kans!')
  print('Dat is dus gemiddeld maar 1 op de 5 keer dat je de code uitvoert!')

```


****













&nbsp;

&nbsp;

&nbsp;

****

# Bonus 6c: willekeurige dingen, willekeurige verhalen

TODO schrijven

van twee bonus terug hebben we ook een samengesteld item met 2 lijsten gemaakt: 'vriendelijke' 'aap' hier kunnen we ook op terugkoppelen in een opdracht: 'laat iets anders gebeuren afh. van bijv. naamwoord'.



