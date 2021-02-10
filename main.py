from View import View
from Garden import Garden
from HUD import HUD
from Menu import Menu
import pygame

def update(graphic_elements):
    for g in graphic_elements:
        if isinstance(g, Garden):
            g.update()

    return graphic_elements

def eventListener(event, elements):
    if isinstance(elements[0], Garden):
        garden = elements[0]
        hud = elements[1]

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = pygame.mouse.get_pos()
            if event.button == 1:
                if mx >= 896:
                    hud.buy(mx, my)
                elif mx < 896:
                    garden.putTower()

        #Delete the tower that is holding
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            if garden.holding != None:
                # The method will detect that garden.holding is not None and will refund
                hud.refund()
            else:
                garden.removeTower()

    else:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            m_pos = pygame.mouse.get_pos()
            menu = elements[0]
            if menu.page == "Menu":
                if m_pos[0] >= 295 and m_pos[0] <= 728 and m_pos[1] >= 350 and m_pos[1] <= 472:

                    #Start game
                    garden = Garden()
                    hud = HUD(garden, 10, 1000)
                    garden.HUD = hud

                    elements = [garden, hud]
                    
                elif m_pos[0] >= 341 and m_pos[0] <= 683 and m_pos[1] >= 492 and m_pos[1] <= 588:
                    menu.page = "Rules"
                    
                elif m_pos[0] >= 341 and m_pos[0] <= 683 and m_pos[1] >= 608 and m_pos[1] <= 704:
                    menu.page = "Credits"
            
            elif menu.page == "Rules":
                if m_pos[0] >= 295 and m_pos[0] <= 728 and m_pos[1] >= 608 and m_pos[1] <= 730:
                    menu.page = "Menu"
                
            elif menu.page == "Credits":
                if m_pos[0] >= 295 and m_pos[0] <= 728 and m_pos[1] >= 608 and m_pos[1] <= 730:
                    menu.page = "Menu"

    return elements

#Main

menu = Menu()

view = View([menu], update, eventListener)
