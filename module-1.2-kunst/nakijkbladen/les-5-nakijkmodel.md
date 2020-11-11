# Les 5

## Even opfrissen!

1\) 1. Deze code print 3 keer Hallo en Allemaal en daaronder 1 keer Goedemorgen.

1. Deze code tekent een vierkant.
2. Deze code tekent twee vierkanten tegen elkaar aan, waarbij het tweede vierkant half zo groot is als het eerste.
3. Deze code tekent een zeshoek.
4. Deze code tekent een zeshoek \(kleiner dan die bij opdracht 4\).
5. Deze code print 2 keer Goedemorgen 1c.
6. Deze code tekent een driehoek.
7. Deze code print 3 keer Hallo 1c.

2\) 1. Deze code tekent een vierkant.

1. Fout: 'aantal\_hoeken' is niet gedefinieerd.
2. Deze code tekent vier zijden van een zeshoek.
3. Deze code tekent een vijfhoek.
4. Fout: de indentatie \(spatie\) mist in regel 4 en 5.
5. Deze code tekent twee evengrote driehoeken tegen elkaar aan.
6. Fout: 'klas' is niet gedefinieerd als een aantal en kan dus niet in het 'range'commando verwerkt woden.

## Kleuren tekenen

1\) 1. Rood 2. Groen 3. Geel 4. blauw 5. Roze/Paars 6. Donkerrood 7. Donkerblauw 8. Mosterdgeel/groen 9. Donkergroen 10. Paars

2\) 1. ![](../../.gitbook/assets/vierkant%20blauw%20lijn.PNG)

1. ![](../../.gitbook/assets/halve%20zeshoek%20rood%20lijn.PNG)
2. ![](../../.gitbook/assets/driehoek%20blauw%20lijn.PNG)
3. ![](../../.gitbook/assets/vierkant%20zwart%20driehoek%20groen%20lijn.PNG)
4. Deze code tekent een vierkant met wit.

3\) 1.

```python
1. pen.color(1,0,0)
2. antal_keer = 4
3. for i in range(aantal_keer):
4.   pen.forward(100)
5.   pen.left(90)
```

1. \`\`\`python
2. pen.color\(1,0,0\)
3. aantal\_keer = 4
4. hoek = 90
5. for i in range\(aantal\_keer\):
6. pen.forward\(100\)
7. pen.left\(hoek\)
8. pen.color\(0.5,0,0\)
9. aantal\_keer = 3
10. hoek = 120
11. for i in range\(aantal\_keer\):
12. pen.forward\(100\)
13. pen.left\(hoek\)

    \`\`\`

14. \`\`\`python
15. pen.color\(0,0,1\)
16. aantal\_keer = 4
17. hoek = 90
18. for i in range\(aantal\_keer\):
19. pen.forward\(100\)
20. pen.left\(hoek\)
21. pen.up\(\)
22. pen.forward\(200\)
23. pen.down\(\)
24. pen.color\(1,0,0\)
25. aantal\_keer = 6
26. hoek = 60
27. for i in range\(aantal\_keer\):
28. pen.forward\(100\)
29. pen.left\(hoek\)

    \`\`\`

## Figuren vullen

1\) 1. ![](../../.gitbook/assets/oranje%20vierkant%20gevuld.PNG)

1. ![](../../.gitbook/assets/zeshoek%20rood%20lijn.PNG)
2. ![](../../.gitbook/assets/halve%20zeshoek%20blauw%20gevuld.PNG)
3. ![](../../.gitbook/assets/driehoek%20turqoise%20lijn.PNG)

2\) 1.

```text
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

![](../../.gitbook/assets/logoCSCert_10cm.jpg)

