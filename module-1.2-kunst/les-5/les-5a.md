# Les 5a

## Kleuren

Aan het einde van de les kun jij:

* Hoe je kleuren in je tekening kunt gebruiken met namen
* Hoe je kleuren in je tekening kunt gebruiken met RGB codes
* Hoe je vlakken in je tekening kunt vullen met kleur

### Even opfrissen

1\) Wat doen deze codes? Leg het in je eigen woorden uit.

Voorbeeld!

```python
hoek = 60
for i in range(6):
  pen.forward(50)
  pen.left(hoek)

hoek = 90
for i in range(4):
  pen.forward(50)
  pen.left(hoek)
```

Jouw antwoord: "Deze code tekent een zeshoek, en daarna op dezelfde plek een vierkant."

Nu jij!

```python
1.
namen = 3
for i in range(namen):
  print('Hallo')
  print('Allemaal')
print('Goedemorgen')
```

```python
2.
aantal_keer = 4
for i in range(aantal_keer):
  pen.forward(100)
  pen.left(90)
```

```python
3.
grootte = 100
for i in range(4):
  pen.forward(grootte)
  pen.left(90)

pen.penup()
pen.forward(grootte)
pen.pendown()

grootte = 50
for i in range(4):
  pen.forward(grootte)
  pen.left(90)
```

```python
4.
aantal_keer = 6
for i in range(aantal_keer):
  pen.forward(100)
  pen.left(60)
```

```python
5.
aantal_keer = 6
hoek = 60
for i in range(aantal_keer):
  pen.forward(50)
  pen.left(hoek)
```

```python
6.
namen = 2
groet = 'Goedemorgen'
klas = '1c'
for i in range(namen):
  print(groet, klas)
```

```python
7.
aantal_hoeken = 3
hoek = 360/aantal_hoeken
for i in range(aantal_hoeken):
  pen.forward(50)
  pen.left(hoek)
```

```python
8.
namen = 3
klas = '1c'
for i in range(namen):
  print('Hallo', klas)
```

2\) Leg ook deze codes uit. Let op: Er kunnen nu ook foutjes in de codes zitten!

```python
1.
aantal_keer = 4
for i in range(aantal_keer):
  pen.forward(100)
  pen.left(90)
```

```python
2.
aantal_keer = 4
for i in range(aantal_hoeken)
  pen.forward(100)
  pen.left(90)
```

```python
3.
aantal_keer = 6
grootte = 100
for i in range(4):
  pen.forward(100)
  pen.left(60)
```

```python
4.
aantal_keer = 5
hoek = 72
for i in range(aantal_keer):
  pen.forward(100)
  pen.left(hoek)
```

```python
5.
aantal_hoeken = 8
hoek = 360/aantal_hoeken   # / betekent gedeeld door in Python
for i in range(aantal_hoeken):
pen.forward(50)
pen.left(hoek)
```

```python
6.
hoeken = 3
for i in range(hoeken):
  pen.forward(100)
  pen.left(120)

pen.forward(100)

for i in range(hoeken):
  pen.forward(100)
  pen.left(120)
```

```python
7.
namen = 3
klas = '1c'
for i in range(klas):
  print('Hallo', klas)
```

Einde werkblad! Ben je klaar, leg dan je schrift bovenaan op je tafel.

### Kleuren tekenen

1\) Welke kleur wordt dit? Tip: de codes zijn RGB, RoodGroenBlauw. En lagere getallen zijn donkerder, niet lichter!

```python
1. pen.color(255, 0, 0)
2. pen.color(0, 255, 0)
3. pen.color(255, 255, 0)
4. pen.color(255, 0, 0)
5. pen.color(255, 0, 255)
6. pen.color(160, 0, 0)
7. pen.color(160, 0, 0)
8. pen.color(160, 160, 0)
9. pen.color(0, 160, 0)
10.pen.color(160, 0, 160)
```

2\) Wat tekenen deze codes? Gebruik kleurpotloden of stiften. Heb je die niet? Zet dan de namen van de kleuren in de tekening.

```python
1.
pen.color('blue')
aantal_keer = 4
for i in range(aantal_keer):
  pen.forward(100)
  pen.left(90)
```

```python
2.
pen.color('red')
aantal_keer = 3
hoek = 60
for i in range(aantal_keer):
  pen.forward(100)
  pen.left(hoek)
```

```python
3.
pen.color(0,0,255)
aantal_keer = 3
hoek = 120
for i in range(aantal_keer):
  pen.forward(100)
  pen.left(hoek)
```

```python
4.
pen.color('black')
aantal_keer = 4
hoek = 90
for i in range(aantal_keer):
  pen.forward(100)
  pen.left(hoek)

pen.color(0, 255, 0)
aantal_keer = 3
hoek = 120
for i in range(aantal_keer):
  pen.forward(100)
  pen.left(hoek)
```

```python
5.
pen.color(255, 255, 255)
aantal_keer = 4
hoek = 90
grootte = 100
for i in range(aantal_keer):
  pen.forward(grootte)
  pen.left(hoek)
```

3\) Schrijf de code voor deze tekeningen. Gebruik RGB codes voor de kleuren.

1\.

![](<../../.gitbook/assets/image-20190406141936243 (1).png>)

1. ![](<../../.gitbook/assets/image-20190406142059944 (1).png>)
2.

![](<../../.gitbook/assets/image-20190406142204920 (1) (1).png>)

Einde werkblad! Ben je klaar, leg dan je schrift bovenaan op je tafel.

### Figuren vullen

1\) Wat tekenen deze codes? Gebruik kleurpotloden of stiften. Heb je die niet? Zet dan de namen van de kleuren in de tekening.

```python
1. pen.color('orange')
aantal_keer = 4
hoek = 90
pen.begin_fill()    
for i in range(antal_keer):
  pen.forward(100)
  pen.left(hoek)
pen.end_fill()
```

```python
2. pen.color(255,0,0)
aantal_keer = 6
hoek = 60
for i in range(aantal_keer):
  pen.forward(100)
  pen.left(hoek)
pen.begin_fill()   
pen.end_fill()
```

```python
3. pen.color(0,0,255)
aantal_keer = 2
hoek = 60
pen.begin_fill()  
for i in range(aantal_keer):
  pen.forward(100)
  pen.left(hoek)
pen.end_fill()  
pen.begin_fill()  
for i in range(aantal_keer):
  pen.forward(100)
  pen.left(hoek)
pen.end_fill()
```

```python
4. pen.color(0,255,255)
aantal_keer = 3
hoek = 120
pen.end_fill()  
for i in range(aantal_keer):
  pen.forward(100)
  pen.left(hoek)
pen.begin_fill()
```

2\) Schrijf de code voor deze tekeningen. Gebruik RGB codes voor de kleuren.

1\. ![](../../.gitbook/assets/Kunst\_5a\_figurenvullen\_21.png)

1. ![](../../.gitbook/assets/Kunst\_5a\_figurenvullen\_22.png)
2. ![](../../.gitbook/assets/Kunst\_5a\_figurenvullen\_23.png)

Einde werkblad! Ben je klaar, leg dan je schrift bovenaan op je tafel.
