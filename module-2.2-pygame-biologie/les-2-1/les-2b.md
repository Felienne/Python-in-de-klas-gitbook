# Les 2b

#### 1) Teken een rechthoek om je dier

Deze opdracht wordt afgetekend als:

* Je een rechthoek om je dier tekent.

Zet deze code in de loop. Dat zie je goed waar het rechthoek staat:`pygame.draw.rect(screen, (100,100,100), schildpad_rechthoek, 1)`

#### **2) Schaal je plaatje**

Deze opdracht wordt afgetekend als:

* Jouw dier steeds kleiner wordt als het meer honger heeft
* Je hiervoor `pygame.transform.rotozoom()` gebruikt.

**Uitleg**

Nu ga je je dier steeds kleiner maken als hij meer honger heeft. Daarvoor gaan we twee stappen zetten:

1. Maak een nieuwe variabele `schildpad_origineel` aan en laad daarin je plaatje.&#x20;
2. Voeg nu een regel toe in de code waar je je dier 'schaalt', maw een andere grootte geeft. Dat ziet er zo uit:`schildpad = pygame.transform.rotozoom(schildpad_origineel, 0, (100-honger)/100)`

{% hint style="info" %}
Bij jou kunnen de variabelen natuurlijk anders heten, bijv `hert_origineel`of `blobvis_origineel`.
{% endhint %}

{% hint style="info" %}
Het kan ook zijn dat jij iets andere getallen nodig hebt, omdat je dier al groter of kleiner begint. Verander de twee getallen 100 in andere getallen tot je het mooi vindt.
{% endhint %}

#### **3) Laat je dier op dezelfde plek krimpen**

Deze opdracht wordt afgetekend als:

* Je dier op dezelfde plek blijft staan tijdens het schalen.

**Uitleg**

Je dier blijft nu aan de bovenkant van het veld hangen, omdat hij niet weet waar hij stond voor het krimpen. Dat moet jij eerst opslaan in een variabele.

1. Maak een nieuwe variabele `midden` aan en sla daarin het midden van de rechthoek op, dat doe je zo: `midden = schildpad_rechthoek.center`\
   In midden zitten nu twee getallen, die stellen het midden van het diertje voor.
2. Hierna komt dan de regel waarin je het dier kleiner maakt:\
   `schildpad = pygame.transform.rotozoom(schildpad_origineel, 0, (100-honger)/100)`\
   Na het kleiner maken moet je het midden weer herstellen, dat doe je met deze regel:\
   `schildpad_rechthoek.center = midden`

**4) Voer het dier met een muisklik**

Deze opdracht wordt afgetekend als:

* Je je dier met een muisklik op het voedsel kan voeren

**Uitleg.**&#x20;

Je dier kan nu alleen kleiner worden en dan is je simulatie natuurlijk snel afgelopen. Zorg daarom dat je op het voedsel kan klikken, en dat de variabele honger dan met 10 verlaagd wordt. Als het goed is, groeit je dier dan ook vanzelf!

