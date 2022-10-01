# Les 4b

**1) Verstop de ja- en nee-knop en het uitvoerveld**

Zoals we het nu geprogrammeerd hebben, zijn de knoppen die bij selecteren horen (ja, nee en het uitvoerveld) meteen al in beeld:

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

Maar die moeten alleen in beeld komen als de gebruiker op selecteren gedrukt heeft. Dat gaan we zou programmeren:

1. Kijk goed hoe de knoppen heten die nodig zijn voor het selecteren. Dat zijn de knoppen voor ja en nee.
2. Verplaats nu alle regels met `.place()`erin **van de knoppen die horen bij selecteren** naar de functie `selecteren()`.  Ze staan dan alleen in de functies `selecteren()` en niet meer onderaan je code.

Voer nu je programma uit en kijk of de knoppen aan het begin wegzijn, en terugkomen als je op Selecteren drukt.

&#x20;**2) Oefenen, de opzet**

Dan gaan we nu aan de slag met de oefenknop. We beginnen nog even zonder jouw oude codes.

1. Maak een lege functie oefenen()
2. Koppel deze functie aan de oefenknop
3. Begin in de functie oefenen met het uitwissen van de knoppen van selecteren, want die hebben we nu niet nodig. Dat doe je zo: \
   `jaknop.place_forget()`\
   `neeknop.place_forget()`
4. Maak deze dingen aan:
   1. Een invoerveld voor de betekenis van het woord&#x20;
   2. Een invoerveld voor de zin
   3. Een nieuwe knop die gaat controleren of het woord goed is. We noemen die de `controleerknop`.
   4.  Een variabele en een functie voor de controleerknop:\
       `controleerknop_is_ingedrukt = IntVar()`

       ``\
       `def controleerknop_ingedrukt():` \
       &#x20;  `controleerknop_is_ingedrukt.set(1)`
5. Laat deze knop en de velden verschijnen als er op Oefenen geklikt is

Test je code goed voordat je verder gaat!

**3) Oefenen, de invulling**

Nu ga de de functie ook echt invullen. Bekijk in jouw oude code en zet deze om, zodat dit er allemaal weer op zit:

* Vroeger gebruikte je een input() code, en die zet het programma vanzelf op pauze. Dat moet nu in tkinter anders. \
  Dus: de functie wacht bij ieder woord tot er op de controleerknop is gedrukt met\
  `controleerknop.wait_variable(controleerknop_is_ingedrukt)`
* De gebruiker kan een betekenis invoeren&#x20;
  * Die betekenis wordt opgeslagen in het bestand in de kolom **Betekenis-ingevoerd**
  * Is de betekenis goed (gelijk aan wat er in het bestand staat) dan:
    * schrijf je goed in het bestand bij de kolom **Goed**
    * print je **Goed** op de command line met `print()` Dat komt dus nog niet in het scherm!
  * Is de betekenis fout:&#x20;
    * dan sla je fout op in de kolom **Goed**
    * print je **Fout** op de command line met `print()` Dat komt dus nog niet in het scherm!
* De gebruiker kan een zin invoeren met het woord erin. Die sla jij op in de kolom **Zin**.

**4) Nog wel een foutje... (extra)**

Oefenen werkt nu goed maar... selecteren niet! Als je op selecteren drukt komen alle knoppen en velden in beeld:

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

We gaan dit foutje in de volgende les oplossen, maar denk alvast eens na hoe je dit zou kunnen aanpakken!&#x20;



