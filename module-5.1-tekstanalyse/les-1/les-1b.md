# Les 1b

**1) Maak een  nieuw C# bestand op repl.it**&#x20;

Klink in replit op Create en maak een nieuw C# bestand aan. Let op dat je de gewone C# kiest en niet mono.&#x20;

![](https://www.dropbox.com/s/uc0fx1cfojy6y1k/Screen%20Shot%202022-08-18%20at%203.26.34%20PM.png?raw=1)

**2) Lees een bestand in!**

Download dit bestand met [een tweet in jsonformaat](https://www.dropbox.com/s/8jykdfbamhkc59l/tweet.json?dl=0) en voeg het toe aan je replit. Gebruik de code uit deel a om de tweets in het bestand in te lezen. Print de inhoud van het bestand uit zodat je kunt zien of het goed gegaan is.

**3) Vertaal het bestand in json**

We hebben het bestand nu als tekst ingelezen maar het is een json file en we kunnen het dus in een keer inlezen in een dictionary (zoals we die ook kennen uit Python en JavaScript).

Zet bovenaan je bestand deze code om een module te importeren:

```csharp
using System.Text.Json;
```

Nu kunnen we de json zo inlezen. Zoek in deel a of op internet op hoe je een bestand inleest als je het niet meer weet.

```csharp
// lees hier het bestand in en zorg dat in inhoud ervan in de variabele text komst

var jsonObject = JsonDocument.Parse(text);
Console.WriteLine(jsonObject);
```

Anders dan in Python kunnen we het object niet goed zien in C#. Als we het printen met `Console.WriteLine`zien we alleen `System.Text.Json.JsonDocument` in beeld.

We kunnen wel een veld opvragen, probeer dat maar eens:

```csharp
var tweetText = jsonObject.RootElement.GetProperty("full_text");
Console.WriteLine(tweetText);
```

**4) Wat zit er allemaal op een tweet?**

Nu we een tweet kunnen inlezen wordt het tijd om eens te bekijken wat er allemaal op zit!&#x20;

Maar... zo'n heel groot tekstbestand, dat is niet handig om te lezen!

Daar zijn gelukkig tooltjes voor, bijv: [http://jsonviewer.stack.hu/](http://jsonviewer.stack.hu/). Plak de json bij text en kijk dan eens bij viewer, zo heb je veel meer overzicht:

<figure><img src="https://www.dropbox.com/s/pxzna9xusxr99ez/Screen%20Shot%202022-08-24%20at%202.23.49%20PM.png?raw=1" alt=""><figcaption></figcaption></figure>

Zoek nu eens uit of je deze dingen kan printen:

* Hoe vaak een tweet is geretweet
* In welke taal de tweet geschreven is
* Of het een "quote tweet" is

**5) Dieper in de "boom"**

Sommige van de velden hebben zelf weer velden, dat zien we aan het plusje dat je uit kan klappen, bijvoorbeeld `user`:

<figure><img src="https://www.dropbox.com/s/xze7o0jf36vtcas/Screen%20Shot%202022-08-24%20at%202.54.34%20PM.png?raw=1" alt=""><figcaption></figcaption></figure>

`user` heeft bijvoorbeeld het veld `id`, maar ook `name`, daaraan kan je zien hoe het account heet. Als je die velden wilt opvragen dan kan dat niet in één stap, maar moet het in twee stappen, zo:

```csharp
var tweetUsername = jsonObject.RootElement.GetProperty("user").GetProperty("name");
```

Probeer nu eens deze dingen op te vragen:

* De screenname van degene die de tweet stuurde (dat is anders dan `name`!)
* De bio van de user, veld: description
* De avatar van de user, zoek zelf op welk veld dat kan zijn

**6) Data analyse**

Deze periode gaan we aan de slag met een grotere dataset van Twitter. Denk eens na over wat je met een hele dataset van zulke tweets zou kunnen doen!

****
