import pygame
import random
from Enemy import Enemy
from random import randint

class Garden:
    def __init__(self, tiles = []):
        self.__tick = 0
        self.__tickMax = 200

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        width = 28
        height = 24

        count = 1
        while count < 100:
            
            tiles = [[0 for _ in range(width)] for _ in range(height)]

            count = 1
            pos = [0, 1]
            tiles[0][1] = 1
            oldr = 0

            while not (pos[1] == width - 3 and pos[0] == height - 1):
                allowed_dirs = directions[:]
                allowed_dirs.remove(allowed_dirs[(oldr + 2) % 4])
                
                if [1, 0] in allowed_dirs:
                    if not (pos[0] + 1 < height - 1 or (pos[0] + 1 < height and pos[1] == width - 3)):
                        allowed_dirs.remove([1, 0])
                    elif pos[0] % 3 != 0 and (pos[1] - 1) % 3 != 0:
                        allowed_dirs.remove([1, 0])
                if [0, 1] in allowed_dirs:
                    if pos[1] + 1 >= width - 1 or not pos[0]:
                        allowed_dirs.remove([0, 1])
                    elif (pos[0] - 1) % 3 != 0 and pos[1] % 3 != 0:
                        allowed_dirs.remove([0, 1])
                if [-1, 0] in allowed_dirs:
                    if pos[0] - 1 <= 0:
                        allowed_dirs.remove([-1, 0])
                    elif (pos[0] - 2) % 3 != 0 and (pos[1] - 1) % 3 != 0:
                        allowed_dirs.remove([-1, 0])
                if [0, -1] in allowed_dirs:
                    if pos[1] - 1 <= 0:
                        allowed_dirs.remove([0, -1])
                    elif (pos[0] - 1) % 3 != 0 and (pos[1] - 2) % 3 != 0:
                        allowed_dirs.remove([0, -1])

                if pos[1] == 26:
                    allowed_dirs = [[0, -1]]

                r  = randint(0, len(allowed_dirs) - 1)
                direction = allowed_dirs[r]
                oldr = directions.index(direction)
                
                next_pos = [pos[0] + direction[0], pos[1] + direction[1]]
                
                if tiles[next_pos[0]][next_pos[1]] == 0:
                    pos[0] += direction[0]
                    pos[1] += direction[1]
                    count += 1
                    tiles[pos[0]][pos[1]] = count
                else:
                    count = tiles[next_pos[0]][next_pos[1]]
                    for i in range(len(tiles)):
                        for j in range(len(tiles[i])):
                            if tiles[i][j] > count:
                                tiles[i][j] = 0
                    pos[0] += direction[0]
                    pos[1] += direction[1]
                            
        self.tiles = tiles
        self.enemies = []

        image = pygame.image.load("assets/tilesets/plowed_soil.png")

        tile1 = image.subsurface(((32, 96), (32, 32)))
        tile2 = image.subsurface(((0, 32), (32, 32)))
        tile3 = image.subsurface(((32, 64), (32, 32)))
        tile4 = image.subsurface(((0, 96), (32, 32)))
        tile5 = image.subsurface(((32, 128), (32, 32)))
        tile6 = image.subsurface(((64, 96), (32, 32)))
        tile7 = image.subsurface(((0, 64), (32, 32)))
        tile8 = image.subsurface(((64, 64), (32, 32)))
        tile9 = image.subsurface(((0, 128), (32, 32)))
        tile10 = image.subsurface(((64, 128), (32, 32)))
        tile11 = image.subsurface(((64, 32), (32, 32)))
        tile12 = image.subsurface(((64, 0), (32, 32)))
        tile13 = image.subsurface(((32, 32), (32, 32)))
        tile14 = image.subsurface(((32, 0), (32, 32)))

        width = len(self.tiles[0]) * 32
        height = len(self.tiles) * 32
        self.__background = pygame.Surface((width, height))

        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                if self.tiles[i][j] > 0:
                    self.__background.blit(tile2, (32 * j, 32 * i))
                else:
                    if i > 0 and self.tiles[i - 1][j]:
                        if j > 0 and self.tiles[i][j - 1]:
                            self.__background.blit(tile7, (32 * j, 32 * i))
                        elif j < len(self.tiles[i]) - 1 and self.tiles[i][j + 1]:
                            self.__background.blit(tile8, (32 * j, 32 * i))
                        else:
                            self.__background.blit(tile3, (32 * j, 32 * i))
                    elif j > 0 and self.tiles[i][j - 1]:
                        if i > 0 and self.tiles[i - 1][j]:
                            self.__background.blit(tile7, (32 * j, 32 * i))
                        elif i < len(self.tiles) - 1 and self.tiles[i + 1][j]:
                            self.__background.blit(tile9, (32 * j, 32 * i))
                        else:
                            self.__background.blit(tile4, (32 * j, 32 * i))
                    elif i < len(self.tiles) - 1 and self.tiles[i + 1][j]:
                        if j > 0 and self.tiles[i][j - 1]:
                            self.__background.blit(tile9, (32 * j, 32 * i))
                        elif j < len(self.tiles[i]) - 1 and self.tiles[i][j + 1]:
                            self.__background.blit(tile10, (32 * j, 32 * i))
                        else:
                            self.__background.blit(tile5, (32 * j, 32 * i))
                    elif j < len(self.tiles[i]) - 1 and self.tiles[i][j + 1]:
                        if i > 0 and self.tiles[i - 1][j]:
                            self.__background.blit(tile8, (32 * j, 32 * i))
                        elif i < len(self.tiles) - 1 and self.tiles[i + 1][j]:
                            self.__background.blit(tile10, (32 * j, 32 * i))
                        else:
                            self.__background.blit(tile6, (32 * j, 32 * i))
                    elif i > 0 and j > 0 and self.tiles[i - 1][j - 1]:
                        self.__background.blit(tile11, (32 * j, 32 * i))
                    elif (
                        i < len(self.tiles) - 1
                        and j > 0
                        and self.tiles[i + 1][j - 1]
                    ):
                        self.__background.blit(tile12, (32 * j, 32 * i))
                    elif (
                        i > 0
                        and j < len(self.tiles[i]) - 1
                        and self.tiles[i - 1][j + 1]
                    ):
                        self.__background.blit(tile13, (32 * j, 32 * i))
                    elif (
                        i < len(self.tiles) - 1
                        and j < len(self.tiles[i]) - 1
                        and self.tiles[i + 1][j + 1]
                    ):
                        self.__background.blit(tile14, (32 * j, 32 * i))
                    else:
                        self.__background.blit(tile1, (32 * j, 32 * i))

    def update(self):
        if self.__tick > self.__tickMax:
            self.spawnEnemy()
            self.__tick = 0
            self.__tickMax = max(30, self.__tickMax - 1)
        else:
            self.__tick += 1

        for en in self.enemies:
            x = en.pos[0]
            y = en.pos[1]
            onTile = self.tiles[y][x]

            possibleMoves = []

            if y > 0 and self.tiles[y - 1][x] > onTile:
                possibleMoves.append(0)

            if x + 1 < len(self.tiles[y]) and self.tiles[y][x + 1] > onTile:
                possibleMoves.append(1)

            if y + 1 < len(self.tiles) and self.tiles[y + 1][x] > onTile:
                possibleMoves.append(2)

            if x > 0 and self.tiles[y][x - 1] > onTile:
                possibleMoves.append(3)

            if len(possibleMoves):
                en.move(random.choice(possibleMoves))
            else:
                self.enemies.remove(en)


    def draw(self, screen):
        screen.blit(self.__background, (0,0))

        for en in self.enemies:
            en.draw(screen)


    def spawnEnemy(self):
        sprite = pygame.image.load("assets/farmer.png")
        self.enemies = [Enemy(sprite, pos = [1, 0])] + self.enemies
