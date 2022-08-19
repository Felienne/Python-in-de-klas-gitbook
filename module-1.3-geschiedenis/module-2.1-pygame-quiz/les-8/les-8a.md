# Les 8a

**Nog eens kijken naar de quizcode**

Hier staat het programma zonder functies:

```python
import pygame
import time

pygame.init()
breedte = 800
hoogte = 600
background_color = 0, 0, 0
font = pygame.font.SysFont(None, 40)
screen = pygame.display.set_mode((breedte, hoogte))

A = pygame.image.load("A.png")
A_rechthoek = A.get_rect()
B = pygame.image.load("B.png")
B_rechthoek = B.get_rect()
C = pygame.image.load("C.png")
C_rechthoek = C.get_rect()
D = pygame.image.load("D.png")
D_rechthoek = D.get_rect()


vraagtekst = "Wat is de hoofdstad van Nederland?"
vraagblok = font.render(vraagtekst, True, (255,255,255))
optiestekst = "A) Haarlem B) Rotterdam C) Amsterdam D) Eindhoven"
optiesblok = font.render(optiestekst, True, (255,255,255))
goede_antwoord = 'C'

antwoord = 'geen'
vorige_antwoord = 'geen'

while not antwoord == goede_antwoord:
  pygame.display.flip()
  screen.fill(background_color)

  screen.blit(vraagblok, (0, 275))
  screen.blit(optiesblok, (0, 310))

  A_rechthoek.center = (100, 100)
  screen.blit(A, A_rechthoek)

  B_rechthoek.center = (600, 100)
  screen.blit(B, B_rechthoek)

  C_rechthoek.center = (100, 500)
  screen.blit(C, C_rechthoek)

  D_rechthoek.center = (600, 500)
  screen.blit(D, D_rechthoek)

  pygame.event.get()
  locatie_muis = pygame.mouse.get_pos()
  knoppen = pygame.mouse.get_pressed()

  if knoppen[0] == 1:
    if A_rechthoek.collidepoint(locatie_muis):
      antwoord = 'A'
    if B_rechthoek.collidepoint(locatie_muis):
      antwoord = 'B'
    if C_rechthoek.collidepoint(locatie_muis):
      antwoord = 'C'
    if D_rechthoek.collidepoint(locatie_muis):
      antwoord = 'D'

    if antwoord == vorige_antwoord:
      print('Dat probeerde je net ook al')
    else:

      if antwoord == goede_antwoord:
        print('Goedzo!')
      else:
        print('Helaas,', antwoord, 'is niet goed')
        vorige_antwoord = antwoord
        antwoord = 'geen' #reset het antwoord zodat de speler nog een keer kan proberen 


    time.sleep(0.5) #even wachten op de volgende klik!


vraagtekst = "Wat is de hoofdstad van Belgie?"
vraagblok = font.render(vraagtekst, True, (255,255,255))
optiestekst = "A) Gent B) Brussel C) Antwerpen D) Brugge"
optiesblok = font.render(optiestekst, True, (255,255,255))
goede_antwoord = 'B'

antwoord = 'geen'
vorige_antwoord = 'geen'

while not antwoord == goede_antwoord:
  pygame.display.flip()
  screen.fill(background_color)

  screen.blit(vraagblok, (0, 275))
  screen.blit(optiesblok, (0, 310))

  A_rechthoek.center = (100, 100)
  screen.blit(A, A_rechthoek)

  B_rechthoek.center = (600, 100)
  screen.blit(B, B_rechthoek)

  C_rechthoek.center = (100, 500)
  screen.blit(C, C_rechthoek)

  D_rechthoek.center = (600, 500)
  screen.blit(D, D_rechthoek)

  pygame.event.get()
  locatie_muis = pygame.mouse.get_pos()
  knoppen = pygame.mouse.get_pressed()

  if knoppen[0] == 1:
    if A_rechthoek.collidepoint(locatie_muis):
      antwoord = 'A'
    if B_rechthoek.collidepoint(locatie_muis):
      antwoord = 'B'
    if C_rechthoek.collidepoint(locatie_muis):
      antwoord = 'C'
    if D_rechthoek.collidepoint(locatie_muis):
      antwoord = 'D'

    if antwoord == vorige_antwoord:
      print('Dat probeerde je net ook al')
    else:

      if antwoord == goede_antwoord:
        print('Goedzo!')
      else:
        print('Helaas,', antwoord, 'is niet goed')
        vorige_antwoord = antwoord
        antwoord = 'geen' #reset het antwoord zodat de speler nog een keer kan proberen 

    time.sleep(0.5) #even wachten op de volgende klik!
```

Kijk nog eens goed naar de code. Welke stukjes zijn hetzelfde? Omcirkel die stukken.

In deel b van de les gaan we de functie zelf ook maken

