from View import View
from Garden import Garden

def calculations(args):

    return args

def update(args, graphic_elements):

    return args, graphic_elements

#Main

garden = Garden()
view = View([garden], [garden], calculations, update)
