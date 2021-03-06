import pygame
import random
import math
from Utils import Utils
from Enemy import Enemy
from Tower import Tower

class Garden:
    pygame.mixer.init()

    musicLoad_watering_can = pygame.mixer.Sound("assets/musics/watering_can.ogg")
    musicLoad_invalid = pygame.mixer.Sound("assets/musics/invalid.ogg")
    musicLoad_ouch = pygame.mixer.Sound("assets/musics/ouch.ogg")
    musicLoad_put = pygame.mixer.Sound("assets/musics/putTower.ogg")
    musicLoad_remove = pygame.mixer.Sound("assets/musics/removeTower.ogg")
    musicLoad = pygame.mixer.Sound("assets/musics/main.ogg")

    def __init__(self, tiles=[]):
        #Initilalisation of the music of the Garden
        self.channel = pygame.mixer.Channel(0)
        self.channel.play(Garden.musicLoad, -1)
        self.channel.set_volume(0.4)

        self.HUD = None
        self.__tick = 0
        self.__wave_enemy_index = 0
        self.__interWave = False

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

                r  = random.randint(0, len(allowed_dirs) - 1)
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
                            
        self.lastTile = count
        self.tiles = tiles
        self.enemies = []
        self.towers = []
        self.pips = []
        self.holding = None

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
        tile15 = image.subsurface(((0, 0), (32, 32)))
        tile16 = image.subsurface(((0, 160), (32, 32)))
        tile17 = image.subsurface(((32, 160), (32, 32)))
        tile18 = image.subsurface(((64, 160), (32, 32)))

        width = len(self.tiles[0]) * 32
        height = len(self.tiles) * 32
        self.__background = pygame.Surface((width, height))

        tmp_garden = []

        for i in range(len(self.tiles)):
            tmp_row = []
            for j in range(len(self.tiles[i])):
                if self.tiles[i][j] > 0:
                    tmp_row.append(self.tiles[i][j])
                    self.__background.blit(tile2, (32 * j, 32 * i))
                else:
                    if i > 0 and self.tiles[i - 1][j]:
                        tmp_row.append(-1)
                        if j > 0 and self.tiles[i][j - 1]:
                            self.__background.blit(tile7, (32 * j, 32 * i))
                        elif j < len(self.tiles[i]) - 1 and self.tiles[i][j + 1]:
                            self.__background.blit(tile8, (32 * j, 32 * i))
                        else:
                            self.__background.blit(tile3, (32 * j, 32 * i))
                    elif j > 0 and self.tiles[i][j - 1]:
                        tmp_row.append(-1)
                        if i > 0 and self.tiles[i - 1][j]:
                            self.__background.blit(tile7, (32 * j, 32 * i))
                        elif i < len(self.tiles) - 1 and self.tiles[i + 1][j]:
                            self.__background.blit(tile9, (32 * j, 32 * i))
                        else:
                            self.__background.blit(tile4, (32 * j, 32 * i))
                    elif i < len(self.tiles) - 1 and self.tiles[i + 1][j]:
                        tmp_row.append(-1)
                        if j > 0 and self.tiles[i][j - 1]:
                            self.__background.blit(tile9, (32 * j, 32 * i))
                        elif j < len(self.tiles[i]) - 1 and self.tiles[i][j + 1]:
                            self.__background.blit(tile10, (32 * j, 32 * i))
                        else:
                            self.__background.blit(tile5, (32 * j, 32 * i))
                    elif j < len(self.tiles[i]) - 1 and self.tiles[i][j + 1]:
                        tmp_row.append(-1)
                        if i > 0 and self.tiles[i - 1][j]:
                            self.__background.blit(tile8, (32 * j, 32 * i))
                        elif i < len(self.tiles) - 1 and self.tiles[i + 1][j]:
                            self.__background.blit(tile10, (32 * j, 32 * i))
                        else:
                            self.__background.blit(tile6, (32 * j, 32 * i))
                    elif i > 0 and j > 0 and self.tiles[i - 1][j - 1]:
                        tmp_row.append(-1)
                        self.__background.blit(tile11, (32 * j, 32 * i))
                    elif (i < len(self.tiles) - 1
                        and j > 0
                        and self.tiles[i + 1][j - 1]):
                        tmp_row.append(-1)
                        self.__background.blit(tile12, (32 * j, 32 * i))
                    elif (i > 0
                        and j < len(self.tiles[i]) - 1
                        and self.tiles[i - 1][j + 1]):
                        tmp_row.append(-1)
                        self.__background.blit(tile13, (32 * j, 32 * i))
                    elif (i < len(self.tiles) - 1
                        and j < len(self.tiles[i]) - 1
                        and self.tiles[i + 1][j + 1]):
                        tmp_row.append(-1)
                        self.__background.blit(tile14, (32 * j, 32 * i))
                    else:
                        tmp_row.append(0)
                        r = random.randint(0, 99)
                        if not r:
                            self.__background.blit(tile15, (32 * j, 32 * i))
                        elif not r - 1:
                            self.__background.blit(tile16, (32 * j, 32 * i))
                        elif not r - 2:
                            self.__background.blit(tile17, (32 * j, 32 * i))
                        elif not r - 3:
                            self.__background.blit(tile18, (32 * j, 32 * i))
                        else:
                            self.__background.blit(tile1, (32 * j, 32 * i))
            tmp_garden.append(tmp_row)
        
        self.__background.blit(pygame.image.load('assets/tilesets/farmer.png'), (800, 736))

        self.tiles = tmp_garden

    def update(self):
        # waves
        wave_nb = self.HUD.get_level()
        
        if self.HUD.get_level() > len(Utils.WAVES) - 1:
            custom_wave = []

            for id, en in Utils.ENEMIES.items():
                how_many =  min(100 + wave_nb, max(1, int((Utils.MIN_SCORE * 100 * wave_nb) / math.log(en['score'], 1.02))))
                for _ in range(how_many):
                    custom_wave.append(id)
            
            random.shuffle(custom_wave)

            custom_time = max(5, 120 - wave_nb - len(Utils.WAVES))

            for i in range(1, len(custom_wave) * 2, 2):
                custom_wave.insert(i, custom_time)

            Utils.WAVES[wave_nb % len(Utils.WAVES)] = tuple(custom_wave)

        wave = Utils.WAVES[wave_nb % len(Utils.WAVES)]
        
        if self.__wave_enemy_index == len(wave):
            self.__wave_enemy_index = 0
            self.__interWave = True

        if self.__interWave:
            if len(self.enemies) == 0:
                time = max(120, self.__tick)
            else:
                time = max(0, 2400 - 120 * wave_nb)
        else:
            time = wave[self.__wave_enemy_index + 1]
        
        if self.__tick >= time:
            if self.__interWave:
                self.HUD.set_level(self.HUD.get_level() + 1)
                self.__interWave = False
            enemy = Utils.ENEMIES[wave[self.__wave_enemy_index]]
            self.enemies = [Enemy(enemy, [1, 0])] + self.enemies
            self.__tick = 0
            self.__wave_enemy_index += 2
        else:
            self.__tick += 1

        #update towers
        for t in self.towers:
            pips, water = t.update(self.enemies)
            if water:
                self.HUD.set_water(self.HUD.get_water() + water)
            if pips:
                for pip in pips:
                    self.pips.append(pip)

        #update pips
        for p in self.pips:
            deadEnemy = p.update()
            
            if deadEnemy:
                if deadEnemy.hp <= 0 and p.ricochet:
                    pos1 = p.coordinates
                    target = None
                    dist_min = 0
                    for enemy in self.enemies[::-1]:
                        pos2 = (enemy.pos[0] * 32 + enemy.pos_in_tile[0] + 16, enemy.pos[1] * 32 + enemy.pos_in_tile[1] + 16)
                        distance = math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

                        if (not dist_min or distance < dist_min) and distance <= 64:
                            target = enemy
                    p.enemy = target
                else:
                    self.pips.remove(p)

                for p2 in self.pips:
                    if p2.enemy == deadEnemy:
                        p2.enemy = None

                    if p2.enemy == None:
                        self.pips.remove(p2)
                
        #update enemies
        for en in self.enemies:
            if en.hp <= 0:
                self.HUD.set_water(self.HUD.get_water() + en.water)
                self.enemies.remove(en)
            else:
                x = en.pos[0]
                y = en.pos[1]
                onTile = self.tiles[y][x]

                if onTile == self.lastTile:
                    #ouch.ogg
                    channel = pygame.mixer.Channel(2)
                    channel.play(Garden.musicLoad_ouch)
                    channel.set_volume(0.25)

                    self.enemies.remove(en)
                    self.HUD.set_life(self.HUD.get_life() - 1)
                    if self.HUD.get_life() <= 0:
                        pygame.event.post(pygame.event.Event(pygame.USEREVENT))
                else:
                    possibleMoves = []

                    if en.confusedTime > 0:
                        if y > 0 and self.tiles[y - 1][x] not in (0, -1) and self.tiles[y - 1][x] < onTile:
                            possibleMoves.append(0)

                        if x + 1 < len(self.tiles[y]) and self.tiles[y][x + 1] not in (0, -1) and self.tiles[y][x + 1] < onTile:
                            possibleMoves.append(1)

                        if y + 1 < len(self.tiles) and self.tiles[y + 1][x] not in (0, -1) and self.tiles[y + 1][x] < onTile:
                            possibleMoves.append(2)

                        if x > 0 and self.tiles[y][x - 1] not in (0, -1) and self.tiles[y][x - 1] < onTile:
                            possibleMoves.append(3)
                    else:
                        if y > 0 and self.tiles[y - 1][x] > onTile:
                            possibleMoves.append(0)

                        if x + 1 < len(self.tiles[y]) and self.tiles[y][x + 1] > onTile:
                            possibleMoves.append(1)

                        if y + 1 < len(self.tiles) and self.tiles[y + 1][x] > onTile:
                            possibleMoves.append(2)

                        if x > 0 and self.tiles[y][x - 1] > onTile:
                            possibleMoves.append(3)

                    move = None

                    if possibleMoves:
                        move = random.choice(possibleMoves)
                    
                    en.update(move)
                    


    def draw(self, screen):
        screen.blit(self.__background, (0,0))

        for t in self.towers:
            t.draw(screen)

        for p in self.pips:
            p.draw(screen)

        for en in self.enemies:
            en.draw(screen)

        if self.holding != None:
            mx, my = pygame.mouse.get_pos()
            if mx < 896:
                x_32, y_32 = (mx - mx % 32, my - my % 32)
                screen.blit(self.holding[1], (x_32, y_32))
                pygame.draw.circle(screen, (255, 0, 0, 128), (x_32 + 16, y_32 + 16), self.holding[0]['range'], 1)

    def hold(self, tower):
        img = tower['sprite'].convert_alpha()
        img.fill((255, 255, 255, 128), special_flags=pygame.BLEND_RGBA_MULT) 
        self.holding = (
            tower,
            img,
        )

    def putTower(self):
        """
        Place a tower at mouse postion if holding one\n
        Parameters :\n
        \ttower : the tower that will be placed
        """

        mx, my = pygame.mouse.get_pos()

        if self.holding != None:
            if mx < 896:
                x, y = (mx - mx % 32, my - my % 32)
                x_mh, y_mh = (x // 32, y // 32)

                pos_already_taken = False
                
                allowed_tile = self.tiles[y_mh][x_mh] == 0

                if self.holding[0]['path_border']:
                    allowed_tile = self.tiles[y_mh][x_mh] == -1
                
                if self.holding[0]['path_mine']:
                    allowed_tile = self.tiles[y_mh][x_mh] > 0

                if allowed_tile:
                    for otherTower in self.towers:
                        if otherTower.coordinates == (x,y):
                            pos_already_taken = True
                            break

                    if not pos_already_taken:
                        self.towers.append(Tower(self.holding[0], (x,y)))
                        self.holding = None
  
                if pos_already_taken or not allowed_tile:
                    #invalid placement sound effect
                    channel = pygame.mixer.Channel(1)
                    channel.play(Garden.musicLoad_invalid)
                    channel.set_volume(0.5)
        else:
            if self.HUD.get_water() > 0:
                for tower in self.towers:
                    if not tower.generator and tower.energy > 0 and tower.energy <= tower.energyMax // 2:
                        x,y = tower.coordinates
                        if mx >= x and mx <= x + 32 and my >= y and my <= y + 32:
                            tower.energy = tower.energyMax
                            self.HUD.set_water(self.HUD.get_water() - 1)
                            #set the music when we water a tower
                            channel = pygame.mixer.Channel(1)
                            channel.play(Garden.musicLoad_watering_can)
                            channel.set_volume(0.5)


    def removeTower(self):
        """
        Remove a tower at mouse postion\n
        Parameters :\n
        \ttower : the tower that will be removed
        """

        mx, my = pygame.mouse.get_pos()
        mx -= mx % 32
        my -= my % 32
        for t in self.towers:
            posx, posy = t.coordinates
            posx -= posx % 32
            posy -= posy % 32
            if mx == posx and my == posy:
                self.HUD.set_water(self.HUD.get_water() + t.price // 2)
                self.towers.remove(t)
                #set the music when we remove a tower
                channel = pygame.mixer.Channel(1)
                channel.play(Garden.musicLoad_remove)
                channel.set_volume(0.1)
                #water refund sound effect
                channel2 = pygame.mixer.Channel(2)
                channel2.play(self.HUD.sound_water_refund)
                channel2.set_volume(0.2)
