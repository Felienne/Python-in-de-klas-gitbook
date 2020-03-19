# Les 5a

**Even opfrissen!**

Aan het einde van de les kun jij:

* Keuzes maken in een programma met if-else
* goede en foute if-else codes herkennen

**Begin op een nieuwe pagina en zet erboven: Les 5a**

1\) Is de code goed of fout?  
Goed -&gt; Schrijf wat de code print  
Fout -&gt; Schrijf FOUT  
Extra -&gt; Schrijf ook op wat de fout it

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
   print(Hallo, naam)
   ---
   Input: Sabine
```

```python
3. print('Koffie', 'of', 'thee?')
   drinken = input()
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

```python
5. print('Over', 'welk', 'dier', 'gaat', 'het?')
   input()
   print('Dit', 'verhaal', 'gaat', 'over', dier)
   ---
   Input: hond
```

**If-else**

1\) Je krijgt een aantal codes, én de invoer van een gebruiker. Wat wordt er geprint?

Voorbeeld:

```python
   print('suiker', 'of', 'melk?')
   in_de_thee = input()
   if in_de_thee == 'melk':
     print('gieten')
   else:
     print('schudden')
   ---
   Input: melk
```

De invoer is: melk \(kijk bij Input:\) De code print: gieten. Nu jij!

```python
1. print('suiker', 'of', 'melk?')
   in_de_thee = input()
   if in_de_thee == 'melk':
     print('gieten')
   else:
     print('schudden')
   ---
   Input: suiker
```

```python
2. print('suiker', 'of', 'melk?')
   in_de_thee = input()
   if in_de_thee == 'melk':
     print('gieten')
   else:
     print('schudden')
   ---
   Input: pindakaas
```

```python
3. print('reptiel of zoogdier?')
   diersoort = input()
   if diersoort == 'reptiel':
     print('legt', 'een', 'ei')
   else:
     print('geeft', 'melk')
   ---
   Input: reptiel
```

```python
4. print('reptiel of zoogdier?')
   diersoort = input()
   if diersoort == 'reptiel':
     print('legt', 'een', 'ei')
   else:
     print('geeft', 'melk')
   ---
   Input: zeptiel
```

```python
6. print('Nederlands of Engels')
   taal = input()
   if taal == 'Engels':
     print('Hello', 'good morning!')
   else:
     print('Hallo', 'goedemorgen!')
   ---
   Input: engels
```

```python
7. print('Nederlands of Engels')
   taal = input()
   if taal == 'Engels':
     print('Hello', 'good morning!')
   else:
     print('Hallo', 'goedemorgen!')
   ---
   Input: Engels
```

```python
8. print('Nederlands of Engels')
   taal = input()
   if taal == 'Engels':
     print('Hello', 'good morning!')
   else:
     print('Hallo', 'goedemorgen!')
   ---
   Input: English
```

2\) Er zijn vijf dingen heel belangrijk bij een if-else. Schrijf er zoveel mogelijk op in je schrift.

3\) Nu maak jij de if-else zelf.

We gaan steeds de goede dierengeluiden printen. Deze horen bij elkaar:

* hond - waf
* kat - miauw
* kikker - kwak
* eend - kwek
* koe - boe
* varken - oink

1\) Wat moet er op de puntjes? Alleen dat hoef je in je schrift te schrijven.

```python
1. print('hond of kat')
   dier = input()
   if dier == 'hond':
     print(...)
   else:
     print('miauw')
```

```python
2. print('hond of kat')
   dier = input()
   if dier __ 'hond':
     print('waf')
   else:
     print('miauw')
```

```python
3. print('koe of varken')
   dier = input()
   if dier == ...:
     print('boe')
   else:
     print('oink')
```

```python
4. print('koe of kikker')
   dier = input()
   if dier == ...:
     print('boe')
   else:
     print(...)
```

Einde werkblad! Ben je klaar, leg dan je schrift bovenaan op je tafel.

**Fouten bij if-else commando's**

1\) Fout of niet? Lees de code plus invoer. Voorspel of er een fout komt, of niet.

Komt er een fout, schrijf dan in je schrift: FOUT. Komt er geen fout, schrijf dan op wat de code print.

Voorbeeld:

```python
   print('Nederlands of Frans')
   taal = input()
   if taal == 'Nederlands':
     print('Hallo')
   else:
     print('Bonjour')
   ---
   Input: Frans
```

De code…. print 'Bonjour'

Voorbeeld:

```python
   print('Nederlands of Frans')
   taal = input()
   if taal == 'Nederlands'
     print('Hallo')
   else:
     print('Bonjour')
   ---
   Input: Frans
```

De invoer is: Frans. De code…. is FOUT, want de eerste regel mist een :

Nu jij!

```python
1. print('Nederlands of Frans')
   taal = input()
   if taal == 'Nederlands':
     print('Hallo')
   else
     print('Bonjour')
   ---
   Input: Frans
```

```python
2. print('Nederlands of Frans')
   taal = input()
   if taal = 'Nederlands':
     print('Hallo')
   else
     print('Bonjour')
    ---
   Input: Nederlands
```

```python
3. print('Nederlands of Frans')
   taal == input()
   if taal = 'Nederlands':
     print('Hallo')
   else:
     print('Bonjour')
    ---
   Input: Frans
```

```python
4. print('Engelse of Frans')
   taal = input()
   if taal == 'Engels':
     print('Bonjour!')
   else:
     print('Hello!')
  ---
   Input: Engelse
```

```python
7. print('Duits', 'of', 'Nederlands')
   taal = input()
   if taal == 'Duits':
   print('Gutenabend!')
   else:
   print('Goedeavond!')
  ---
   Input: Duits
```

```python
7. print('Duits', 'of', 'Nederlands')
   taal = input()
   if taal == 'Duits':
     print('Gutenabend!')
   else:
     print('Goedeavond!')
  ---
   Input: Nederlands
```

```python
7. print('Duits', 'of', 'Nederlands')
   taal = input()
   if taal() == 'Duits':
     print('Gutenabend!')
   else:
     print('Goedeavond!')
  ---
   Input: Duits
```

2\) Foutmeldingen lezen

Je krijgt steeds een foutmelding te zien. Wat is er mis?

```python
1.  if in_de_thee == 'suiker'                                       ^

    SyntaxError: invalid syntax
```

```python
2.  print('gieten')
        ^
    IndentationError: expected an indented block
```

```python
3.  if input('melk of suiker?') = 'suiker':
                                ^
    SyntaxError: invalid syntax
```

```python
4.  if in_de_thee == 'suiker:
                                        ^
    SyntaxError: invalid syntax
```

