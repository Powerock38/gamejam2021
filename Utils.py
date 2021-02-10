import pygame

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
            'fire_rate':2,
            'damage':1,
            'range':85,
            'max_attack': 1,
            'energy_consumption':10,
            'sleeping_time': 5,
            'ricochet': False
        },
        'potato' : {
            'path':'assets/fruits-veggies/potato.png',
            'name':'Potato',
            'price':100,
            'description':'blablabla',
            'fire_rate':0.1,
            'damage':100,
            'range':85,
            'max_attack': 1,
            'energy_consumption':1,
            'sleeping_time': 4,
            'ricochet': False
        },

        'pear' : {
            'path':'assets/fruits-veggies/pear.png',
            'name':'Pear',
            'price':20,
            'description':'blablabla',
            'fire_rate':3,
            'damage':1,
            'range':90,
            'max_attack': 1,
            'energy_consumption':9,
            'sleeping_time': 4,
            'ricochet': True
        },
        'pepper' : {
            'path':'assets/fruits-veggies/pepper_green.png',
            'name':'Pepper',
            'price':30,
            'description':'blablabla',
            'fire_rate':0.5,
            'damage':20,
            'range':100,
            'max_attack': 1,
            'energy_consumption':50,
            'sleeping_time': 10,
            'ricochet': False
        },

        'banana' : {
            'path':'assets/fruits-veggies/banana.png',
            'name':'Banana',
            'price':100,
            'description':'blablabla',
            'fire_rate':6,
            'damage':3,
            'range':85,
            'max_attack': 3,
            'energy_consumption':8,
            'sleeping_time': 4,
            'ricochet': False
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
            'sleeping_time': 4,
            'ricochet': False
        },

        'tomato' : {
            'path':'assets/fruits-veggies/tomato.png',
            'name':'Tomato',
            'price':20,
            'description':'blablabla',
            'fire_rate':0.5,
            'damage':5,
            'range':100,
            'max_attack': 1,
            'energy_consumption':2,
            'sleeping_time': 4,
            'ricochet': False
        },
        'carrot' : {
            'path':'assets/fruits-veggies/carrot.png',
            'name':'Carrot',
            'price':50,
            'description':'blablabla',
            'fire_rate':5,
            'damage':10,
            'range':100,
            'max_attack': 1,
            'energy_consumption':1.8,
            'sleeping_time': 4,
            'ricochet': False
        },

        'peach' : {
            'path':'assets/fruits-veggies/peach.png',
            'name':'Peach',
            'price':50,
            'description':'blablabla',
            'fire_rate':1,
            'damage':5,
            'range':100,
            'max_attack': 2,
            'energy_consumption':1.5,
            'sleeping_time': 4,
            'ricochet': False
        },
        'squash' : {
            'path':'assets/fruits-veggies/squash.png',
            'name':'Squash',
            'price':20,
            'description':'blablabla',
            'fire_rate':1,
            'damage':5,
            'range':100,
            'max_attack': 1,
            'energy_consumption':3.5,
            'sleeping_time': 4,
            'ricochet': False
        },

        'orange' : {
            'path':'assets/fruits-veggies/orange.png',
            'name':'Orange',
            'price':28,
            'description':'blablabla',
            'fire_rate':2,
            'damage':2,
            'range':100,
            'max_attack': 3,
            'energy_consumption':2,
            'sleeping_time': 4,
            'ricochet': False
        },
        'aubergine' : {
            'path':'assets/fruits-veggies/aubergine.png',
            'name':'Aubergine',
            'price':200,
            'description':'blablabla',
            'fire_rate':2,
            'damage':10,
            'range':300,
            'max_attack':1,
            'energy_consumption':2,
            'sleeping_time': 4,
            'ricochet': False
        },

        'cherry' : {
            'path':'assets/fruits-veggies/cherry.png',
            'name':'Cherry',
            'price':250,
            'description':'blablabla',
            'fire_rate':5,
            'damage':3,
            'range':150,
            'max_attack': 4,
            'energy_consumption':2,
            'sleeping_time': 4,
            'ricochet': False
        },
        'broccoli' : {
            'path':'assets/fruits-veggies/broccoli.png',
            'name':'Broccoli',
            'price':1000,
            'description':'blablabla',
            'fire_rate':10,
            'damage':10,
            'range':200,
            'max_attack': 1,
            'energy_consumption':3.5,
            'sleeping_time': 4,
            'ricochet': False
        }
    }

    ENEMIES = {
            'cow' : {
                'path': 'assets/sprites/cow.png',
                'hp': 100,
                'speed': 0.5,
                'water': 1
            },
            'chicken' : {
                'path': 'assets/sprites/chicken.png',
                'hp': 10,
                'speed': 1,
                'water': 3
            },
            'bat' : {
                'path': 'assets/sprites/bat.png',
                'hp': 10,
                'speed': 2.5,
                'water': 1
            },
            'dog' : {
                'path': 'assets/sprites/dog.png',
                'hp': 50,
                'speed': 2,
                'water': 1
            },
            'fox' : {
                'path': 'assets/sprites/fox.png',
                'hp': 40,
                'speed': 2,
                'water': 1
            },
            'frog' : {
                'path': 'assets/sprites/frog.png',
                'hp': 100,
                'speed': 0.5,
                'water': 1
            },
            'hyena' : {
                'path': 'assets/sprites/hyena.png',
                'hp': 100,
                'speed': 2,
                'water': 1
            },
            'monkey' : {
                'path': 'assets/sprites/monkey.png',
                'hp': 100,
                'speed': 0.5,
                'water': 1
            },
            'rabbit' : {
                'path': 'assets/sprites/rabbit.png',
                'hp': 30,
                'speed': 2,
                'water': 10
            },
            'rat' : {
                'path': 'assets/sprites/rat.png',
                'hp': 5,
                'speed': 0.5,
                'water': 1
            },
        }

    WAVES = (
        (5 * ('rat', 80)),
        
        (7 * ('rat', 70)),
        
        (10 * ('rat', 60) +
         3 * ('chicken', 90)),

        (15 * ('rat', 50) +
         7 * ('chicken', 75)),
        
        (1 * ('rabbit', 120)),

         (30 * ('rat', 40) +
         1 * ('rabbit', 300)),
          
         (40 * ('rat', 40) +
         10 * ('chicken', 60) +
         1 * ('rabbit', 240))
    )

    for id, tw in TOWERS.items():
        tw['sprite'] = pygame.image.load(tw['path'])

    for id, en in ENEMIES.items():
        spritesheet = pygame.image.load(en['path'])
        sprite_list = []
        for direction in range(4):
            frames = []
            for frame in range(3):
                frames.append(spritesheet.subsurface(((32 * frame, 32 * direction), (32, 32))))
            sprite_list.append(frames)
        
        en['sprites'] = sprite_list
