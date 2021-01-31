# Les 5b

#### 1\) Printen bij een 'collision' \(botsing\)

Deze opdracht wordt afgetekend als:

* Er "hap hap" geprint wordt als het dier het eten aanraakt.

**Uitleg**

Straks moet je dier natuurlijk groter worden als het eten pakt! Maar we beginnen met een makkelijkere versie, we gaan eerst alleen printen als het dier voedsel pakt.

Gebruik de _'collision detection'_ code om te kijken of het dier zijn voedsel aanraakt. De code werkt zo:

```python
if schildpad_rechthoek.colliderect(sla_rechthoek):
   print('hap hap')
```

Maar dan natuurlijk met jouw dier en jouw variabelen!

#### 2\) Groeien bij een 'collision'

Deze opdracht wordt afgetekend als:

* Je dier groeit als het zijn eten aanraakt.

**Uitleg**

Verlaag de variabele `honger` in de code van opdracht 1. Als het goed is gaat het dier nu vanzelf groeien!

#### 3\) Voedsel verspringen bij een 'collision'

Deze opdracht wordt afgetekend als:

* Het voedsel naar een andere plek gaat als het dier het heeft opgegeten.

**Uitleg**

Vorige les heb je het voedsel al laten verspringen. Die code ga je nu gebruiken om het voedsel ook te laten verspringen als het wordt opgegeten. Lees je code van vorige week goed en zet het springen op je juiste plek.



