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

We kunnen het bijvoeglijk naamwoord gebruiken om te veranderen wat er geprint wordt. Hiervoor lopen we weer alle opties af met `elif`, net zoals in bonus-6a. Voor de laatste optie kunnen we altijd ook gewoon `else` gebruiken.

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
