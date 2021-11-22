# Les 4

## Even opfrissen!

1\)

1. `Zullen we gaan voetballen morgen`
2. `Mijn beste vriend heet Jan`
3. FOUT\
   De gedefineerde lijst heet `talen` en in de print wordt gebruikt gemaakt van de ongedefineerde lijst `taal`.
4. FOUT\
   Er worden ronde haken gebruikt bij `snoepjes(2)`, dit moeten rechte haken zijn dus zo: `snoepjes[2]`.
5. `Ik woon in de straatnamen[2]`
6. `Ik zit op dansen`
7. FOUT\
   `kleuren[5]` bestaat niet: blauw = 0, geel = 1, groen = 2, paars = 3 en roze = 4. Python begint tellen bij 0 en niet bij 1. Trucje: tel op de hoeveelste plek het element staat en trek hier 1 vanaf, dan zit je op het juiste cijfer voor het aanwijzen van het element.
8. FOUT\
   `namen[3]` bestaat niet: Jan = 0, Robin = 1 en Samir = 2. Python begint tellen bij 0 en niet bij 1. Trucje: tel op de hoeveelste plek het element staat en trek hier 1 vanaf, dan zit je op het juiste cijfer voor het aanwijzen van het element.
9. FOUT\
   `vakken[4]` bestaat niet: Aardrijkskunde = 0, Nederlands = 1 en Coderen = 2. Python begint tellen bij 0 en niet bij 1. Trucje: tel op de hoeveelste plek het element staat en trek hier 1 vanaf, dan zit je op het juiste cijfer voor het aanwijzen van het element.
10. `De deur is geel`
11. `Hallo leerlingen`
12. Hier wordt niets uitgeprint, de tweede regel is commentaar (uitgecommente code) en python kan deze regel dus niet lezen. Let op: de code is niet fout, er verschijnt geen error na het uitvoeren van deze code.
13. FOUT\
    De bovenste regel wordt niet uitgeprint, dit is commentaar (uitgecommente code) en python kan deze regel dus niet lezen. Vervolgens wordt de variabele `les` gebruikt in de code, maar deze variabele is niet gedeclareerd en daarom zal Python een NAME ERROR geven.
14. `Het is vandaag woensdag` De code is niet fout, maar let op. Er wordt geen gebruikt gemaakt van de variabele `dag`!

2\)

1.  `kleuren[2]`. De volledige code is

    ```python
       kleuren = ['blauw', 'geel', 'groen']            
       print('De', 'trui', 'is', kleuren[2])
    ```
2.  `snoepjes[2]`. De volledige code is

    ```python
       snoepjes = ['chocolade', 'zuurtjes', 'drop']
       print('Ik', 'hou', 'van', snoepjes[2])
    ```
3.  `hobbies[0]`. De volledige code is

    ```python
       hobbies = ['gamen', 'voetballen', 'zingen']            
       print('Zullen', 'we', 'gaan', hobbies[0], 'morgen?')
    ```
4.  `namen[2]`. De volledige code is

    ```python
       namen = ['Jan', 'Robin', 'Samir']
       print('Mijn', 'beste', 'vriend', 'heet', namen[2])
    ```
5.  `talen[0]`. De volledige code is

    ```python
       talen = ['Python', 'JavaScript', 'HTML']
       print('De', 'beste', 'programmeertaal', 'is', talen[0] )
    ```
6.  `straatnamen[1]`. De volledige code is

    ```python
       straatnamen = ['Witte Hertstraat', 'Takstraat', 'Coolsingel']
       print('Ik', 'woon', 'in', 'de', straatnamen[1])
    ```

## Invoer

1\)

1. `Okee ik doe er melk in`\
   De invoer van de gebruiker wordt opgeslagen in de variabele `in_de_thee`. Deze wordt vervolgens in de print gebruikt.
2. `Het is tien uur`\
   De invoer van de gebruiker wordt opgeslagen in de variabele `tijd`. Deze wordt vervolgens in de print gebruikt.
3. `Hallo Jantien`\
   De invoer van de gebruiker wordt opgeslagen in de variabele `naam`. Deze wordt vervolgens in de print gebruikt.
4. `Hallo naam`\
   De invoer van de gebruiker wordt opgeslagen in de variabele `naam`, maar in de print wordt de variabele niet gebruikt maar staat `naam` tussen aanhalingstekens!

## Fouten bij invoer

1\) 1. FOUT\
Er mist een ronde haak sluiten op de eerste regel. Dit geeft een SyntaxError.

1.  FOUT  &#x20;

    De gebruikte variabele `naam` is niet gedefinieerd, en de gedefinieerde variabele `voornaam` wordt niet gebruikt. Onderstaand is de juiste manier:

```python
print('Hoe', 'heet', 'jij?')
naam = input()
print('Hallo', naam)
---
Input: Sabine
```

1. FOUT\
   De ronde haken missen achter `input`.
2. `Ja het regent`

2\) 1. De rond haak mist op de onderste regel. De juiste code moet zijn:

```python
print('Over', 'welk', 'dier', 'gaat', 'het?')
dier = input()
print('Dit', 'verhaal', 'gaat', 'over', dier)
```

1.  De variabele `dier` wordt niet gedefineerd. De juiste code moet zijn:

    ```python
    print('Over', 'welk', 'dier', 'gaat', 'het?')
    dier = input()
    print('Dit', 'verhaal', 'gaat', 'over', dier)
    ```
2.  De ronde haken missen achter `input`. De juiste code moet zijn:

    ```python
    print('Koffie', 'of', 'thee?')
    drinken = input()
    print('Je', 'wilt', 'dus', drinken)
    ```
3.  Het `=` teken mist tussen `antwoord` en `input()`. De juiste code moet zijn:

    ```python
    print('Regent', 'het?')
    antwoord input()
    print(antwoord, 'het', 'regent')
    ```
