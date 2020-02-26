# Bonus 5: input valideren

Soms wil je dat de lezer van je verhaal keuzes kan maken, maar niet alle keuzes zijn natuurlijk mogelijk. Daarom moet jij, als de programmeer, ervoor zorgen dat de lezer alleen keuzes kan maken die van jou mogen.

## Voorkennis

* Les 4: lijsten
* Les 5: input

## Leerdoelen

Aan het einde van deze bonus kun jij:

* De lezer laten kiezen tussen een paar acties
* Controleren of de input van de lezer mogelijk is

****




## Mogelijke antwoorden opslaan in een lijst

Voordat we kunnen controleren of het antwoord van de lezer juist is, moeten we deze antwoorden eerst opslaan in een lijst. Stel dat de opties zijn 'ren weg', 'wacht af', en 'ga kijken'. Dan wil je een lijst maken met die drie acties:

```python
keuzes = [ 'ren weg', 'wacht af', 'ga kijken' ]
print('Wat doe je? Kies tussen:', keuzes)
```

Met de ``print`` kunnen we de lezer laten zien welke keuzes hij heeft.

## Lezer vragen om actie

Vervolgens kunnen we de lezer vragen wat hij/zij wilt doen, en dit antwoord opslaan in een variabele genaamd 'antwoord'.

```python
antwoord = input()
```


## Opdracht bonus-5-1\) Laat de lezer kiezen!

Deze opdracht wordt afgetekend als:

- Je een verhaal van 3-5 zinnen print.
- Je aan de lezer vraagt om een keuze te maken tussen drie opties die opgeslagen staan in een lijst.
- Je in je schrift in eigen woorden opschrijft hoe deze code werkt.

### Opdracht.

Schrijf een verhaal van 3-5 zinnen over een dier. Het dier komt zijn natuurlijke vijand tegen. (Bijvoorbeeld: kip-vos, schaap-wolf, muis-kat, olifant-muis, ...) Laat de lezer vervolgens kiezen tussen drie mogelijke acties: wat moet het dier doen?

****




## Controleren of het antwoord mogelijk is: valideren

**Controleren** of het antwoord van de lezer mogelijk is, heet het **'valideren'** van het antwoord.

Daarvoor willen we nu kijken of `antwoord` in de lijst voorkomt. _in lijst_ voorkomt. Dat verklapt al hoe het in Python moet: met `in`!

```python
print(antwoord in keuzes)
```

### Nu jij: probeer het!

Probeer het uit, en beantwoord deze vragen:
1) Wat zegt de computer als je een antwoord invoert wat in de lijst staat? 
2) En wat als deze niet in de lijst staat?
3) Kun je bedenken wat die twee woorden -- die je bij (1) en (2) te zien kreeg -- dus betekenen?


### Wachten totdat het antwoord mogelijk is

Als de lezer een goed antwoord geeft, kreeg je `True` te zien. Oftewel, 'waar' of 'juist'. Als de lezer echter een fout antwoord geeft, dan kreeg je `False` te zien. Oftewel, 'onwaar' of 'fout'.

Als de lezer een fout antwoord geeft, dan moeten we nogmaals vragen om een antwoord. En als het dan weer fout is, dan moeten we het nogmaals vragen. Zo moeten we door blijven _herhalen totdat_ we een geldig antwoord krijgen.

Herhalen totdat iets gebeurd, kun je met `while` doen. Naar het Nederlands vertaald: 'zolang'. Dat ziet er zo uit:

```python
while VOORWAARDE:
  DOE IETS
```

Op de plek van `VOORWAARDE` zetten we de voorwaarde neer dat de `while` (_zolang_) moet door blijven gaan met `DOE IETS` te herhalen. Merk op dat de `while` regel eindigt met **een dubbele punt**, en dat de volgende regel met `DOE IETS` **een inspringing** heeft aan de voorkant heeft. Die zijn beiden **verplicht**!

We willen nu blijven _herhalen totdat_ de lezer een goed antwoord geeft... maar dat is _herhalen zolang_ de lezer _geen_ goed antwoord geeft. Precies andersom dus! Dus we moeten `not` toevoegen om die '_geen_' te programmeren: `while antwoord not in keuzes`:

