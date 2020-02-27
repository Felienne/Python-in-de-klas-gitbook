# Bonus 4: willekeurige dingen

Nu is jouw verhaal iedere keer hetzelfde... Zou het niet leuker zijn als er iedere keer iets anders zou gebeuren? Dan wordt het voor de lezer leuk om jouw verhaal meerdere keren te lezen! Awesome!

## Voorkennis

* Bonus 3: `import random` (alleen de eerste helft van deze bonus is voldoende voorkennis)
* Les 4: lijsten

## Leerdoelen

Aan het einde van deze bonus kun jij:

* Willekeurige dingen uit een lijst halen.
* Iedere keer dat jouw verhaal gelezen wordt, ervoor zorgen dat het verhaal net ietsje anders is.

****




## Willekeurige dingen

Met de 'random' library kunnen we willekeurige dingen laten gebeuren. Herinner je: met een 'library' breid je Python uit met nieuwe stukjes code die jij kunt gebruiken!

We kunnen een willekeurig ding uit een lijst halen. Dit gaat op dezelfde manier als met een stok kaarten. Je schudt het stok kaarten!

Het schudden van een lijst doe je met:
```python
random.shuffle(dingen)
```
'Shuffle' is Engels voor schudden. Met die code schudden we dus de lijst `dingen` door elkaar!

Vervolgens kun je de bovenste kaart pakken. Omdat het stok kaarten geschud is, is die bovenste kaart volkomen willekeurig! We pakken dus het eerste ding van onze geschudde lijst, met index nummer 0:

```python
print(dingen[0])
```

### Nu jij: probeer het!

We kunnen `random.shuffle(dingen)` nu gebruiken in een klein verhaaltje.

```python
import random
print('Hoe','ga','ik','vandaag','naar','school?')
vervoer = [ 'auto', 'fiets', 'bus' ]
random.shuffle(vervoer)
print('Ik','neem','vandaag','de',vervoer[0],'!')
```

1) Voer de code een paar keer zelf uit. Wat gebeurt er? Is het verhaal nu nog steeds altijd hetzelfde?
2) Schrijf duidelijk in je schrift wat je denkt dat alle regels precies doen.





## Opdracht bonus-4-1\) Een willekeurig dier in je verhaal

Deze opdracht wordt afgetekend als:

* Je bovenaan je code hebt geschreven `import random`
* Je een zin in je code hebt waarin steeds een ander dier verschijnt
* Je in je schrift in eigen woorden schrijft hoe deze code werkt

### Opdracht.

Open jouw code van opdracht 4b-4. Je had daar een lijst met vijf dieren erin gemaakt. Maar je krijgt nu steeds dezelfde te zien in je verhaal. Pas deze code aan zodat je steeds een ander dier in je verhaal krijgt.




****

## Meerdere willekeurige lijsten

Om nog meer variatie te krijgen in je verhaal, kun je ook **een willekeurig zelfstandig naamwoord** met **een willekeurig bijvoeglijk naamwoord** combineren. Zo kan de lezer bijvoorbeeld een 'grote auto', een 'snelle bus', een 'snelle auto', of een 'mooie fiets' krijgen. Dit is een combinatie van twee lijsten, één voor het zelfstandig naamwoord en één voor het bijvoeglijk naamwoord:

```python
voorstukje = [ 'grote', 'snelle', 'mooie' ]
vervoer = [ 'auto', 'fiets', 'bus' ]
```

Als we nu beide lijsten schudden, en beiden printen, dan hebben we een willekeurig zelfstandig naamwoord met een willekeurig bijvoeglijk naamwoord ervoor:

```python
import random
print('Hoe','ga','ik','vandaag','naar','school?')
voorstukje = [ 'grote', 'snelle', 'mooie' ]
vervoer = [ 'auto', 'fiets', 'bus' ]
random.shuffle(voorstukje)
random.shuffle(vervoer)
print('Ik','neem','vandaag','de',voorstukje[0],vervoer[0],'!')
```

### Nu jij: probeer het!

1) Voer de code een paar keer zelf uit. Wat gebeurt er? Kun je alle combinaties krijgen?
2) Schrijf duidelijk in je schrift wat je denkt dat alle regels precies doen.





## Opdracht bonus-4-2\) Nog meer mogelijkheden!

Deze opdracht wordt afgetekend als:

* Je in de lijst `voorstukje` vijf verschillende bijvoeglijk naamwoorden hebt staan.
* Je in de lijst `vervoer` vijf verschillende zelfstandig naamwoorden hebt staan.
* Je een zin in je code hebt waarin steeds een ander vervoermiddel met daarvoor een ander bijvoeglijk naamwoord verschijnt
* Je in je schrift in eigen woorden schrijft hoe deze code werkt

### Opdracht.

Breid de voorgaande code over het willekeurige vervoer uit door 5 verschillende bijvoeglijk naamwoorden en 5 verschillende zelfstandig naamwoorden in de lijsten te zetten.





## Opdracht bonus-4-3\) Een willekeurig emotioneel dier in je verhaal

Deze opdracht wordt afgetekend als:

* Je een zin in je code hebt waarin steeds een ander dier met een ander bijvoeglijk naamwoord (bijv. aardige, boze, ...) verschijnt
* Je in je schrift in eigen woorden schrijft hoe deze code werkt

### Opdracht.

Open je code met het verhaal over een willekeurig dier uit opdracht bonus-4-1.
Maak een nieuwe lijst met minstens 5 willekeurige emoties als bijvoeglijk naamwoord (boze, vrolijke, ...).
Voeg aan de zin waarin je het willekeurig dier print een willekeurige emotie voor het dier toe.

