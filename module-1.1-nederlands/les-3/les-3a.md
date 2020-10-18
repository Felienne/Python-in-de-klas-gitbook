# Les 3a

## Variabelen

Aan het einde van de les kun jij:

* tekst opslaan in een variabele
* een variabele gebruiken om een tekst meerdere keren te printen
* voorspellen wat een code doet met een variabele erin
* goede en foute print\(\)-codes vinden met een variabele erin

### **Even opfrissen!**

**Begin op een nieuwe pagina en zet erboven: Les 3a**

1\) Hieronder staan vijf codes met commentaar erin. Wat printen deze codes uit?

Schrijf de uitvoer in je schrift.

```python
1. #print('Goedemorgen')               
   print('Klas', '1c')
```

```python
2. #goedemorgen, dit is een Pythonprogramma

   #print('Hallo', 'kinderen!')
```

```python
3. print('Hallo', 'allemaal') #je kunt twee woorden printen
   print('Ik', 'ben', 'Python!') #maar ook drie
```

```python
4. print('Goedemorgen')  #een woord           
   #print('klas 1c') #twee woorden met een spatie ertussen
```

```python
5. print('Hallo')               
   print('klas', '1c')
   #print('hebben', 'jullie', 'er', 'zin', 'in?')
```

2\) Wat is de fout?

Al deze codes zijn fout. Wat is er mis?

Schrijf in je schrift wat de fout is.

```python
1. prnt('Hallo', 'allemaal')
```

```python
2. print('Hallo') print('Allemaal')
```

```python
3. print('Hallo' , allemaal')
```

```python
4. print('Hallo' 'allemaal')
```

```python
5. print 'Hallo Allemaal'
```

```python
6. prit('Hallo')
   prit('Allemaal')
```

Einde werkblad! Ben je klaar, leg dan je schrift bovenaan op je tafel.

### **Waardes zoeken**

1\) In Python kun je woorden zonder aanhalingstekens gebruiken. Dat zijn variabeles. Als Python een variabele tegenkomt gaat hij omhoog zoeken in het programma naar de _definitie_ van de variabele. Dat betekent waar de variabele wordt ingesteld met een is-teken:

```python
naam = 'Felienne'
```

Schrijf deze codes over. Zet een pijltje tussen het gebruik van een variabele en zijn definitie.

![De variabele klas en een pijltje naar de definitie ervan](../../.gitbook/assets/image-20190206124246541.png)

```python
1. les = 'Coderen'
   print('Welkom', 'bij', les)
```

```python
2. klas = '1c'
   print('Hallo', klas)
```

```python
3. les = 'Coderen'
   klas = '1c'
   print('Hallo' , klas, 'dit', 'is', les)
```

2\) Hieronder staan codes met een variabele erin. Wat print Python uit als we deze codes uitvoeren?

Schrijf de uitvoer in je schrift.

**Let op!** Een van de codes is fout. Schijf daarbij op: FOUT.

```python
1. print('Hallo', 'allemaal')
```

```python
2. klas = '1c'
   print('Hallo', klas)
```

```python
3. achternaam = 'Hermans'
   print('Hallo', 'mevrouw', achternaam)
```

```python
4. print('Hallo', )
```

```python
5. klas = 'klas 1c'
   print('Hallo' 'leerlingen', 'van', klas)
```

Einde werkblad! Ben je klaar, leg dan je schrift bovenaan op je tafel.

### **Naam niet gedefinieerd**

Is de code goed of fout? Kijk goed of de variabele die gebruikt wordt wel gedefinieerd is.

* Als de code fout is, schijf je Fout
* Als de code goed is, schrijf je op wat er geprint wordt.

Voorbeeld 1\)

```python
naam = 'Felienne'
print(voornaam)
```

Deze code is fout, want `voornaam` bestaat niet. Dan schrijf je:

Fout

Voorbeeld 2\)

```python
klas = '1c'
print('Hallo', klas)
```

Deze code is goed, klas is nu '1c'. Dan schrijf je:

Hallo 1c

Nu jij!

```python
1. klas = '1c'
   print('Hallo', naam)
```

```python
2. klas = '1c'
   print('Hallo', '1c')
```

```python
3. achternaam = 'Hermans'
   print('Hallo', 'mevrouw', Hermans)
```

```python
4. tijd_op_klok = 'half 9'
   print('Het', 'is', tijd_op_klok)
```

```python
5. klas = 'klas 1c'
   print('Hallo', 'leerlingen', 'van', klas)
```

```python
6. print(Goedemorgen)

```

```python
7. tijd = 'half 9'
   print('Het', 'is', 'tijd')
```

```python
8. print('Goedemorgen')

```

