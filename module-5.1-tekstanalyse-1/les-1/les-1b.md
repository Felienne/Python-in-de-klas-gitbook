# Les 1b

**File inlezen en opruimen**

File inlezen en opruimen We gaan beginnen met het inlezen van een tekstfile. We lezen iedere regel van het bestand in, en hakken het op in losse woorden met `.split()`

Daarna filteren we alle interpunctie eruit, want we gaan alleen naar woorden kijken.&#x20;

```python
lines = []

overslaan = [', ', '.', ',', '']

for regel in open("alice-combined.txt").readlines():
    regel = regel.replace("\n", " ")
    
    regel_als_lijst = regel.split(' ')
    
    regel_als_lijst_gefilterd = [x for x in regel_als_lijst if not x in overslaan]
    if regel_als_lijst_gefilterd != []:
        lines.append(regel_als_lijst_gefilterd)
```

**Opdracht 1: Verder opruimen**

Print de variabele lijn uit en kijk eens wat er in zit. Zie je nog meer interpunctie? Voeg die toe aan de lijst `overslaan` zodat die niet meer meetelt.

**Opdracht 2: Turven met een lijst**

We gaan een begin maken met turven. Stap 1 is het maken van een lijst voor ieder woord, met daarin de woorden die erna kunnen komen. We bekijken even een stukje van de invoer:

```
Alice was beginning to get very tired of sitting by her sister on the
bank , and of having nothing to do  : once or twice she had peeped into
the book her sister was reading , but it had no pictures or
conversations in it , and what is the use of a book , thought Alice
without pictures or conversations ?
```

Kijk naar het woord **Alice**. Daarna kan of **was** komen of **without**. Dus, dit is wat we willen als uitvoer, in een dictionary komt bij de key Alice een lijst met was en without erin, zo:

`{'Alice' : ['was', 'without']}`

Dat doen we zo voor ieder woord. Na **was** komt **beginning** of **reading**, dan wordt de hele dictionary:\
\
`{'Alice' : ['was', 'without'],`\
`'was' : ['beginning', 'reading']}`

Na beginning komt maar een woord (namelijk **to**), maar zet ook dat woord in een lijst!

`{'Alice' : ['was', 'without'],`\
`'was' : ['beginning', 'reading'],`\
`'beginning': ['to']}`

Schrijf code dit deze lijsten maakt voor het hele bestand.

**Opdracht 3: Jullie eigen data**

We willen natuurlijk geen Alice in Wonderland uitspugen maar iets dat klinkt zoals jezelf. Ga op zoek naar de data die je kan vinden en zorg dat je die in een tekstformaat (.txt) zet. Denk aan:

* Email
* Verslagen op Google Drive
* Opdrachten op Magister
* Social media met tekst (Instagram, Twitter)

Kopieer natuurlijk niet met de hand, maar zoek naar export-opties. Veel systemen hebben zo'n optie. Laat het in losse bestanden staan, dan kan je later nog verschil maken.\
\
**Opdracht 4: Vertaal de lijst naar een dictionary (voor tijd over)**\
\
Heb je tijd over? Dan kun je je data al een beetje gaan aanpassen.

Als je je code runt op het hele bestand, krijg je voor sommige woorden lijsten met veel dezelfde dingen erin, bijv voor Lion:

`'Lion': ['and', 'and', 'and', 'and', 'beat', 'and', 'and', 'had', 'looked', 'said', 'replied', 'growled', 'she', 'as', 'twice', 'Do', 'and', 'and']`

&#x20;\
Dat maakt het lastig om het volgende woord te vinden. Wat makkelijk is, is een dictionary met kansen, bijv **and** komt in 8 keer voor uit 18, dus dat is 44 procent. **Do** komt een keer uit de 18 voor dus dat is 5.5 procent. Dus, we willen een uitvoer zoals deze:\
\
`'Lion': [('and', 0.44), ('Do', 5.5), ...]`\
\
Bedenk zelf een plan voor hoe je de data omzet. Lukt dat niet dan doen we het volgende week samen!
