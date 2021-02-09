from View import View
from Garden import Garden
from Tower import Tower
from Pip import Pip
from HUD import HUD
from Enemy import Enemy
import pygame

def update(graphic_elements):
    for g in graphic_elements:
        if isinstance(g, Garden):
            g.update()
        
        elif isinstance(g, Pip):
            next_pos = g.move()
            if next_pos[0] > 0 and next_pos[0] < 896 and next_pos[1] > 0 and next_pos[1] < 768 and not next_pos[2]:
                g.coordinates = (next_pos[0], next_pos[1])
            else:
                graphic_elements.remove(g)
                del g

        elif isinstance(g, Tower):
            g.tick += 1
            if g.tick == g.rate:
                g.tick = 0
                attack = 0
                for enemy in graphic_elements[0].get_ennemies():
                    
                    if attack < g.max_attack:
                        pip = g.attack(enemy)
                        
                        if pip:
                            graphic_elements.append(pip)
                            attack += 1
            if g.name == "hover":
                g.coordinates = (
                    (pygame.mouse.get_pos()[0] - pygame.mouse.get_pos()[0] % 32,
                     pygame.mouse.get_pos()[1] - pygame.mouse.get_pos()[1] % 32))
    return graphic_elements

#Main

garden = Garden()

# Create HUD
hud = HUD(100,10)

view = View([garden,hud], update)
