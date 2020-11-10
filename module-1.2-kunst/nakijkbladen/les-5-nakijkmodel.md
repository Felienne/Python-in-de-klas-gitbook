# Les 5a nakijkmodel

## Even opfrissen!

1\)
1. Deze code print 3 keer Hallo en Allemaal en daaronder 1 keer Goedemorgen.

2. Deze code tekent een vierkant.

3. Deze code tekent twee vierkanten tegen elkaar aan, waarbij het tweede vierkant half zo groot is als het eerste.

4. Deze code tekent een zeshoek.

5. Deze code tekent een zeshoek (kleiner dan die bij opdracht 4).

6. Deze code print 2 keer Goedemorgen 1c.

7. Deze code tekent een driehoek.

8. Deze code print 3 keer Hallo 1c.

2\)
1. Deze code tekent een vierkant.

2. Fout: 'aantal_hoeken' is niet gedefinieerd.

3. Deze code tekent vier zijden van een zeshoek.

4. Deze code tekent een vijfhoek. 

5. Fout: de indentatie (spatie) mist in regel 4 en 5.

6. Deze code tekent twee evengrote driehoeken tegen elkaar aan.

7. Fout: 'klas' is niet gedefinieerd als een aantal en kan dus niet in het 'range'commando verwerkt woden.

## Kleuren tekenen

1\)
1. Rood
2. Groen
3. Geel
4. blauw
5. Roze/Paars
6. Donkerrood
7. Donkerblauw
8. Mosterdgeel/groen
9. Donkergroen
10. Paars

2\)
1. <img src="../../img/vierkant blauw lijn.PNG">

2. <img src="../../img/halve zeshoek rood lijn.PNG">

3. <img src="../../img/driehoek blauw lijn.PNG">

4. <img src="../../img/vierkant zwart driehoek groen lijn.PNG">

5. Deze code tekent een vierkant met wit. 

3\)
1.
```python
1. pen.color(1,0,0)
2. antal_keer = 4
3. for i in range(aantal_keer):
4.   pen.forward(100)
5.   pen.left(90)
```

2. 
```python
1. pen.color(1,0,0)
2. aantal_keer = 4
3. hoek = 90
4. for i in range(aantal_keer):
5.   pen.forward(100)
6.   pen.left(hoek)

7. pen.color(0.5,0,0)
8. aantal_keer = 3
9. hoek = 120
10. for i in range(aantal_keer):
11.   pen.forward(100)
12.   pen.left(hoek)
```

3. 
```python
1. pen.color(0,0,1)
2. aantal_keer = 4
3. hoek = 90
4. for i in range(aantal_keer):
5.   pen.forward(100)
6.   pen.left(hoek)

7. pen.up()
8. pen.forward(200)
9. pen.down()

10. pen.color(1,0,0)
11. aantal_keer = 6
12. hoek = 60
13. for i in range(aantal_keer):
14.   pen.forward(100)
15.   pen.left(hoek)
```

## Figuren vullen

1\)
1. <img src="../../img/oranje vierkant gevuld.PNG">

2. <img src="../../img/zeshoek rood lijn.PNG">

3. <img src="../../img/halve zeshoek blauw gevuld.PNG">

4. <img src="../../img/driehoek turqoise lijn.PNG">

2\)
1.
```pyton
1. pen.color(0,1,0)
2. pen.begin_fill()
3. aantal_keer = 4
4. hoek = 90
5. for i in range(aantal_keer):
6.   pen.forward(100)
7.   pen.left(hoek) 
8. pen.end_fill()     
```

2.
```python
1. pen.color(1,1,0)
2. pen.begin_fill()
3. aantal_keer = 3
4. hoek = 120
5. for i in range(aantal_keer):
6.   pen.forward(100)
7.   pen.left(hoek) 
8. pen.end_fill()     
```

3.
```python
1. pen.color(1,0,1)
2. pen.begin_fill()
3. aantal_keer = 2
4. hoek = 90
5. for i in range(aantal_keer):
6.   pen.forward(100)
7.   pen.left(hoek) 
8. pen.end_fill()    
```

<img src="../../img/logoCSCert_10cm.jpg" align="right">
