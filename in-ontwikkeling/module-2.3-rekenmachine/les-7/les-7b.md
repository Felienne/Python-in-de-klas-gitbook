# Les 7b

**Opdracht 1) Schakel je code uit en voeg de UI toe**

We gaan de User Interface (of UI, zeg: Joe-Ai) stap voor stap toevoegen. Open je code van vorige week en zet even alles uit. Dat doet je met ctrl-a (alles selecteren) en dan ctrl-? (alles op commentaar zetten). Dat ziet er zo uit:

![](https://www.dropbox.com/s/loq2buxpzippru0/Screen%20Shot%202022-08-12%20at%2011.57.48%20AM.png?raw=1)

Zet nu deze code bovenaan. Deze regels maken een UI aan met een knop en een invoerveld.

{% code lineNumbers="true" %}
```python
# import time 

from tkinter import *

root = Tk()

root.title("Mijn rekenmachine")
root.geometry("600x400")

def Rekenen():
  som = invoerveld.get()
  # hier moet natuurlijk jouw code gekoppeld worden
  
  uitvoerveld["text"] = "0"

invoerlabel = Label(root)
invoerlabel["text"] = "Vul hier jouw som in:"
invoerlabel.place(x=0, y=0)

invoerveld = Entry(root) 
invoerveld.place(x=0, y=60)

knop = Button(root)
knop["text"] = "Rekenen"
knop["command"] = Rekenen
knop.place(x=0, y=120)

uitvoerveld = Label(root)
uitvoerveld["text"] = "Berekening komt hier"
uitvoerveld.place(x=0, y=180)
```
{% endcode %}

Voer de code uit en zie dat je drie elementen in beeld hebt: een invoerveld, een knop en een uitvoerveld, zo:

![](https://www.dropbox.com/s/5t4xsfjat3lm8qt/Screen%20Shot%202022-08-12%20at%2011.58.01%20AM.png?raw=1)

Vind je de namen of plaatsen van de velden niet mooi? Verander dan de regels 7, 17, 18, 21, 24, 25 29 en 30.

**Opdracht 2) Koppel jouw rekenmachine**

Nu gaan we jouw bestaande codes invoegen in de functie `rekenen()`. Pak alle code op die je onderaan de pagina in commentaar had gezet en doe het volgende. Ben heel zorgvuldig anders lukt het niet!



1.  Verwijder deze regels:\


    ```python
    # vraag de gebruiker om een som
    som = input('Voer een som in.')
    ```


2. Selecteer nu alle codes onderaan die beginnen met #&#x20;
3. Zet het weer aan met ctrl-?
4. Spring de code in met tab\


Gelukt? Plak de codes nu in de functie `rekenen()` Als het goed is kun je de functie nu mooi dichtklappen en zitten als jouw codes erin:

![](https://www.dropbox.com/s/kz4dc30lo4uusc9/Screen%20Shot%202022-08-12%20at%2012.13.01%20PM.png?raw=1)

{% hint style="info" %}
Voer nu je code uit om te kijken of alles in orde is! Klik op de rekenknop en kijk
{% endhint %}

Voer nu je code uit en kijk of alles werkt. Als je goed is kan je een som invoeren in het veld, en komt de uitvoer onder in beeld (nog niet in je UI, dat komt nog).

Als het goed is, ziet het er zo uit:

![](https://www.dropbox.com/s/kdjhiqb13ckvgn5/Screen%20Shot%202022-08-12%20at%2012.20.34%20PM.png?raw=1)

Krijg je deze foutmelding? Dan ben je vergeten de regel met `input()` weg te halen.

![](https://www.dropbox.com/s/5bkj44df5s06ghb/Screen%20Shot%202022-08-12%20at%2012.19.36%20PM.png?raw=1)

**Opdracht 3) Uitvoer in het label**

Zo, de rekenmachine werkt, maar... de uitvoe komt nu onderin beeld en niet in onze mooi UI. Dat gaan we nu aanpassen.&#x20;



Lees je code goed door en zoek naar allen `print()` codes. Verander iedere print in het instellen van de tekst van het label `uitvoerveld`. \
\
Bijvoorbeeld:

`print('Je voerde geen geldige getallen in!')`\
\
wordt\
\
`uitvoerveld["text"] = 'Je voerde geen geldige getallen in!'`

Probeer je code weer uit! Komt het resultaat van de som mooi in beeld?

**Opdracht 4) Foutje in het rood**

Als het goed is, komen ook al je foutmeldingen in de UI, maar ze zien er hetzelfde uit als een uitvoer. In tkinter kan je ook de achtergrondkleur veranderen, zo:

```
uitvoerveld["bg"] = "red"
```

Zet deze code op de 2 plekken waar je een foutmelding print. Als je wilt kun je ook de tekstkleur nog veranderen, bijv in geel:

```
uitvoerveld["fg"] = "yellow"
```
