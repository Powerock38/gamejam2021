from View import View
from Garden import Garden
from Tower import Tower
from Pip import Pip
from HUD import HUD
from Utils import Utils
from Enemy import Enemy
from Menu import Menu
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
                mouse_pos = pygame.mouse.get_pos()

                if (mouse_pos[0] < 896):
                    x = mouse_pos[0] - mouse_pos[0] % 32
                    y = mouse_pos[1] - mouse_pos[1] % 32
                else:
                    y = mouse_pos[1] - mouse_pos[1] % 32

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

def eventListener(event, elements):
    garden = elements[0]
    hud = elements[1]

    if event.type == pygame.MOUSEBUTTONDOWN:
        mx, my = pygame.mouse.get_pos()
        if event.button == 1:
            if mx >= 896:
                hud.buy(mx, my)
            elif mx < 896:
                garden.putTower()

    # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not hover:
    #     if (graphic_elements[1].get_water() - vegetable['price']) >= 0:
    #         graphic_elements.append(Tower(
    #                 pygame.image.load(vegetable['path']),
    #                 "hover",
    #                 vegetable['fire_rate'],
    #                 vegetable['damage'],
    #                 (mouse_pos[0] - mouse_pos[0] % 32,
    #                 mouse_pos[1] - mouse_pos[1] % 32),
    #                 vegetable['range'])
    #             )
    #         hover = True
    #     else:
    #         print("Not enough water !")

    # elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and hover:
    #     putTower(graphic_elements, vegetable, hover)
    
    # elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3: #3 => right click
    #     print("coucou")
    #     for g in graphic_elements:
    #         if isinstance(g, Tower) and \
    #                 mouse_pos[0] // 32 < g.coordinates[0] // 32 and \
    #                 mouse_pos[0] // 32 > g.coordinates[0] // 32 and \
    #                 mouse_pos[1] // 32 > g.coordinates[1] // 32 and \
    #                 mouse_pos[1] // 32 > g.coordinates[1] // 32:
    #             graphic_elements[1].set_water(
    #                 graphic_elements[1].get_water() + vegetable['price'] / 2)
    #             graphic_elements.remove(g)
    #             del g #c'est pas encore bon !!

    # elif event.type == pygame.KEYDOWN:
    #     if event.key == pygame.K_SPACE and hover:
    #         if (graphic_elements[1].get_water() - vegetable['price']) >= 0:
    #             graphic_elements, hover = putTower(graphic_elements, vegetable, hover)
    #         else:
    #             print("Not enough water !")

    # return graphic_elements

#Main

garden = Garden()
menu = Menu()

# Create HUD
hud = HUD(garden, 100,10)

garden.HUD = hud

view = View([garden, hud], update, eventListener)
