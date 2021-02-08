import pygame

class Garden:

    def __init__(self, tiles):
        self.__tiles = tiles

    def draw(self, screen):
        
        image_path = "assets/tilesets/plowed_soil.png"

        image = pygame.image.load(image_path)
        
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

        for i in range(len(self.__tiles)):
            for j in range(len(self.__tiles[i])):
                if self.__tiles[i][j] > 0:
                    screen.blit(tile2, (32 * j, 32 * i))
                else:
                    if i > 0 and self.__tiles[i - 1][j]:
                        if j > 0 and self.__tiles[i][j - 1]:
                            screen.blit(tile7, (32 * j, 32 * i))
                        elif j < len(self.__tiles[i]) - 1 and self.__tiles[i][j + 1]:
                            screen.blit(tile8, (32 * j, 32 * i))
                        else:
                            screen.blit(tile3, (32 * j, 32 * i))
                    elif j > 0 and self.__tiles[i][j - 1]:
                        if i > 0 and self.__tiles[i - 1][j]:
                            screen.blit(tile7, (32 * j, 32 * i))
                        elif i < len(self.__tiles) - 1 and self.__tiles[i + 1][j]:
                            screen.blit(tile9, (32 * j, 32 * i))
                        else:
                            screen.blit(tile4, (32 * j, 32 * i))
                    elif i < len(self.__tiles) - 1 and self.__tiles[i + 1][j]:
                        if j > 0 and self.__tiles[i][j - 1]:
                            screen.blit(tile9, (32 * j, 32 * i))
                        elif j < len(self.__tiles[i]) - 1 and self.__tiles[i][j + 1]:
                            screen.blit(tile10, (32 * j, 32 * i))
                        else:
                            screen.blit(tile5, (32 * j, 32 * i))
                    elif j < len(self.__tiles[i]) - 1 and self.__tiles[i][j + 1]:
                        if i > 0 and self.__tiles[i - 1][j]:
                            screen.blit(tile8, (32 * j, 32 * i))
                        elif i < len(self.__tiles) - 1 and self.__tiles[i + 1][j]:
                            screen.blit(tile10, (32 * j, 32 * i))
                        else:
                            screen.blit(tile6, (32 * j, 32 * i))
                    elif i > 0 and j > 0 and self.__tiles[i - 1][j - 1]:
                        screen.blit(tile11, (32 * j, 32 * i))
                    elif i < len(self.__tiles) - 1 and j > 0 and self.__tiles[i + 1][j - 1]:
                        screen.blit(tile12, (32 * j, 32 * i))
                    elif i > 0 and j < len(self.__tiles[i]) - 1 and self.__tiles[i - 1][j + 1]:
                        screen.blit(tile13, (32 * j, 32 * i))
                    elif i < len(self.__tiles) - 1 and j < len(self.__tiles[i]) - 1 and self.__tiles[i + 1][j + 1]:
                        screen.blit(tile14, (32 * j, 32 * i))
                    else:
                        screen.blit(tile1, (32 * j, 32 * i))
                    
