from View import View
from Garden import Garden
from Tower import Tower
from Pip import Pip
from HUD import HUD

def update(graphic_elements):
    for elem in graphic_elements:
        if isinstance(elem, Pip):
            if elem.move()[0] > 0 and elem.move()[0] < 1024 and elem.move()[1] > 0 and elem.move()[1] < 768:
                elem.set_coordinates(elem.move())
            else :
                graphic_elements.remove(elem)
                del elem

    return graphic_elements

#Main

garden = Garden()

garden.spawnEnemy()

# Create HUD
hud = HUD(100,10,10)

view = View([garden,hud], update)
