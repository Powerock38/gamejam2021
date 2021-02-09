from View import View
from Garden import Garden
from Tower import Tower
from Pip import Pip
from HUD import HUD
from Enemy import Enemy
import pygame
import math

def update(graphic_elements):

    for g in graphic_elements:
        if isinstance(g, Garden):
            g.update()
        
        elif isinstance(g, Pip):
            next_pos = g.move()
            if next_pos[0] > 0 and next_pos[0] < 896 and next_pos[1] > 0 and next_pos[1] < 768 and not next_pos[2]:
                g.coordinates = (next_pos[0], next_pos[1])
            else:
                if g.enemy:
                    g.enemy.hp -= g.damage
                    if g.enemy.hp <= 0:
                        index = graphic_elements[0].enemies.index(g.enemy)
                        graphic_elements[0].enemies.remove(graphic_elements[0].enemies[index])
                        enemy = g.enemy
                        for pip in range(len(graphic_elements)):
                            if isinstance(graphic_elements[pip], Pip):
                                if graphic_elements[pip].enemy == enemy:
                                    graphic_elements[pip].enemy = None
                        del enemy
                graphic_elements.remove(g)
                del g

        elif isinstance(g, Tower):
            if g.name == "hover":
                x = g.coordinates[0]
                y = g.coordinates[1]

                if (pygame.mouse.get_pos()[0] < 896):
                    x = pygame.mouse.get_pos()[0] - pygame.mouse.get_pos()[0] % 32
                    y = pygame.mouse.get_pos()[1] - pygame.mouse.get_pos()[1] % 32
                else:
                    y = pygame.mouse.get_pos()[1] - pygame.mouse.get_pos()[1] % 32
                g.coordinates = ((x,y))

            else :
                g.tick += 1
                if g.tick == g.rate:
                    g.tick = 0
                    attack = 0
                    for enemy in graphic_elements[0].enemies:
                        
                        if attack < g.max_attack:
                            pip = g.attack(enemy)
                            
                            if pip:
                                graphic_elements.append(pip)
                                attack += 1
    return graphic_elements

def eventListener(event, graphic_elements, hover):

    if event.type == pygame.MOUSEBUTTONDOWN and not hover:
        graphic_elements.append(Tower(
                pygame.image.load("assets/fruits-veggies/Acorn.png"),
                "hover",
                20,
                1,
                (mouse_pos[0] - mouse_pos[0] % 32, mouse_pos[1] - mouse_pos[1] % 32)))
        hover = True

    elif event.type == pygame.MOUSEBUTTONDOWN and hover:
        graphic_elements.append(Tower(
            pygame.image.load("assets/fruits-veggies/Acorn.png"), "Acorn", 20, 1,
            (mouse_pos[0] - pygame.mouse.get_pos()[0] % 32,
            pygame.mouse.get_pos()[1] - pygame.mouse.get_pos()[1] % 32)))
        hover = False

        #delete the hover tower
        for g in graphic_elements:
            if isinstance(g, Tower) and g.name == "hover":
                graphic_elements.remove(g)
                del g

    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and hover:
            graphic_elements.append(Tower(
                pygame.image.load("assets/fruits-veggies/Acorn.png"),
                "Acorn",
                20,
                1,
                (pygame.mouse.get_pos()[0] - pygame.mouse.get_pos()[0] % 32,
                    pygame.mouse.get_pos()[1] - pygame.mouse.get_pos()[1] % 32)))
            hover = False

            #delete the hover tower
            for g in graphic_elements:
                if isinstance(g, Tower) and g.name == "hover":
                    graphic_elements.remove(g)
                    del g

        elif event.key == pygame.K_a:
            for elem in graphic_elements:
                if isinstance(elem, Tower) and elem.name != "hover":
                    graphic_elements.append(elem.attack(math.pi/2))

    return (graphic_elements, hover)

#Main

garden = Garden()

# Create HUD
hud = HUD(100,10)

view = View([garden,hud], update, eventListener)
