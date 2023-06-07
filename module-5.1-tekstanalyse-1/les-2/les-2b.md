# Les 2b

**Opdracht 1: Vertaal de lijst naar een dictionary**\
\
Vorige les ben je geëindigd met een lijst, bijv deze voor Lion:

`'Lion': ['and', 'and', 'and', 'and', 'beat', 'and', 'and', 'had', 'looked', 'said', 'replied', 'growled', 'she', 'as', 'twice', 'Do', 'and', 'and'],`

Dat maakt het lastig om het volgende woord te vinden. Je moet dan alle woorden steeds tellen en kijken welke het vaakste voor komt, en die voorspellen.

Wat makkelijk is, is een dictionary met aantallen, bijv **and** komt in 8 keer. **Do** komt één keer voor. Dus, we willen een uitvoer zoals deze:\
\
`'Lion': [('and', 8), ('Do', 1), ...]`\
\
Dan kunnen we makkelijk tellen welk woord het meest waarschijnlijk is. Zet je code om zodat er een dictionary van dictionaries uitkomt ipv een dictionary van lijsten.&#x20;

Volg deze stappen (de code staat hier onder)

* Begin met een woord uit je lijst. Ik neem `Lion` als voorbeeld maar jij kan ook een ander voorbeeld kiezen.
* Verander de lijst in een dictionary met `count`&#x20;
* Sorteer de lijst

```python
volgende_woord_opzoeker[woord] = {x: volgende_woorden.count(x) for x in volgende_woorden}
volgende_woord_opzoeker[woord] = sorted(volgende_woord_opzoeker[woord].items(), key=lambda x: -x[1])
```



**Opdracht 2: Voorspellen maar!**

We kunnen nu voor het woord Lion een voorspelling doen, zo:

```python
eerste_woord = 'Lion'
volgende_woord = volgende_woord_opzoeker[eerste_woord][0][0]
```

Volgende woord wordt nu **and**!

\
**Opdracht 3: En dan nu voor alle woorden**

We hebben nu alleen voor een woord voorspeld, maar we gaan nu de hele lijst van dictionaries doorlopen en dan kunnen we voor ieder woord voorspellen.

* Lees nu de hele lijst van dictionaries door, dat kan met\
  `woord, volgende_woorden in volgende_woord_opzoeker.items():`

Probeer nu eens wat teksten te voorspellen.

**Opdracht 4: delen**

We hebben nu alle geteld. Maar de tekst die nu uit het algoritme komt klinkt nog niet zo mooi. Dat komt omdat het helemaal niet random is! Daar gaan we nu aan werken.

Maar we willen straks kansen, dus een dictionary met kansen, bijv **and** komt in 8 keer voor uit 18, dus dat is 55 procent. **Do** komt één keer uit de 18 voor dus dat is ongeveer 6 procent. Dus, we willen een uitvoer zoals deze:\
\
`'Lion': [('and', 0.47), ('Do', 0.06), ...]`\
\
