from View import View
from Garden import Garden
from Tower import Tower
from Pip import Pip
from HUD import HUD

def update(graphic_elements):

    return graphic_elements

#Main

garden = Garden()

garden.spawnEnemy()

towertest = Tower("assets/fruits-veggies/Acorn.png","Acorn",1,1,(5*32,10*32))

# Create HUD
hud = HUD(100,10)

view = View([garden,hud,towertest], update)
