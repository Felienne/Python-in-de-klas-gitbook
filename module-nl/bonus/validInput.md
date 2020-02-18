# Bonus: input valideren

Soms wil je dat de lezer van je verhaal keuzes kan maken, maar niet alle keuzes zijn natuurlijk mogelijk. Daarom moet jij, als de programmeer, ervoor zorgen dat de lezer alleen keuzes kan maken die van jou mogen.

**Voorkennis**

Les 4: lijsten
Les 5: input

**Leerdoelen**

Aan het einde van de bonus kun jij:

* Geldige antwoorden opslaan in een lijst
* Die lijst gebruiken om te controleren of de input van de gebruiker geldig (valide) is.

**Geldige antwoorden in een lijst**

Voordat we kunnen controleren of het antwoord van de lezer juist is, moeten we deze antwoorden eerst opslaan in een lijst. Stel dat de opties zijn 'ren weg', 'wacht af', en 'ga kijken'. Dan wil je een lijst maken met die drie acties:

```python
keuzes = [ 'ren weg', 'wacht af', 'ga kijken' ]
print('Wat doe je? Kies tussen:', keuzes)
```

Met de ``print`` kunnen we de lezer laten zien welke keuzes hij heeft.

**Lezer vragen om actie**

Vervolgens kunnen we de lezer vragen wat hij/zij wilt doen, en dit antwoord opslaan in een variabele genaamd 'antwoord'.

```python
antwoord = input()
```

**Controleren of het goed is.**

Nu willen we kijken of `antwoord` in de lijst voorkomt. _in lijst_ voorkomt. Dat verklapt al hoe het in Python moet: `in`.

```python
print(antwoord in keuzes)
```

***Test het!***

Probeer het uit. Wat zegt de computer als je een antwoord invoert wat in de lijst staat? En wat als deze niet in de lijst staat?

**Wachten totdat het antwoord goed is.**

Als de lezer een goed antwoord geeft, kreeg je `True` te zien. Oftewel, 'waar' of 'juist'. Als de lezer echter een fout antwoord geeft, dan kreeg je `False` te zien. Oftewel, 'onwaar' of 'fout'.

Als de lezer een fout antwoord geeft, dan moeten we nogmaals vragen om een antwoord. En als het dan weer fout is, dan moeten we het nogmaals vragen. Zo moeten we door blijven _herhalen totdat_ we een geldig antwoord krijgen.

Herhalen totdat iets gebeurd, kun je met `while` doen. Naar het Nederlands vertaald: 'zolang'. Dat ziet er zo uit:

```python
while ---een voorwaarde---:
  ---herhaal dit commando---
```

Op de plek van `---een voorwaarde---` zetten we de voorwaarde neer dat de _zolang_ moet door blijven gaan met `---herhaal dit comando---` te herhalen.

We willen nu blijven _herhalen totdat_ de lezer een goed antwoord geeft... maar dat is _herhalen zolang_ de lezer _geen_ goed antwoord geeft, dus moeten we `not` toevoegen: `while antwoord not in keuzes`:

```python
antwoord=''
while antwoord not in keuzes:
  print('Wat doe je? Kies tussen:', keuzes)
  antwoord = input()
print('Jouw antwoord was:', antwoord)
```

(TODO: dit opsplitsen in uitleg eerst zonder de print)

***Test het!***

1) Wat gebeurd er als we die `antwoord=''` regel niet hebben?
2) Leg in eigen woorden uit waarom die foutmelding gebeurd.

**Alles samenbrengen...**

Samegevat, je kunt dit stukje Python code gebruiken om ervoor te zorgen dat de lezer alleen een mogelijk antwoord ik kan voeren.

```python
print('Vertel hier een verhaal.')

keuzes = [ 'ren weg', 'wacht af', 'ga kijken' ]
antwoord=''
while antwoord not in keuzes:
  print('Wat doe je? Kies tussen:', keuzes)
  antwoord = input()

print('Verhaal gaat verder.')
```

***Opdracht:***
1) Schrijf zelf een klein verhaal van 5 zinnen.
2) Vraag de lezer daarna om een keuze te maken tussen drie opties.
3) Zorg ervoor dat het verhaal niet doorgaat totdat de lezer een juiste keuze maakt.


In de volgende les leer je om iets met de keuze van de lezer te doen.

