from View import View
from Garden import Garden
from Tower import Tower

def calculations(args):

    return args

def update(args, graphic_elements):

    return args, graphic_elements

#Main

#towerTest= Tower('assets/fruits-veggies/Acorn.png','Acorn',1,1)
#view = View([garden], [garden, towerTest], calculations, update)
garden = Garden([])
view = View([garden], [garden], calculations, update)
