<img src="../../img/Logo cs-certificate.jpg" style="zoom:9%">

## Module Nederlands Les 4 werkblad a nakijkmodel

### Even opfrissen!

1)

1. `Hallo leerlingen` <br/>


2. Hier wordt niets uitgeprint, de tweede regel is commentaar (uitgecommente code) en python kan deze regel dus niet lezen.


3. `We eten stamppot`<br/>


4. `Klas 1c`
De bovenste regel wordt niet uitgeprint, dit is commentaar (uitgecommente code) en python kan deze regel dus niet lezen.


5. `Hallo 1c`<br/>
  Code zal geen foutmelding geven, maar in plaats van `'1c'` moet er in de print gebruik gemaakt worden van de gedefinieerde variabele `klas` die als waarde `'1c'` heeft gekregen. Onderstaand is de goede manier:

  ```python
  klas = '1c'
  print('Hallo', klas)
  ```

6. FOUT, De bovenste regel wordt niet uitgeprint, dit is commentaar (uitgecommente code) en python kan deze regel dus niet lezen. Vervolgens wordt er wel een variabele gebruikt in de code, maar deze variabele is niet gedeclareerd en daarom zal Python een NAME ERROR geven. Onderstaand is de goede manier:

  ```python
  klas = 'c'
  print('Leerlingen', 'uit', klas)
  ```

7. FOUT, De gebruikte variabele `half` en `9` zijn niet gedefinieerd, en de gedefinieerde variabele `tijd` wordt niet gebruikt. Onderstaand is de goede manier:

  ```python
  tijd = 'half 9'
  print('Het', 'is', tijd)
  ```
<div style="page-break-after: always;"></div>

### Lijsten maken

1)
```python
1. dieren = ['konijn', 'biggetje']
```
Op de stippellijn komt een komma


```python
2. hobbies = ['dansen', 'voetballen']
```
Op de stippelijnen komen: = teken, aanhalingsteken, aanhalingsteken, aanhalingsteken, aanhalingsteken

```python
3. kleuren = ['groen', 'geel', 'blauw']
```
Op de stippelijnen komen: = teken, rechte haak open, aanhalingsteken, aanhalingsteken, aanhalingsteken, aanhalingsteken, komma, aanhalingsteken, aanhalingsteken, rechte haak sluit.

2)
```python
1. namen = ['Jan', 'Merel', 'Samir']
```

```python
2. vakken = ['Frans', 'Aardrijkskunde', 'Coderen']
```

```python
3. engelse_woorden = ['dog', 'cat', 'mouse']
```

<div style="page-break-after: always;"></div>

### Aanwijzen in een lijst

1)
1. `vleermuis`

2. `konijn`

3. FOUT, dieren[3] bestaat niet: konijn = 0, biggetje = 1 en vleermuis = 2. Python begint tellen bij 0 en niet bij 1. Trucje: tel op de hoeveelste plek het element staat en trek hier 1 vanaf, dan zit je op het juiste cijfer voor het aanwijzen van het element. 

4. `geel` 

5. `blauw` 


2)
1. `In het bos loopt een biggetje`

2. `De deur is blauw`

3. `Ik zit op zingen`

4. `Mijn trui is roze`

5. `Samir is mijn beste vriend`

6. `Ik vind Coderen een leuk vak`


3)
  ```python
1. kleuren = ['blauw', 'geel', 'groen']
   print('De', 'deur', 'is', kleuren[1])
  ```

```python
2. snoepjes = ['chocolade', 'zuurtjes', 'drop']
   print('Ik', 'hou', 'van', snoepjes[0])
```
<div style="page-break-after: always;"></div>

### Foutjes bij aanwijzen

1)
1. FOUT, dieren[3] bestaat niet: konijn = 0, biggetje = 1 en vleermuis = 2. Python begint tellen bij 0 en niet bij 1. Trucje: tel op de hoeveelste plek het element staat en trek hier 1 vanaf, dan zit je op het juiste cijfer voor het aanwijzen van het element. 

2. `konijn`

3. FOUT, dieren[10] bestaat niet: konijn = 0, biggetje = 1 en vleermuis = 2. Python begint tellen bij 0 en niet bij 1. Trucje: tel op de hoeveelste plek het element staat en trek hier 1 vanaf, dan zit je op het juiste cijfer voor het aanwijzen van het element. 

4. `kleuren[1]`
Door de aanhalingstekens leest Python de onderste regel als een string, en niet als een lijst. Hierdoor wordt de letterlijke tekst uitgeprint die in de print code staat. Verwijder de aanhalingstekens om `geel` uit te printen.

5. FOUT, op de tweede regel staat geen cijfer tussen de rechte haken. Python zal nu een SyntaxError geven. 

2)
1. FOUT, er staat een spelfout in het woord print, de i mist en hobbies[4] bestaat niet, het laatste element is hobbies[3].

2. FOUT, er staan aanhalingsteken om het cijfer 1. Python zal nu een TypeError geven, dit betekent dat er een verkeerd 'type' aanwijzer gebruikt wordt tussen de blokhaken. Python verwacht een integer (dat is een cijfer) maar krijgt nu een char of string (dat is een letter of reeks van letters). De aanhalingstekens rondom 1 moeten worden verwijderd. 

3. FOUT, de ronde haak sluit aan het einde van de regel code mist. 

4. FOUT, er staan ronde haken in plaats van rechte haken voor het aanwijzen van het element namen[1]. Python zal nu een TypeError geven en zeggen dat de lijst niet oproepbaar is, omdat Python de juiste aanwijscode mist en dus niet weet waar hij moet kijken.

5. `Ik woon in de straatnamen[2]`
Door de aanhalingstekens leest Python het stukje `straatnamen[2]` als een string, en niet als een lijst. Hierdoor wordt de letterlijke tekst uitgeprint die in de print code staat. Verwijder de aanhalingstekens om `Ik woon in de Coolsingel` uit te printen. 

6. `Ik zit op dansen`

7. FOUT, kleuren[5] bestaat niet: blauw = 0, geel = 1 en groen = 2, paars = 3 en roze = 4. Python begint tellen bij 0 en niet bij 1. Trucje: tel op de hoeveelste plek het element staat en trek hier 1 vanaf, dan zit je op het juiste cijfer voor het aanwijzen van het element. 

8. FOUT, de ronde haak open na print mist.

9. `Ik vind Aardrijkskunde leuk`

10. `De deur is geel`


