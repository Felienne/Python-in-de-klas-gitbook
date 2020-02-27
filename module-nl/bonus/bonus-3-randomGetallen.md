# Bonus 3: willekeurige getallen

Nu is jouw verhaal iedere keer hetzelfde... Zou het niet leuker zijn als er iedere keer iets anders zou gebeuren? Dan wordt het voor de lezer leuk om jouw verhaal meerdere keren te lezen! Awesome!

## Voorkennis

* Bonus 2: `import` library, en vertraging
* Les 3: variabelen

## Leerdoelen

Aan het einde van deze bonus kun jij:

* Willekeurige getallen maken en gebruiken in jouw verhaal.
* Iedere keer dat jouw verhaal gelezen wordt, ervoor zorgen dat het verhaal net ietsje anders is.

****




## De 'random' library

In de vorige bonus hebben we de 'time' library geïmporteerd in ons programma. Herinner je: 'library' is Engels voor 'bibliotheek'. Door een library te importeren, kunnen we nieuwe stukjes code gebruiken in ons Python programma.

Vandaag hebben we de 'random' library nodig. Random is Engels voor willekeurig. Met random-opdrachten kun je Python steeds iets anders laten doen.

Deze library importeer je door **helemaal bovenaan je code** dit stukje code te gebruiken:

```python
import random
```


## Willekeurige gehele getallen

Een willekeurig geheel getal tussen 2 en 10 kun je maken met `random.randint(2,10)`.
`randint` is de afkorting van de twee Engelse woorden 'random integer'. Dit betekent 'willekeurig geheel getal'. Een '_geheel getal_' is een getal zonder decimalen achter de komma, zoals bijvoorbeeld '2', '5', '73', of '707'.

### Nu jij: probeer het!

Probeer dit stukje code maar eens uit (vergeet `import random` niet):

```python
aantal = random.randint(2,10)
print('Aantal:', aantal)
```

Probeer het volgende nu zelf:
- Voer het programma een paar keer uit. Wat zie je gebeuren?
- Kun je de getallen '2' en '10' ook krijgen?



## Opdracht bonus-3-1\) Een verhaal met een willekeurig getal

Deze opdracht wordt afgetekend als:

* Je bovenaan je code hebt geschreven `import random`.
* Je onderstaande tekst print, met een willekeurig geheel getal tussen 2 en 5.
* Je in je schrift in eigen woorden schrijft hoe deze code werkt.

### Opdracht.

Schrijf een code die print:
```
De aap heeft honger.
Hij kan wel 4 banen op!
```
Gebruik hierbij _een willekeurig geheel getal_ tussen 2 en 5.


## Opdracht bonus-3-2\) Een dobbelsteen gooien

Deze opdracht wordt afgetekend als:

* Je bovenaan je code hebt geschreven `import random`.
* Je onderstaande tekst print, met een willekeurige uitkomst voor de dobbelsteen worp.
* Je in je schrift in eigen woorden schrijft hoe deze code werkt.

### Opdracht.

Schrijf een code die print:
```
Je gooit een dobbelsteen op.
De dobbelsteen rolt...
En het wordt een...
5
```
Gebruik een willekeurig getal voor de uitkomst van de dobbelsteenworp.

## Opdracht bonus-3-3\) Een dobbelsteen _spannend_ gooien

Deze opdracht wordt afgetekend als:

* Je tussen de vier regels van de vorige opdracht een vertraging in hebt gebouwd.
* Je in je schrift in eigen woorden schrijft hoe deze code werkt.

### Opdracht.

In bonus-2 heb je geleerd hoe je vertraging kunt programmeren. Programmeer nu vertraging in jouw dobbelsteen verhaal van de vorige opdracht, tussen alle zinnen. Daarmee wordt de uitkomst van de dobbelsteenworp veel spannender!!!

****

## Willekeurige kommagetallen

Soms wil je een kommagetal gebruiken. Dit kan ook met Python als je `random.uniform(2.5,4.5)` gebruikt. In dit voorbeeld krijg je een willekeurig kommagetal tussen 2,5 en 4,5. **Let op: gebruik _een punt_ in plaats van een komma in Python code!**

```python
aantal = random.uniform(2.5,4.5)
print(aantal)
```

### Nu jij: probeer het!

Probeer het volgende nu zelf:
- Voer het programma een paar keer uit. Wat zie je gebeuren?
- Lukt het je om precies 2.5 of precies 4.5 te krijgen? Waarom wel/niet?


### Afronden

Je krijgt nu wel heel erg veel getallen achter de komma te zien... Bijvoorbeeld: `3.7882344812977244`. Met `round` kunnen we dit afronden. 'round' is Engels voor 'afronden'.

Om af te ronden op bijvoorbeeld 2 getallen achter de komma, oftewel op 2 _decimalen_, schrijven we:
```python
print(round(3.7882344812977244,2))
```


### Nu jij: probeer het!

Probeer dit eens zelf!
- Kun je het getal nu ook afronden op 5 getallen achter de komma?
- En op geen getallen achter de komma?


### Een afgerond willekeurig kommagetal

Om in één keer een afgerond getal te krijgen, kun je de `random.uniform` in de `round` plaatsen:

```python
aantal = round(random.uniform(1,10),1)
print(aantal)
```


## Opdracht bonus-3-4\) Python cijfers laten uitdelen

Deze opdracht wordt afgetekend als:

* Je bovenaan je code hebt geschreven `import random`
* Je onderstaande tekst print.
* Je een willekeurig kommagetal tussen 1.0 en 10.0 afgerond op één decimaal gebruikt.
* Je in je schrift in eigen woorden schrijft hoe deze code werkt.

### Opdracht.

Schrijf een code die jouw docent automatisch een willekeurig cijfer geeft:
```
Mijn docent krijgt een 7.3 van mij.
```
Gebruik hierbij _een willekeurig kommagetal getal_ tussen 1.0 en 10.0, afgerond op één getal achter de komma.

## Opdracht bonus-3-5\) Python _spannend_ cijfers laten uitdelen

Deze opdracht wordt afgetekend als:

* Je tussen de twee regels van de vorige opdracht een vertraging in hebt gebouwd.
* Je in je schrift in eigen woorden schrijft hoe deze code werkt.

### Opdracht.

Pas je code van de vorige vraag aan, zodat dit geprint wordt:
```
Mijn docent krijgt van mij een...
7.3
```
Bouw een vertraging in tussen de twee zinnen, zodat het voor de lezer _spannender_ wordt wat het cijfer zal zijn!

