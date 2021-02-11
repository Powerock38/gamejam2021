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
            'path_mine': False,
            'generator': False,
            'poison': 0,
            'confusing': 0
        },
        'potato': {
            'path': 'assets/fruits-veggies/potato.png',
            'name': 'Potato',
            'price': 10,
            'description': 'blablabla',
            'fire_rate': 10,
            'damage': 15,
            'range': 16,
            'max_attack': 1,
            'energy_consumption': 100,
            'sleeping_time': 10,
            'ricochet': False,
            'path_border': False,
            'path_mine': True,
            'generator': False,
            'poison': 0,
            'confusing': 0
        },

        'pear': {
            'path': 'assets/fruits-veggies/pear.png',
            'name': 'Pear',
            'price': 20,
            'description': 'blablabla',
            'fire_rate': 3,
            'damage': 2,
            'range': 90,
            'max_attack': 1,
            'energy_consumption': 9,
            'sleeping_time': 4,
            'ricochet': True,
            'path_border': False,
            'path_mine': False,
            'generator': False,
            'poison': 0,
            'confusing': 0
        },
        'pepper': {
            'path': 'assets/fruits-veggies/pepper_green.png',
            'name': 'Pepper',
            'price': 50,
            'description': 'blablabla',
            'fire_rate': 0.5,
            'damage': 50,
            'range': 100,
            'max_attack': 1,
            'energy_consumption': 50,
            'sleeping_time': 10,
            'ricochet': False,
            'path_border': False,
            'path_mine': False,
            'generator': False,
            'poison': 0,
            'confusing': 0
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
            'path_mine': False,
            'generator': False,
            'poison': 0,
            'confusing': 0
        },
        'lettuce': {
            'path': 'assets/fruits-veggies/lettuce.png',
            'name': 'Lettuce',
            'price': 200,
            'description': 'blablabla',
            'fire_rate': 30,
            'damage': 0.5,
            'range': 50,
            'max_attack': 10,
            'energy_consumption': 0.5,
            'sleeping_time': 10,
            'ricochet': False,
            'path_border': True,
            'path_mine': False,
            'generator': False,
            'poison': 0,
            'confusing': 0
        },

        'tomato': {
            'path': 'assets/fruits-veggies/tomato.png',
            'name': 'Tomato',
            'price': 250,
            'description': 'blablabla',
            'fire_rate': 1,
            'damage': 5,
            'range': 0,
            'max_attack': 1,
            'energy_consumption': 2,
            'sleeping_time': 10,
            'ricochet': False,
            'path_border': False,
            'path_mine': False,
            'generator': True,
            'poison': 0,
            'confusing': 0
        },
        'carrot': {
            'path': 'assets/fruits-veggies/carrot.png',
            'name': 'Carrot',
            'price': 500,
            'description': 'blablabla',
            'fire_rate': 1,
            'damage': 50,
            'range': 300,
            'max_attack': 1,
            'energy_consumption': 25,
            'sleeping_time': 5,
            'ricochet': False,
            'path_border': False,
            'path_mine': False,
            'generator': False,
            'poison': 0,
            'confusing': 0
        },

        'peach': {
            'path': 'assets/fruits-veggies/peach.png',
            'name': 'Peach',
            'price': 1000,
            'description': 'blablabla',
            'fire_rate': 5,
            'damage': 10,
            'range': 150,
            'max_attack': 1,
            'energy_consumption': 5,
            'sleeping_time': 5,
            'ricochet': False,
            'path_border': False,
            'path_mine': False,
            'generator': False,
            'poison': 0,
            'confusing': 300
        },
        'squash': {
            'path': 'assets/fruits-veggies/squash.png',
            'name': 'Squash',
            'price': 20,
            'description': 'blablabla',
            'fire_rate': 1,
            'damage': 1,
            'range': 120,
            'max_attack': 1,
            'energy_consumption': 5,
            'sleeping_time': 5,
            'ricochet': False,
            'path_border': False,
            'path_mine': False,
            'generator': False,
            'poison': 600,
            'confusing': 0
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
            'path_mine': False,
            'generator': False,
            'poison': 0,
            'confusing': 0
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
            'path_mine': False,
            'generator': False,
            'poison': 0,
            'confusing': 0
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
            'path_mine': False,
            'generator': False,
            'poison': 0,
            'confusing': 0
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
            'path_mine': False,
            'generator': False,
            'poison': 0,
            'confusing': 0
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
            'speed': 1.5,
            'water': 25,
            'fly': True
        },
        'dog': {
            'path': 'assets/sprites/dog.png',
            'hp': 2000,
            'speed': 1.25,
            'water': 500,
            'fly': False
        },
        'fox': {
            'path': 'assets/sprites/fox.png',
            'hp': 500,
            'speed': 0.75,
            'water': 150,
            'fly': False
        },
        'frog': {
            'path': 'assets/sprites/frog.png',
            'hp': 3000,
            'speed': 0.25,
            'water': 200,
            'fly': False
        },
        'hyena': {
            'path': 'assets/sprites/hyena.png',
            'hp': 100000,
            'speed': 1.25,
            'water': 50000,
            'fly': False
        },
        'monkey': {
            'path': 'assets/sprites/monkey.png',
            'hp': 150,
            'speed': 1,
            'water': 50,
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
        'eagle': {
            'path': 'assets/sprites/eagle.png',
            'hp': 2500,
            'speed': 2.5,
            'water': 2000,
            'fly': True
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

        (5 * ('bat', 600)),

        (10 * ('cow', 300) +
         20 * ('chicken', 30) +
         10 * ('bat', 120)),

        (5 * ('monkey', 60)),

        (1 * ('frog', 60)),

        (1 * ('frog', 600) +
         50 * ('rat', 10) +
         10 * ('cow', 60) +
         30 * ('chicken', 20) +
         15 * ('rabbit', 30) +
         10 * ('bat', 60) +
         10 * ('cow', 60)),

        (2 * ('frog', 300) +
         120 * ('rat', 5) +
         10 * ('monkey', 60)),

        (5 * ('monkey', 60)),

        (1 * ('fox', 60)),

        (3 * ('fox', 60) +
         120 * ('bat', 20) +
         10 * ('monkey', 60)),

        (1 * ('dog', 60) +
         1200 * ('rat', 1) +
         120 * ('cow', 5) +
         60 * ('bat', 10)),

        (3 * ('dog', 60) +
         50 * ('rat', 1) +
         60 * ('bat', 10)),

        (5 * ('eagle', 10)),

        (100 * ('rat', 30) +
         90 * ('chicken', 30) +
         80 * ('rabbit', 30) +
         70 * ('cow', 30) +
         60 * ('bat', 30) +
         50 * ('monkey', 30) +
         40 * ('frog', 30) +
         30 * ('fox', 30) +
         20 * ('dog', 30) +
         10 * ('eagle', 240)),

        (1 * ('hyena', 60)),

        (1 * ('rat', 300) +
         1 * ('chicken', 300) +
         1 * ('rabbit', 300) +
         1 * ('cow', 300) +
         1 * ('bat', 300) +
         1 * ('monkey', 300) +
         1 * ('frog', 300) +
         1 * ('fox', 300) +
         1 * ('dog', 300) +
         1 * ('eagle', 300) +
         1 * ('hyena', 300) +

         1 * ('rat', 240) +
         1 * ('chicken', 240) +
         1 * ('rabbit', 240) +
         1 * ('cow', 240) +
         1 * ('bat', 240) +
         1 * ('monkey', 240) +
         1 * ('frog', 240) +
         1 * ('fox', 240) +
         1 * ('dog', 240) +
         1 * ('eagle', 240) +
         1 * ('hyena', 240) +

         1 * ('rat', 180) +
         1 * ('chicken', 180) +
         1 * ('rabbit', 180) +
         1 * ('cow', 180) +
         1 * ('bat', 180) +
         1 * ('monkey', 180) +
         1 * ('frog', 180) +
         1 * ('fox', 180) +
         1 * ('dog', 180) +
         1 * ('eagle', 180) +
         1 * ('hyena', 180) +

         1 * ('rat', 120) +
         1 * ('chicken', 120) +
         1 * ('rabbit', 120) +
         1 * ('cow', 120) +
         1 * ('bat', 120) +
         1 * ('monkey', 120) +
         1 * ('frog', 120) +
         1 * ('fox', 120) +
         1 * ('dog', 120) +
         1 * ('eagle', 120) +
         1 * ('hyena', 120) +

         1 * ('rat', 60) +
         1 * ('chicken', 60) +
         1 * ('rabbit', 60) +
         1 * ('cow', 60) +
         1 * ('bat', 60) +
         1 * ('monkey', 60) +
         1 * ('frog', 60) +
         1 * ('fox', 60) +
         1 * ('dog', 60) +
         1 * ('eagle', 60) +
         1 * ('hyena', 60) +

         1 * ('rat', 30) +
         1 * ('chicken', 30) +
         1 * ('rabbit', 30) +
         1 * ('cow', 30) +
         1 * ('bat', 30) +
         1 * ('monkey', 30) +
         1 * ('frog', 30) +
         1 * ('fox', 30) +
         1 * ('dog', 30) +
         1 * ('eagle', 30) +
         1 * ('hyena', 30) +

         1 * ('rat', 10) +
         1 * ('chicken', 10) +
         1 * ('rabbit', 10) +
         1 * ('cow', 10) +
         1 * ('bat', 10) +
         1 * ('monkey', 10) +
         1 * ('frog', 10) +
         1 * ('fox', 10) +
         1 * ('dog', 10) +
         1 * ('eagle', 10) +
         1 * ('hyena', 10))
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
