from View import View
from Garden import Garden
from HUD import HUD

def calculations(args):

    return args

def update(args, graphic_elements):

    return args, graphic_elements

#Main

garden = Garden([])
# Initilase HUD with 100% life and 100 water money
hud = HUD(100, 100)

view = View([garden], [garden, hud], calculations, update)
