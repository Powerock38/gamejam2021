import pygame


class Utils:

    GRAY = (89, 89, 89)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (115, 182, 254)
    RED = (255, 0, 0)
    GREEN = (50, 255, 0)

    TOWERS = {
        'apple': {
            'path': 'assets/fruits-veggies/apple_red.png',
            'name': 'Apple',
            'price': 5,
            'description': 'blablabla',
            'fire_rate': 2,
            'damage': 1,
            'range': 85,
            'max_attack': 1,
            'energy_consumption': 10,
            'sleeping_time': 5,
            'ricochet': False,
            'path_border': False,
            'path_mine': False
        },
        'potato': {
            'path': 'assets/fruits-veggies/potato.png',
            'name': 'Potato',
            'price': 10,
            'description': 'blablabla',
            'fire_rate': 10,
            'damage': 10,
            'range': 16,
            'max_attack': 1,
            'energy_consumption': 100,
            'sleeping_time': 10,
            'ricochet': False,
            'path_border': False,
            'path_mine': True
        },

        'pear': {
            'path': 'assets/fruits-veggies/pear.png',
            'name': 'Pear',
            'price': 20,
            'description': 'blablabla',
            'fire_rate': 3,
            'damage': 1,
            'range': 90,
            'max_attack': 1,
            'energy_consumption': 9,
            'sleeping_time': 4,
            'ricochet': True,
            'path_border': False,
            'path_mine': False
        },
        'pepper': {
            'path': 'assets/fruits-veggies/pepper_green.png',
            'name': 'Pepper',
            'price': 30,
            'description': 'blablabla',
            'fire_rate': 0.5,
            'damage': 20,
            'range': 100,
            'max_attack': 1,
            'energy_consumption': 50,
            'sleeping_time': 10,
            'ricochet': False,
            'path_border': False,
            'path_mine': False
        },

        'banana': {
            'path': 'assets/fruits-veggies/banana.png',
            'name': 'Banana',
            'price': 100,
            'description': 'blablabla',
            'fire_rate': 6,
            'damage': 3,
            'range': 85,
            'max_attack': 3,
            'energy_consumption': 8,
            'sleeping_time': 4,
            'ricochet': False,
            'path_border': False,
            'path_mine': False
        },
        'lettuce': {
            'path': 'assets/fruits-veggies/lettuce.png',
            'name': 'Lettuce',
            'price': 200,
            'description': 'blablabla',
            'fire_rate': 35,
            'damage': 0.2,
            'range': 50,
            'max_attack': 10,
            'energy_consumption': 1,
            'sleeping_time': 10,
            'ricochet': False,
            'path_border': True,
            'path_mine': False
        },

        'tomato': {
            'path': 'assets/fruits-veggies/tomato.png',
            'name': 'Tomato',
            'price': 20,
            'description': 'blablabla',
            'fire_rate': 0.5,
            'damage': 5,
            'range': 100,
            'max_attack': 1,
            'energy_consumption': 2,
            'sleeping_time': 4,
            'ricochet': False,
            'path_border': False,
            'path_mine': False
        },
        'carrot': {
            'path': 'assets/fruits-veggies/carrot.png',
            'name': 'Carrot',
            'price': 50,
            'description': 'blablabla',
            'fire_rate': 5,
            'damage': 10,
            'range': 100,
            'max_attack': 1,
            'energy_consumption': 1.8,
            'sleeping_time': 4,
            'ricochet': False,
            'path_border': False,
            'path_mine': False
        },

        'peach': {
            'path': 'assets/fruits-veggies/peach.png',
            'name': 'Peach',
            'price': 50,
            'description': 'blablabla',
            'fire_rate': 1,
            'damage': 5,
            'range': 100,
            'max_attack': 2,
            'energy_consumption': 1.5,
            'sleeping_time': 4,
            'ricochet': False,
            'path_border': False,
            'path_mine': False
        },
        'squash': {
            'path': 'assets/fruits-veggies/squash.png',
            'name': 'Squash',
            'price': 20,
            'description': 'blablabla',
            'fire_rate': 1,
            'damage': 5,
            'range': 100,
            'max_attack': 1,
            'energy_consumption': 3.5,
            'sleeping_time': 4,
            'ricochet': False,
            'path_border': False,
            'path_mine': False
        },

        'orange': {
            'path': 'assets/fruits-veggies/orange.png',
            'name': 'Orange',
            'price': 28,
            'description': 'blablabla',
            'fire_rate': 2,
            'damage': 2,
            'range': 100,
            'max_attack': 3,
            'energy_consumption': 2,
            'sleeping_time': 4,
            'ricochet': False,
            'path_border': False,
            'path_mine': False
        },
        'aubergine': {
            'path': 'assets/fruits-veggies/aubergine.png',
            'name': 'Aubergine',
            'price': 200,
            'description': 'blablabla',
            'fire_rate': 2,
            'damage': 10,
            'range': 300,
            'max_attack': 1,
            'energy_consumption': 2,
            'sleeping_time': 4,
            'ricochet': False,
            'path_border': False,
            'path_mine': False
        },

        'cherry': {
            'path': 'assets/fruits-veggies/cherry.png',
            'name': 'Cherry',
            'price': 250,
            'description': 'blablabla',
            'fire_rate': 5,
            'damage': 3,
            'range': 150,
            'max_attack': 4,
            'energy_consumption': 2,
            'sleeping_time': 4,
            'ricochet': False,
            'path_border': False,
            'path_mine': False
        },
        'broccoli': {
            'path': 'assets/fruits-veggies/broccoli.png',
            'name': 'Broccoli',
            'price': 1000,
            'description': 'blablabla',
            'fire_rate': 10,
            'damage': 10,
            'range': 200,
            'max_attack': 1,
            'energy_consumption': 3.5,
            'sleeping_time': 4,
            'ricochet': False,
            'path_border': False,
            'path_mine': False
        }
    }

    ENEMIES = {
        'cow': {
            'path': 'assets/sprites/cow.png',
            'hp': 150,
            'speed': 0.5,
            'water': 20,
            'fly': False
        },
        'chicken': {
            'path': 'assets/sprites/chicken.png',
            'hp': 10,
            'speed': 1,
            'water': 3,
            'fly': False
        },
        'bat': {
            'path': 'assets/sprites/bat.png',
            'hp': 50,
            'speed': 2,
            'water': 25,
            'fly': True
        },
        'dog': {
            'path': 'assets/sprites/dog.png',
            'hp': 999,
            'speed': 2,
            'water': 1,
            'fly': False
        },
        'fox': {
            'path': 'assets/sprites/fox.png',
            'hp': 999,
            'speed': 2,
            'water': 1,
            'fly': False
        },
        'frog': {
            'path': 'assets/sprites/frog.png',
            'hp': 999,
            'speed': 0.5,
            'water': 1,
            'fly': False
        },
        'hyena': {
            'path': 'assets/sprites/hyena.png',
            'hp': 999,
            'speed': 2,
            'water': 1,
            'fly': False
        },
        'monkey': {
            'path': 'assets/sprites/monkey.png',
            'hp': 999,
            'speed': 0.5,
            'water': 1,
            'fly': False
        },
        'rabbit': {
            'path': 'assets/sprites/rabbit.png',
            'hp': 30,
            'speed': 2,
            'water': 10,
            'fly': False
        },
        'rat': {
            'path': 'assets/sprites/rat.png',
            'hp': 5,
            'speed': 0.5,
            'water': 1,
            'fly': False
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
         1 * ('rabbit', 240)),
         
        (2 * ('cow', 600)),

        (3 * ('cow', 540) +
         10 * ('chicken', 120) +
         3 * ('rabbit', 240)),

        (10 * ('cow', 480)),

        (5 * ('bat', 600))
    )

    for id, tw in TOWERS.items():
        tw['sprite'] = pygame.image.load(tw['path'])

    for id, en in ENEMIES.items():
        spritesheet = pygame.image.load(en['path'])
        sprite_list = []
        for direction in range(4):
            frames = []
            for frame in range(3):
                frames.append(spritesheet.subsurface(
                    ((32 * frame, 32 * direction), (32, 32))))
            sprite_list.append(frames)

        en['sprites'] = sprite_list
