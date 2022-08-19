# Les 8b

**Opdracht 1 : Gebruik een functie in de quiz \(herhaling\)**

Deze opdracht wordt afgetekend als:

1. Je  meerdere vragen kunt stellen in je quiz
2. Je daarvoor een functie gebruikt.

**Uitleg.** Ga naar jouw code van vorige week. Zorg nu dat je meerdere vragen kunt stellen met een functie. Je kunt het op twee manieren doen:

* Meteen de functie maken en dan aanroepen \(moeilijker\)
* Eerst je code copy-pasten en dan aanpassen zoals we geoefend hebben in deel a \(iets makkelijker\)

**Opdracht 2: Zet je vragen in een lijst**

Deze opdracht wordt afgetekend als:

1. Je vragen in een lijst opgeslagen zijn
2. De antwoorden en antwoordopties ook ieder in een lijst staan
3. Je de eerste vraag uit de lijst kiest
4. Je de vraag verwijdert als je de vraag gesteld hebt
5. Je ook de goede antwoordenopties verwijdert

**Uitleg.** Je zet je vragen nu steeds in de code, maar dan krijg je ze altijd in dezelfde volgorde. Dat is niet zo spannend. We gaan de vragen in een lijst zetten, dan kan je er steeds een willekeurige uit kiezen. Dat doen we in opdracht 3. Voor deze opdracht zetten we alles eerst in een lijstje.

Maak drie lijsten:

1. vragen
2. antwoord\_opties
3. goede\_antwoorden

Kies dan steeds de eerste vraag uit, en stel die vraag. Je programma blijft dus hetzelfde werken. Verwijder na iedere vraag alle drie dingen die je gebruikt hebt. Dat doe je met een pop\(0\), zo:

```python
vragen.pop(0)
antwoord_opties.pop(0)
goede_antwoorden.pop(0)
```

**Opdracht 3: Kies een willekeurige vraag**

Deze opdracht wordt afgetekend als:

1. Je uit de vraag een willekeurige vraag kiest
2. Je ook de bijbehorende opties en het bijbehorende goede antwoord opzoekt

**Uitleg.** Nu maken we het spel leuker door steeds een willekeurige vraag te kiezen. Weet je nog hoe dat moet? Volg deze stappen:

1. Zet bovenin je code `import random`
2. Maak een variabele `getal` waarin je een willekeurige getal kiest. Dat doe je met `random.randint(0,10)` Bij de 10 moet het aantal vragen dat jij in je lijst hebt.
3. Overal waar je eerst de de 0 had staan, zet je nu getal neer. Dan krijg je niet de eerste vraag maar een willekeurige. Vergeet ook niet de nullen bij pop\(\) te vervangen!

**Opdracht 4: Tel de punten \(extra\)**

Deze opdracht wordt afgetekend als:

1. Je telt hoeveel goede antwoorden de speler heeft aangeklikt

**Opdracht 5: Deel strafpunten uit \(extra\)**

Deze opdracht wordt afgetekend als:

1. Je telt hoeveel goede antwoorden de speler heeft aangeklikt
2. De speler per fout antwoord een strafpunt krijgt

