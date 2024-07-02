# Les 5b

De app die we gaan maken kent twee fases:&#x20;

1. Woorden selecteren
2. Woorden oefenen

In deze les gaan we het oefenen verder uitbreiden door de ingevulden antwoorden van de gebruiker op te slaan in het bestand.&#x20;

**Opdracht 1) Antwoorden opslaan**

We gaan eerst de antwoorden van de gebruiker in =de dictionary opslaan, dat doen we zo:

`rij['Betekenis'] = betekenis`

Doe dat meteen na de invoer, en doe het ook voor de variabele zin om dezelfde manier

**Opdracht 2) kolommen aanmaken in het csv bestand**

Er is nu nog niets veranderd aan het bestand, voer je code maar eens uit, er is nog niets terug geschreven in het bestand. We moeten nog aan het csv bestand vertellen welke kolommen er in zitten, dat gaat zo:

`headers = ['Nummer', 'Woord', 'Beschrijving',` ....`]`

Vul op de puntjes zelf de nieuwe kolommen in. Krijg je een foutmelding? Lees dan goed wat er staat, waarschijnlijk heb je een foutje gemaakt in een naam van een kolom.

**Opdracht 3) data opslaan**

Sla nu de data op, dat doe je met deze code:

```python
    with open('words-selectie.csv', 'w', newline='') as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=headers)
      writer.writeheader()
      writer.writerows(woordlijst)
```



