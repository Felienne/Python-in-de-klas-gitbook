# Les 2: Time

## Aftellen
```python
import time

print('3...', end='\r')
time.sleep(1)
print('2...', end='\r')
time.sleep(1)
print('1...', end='\r')
time.sleep(1)
```

`end='\r'` betekent:
* eindig (`end`) de geprinte regel met ...
* `\r` betekent 'ga terug naar het begin van de regel'
* als je dus iets nieuws print, dan overschrijf je de vorige regel die geprint was

## meer time library features

* huidige tijd opvragen
* elapsed time
* timezones

--> https://docs.python.org/3/library/time.html#functions

# Les 3: Random

Dobbelsteen 'gooien'

# Les 4: Lijsten

## Lijst printen met layout
hele lijst in één keer printen;
lijst mooier weergeven door hem te unpacken en een separator te definiëren

```python
lst = ['foo', 'bar', 'spam', 'egg']
print(*lst, sep='\n')
```

# brainstorm les 6


TODO: opdracht over: --> bonus 6a?

we hebben van de vorige bonus een lijst met opties, en een gevalideerd antwoord van de gebruiker
we willen nu een if-then-else tree maken om alle opties van die lijst af te lopen
gewoon hard-coded... `if antwoord == lijst[0]:` enzo.
dat gaat niet echt anders (zonder dynamic functies),
omdat er in elke branch van die tree een heel ander verhaal zal gaan gebeuren

van twee bonus terug hebben we ook een samengesteld item met 2 lijsten gemaakt: 'vriendelijke' 'aap'
hier kunnen we ook op terugkoppelen in een opdracht: 'laat iets anders gebeuren afh. van bijv. naamwoord'.



TODO: opdracht over: --> bonus 5b?

gebruik een functie om antwoord te valideren (prevent code duplication)



TODO: opdracht over: --> bonus 6b?

maak een aparte functie per branch om de code beter te structureren

## Kans dat iets gebeurt

We kunnen al 'dobbelsteen' opgooien. Met if-then-else kunnen we nu iets met een kans laten gebeuren.


