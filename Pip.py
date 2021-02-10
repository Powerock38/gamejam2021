import pygame
import math


class Pip:
    """
    Class Pip :\n
    Attibuts :\n
    \tcoordinates : the coordinates of the pip (int) (default (10,10))
    \tdamage : damage of the pip (int) (default 1)
    """

    numPip = 0

    pygame.mixer.init()
    pygame.mixer.set_num_channels(1000)

    sprite = pygame.image.load('assets/particles/bullet.png').subsurface(((14, 14), (4, 4)))
    musicLoad = pygame.mixer.Sound("assets/musics/attack.ogg")

    def __init__(self, coordinates, enemy, damage = 1):
        """
        Constructor of the pips\n
        Arguments :\n
        \tcoordinates : the coordinates of the pip (int) (default (10,10))
        \tdamage : damage of the pip (int) (default 1)\n
        Return :\n
        None
        """
        #Set the music for the pip
        channel = pygame.mixer.Channel(Pip.numPip % 1000 + 2)
        channel.play(Pip.musicLoad, 0)
        channel.set_volume(0.08)
        Pip.numPip += 1

        self.coordinates = (coordinates[0] + 16, coordinates[1] + 16)
        self.enemy = enemy
        self.damage = damage
    
    def move(self):
        """
        Move the pip with the direction given in the constructor
        """
        if self.enemy:
            pos1 = self.coordinates
            pos2 = (self.enemy.pos[0] * 32 + self.enemy.pos_in_tile[0] + 16, self.enemy.pos[1] * 32 + self.enemy.pos_in_tile[1] + 16)
            delta1 = pos2[0] - pos1[0]
            delta2 = pos2[1] - pos1[1]
            distance = math.sqrt((delta1)**2 + (delta2)**2)
            target_touched = distance < 5
            angle = math.atan2(delta2, delta1)
            return (self.coordinates[0] + math.cos(angle) * 10, self.coordinates[1] + math.sin(angle) * 10, target_touched)
        else:
            return (self.coordinates[0], self.coordinates[1], True)

    def draw(self, screen):
        """
        Attack a position\n
        Parameters :\n
        \tscreen : the pygame screen\n
        Return :\n
        None
        """

        screen.blit(Pip.sprite, self.coordinates)

    def update(self):
        """
        Return :\n
        deadEnemy
        """
        
        nx, ny, touched = self.move()
        if nx > 0 and nx < 896 and ny > 0 and ny < 768 and not touched:
            self.coordinates = (nx, ny)
        else:
            if self.enemy:
                self.enemy.hp -= self.damage
            return self.enemy
