## Les 5 werkblad a

### input

Aan het einde van de les kun jij:

-  invoer gebruiken in je programma met `input()`
-  je verhaal een ander verloop geven op basis van invoer met een if-else commando

**Even opfrissen!**

**Begin op een nieuwe pagina en zet erboven: Les 5a**

**Goed of fout?**

1) Is de code goed of fout?

* De code is goed -> schrijf wat de code print
* De code is fout -> schrijf FOUT
* Extra: schrijf ook **wat** er fout is

```python
1. hobbies = ['dansen', 'voetballen', 'zingen']            
   print('Zullen', 'we', 'gaan', hobbies[1], 'morgen')
```
```python
2. namen = ['Jan', 'Robin', 'Samir']
   print('Mijn', 'beste', 'vriend', 'heet', namen[0])
```
```python
3. talen = ['Python', 'JavaScript', 'HTML']
   print('De', 'beste', 'programmeertaal', 'is', taal[1])
```
```python
4. snoepjes = ['chocolade', 'zuurtjes', 'drop']
   print('Ik', 'hou', 'van', snoepjes(2))
```
```python
5. straatnamen = ['Witte Hertstraat', 'Takstraat', 'Coolsingel']
   print('Ik', 'woon', 'in', 'de', 'straatnamen[2]')
```

```python
6. hobbies = ['dansen', 'voetballen', 'zingen']            
   print('Ik', 'zit', 'op', hobbies[0])
```

```python
7. kleuren = ['blauw', 'geel', 'groen', 'paars', 'roze']            
   print('Mijn', 'trui', 'is', kleuren[5])
```
```python
8. namen = ['Jan', 'Robin', 'Samir']
   print(namen[3], 'is', 'mijn', 'beste', 'vriend')
```

```python
9. vakken = ['Aardrijkskunde', 'Nederlands', 'Coderen']
   print('Ik', 'vind', vakken[4], 'leuk')
```

```python
10.kleuren = ['blauw', 'geel', 'groen']            
   print('De', 'deur', 'is', kleuren[1])
```

```python
11.doelgroep = 'leerlingen'
   print('Hallo', doelgroep)
```

```python
12.naam = 'Jansen'
   #print('Hallo', 'meneer', naam)
```
```python
13. #klas = c              
   print('Leerlingen', 'uit', klas)
```
```python
14.dag = 'woensdag'
   print('Het', 'is', 'vandaag', 'woensdag')
```
 <div style="page-break-after: always;"></div>
2) Maak de code af

Je krijgt een zin, en jij moet de code afmaken. Je hoeft alleen de lijst en de aanwijzer in je schrift te schrijven. Voorbeeld:

Er moet geprint worden: 'Ik vind geel mooi' Maak de code af in je schrift. 

```python
   kleuren = ['blauw', 'geel', 'groen']            
   print('Ik', 'vind', kleuren[...], 'mooi')
```
Dan schijf jij in je schrift: kleuren[1]
Nu jij!

1. Er moet geprint worden: 'De trui is groen' Maak de code af in je schrift. 

```python
   kleuren = ['blauw', 'geel', 'groen']            
   print('De', 'trui', 'is', kleuren[...])
```

2. Er moet geprint worden: 'Ik hou van drop' 

```python
   snoepjes = ['chocolade', 'zuurtjes', 'drop']
   print('Ik', 'hou', 'van', snoepjes[...])
```

3. Er moet geprint worden: 'Zullen we gaan gamen morgen?'

```python
   hobbies = ['gamen', 'voetballen', 'zingen']            
   print('Zullen', 'we', 'gaan', hobbies[...], 'morgen?')
```

4. Er moet geprint worden: 'Mijn beste vriend heet Samir'

```python
   namen = ['Jan', 'Robin', 'Samir']
   print('Mijn', 'beste', 'vriend', 'heet', namen[...])
```

5. Er moet geprint worden: 'De beste programmeertaal is Python'

```python
   talen = ['Python', 'JavaScript', 'HTML']
   print('De', 'beste', 'programmeertaal', 'is', talen[...] )
```

6. Er moet geprint worden: 'Ik woon in de Takstraat'

```python
   straatnamen = ['Witte Hertstraat', 'Takstraat', 'Coolsingel']
   print('Ik', 'woon', 'in', 'de', straatnamen[...])
```

------

Einde werkblad! Ben je klaar, leg dan je schrift bovenaan op je tafel.

Als je klaar bent mag je aan het Extra Opgaves blad gaan werken.

 <div style="page-break-after: always;"></div>
**Invoer**

1) Je krijgt een aantal codes, én de invoer van een gebruiker. 

Voorbeeld:

```python
   print('Koffie', 'of', 'thee?')
   drinken = input()
   print('Je', 'wilt', 'dus', drinken)
   ---
   Input: koffie
```

De invoer is: koffie (kijk bij Input)
De code print: Je wilt dus koffie.

Nu jij!

```python
1. print('Suiker', 'of', 'melk?')
   in_de_thee = input()
   print('Okee', 'ik', 'doe', 'er', in_de_thee, 'in')
   ---
   Input: melk
```

```python
2. print('Hoe', 'laat', 'is', 'het?')
   tijd = input()
   print('Het', 'is', tijd)
   ---
   Input: tien uur
```

```python
3. print('Hoe', 'heet', 'jij?')
   naam = input()
   print('Hallo', naam)
   ---
   Input: Jantien
```

```python
4. print('Hoe', 'heet', 'jij?')
   naam = input()
   print('Hallo', 'naam')
   ---
   Input: Achmed
```

**Fouten bij input**

1) Wat print deze code?
Is de code fout -> schrijf FOUT
Is de code goed -> schrijf wat de code print

```python
1. print('Hoe', 'heet', 'jij?'
   naam = input()
   print('Hallo', 'naam')
   ---
   Input: Achmed
```

```python
2. print('Hoe', 'heet', 'jij?')
   voornaam = input()
   print('Hallo', naam)
   ---
   Input: Sabine
```

```python
3. print('Koffie', 'of', 'thee?')
   drinken = input
   print('Je', 'wilt', 'dus', drinken)
   ---
   Input: thee
```

```python
4. print('Regent', 'het?')
   antwoord = input()
   print(antwoord, 'het', 'regent')
   ---
   Input: Ja
```

2) Fouten

Al deze codes zijn fout. Wat is er mis?

```python
1. print('Over', 'welk', 'dier', 'gaat', 'het?')
   dier = input()
   print('Dit', 'verhaal', 'gaat', 'over', dier
```
```python
2. print('Over', 'welk', 'dier', 'gaat', 'het?')
   input()
   print('Dit', 'verhaal', 'gaat', 'over', dier)
```
```python
3. print('Koffie', 'of', 'thee?')
   drinken = input
   print('Je', 'wilt', 'dus', drinken)
```

```python
4. print('Regent', 'het?')
   antwoord input()
   print(antwoord, 'het', 'regent')
```




