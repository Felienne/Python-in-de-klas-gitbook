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
