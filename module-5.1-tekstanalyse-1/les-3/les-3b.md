# Les 3b

**Opdracht 1: Kies af een toe eens een ander woord**\
\
Vorige les heb je voorspeld maar die voorspelling werkte niet zo heel goed. Je moet niet altijd het eerste woord kiezen, maar af en toe een ander woord. Kies bijvoorbeeld in 80% van de gevallen het eerste woord, maar in 20% van de gevallen een willekeurig woord uit de lijst. Programmeer dat zelf.

We noemen dit de temperatuur van de voorspelling, in GPT is het ook ongeveer 80%.

**(extra)** Je kan ook sommige woorden overslaan, bijv woorden die maar 1x voorkomen, of woorden met minder dan 5% kans.&#x20;

**Opdracht 2: Een functie voor voorspellen**\
\
We gaan nu met de computer tellen of de voorspellingen wel kloppen. Volg deze stappen om je code in orde te krijgen:

1. Maak een functie, en noem die `voorspel_woord(woord)`
2. Zet de code die je gebruikt om een volgende woord te voorspellen in deze functie. Dat is dus code die op basis van één woord een volgende woord kiest.\
   Die functie heeft als parameter een woord, en return ook een woord. \
   Vergeet dus niet  `return woord` in je code te gebruiken!
3. Test de code met de hand een paar keer, bijv weer op het woordje **Lion**. Komt er het goede woord uit? Probeer nog meer willekeurige woorden!

**Opdracht 3: Soms vindt de functie... niks?**

Soms krijg je een foutje, een `KeyError`bijvoorbeeld bij het woord **brainless** kan dat gebeuren. Probeer maar eens! Denk eens na hoe dat zou kunnen komen?

Het komt omdat het woord wel als tweede woord voorkomt maar niet als eerste woord. We moeten het dus een klein beetje anders programmeren. In plaats van:

`opties = volgende_woord_opzoeker[woord]`

&#x20;moeten we een nieuwe code gebruiken, `get`.

Dat doen we zo:

```python
opties = volgende_woord_opzoeker.get(woord, None)
if opties is None:
    return None #er zijn geen opties, we hebben geen suggestie
```

`get(woord)` is precies hetzelfde als `[woord]`, maar je kan als tweede argument aan Python vertellen wat er terug gegeven moet worden als er niks gevonden is. Doe je dat zoals hierboven, dan krijg je `None` terug als er niks gevonden is, in plaats van een fout.

**Opdracht 4: Splitsen maar**

Nu gaan we de data splitsen:

* Maak een variabele aan die `verdeling` heet, en zet die op 0.9.
* Maak een tweede variabele die aangeeft to waar we inlezen, rond de waarde af, anders wordt het geen integer en krijg je een fout:\
  `grens = round(len(lines)*verdeling)`
* Met de variabele grens gaan we de data splitsen.&#x20;
*   In de lus die je al hebt, ga je nu niet alle dat inlezen, maar maar een stuk: het wordt nu `lines[0:grens]`, van 0 tot grens



Nu gaan we een tweede lus toevoegen waarin je over de data loopt. Die lus gaat van grens tot het einde, zo: `lines[grens:]` In de lus gaan we nu de rest van de lijst lines inlezen.&#x20;

We kijken dan steeds bij een woord of het volgende woord goed voorspeld wordt. Maak de code af op de streepjes. Zet er eerst in woorden bij wat er moet gebeuren, en dan pas code. \
\
Tip: Je hebt 3 nieuwe variabele nodig om goed, fout en niks voorspeld te tellen.

```python
for line in lines[grens:]:
    for i in range(0, len(line)-1):
        # line is a list of words
        woord = line[i]
        ingelezen_woord = line[i+1]

        voorspelde_woord = voorspel_volgende_woord(woord)
        
        if voorspelde_woord == None:
             ___
        elif voorspelde_woord == ingelezen_woord:
             ___
        else:
             ___ 
```

Print op het einde van je code de waardes uit. Het wordt ongeveer dit:

```
Goed voorspeld 957
Fout voorspeld 6631
Niks voorspeld 357
```

Het kan zijn dat jouw getallen een beetje anders zijn, maar het zou wel ongeveer hetzelfde moeten zijn met temperatuur 80 en splitsing 90.

**Opdracht 5: Delen (extra)**

Als je deze uitvoer hebt, maak het dan wat mooier door door het totaal aantal voorspellingen te delen (goed plus fout plus niks), dan krijg je het aantal keer dat het goed of fout is in percentages uitgedrukt. Dat geeft straks een handiger overzicht. Je krijgt dan ongeveer dit:

```
Percentage goed 12.05
Percentage fout 83.46
Percentage niks 4.49
```













