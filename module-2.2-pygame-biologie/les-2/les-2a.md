# Les 3a

#### 1\) Code tot nu toe

Deze opdracht wordt afgetekend als:

* Je voor alle blokken code hebt opgeschreven wat ze doen

Hier lees je de basiscode tot nu toe. De code is opgedeeld in blokken, tussen de strepen. Schrijf per stuk in je schrift wat de code doet. Leg ook per blok uit waarom deze code nodig is. 

Je mag hiervoor samenwerken met je buur.

```python
------- Blok 1 ------
import pygame
import time

------- Blok 2 ------
pygame.init()
breedte = 800
hoogte = 600
screen = pygame.display.set_mode((breedte, hoogte))
backgroundColor = 0, 0, 0

------- Blok 3 ------
schildpad_origineel = pygame.image.load("pad-wit-klein.png")

------- Blok 4 ------
schildpad = pygame.image.load("pad-wit-klein.png")

------- Blok 5 ------
dier_leeft = True
honger = 0

------- Blok 6 ------
while dier_leeft:

------- Blok 7 ------
  pygame.draw.rect(screen, (100,100,100), schildpad_rechthoek, 1)

------- Blok 8 ------
  pygame.display.flip()
  screen.fill(background_color)
  screen.blit(schildpad, schildpad_rechthoek)
  screen.blit(sla, sla_rechthoek)

------- Blok 9 ------
  print(f'ik heb zoveel honger: {honger}')
  honger = honger + 1
  if honger > 100:
    dier_leeft = False

------- Blok 10 ------
  pygame.event.get()
  locatie_muis = pygame.mouse.get_pos()
  knoppen = pygame.mouse.get_pressed()

  if knoppen[0] == 1:
    if sla_rechthoek.collidepoint(locatie_muis):
      print('haphap')
      honger = honger - 10

------- Blok 11 ------
  midden = schildpad_rechthoek.center
  schildpad = pygame.transform.rotozoom(schildpad_origineel, 0, (100-honger)/100)
  schildpad_rechthoek = schildpad.get_rect()
  schildpad_rechthoek.center = midden

------- Blok 12 ------
  time.sleep(0.1)

------- Blok 13 ------
print('Helaas, je schildpad is overleden')
```



