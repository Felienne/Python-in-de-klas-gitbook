# Bonus: willekeurige dingen

Nu is jouw verhaal iedere keer hetzelfde... Zou het niet leuker zijn als er iedere keer iets anders zou gebeuren? Dan wordt het voor de lezer leuk om jouw verhaal meerdere keren te lezen! Awesome!

## Voorkennis

* Les 4: lijsten

## Leerdoelen

Aan het einde van deze bonus kun jij:

* Willekeurige dingen uit een lijst halen.
* Iedere keer dat jouw verhaal gelezen wordt, ervoor zorgen dat het verhaal net ietsje anders is.

## De 'random' library

In de vorige bonus hebben we de 'time' library geïmporteerd in ons programma. Herinner je: 'library' is Engels voor 'bibliotheek'. Door een library te importeren, kunnen we nieuwe stukjes code gebruiken in ons Python programma.

Vandaag hebben we de 'random' library nodig. Random is Engels voor willekeurig. Met random-opdrachten kun je Python steeds iets anders laten doen.

Deze library importeer je door **helemaal bovenaan je code** dit stukje code te gebruiken:

```python
import random
```

## A) Willekeurige dingen









## B) Willekeurige getallen

We kunnen de library 'random' gebruiken om de computer willekeurige getallen te laten kiezen.

### Gehele getallen

Een willekeurig geheel getal tussen 2 en 10 kun je maken met `random.randint(2,10)`. `randint` is de afkorting van het Engelse 'random integer', wat betekent 'willekeurig geheel getal'. Probeer dit stukje code maar eens uit:

```python
aantal = random.randint(2,10)
print(aantal)
```

Probeer het volgende nu zelf:
- Voer het programma een paar keer uit. Wat zie je gebeuren?
- Kun je de getallen '2' en '10' ook krijgen?

### Opdracht 1

Nu jij!
- Schrijf een code die print:
```
De aap heeft honger.
Hij kan wel 4 banen op!
```
- Gebruik hierbij _een willekeurig geheel getal_ tussen 2 en 5.

Nu kan jij een willekeurig geheel getal in jouw code gebruiken!

### Komma getallen

Soms wil je een kommagetal gebruiken. Dit kan ook met Python als je `random.uniform(2.5,4.5)` gebruikt. In dit voorbeeld krijg je een willekeurig kommagetal tussen 2,5 en 4,5. **Let op: gebruik _een punt_ in plaats van een komma in Python code!**

```python
aantal = random.uniform(2.5,4.5)
print(aantal)
```

Probeer het volgende nu zelf:
- Voer het programma een paar keer uit. Wat zie je gebeuren?
- Lukt het je om 2.5 en 4.5 te krijgen? Waarom wel/niet?

Je krijgt nu wel heel erg veel getallen achter de komma te zien... Bijvoorbeeld: `3.7882344812977244`. Met `round` kunnen we dit afronden. 'round' is Engels voor 'afronden'.

Om af te ronden op bijvoorbeeld 2 getallen achter de komma, schrijven we:
```python
print(round(3.7882344812977244,2))
```

- Probeer dat eens zelf!
- Kun je het getal nu ook afronden op 5 getallen achter de komma?
- En op geen getallen achter de komma?

Om in één keer een afgerond getal te krijgen, kun je de `random.uniform` in de `round` plaatsen:

```python
aantal = round(random.uniform(1,10),1)
print(aantal)
```

### Opdracht 2

Nu jij!
- Schrijf een code die jouw docent automatisch een willekeurig cijfer geeft:
```
De docent krijgt een 5.3 van mij.
```
- Gebruik hierbij _een willekeurig kommagetal getal_ tussen 1.0 en 10.0, afgerond op één getal achter de komma.

## Willekeurige dingen

Voordat 


TODO: opdracht over:

import random
random.shuffle(lijst)

en over meerdere lijsten combineren om een samengesteld resultaat te krijgen: 'boze' 'aap'.



TODO: opdracht over:

hele lijst in één keer printen
lijst mooier weergeven door hem te unpacken en een separator te definiëren

```python
lst = ['foo', 'bar', 'spam', 'egg']
print(*lst, sep='\n')
```