```python
antwoord=''
while antwoord not in keuzes:
  antwoord = input()
```

Deze drie regels code zijn dus in plaats van alleen `antwoord = input()`. Het kost dus **slechts twee extra regels code** om input te valideren!


### De keuze laten zien

Tot slot kun je een `print` toevoegen om de keuze van de lezer te laten zien.
**Let op: er staat _geen inspringing_ voor die `print`**, omdat de `print` pas moet gebeuren wanneer de herhaling van de `while` helemaal klaar is!

```python
antwoord=''
while antwoord not in keuzes:
  antwoord = input()
print('Je hebt gekozen voor:', antwoord)
```

### Nu jij: probeer het!

Probeer deze dingen zelf uit:
1) Wat gebeurd er als we die `antwoord=''` regel niet hebben?
2) Schrijf in eigen woorden in je schrift waarom die foutmelding gebeurd.


## Opdracht bonus-5-2\) input valideren in jouw verhaal

Deze opdracht wordt afgetekend als:

- Je verhaal minstens 4 zinnen print.
- Je aan de lezer vraagt om een keuze te maken tussen drie opties.
  - Bij een fout antwoord: de lezer kan nogmaals een antwoord invoeren.
  - Bij een goed antwoord: we zien de gemaakte keuze, en het verhaal gaat verder.
- Je in je schrift in eigen woorden opschrijft hoe deze code werkt.

### Opdracht.

Ga verder met je code van opdracht bonus-5-1. Zorg er nu voor dat het verhaal niet doorgaat totdat de lezer een juiste keuze maakt! Voeg aan het einde van je programma nog één zinnetje toe die de keuze van de lezer vertelt: "Je hebt gekozen voor: ...".

****




## Geef de lezer feedback

Als je nu het programma uitvoert, dan gaat het programma pas verder wanneer de lezer een goed antwoord geeft. Dat is niet heel gebruiksvriendelijk: we moeten de lezer natuurlijk wel vertellen dat hij/zij een fout antwoord heeft gegeven!

Dit kunnen we eenvoudig bereiken door de `print('Wat doe je? Kies tussen:', keuzes)` die we al hadden, in de herhaallus te plaatsen:

```python
antwoord=''
while antwoord not in keuzes:
  print('Wat doe je? Kies tussen:', keuzes)
  antwoord = input()
print('Je hebt gekozen voor:', antwoord)
```

### Nu jij: probeer het!

1) Wat krijgt de lezer nu te zien als hij/zij een fout antwoord geeft?



## Opdracht bonus-5-3\) geef de lezer ook feedback in jouw verhaal

Deze opdracht wordt afgetekend als:

- Je verhaal minstens 4 zinnen print.
- Je aan de lezer vraagt om een keuze te maken tussen drie opties.
  - Bij een fout antwoord, krijgt de lezer dezelfde vraag nogmaals.
  - Bij een goed antwoord, zien we de gemaakte keuze, en gaat het verhaal verder.
- Je in je schrift in eigen woorden opschrijft hoe deze code werkt.

### Opdracht.

Ga verder met je code van opdracht bonus-5-2. Zorg er nu ook voor dat wanneer de lezer een fout antwoord invoert, dat de lezer weer dezelfde vraag te zien krijgt.

### Volgende keer...

In de volgende les leer je om iets met de keuze van de lezer te doen, dus bewaar je code goed, zodat je hier volgende les mee verder kunt gaan!




****

## Samenvatting

Samengevat, je kunt dit stukje Python code gebruiken om ervoor te zorgen dat de lezer alleen een mogelijk antwoord kan kiezen.

```python
print('Vertel hier een verhaal.')

keuzes = [ 'ren weg', 'wacht af', 'ga kijken' ]
antwoord=''
while antwoord not in keuzes:
  print('Wat doe je? Kies tussen:', keuzes)
  antwoord = input()
print('Je hebt gekozen voor:', antwoord)

print('Verhaal gaat verder.')
```
