# Les 3a

Tot nu toe hebben we steeds de tweets ingelezen met een dynamisch object. Dat lijkt een beetje op Python, want als je een veld kiest dat niet op de tweet zit, krijg je pas bij het uitvoeren een fout. Dat noem je op _runtime._ Dat is de tijd (_time_) dat het programma uitgevoerd wordt (_run_).

Typ je een naam fout, dan krijg je bijvoorbeeld zo'n foutmelding:

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

Niet zo handig, want de foutmelding vertelt niet eens welke key er niet gevonden is!

C# is anders dan Python omdat er ook typed gebruikt kunnen worden. Daar kunnen we dus ook gebruik van maken om de tweet op een betere manier in te laden.

Om de tweets handiger te kunnen inlezen moeten we een klasse maken met daarop de velden van de tweet. Zo doe je dat voor een paar velden:

```csharp
class Tweet
    {
        public string fulltext { get; set; }
        public Int64 id { get; set; }
    }
```

We moeten dus voor ieder veld vertellen wat voor type heft heeft. `fullltext` is een string maar `id` is een getal: een Int64 omdat het een heel grot getal is. De `{ get; set; }`moet achter ieder veld, we komen er nog op terug waar dat voor nodig is.

Nu we deze klasse gemaakt hebben, kunnen we een tweet daar direct in inladen, zo:

```csharp
    var tweetObject = JsonSerializer.Deserialize<Tweet>(text);
```

&#x20;De code `<Tweet>` hier geeft aan dat we het json object in de klasse `Tweet` gaan laden. Nu we dat gedaan hebben, kunnen we de velden met de dot-notatie ophalen:

```csharp
    Console.WriteLine(tweetObject.fulltext);
```

Dat is veel handiger, want als we nu een tikfoutje maken, zien we dat meteen:

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

En, ben je even vergeten wat er op je tweet zit? replit vertelt het nu automatisch als je een punt typt:

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

****
