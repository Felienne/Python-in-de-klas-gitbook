# Les 4b

**Opdracht 1\) Maak een variabele antwoord**

Deze opdracht wordt afgetekend als:

* Je een variabele `antwoord` hebt gemaakt om het antwoord van een som in op te slaan. 

**Uitleg.** Je hoeft vanaf deze les de code niet meer te forken, je mag steeds aan je eigen rekenmachine doorwerken.  
  
Als eerste stap gaan we een variabele toevoegen. In plaats van het antwoord meteen te printen met `print(getal1 + getal2)` gaan we de waarde eerst in een variabele zetten.  
  
Vervang alle vier regels voor operatoren door toewijzingen, bijvoorbeeld:

`print(getal1 + getal2)`

wordt ****

`antwoord  = getal1 + getal2   
print (antwoord)`

Test je code nu uit. Als het goed is, werkt alles nog precies hetzelfde!

**Opdracht 2\) Pas je if aan**

Deze opdracht wordt afgetekend als:

* Je nog maar een keer **** `print(antwoord)` in je code hebt staan.

**Uitleg.** We hebben nu vier keer dezelfde regen in de code staan. Dat is niet zo handig, dus dat gaan we eerst netjes maken voor we verder gaan.

We gaan eerst kijken of de operator wel in het lijstjes operatoren zit. Dat doen we met de regel `if operator in operatoren:`Die if gaan we combineren met de else die we al hadden, zoals in de code hier onder. Op de \_\_\_\_ staart de code die jij al had, met 4 if's.

```python
  if operator in operatoren:
    _____
  else:
    print('deze operator ken ik niet!')
```

Nu mag je de regel print\(antwoord\) bij alle vier de regels weghalen en alleen op het einde printen, zoals in deze code. Op de streepjes staan dan de andere drie operatoren, zonder `print(antwoord)`

```python
  if operator in operatoren:
    if operator == '+':
      antwoord = getal1 + getal2
    ____
      
    print (antwoord)
  else:
    print('deze operator ken ik niet!')
```

{% hint style="info" %}
Test je code nu weer goed, met een kloppende som en een foute som! Bijv:   
3 + 5 -&gt; dat wordt natuurlijk 8  
hallo dit is een som -&gt; dat moet een nette foutmelding geven
{% endhint %}

**Opdracht 3\) Zet het antwoord in de lijst**

Deze opdracht wordt afgetekend als:

* Je het antwoord op de som in de lijst hebt gezet.

**Uitleg.** We gaan nu het antwoord in de lijst zetten op de plek van de som. Dat gaat zo:

We zetten eerst deze code onder `print(antwoord)`

```php
som_onderdelen = [str(antwoord)] + som_onderdelen
print(som_onderdelen)
```

Deze code pakt antwoord, maakt er een lijst van en plakt 'm vooraan. We printen de lijst even zodat je goed ziet wat er in zit, bijv bij de som 1+ 4, wordt dit de lijst:  
  
\['5', '1', '+', '4'\]  
  
De 5 ziet er nu netjes in zoals je ziet. Maar... de 1, de plus en de 4 die mogen eruit. Want die som hebben we al opgelost. Dat gaan we zo doen:

```python
som_onderdelen.pop(1)
som_onderdelen.pop(1)
som_onderdelen.pop(1)
print(som_onderdelen)
```

Ken je `pop()`nog van de geschiedenisquiz? Die haalt een element uit de lijst op een bepaalde plek. Wij halen plekje 1, drie keer weg. Dus dat betekent dat plekken 1 \(de tweede plek\), 2 en 3 worden weggehaald.

We printen de lijst weer zodat je ziet wat er gebeurt.  
  
Er is nog een stapje nodig, omdat we nu de lijst printen. Bij 1 + 6 krijgen we dit: \['7'\]. Dat is niet zo mooi. Verander de laatste regel dus in het printen van alleen het eerste element van `som_onderdelen`. Je weet vast hoe dat moet!

**Opdracht 4\) Voeg een while lus toe**

Deze opdracht wordt afgetekend als:

* Je een while lus aan je code hebt toegevoegd 

**Uitleg.** Nu we een sommetje van drie elementen kunnen vervangen door het antwoord, kunnen we dat steeds herhalen! Het gaat bijvoorbeeld zo:

De som is: 1 + 2 + 3 + 8  
In de lijst krijgen we dan \['1', '+', '2', '+', '3', '+', '8'\]  
We rekenen nu het eerste stukje som uit. Dat is 1 + 2, dat wordt natuurlijk 3.   
Dan zetten we '3' op de plaats in de lijst van '1' en '+' en '2'. Zo: \['3', '+', '3', '+', '8'\]  
Dat kunnen we weer herhalen.  
Dus nu is de lijst: \['3', '+', 3, '+', '8'\]  
We rekenen nu het eerste stukje som uit. Dat is 3 + 3, dat wordt natuurlijk 6.  
Dan zetten we 6 op de plaats in de lijst van '3' en '+' en '3'. Zo: \['6', '+', '8'\]  
Het laatste stukje som gaat ook hetzelfde, 6 en 8 worden vervangen door 14.

Dat herhalen gaan we in de code doen met een while-lus. Die ken je natuurlijk wel van andere opdrachten. We gaan de lus herhalen zolang de lijst nog meer dan 3 elementen heeft. Weet jij nog hoe dat geschreven moet worden?  
  
Zet al jouw code vanaf de regel `getal_1 = som_onderdelen[0]`in de while lus.

Test je code weer goed!

**Opdracht 5\) Stop op tijd \(Extra\)**

Heb je ook geprobeerd om een verkeerde som in de voeren? Bijv x + y? Dat wordt niks! Je code vertelt wel dat het geen geldige getallen zijn, maar hij houdt er nooit meer mee op. Dat kun je oplossen door onder `print('Je voerde geen geldige getallen in!')`een nieuwe code te zetten: `break`. Dat zorgt ervoor dat de lus gestopt wordt. 

Dat foutje zit nog op een andere plek in de code. Weet jij waar?

**Opdracht 6\) Nog betere foutmeldingen \(Extra\)**

We krijgen nu een mooie foutmelding als we geen getallen invoeren of een gekke operator. Maar als je alleen tekst invoert, gebeurt er niets. Probeer bijv. maar eens **hallo** in te voeren. Weet jij hoe dat komt? En kan jij zorgen dat er in zo'n geval ook een goede foutmelding komt? Bijv: dit is geen som.



