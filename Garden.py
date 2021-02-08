import pygame
import random
from Enemy import Enemy
from random import randint

class Garden:
    def __init__(self, tiles = []):
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        width = 28
        height = 24

        tiles = [[0 for _ in range(width)] for _ in range(height)]

        count = 1
        pos = [0, 1]
        tiles[0][1] = 1

        while pos[1] != width - 1 and pos[0] != height - 1:

            r = randint(0, 3)
            
            for i in range(3):
                if pos[0] + directions[r][0] >= 0 and pos[1] + directions[r][1] >= 0 and pos[0] + directions[r][0] < height and pos[1] + directions[r][1] < width:
                    if tiles[pos[0] + directions[r][0]][pos[1] + directions[r][1]] == 0:
                        pos[0] += directions[r][0]
                        pos[1] += directions[r][1]
                        count += 1
                        tiles[pos[0]][pos[1]] = count
                    else:
                        pos[0] += directions[r][0]
                        pos[1] += directions[r][1]
                        count = tiles[pos[0]][pos[1]]
                        for i in range(len(tiles)):
                            for j in range(len(tiles[i])):
                                if tiles[i][j] > count:
                                    tiles[i][j] = 0
                            
        self.__tiles = tiles
        self.__enemies = []

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

        width = len(self.__tiles[0]) * 32
        height = len(self.__tiles) * 32
        self.__background = pygame.Surface((width, height))

        for i in range(len(self.__tiles)):
            for j in range(len(self.__tiles[i])):
                if self.__tiles[i][j] > 0:
                    self.__background.blit(tile2, (32 * j, 32 * i))
                else:
                    if i > 0 and self.__tiles[i - 1][j]:
                        if j > 0 and self.__tiles[i][j - 1]:
                            self.__background.blit(tile7, (32 * j, 32 * i))
                        elif j < len(self.__tiles[i]) - 1 and self.__tiles[i][j + 1]:
                            self.__background.blit(tile8, (32 * j, 32 * i))
                        else:
                            self.__background.blit(tile3, (32 * j, 32 * i))
                    elif j > 0 and self.__tiles[i][j - 1]:
                        if i > 0 and self.__tiles[i - 1][j]:
                            self.__background.blit(tile7, (32 * j, 32 * i))
                        elif i < len(self.__tiles) - 1 and self.__tiles[i + 1][j]:
                            self.__background.blit(tile9, (32 * j, 32 * i))
                        else:
                            self.__background.blit(tile4, (32 * j, 32 * i))
                    elif i < len(self.__tiles) - 1 and self.__tiles[i + 1][j]:
                        if j > 0 and self.__tiles[i][j - 1]:
                            self.__background.blit(tile9, (32 * j, 32 * i))
                        elif j < len(self.__tiles[i]) - 1 and self.__tiles[i][j + 1]:
                            self.__background.blit(tile10, (32 * j, 32 * i))
                        else:
                            self.__background.blit(tile5, (32 * j, 32 * i))
                    elif j < len(self.__tiles[i]) - 1 and self.__tiles[i][j + 1]:
                        if i > 0 and self.__tiles[i - 1][j]:
                            self.__background.blit(tile8, (32 * j, 32 * i))
                        elif i < len(self.__tiles) - 1 and self.__tiles[i + 1][j]:
                            self.__background.blit(tile10, (32 * j, 32 * i))
                        else:
                            self.__background.blit(tile6, (32 * j, 32 * i))
                    elif i > 0 and j > 0 and self.__tiles[i - 1][j - 1]:
                        self.__background.blit(tile11, (32 * j, 32 * i))
                    elif (
                        i < len(self.__tiles) - 1
                        and j > 0
                        and self.__tiles[i + 1][j - 1]
                    ):
                        self.__background.blit(tile12, (32 * j, 32 * i))
                    elif (
                        i > 0
                        and j < len(self.__tiles[i]) - 1
                        and self.__tiles[i - 1][j + 1]
                    ):
                        self.__background.blit(tile13, (32 * j, 32 * i))
                    elif (
                        i < len(self.__tiles) - 1
                        and j < len(self.__tiles[i]) - 1
                        and self.__tiles[i + 1][j + 1]
                    ):
                        self.__background.blit(tile14, (32 * j, 32 * i))
                    else:
                        self.__background.blit(tile1, (32 * j, 32 * i))

                pygame.font.init()
                self.__background.blit(pygame.font.Font('assets/font/comic_book.otf', 27).render(str(self.__tiles[i][j]) if self.__tiles[i][j] else '', True, (255,255,255)), (j * 32, i * 32))

    def update(self):
        for en in self.__enemies:
            x = en.pos[0]
            y = en.pos[1]
            onTile = self.__tiles[y][x]

            possibleMoves = []

            """
                0
              3 X 1
                2
            """

            if y > 0 and self.__tiles[y - 1][x] > onTile:
                possibleMoves.append(0)

            if x + 1 < len(self.__tiles[y]) and self.__tiles[y][x + 1] > onTile:
                possibleMoves.append(1)

            if y + 1 < len(self.__tiles) and self.__tiles[y + 1][x] > onTile:
                possibleMoves.append(2)

            if x > 0 and self.__tiles[y][x - 1] > onTile:
                possibleMoves.append(3)

            if len(possibleMoves):
                en.move(random.choice(possibleMoves))
            else:
                print('fermier arrivé au bout')
                self.__enemies.remove(en)


    def draw(self, screen):
        screen.blit(self.__background, (0,0))

        for en in self.__enemies:
            en.draw(screen)


    def spawnEnemy(self):
        sprite = pygame.image.load("assets/farmer.png")
        self.__enemies.append(Enemy(sprite, pos = [1, 0]))
