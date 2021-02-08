from View import View
from Garden import Garden
from Tower import Tower
from Pip import Pip
from HUD import HUD

def update(graphic_elements):
    for g in graphic_elements:
        if isinstance(g, Garden):
            g.update()
        
        elif isinstance(g, Pip):
            if g.move()[0] > 0 and g.move()[0] < 1024 and g.move()[1] > 0 and g.move()[1] < 768:
                g.set_coordinates(g.move())
            else :
                graphic_elements.remove(g)
                del g
                
    return graphic_elements

#Main

garden = Garden()

garden.spawnEnemy()

towertest = Tower("assets/fruits-veggies/Acorn.png","Acorn",1,1,(5*32,10*32))

# Create HUD
hud = HUD(100,10)

view = View([garden,hud,towertest], update)
