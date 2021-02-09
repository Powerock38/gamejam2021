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

    return graphic_elements

def eventListener(event, elements):
    if isinstance(elements[0], Garden):
        garden = elements[0]
        hud = elements[1]

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if event.button == 1:
                if mx >= 896:
                    hud.buy(mx, my)
                elif mx < 896:
                    garden.putTower()
    else:
        m_pos = pygame.mouse.get_pos()
        if m_pos[0] >= 295 and m_pos[0] <= 728 and m_pos[1] >= 350 and m_pos[1] <= 672:
            garden = Garden()

            # Create HUD
            hud = HUD(garden, 100, 10)

            garden.HUD = hud

            elements = [garden, hud]

    return elements
    
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

menu = Menu()

view = View([menu], update, eventListener)
