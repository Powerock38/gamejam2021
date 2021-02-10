
class Utils:

    GRAY = (89,89,89)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    BLUE = (115,182,254)
    RED = (255,0,0)
    GREEN = (50,255,0)

    TOWERS = {
        'apple' : {
            'path':'assets/fruits-veggies/apple_red.png',
            'name':'Apple',
            'price':5,
            'description':'blablabla',
            'fire_rate':15,
            'damage':1,
            'range':100,
            'max_attack': 1,
            'energy_consumption':1,
            'sleeping_time': 4
        },
        'potato' : {
            'path':'assets/fruits-veggies/potato.png',
            'name':'Potato',
            'price':56,
            'description':'blablabla',
            'fire_rate':10,
            'damage':3,
            'range':5,
            'max_attack': 1,
            'energy_consumption':1,
            'sleeping_time': 4
        },

        'pear' : {
            'path':'assets/fruits-veggies/pear.png',
            'name':'Pear',
            'price':7,
            'description':'blablabla',
            'fire_rate':20,
            'damage':1,
            'range':100,
            'max_attack': 1,
            'energy_consumption':1,
            'sleeping_time': 4
        },
        'pepper' : {
            'path':'assets/fruits-veggies/pepper_green.png',
            'name':'Pepper',
            'price':78,
            'description':'blablabla',
            'fire_rate':40,
            'damage':0.5,
            'range':100,
            'max_attack': 3,
            'energy_consumption':2.5,
            'sleeping_time': 4
        },

        'banana' : {
            'path':'assets/fruits-veggies/banana.png',
            'name':'Banana',
            'price':10,
            'description':'blablabla',
            'fire_rate':25,
            'damage':1.5,
            'range':100,
            'max_attack': 3,
            'energy_consumption':1.5,
            'sleeping_time': 4
        },
        'lettuce' : {
            'path':'assets/fruits-veggies/lettuce.png',
            'name':'Lettuce',
            'price':100,
            'description':'blablabla',
            'fire_rate':20,
            'damage':5,
            'range':100,
            'max_attack': 2,
            'energy_consumption':2.5,
            'sleeping_time': 4
        },

        'tomato' : {
            'path':'assets/fruits-veggies/tomato.png',
            'name':'Tomato',
            'price':14,
            'description':'blablabla',
            'fire_rate':20,
            'damage':1,
            'range':100,
            'max_attack': 1,
            'energy_consumption':2,
            'sleeping_time': 4
        },
        'carrot' : {
            'path':'assets/fruits-veggies/carrot.png',
            'name':'Carrot',
            'price':140,
            'description':'blablabla',
            'fire_rate':3,
            'damage':10,
            'range':100,
            'max_attack': 1,
            'energy_consumption':1.8,
            'sleeping_time': 4
        },

        'peach' : {
            'path':'assets/fruits-veggies/peach.png',
            'name':'Peach',
            'price':20,
            'description':'blablabla',
            'fire_rate':15,
            'damage':2,
            'range':100,
            'max_attack': 2,
            'energy_consumption':1.5,
            'sleeping_time': 4
        },
        'squash' : {
            'path':'assets/fruits-veggies/squash.png',
            'name':'Squash',
            'price':200,
            'description':'blablabla',
            'fire_rate':20,
            'damage':0.6,
            'range':7,
            'max_attack': 5,
            'energy_consumption':3.5,
            'sleeping_time': 4
        },

        'orange' : {
            'path':'assets/fruits-veggies/orange.png',
            'name':'Orange',
            'price':28,
            'description':'blablabla',
            'fire_rate':2,
            'damage':2,
            'range':100,
            'max_attack': 2,
            'energy_consumption':2,
            'sleeping_time': 4
        },
        'aubergine' : {
            'path':'assets/fruits-veggies/aubergine.png',
            'name':'Aubergine',
            'price':280,
            'description':'blablabla',
            'fire_rate':40,
            'damage':0.6,
            'range':100,
            'max_attack':1,
            'energy_consumption':2,
            'sleeping_time': 4
        },

        'cherry' : {
            'path':'assets/fruits-veggies/cherry.png',
            'name':'Cherry',
            'price':40,
            'description':'blablabla',
            'fire_rate':5,
            'damage':3,
            'range':100,
            'max_attack': 2,
            'energy_consumption':2,
            'sleeping_time': 4
        },
        'broccoli' : {
            'path':'assets/fruits-veggies/broccoli.png',
            'name':'Broccoli',
            'price':350,
            'description':'blablabla',
            'fire_rate':1,
            'damage':15,
            'range':100,
            'max_attack': 1,
            'energy_consumption':3.5,
            'sleeping_time': 4
        }
    }

    ENEMIES = {
        'farmer' : {
            'path': 'assets/farmer.png',
            'hp': 100,
            'speed': 0.5,
            'water': 1
        },
    }
