# Les 3

## Even opfrissen!

1\)

1. `We gaan programmeren`\
   `#print('goedemorgen')` wordt niet uitgevoerd, deze code is namelijk uitgecomment. Python slaat commentaar over en print `goedemorgen`dus niet uit.
2. Hier wordt niets uitgeprint, de eerste regel is commentaar met uitleg over het programma, de tweede regel is commentaar (uitgecommente code).
3. `Hallo allemaal`\
   `Ik ben Python!`\
   De teksten '# je kunt twee woorden printen' en '#maar ook drie' worden niet uitgeprint, dit zijn comments die achter de code zijn geplaatst (een comment begint wanneer je een hekje plaatst).
4. `Hallo`\
   `leerlingen uit deze klas`\
   De onderste regel wordt niet geprint, dit is uitgecommente code.

2\)

1. `Hallo leerlingen`
2. Hier wordt niets uitgeprint, de tweede regel is commentaar (uitgecommente code) en python kan deze regel dus niet lezen.
3. `We eten stamppot`
4. `Klas` De bovenste regel wordt niet uitgeprint, dit is commentaar (uitgecommente code) en python kan deze regel dus niet lezen.
5.  `Hallo leerlingen`\
    Code zal geen foutmelding geven, maar in plaats van `'leerlingen'` moet er in de print gebruik gemaakt worden van de gedefinieerde variabele `doelgroep` die als waarde `'leerlingen'` heeft gekregen. Onderstaand is de goede manier:

    ```python
    doelgroep = 'leerlingen'
    print('Hallo', doelgroep)
    ```
6.  FOUT\
    De bovenste regel wordt niet uitgeprint, dit is commentaar (uitgecommente code) en python kan deze regel dus niet lezen. Vervolgens wordt er wel een variabele gebruikt in de code, maar deze variabele is niet gedeclareerd en daarom zal Python een NAME ERROR geven. Onderstaand is de goede manier:

    ```python
    les = 'coderen'
    print('We', 'gaan', les)
    ```
7.  FOUT\
    De gebruikte variabele `half` en `9` zijn niet gedefinieerd, en de gedefinieerde variabele `tijd` wordt niet gebruikt. Onderstaand is de juiste manier:

    ```python
    tijd = 'half 9'
    print('Het', 'is', tijd)
    ```

## Lijsten maken

1\)

```python
1. dieren = ['konijn', 'biggetje']
```

Op de stippellijn komt een komma.

```python
2. hobbies = ['dansen', 'voetballen']
```

Op de stippelijnen komen: = teken, aanhalingsteken, aanhalingsteken, aanhalingsteken, aanhalingsteken.

```python
3. kleuren = ['groen', 'geel', 'blauw']
```

Op de stippelijnen komen: = teken, rechte haak open, aanhalingsteken, aanhalingsteken, aanhalingsteken, aanhalingsteken, komma, aanhalingsteken, aanhalingsteken, rechte haak sluit.

2\)

```python
1. namen = ['Jan', 'Merel', 'Samir']
```

```python
2. vakken = ['Frans', 'Aardrijkskunde', 'Coderen']
```

```python
3. engelse_woorden = ['dog', 'cat', 'mouse']
```

## Aanwijzen in een lijst

1\) 1. `vleermuis`

1. `konijn`
2. FOUT, dieren\[3] bestaat niet: konijn = 0, biggetje = 1 en vleermuis = 2. Python begint tellen bij 0 en niet bij 1. Trucje: tel op de hoeveelste plek het element staat en trek hier 1 vanaf, dan zit je op het juiste cijfer voor het aanwijzen van het element.
3. `geel`
4. `blauw`

2\) 1. `In het bos loopt een biggetje`

1. `De deur is blauw`
2. `Ik zit op zingen`
3. `Mijn trui is roze`
4. `Samir is mijn beste vriend`
5. `Ik vind Coderen een leuk vak`

3\)

```python
1. kleuren = ['blauw', 'geel', 'groen']
   print('De', 'deur', 'is', kleuren[1])
```

```python
2. snoepjes = ['chocolade', 'zuurtjes', 'drop']
   print('Ik', 'hou', 'van', snoepjes[0])
```

## Foutjes bij aanwijzen

1\) 1. FOUT\
`dieren[3]` bestaat niet: konijn = 0, biggetje = 1 en vleermuis = 2. Python begint tellen bij 0 en niet bij 1. Trucje: tel op de hoeveelste plek het element staat en trek hier 1 vanaf, dan zit je op het juiste cijfer voor het aanwijzen van het element.

1. `konijn`
2. FOUT\
   `dieren[10]` bestaat niet: konijn = 0, biggetje = 1 en vleermuis = 2. Python begint tellen bij 0 en niet bij 1. Trucje: tel op de hoeveelste plek het element staat en trek hier 1 vanaf, dan zit je op het juiste cijfer voor het aanwijzen van het element.
3. `kleuren[1]` Door de aanhalingstekens leest Python de onderste regel als een string, en niet als een lijst. Hierdoor wordt de letterlijke tekst uitgeprint die in de print code staat. Verwijder de aanhalingstekens om `geel` uit te printen.
4. FOUT\
   Op de tweede regel staat geen cijfer tussen de rechte haken. Python zal nu een SyntaxError geven.

2\) 1. FOUT\
Er staat een spelfout in het woord `print`, de `i` mist en `hobbies[4]` bestaat niet, het laatste element is `hobbies[3]`.

1. FOUT\
   Er staan aanhalingsteken om het cijfer 1. Python zal nu een TypeError geven, dit betekent dat er een verkeerd 'type' aanwijzer gebruikt wordt tussen de blokhaken. Python verwacht een integer (dat is een cijfer) maar krijgt nu een char of string (dat is een letter of reeks van letters). De aanhalingstekens rondom 1 moeten worden verwijderd.
2. FOUT\
   De gedefineerde lijst heet `talen` en in de print wordt gebruikt gemaakt van de ongedefineerde lijst `taal`.
3. FOUT\
   Er staan ronde haken in plaats van rechte haken voor het aanwijzen van het element `snoepjes[2]`. Python zal nu een TypeError geven en zeggen dat de lijst niet oproepbaar is, omdat Python de juiste aanwijscode mist en dus niet weet waar hij moet kijken.
4. `Ik woon in de straatnamen[2]` Door de aanhalingstekens leest Python het stukje `straatnamen[2]` als een string, en niet als een lijst. Hierdoor wordt de letterlijke tekst uitgeprint die in de print code staat. Verwijder de aanhalingstekens om `Ik woon in de Coolsingel` uit te printen.
5. `Ik zit op dansen`
6. FOUT `kleuren[5]` bestaat niet: blauw = 0, geel = 1 en groen = 2, paars = 3 en roze = 4. Python begint tellen bij 0 en niet bij 1. Trucje: tel op de hoeveelste plek het element staat en trek hier 1 vanaf, dan zit je op het juiste cijfer voor het aanwijzen van het element.
7. FOUT De ronde haak open na `print` mist.
8. `Ik vind Aardrijkskunde leuk`
9. `De deur is geel`
