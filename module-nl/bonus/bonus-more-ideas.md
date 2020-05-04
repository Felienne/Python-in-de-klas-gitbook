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

Zie ook:
* https://www.quora.com/How-can-I-delete-the-last-printed-line-in-Python-language

### Meer overschrijven

Alle tekst clearen:
* https://stackoverflow.com/questions/19596750/is-there-a-way-to-clear-your-printed-text-in-python

## meer time library features

* huidige tijd opvragen
* elapsed time
* timezones

--> https://docs.python.org/3/library/time.html#functions

# Les 3: Random

Uitbreiding voor de dobbelsteen: gooien met animatie.

```python
print(random.randint(1,6),end='\r')
time.sleep(0.1)
print(random.randint(1,6),end='\r')
time.sleep(0.1)
print(random.randint(1,6),end='\r')
time.sleep(0.1)
print(random.randint(1,6),end='\r')
time.sleep(0.1)
print(random.randint(1,6),end='\r')
time.sleep(0.2)
print(random.randint(1,6),end='\r')
time.sleep(0.2)
print(random.randint(1,6),end='\r')
time.sleep(0.2)
print(random.randint(1,6),end='\r')
time.sleep(0.25)
print(random.randint(1,6),end='\r')
time.sleep(0.25)
print(random.randint(1,6),end='\r')
time.sleep(0.3)
worp = random.randint(1,6)
print(worp)
```

# Les 4: Lijsten

## Lijst printen met layout
hele lijst in één keer printen;
lijst mooier weergeven door hem te unpacken en een separator te definiëren

```python
lst = ['foo', 'bar', 'spam', 'egg']
print(*lst, sep='\n')
```

# Les 5: input met een functie

gebruik een functie om antwoord te valideren (prevent code duplication)

# Les 6: if met functies

maak een aparte functie per branch om de code beter te structureren

# Les 6: hoofdletterongevoelig

```python
print('Hond of kat?')
antwoord = input()
if antwoord.lower() == 'hond':
  print('waf waf')
else:
  print('miauw miauw')
```
