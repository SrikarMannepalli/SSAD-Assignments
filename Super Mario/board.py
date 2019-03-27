import config
import os
import sys
import obspow
from colorama import Fore
import time

arr = [[" " for i in range(400)] for j in range(35)]


class Board(object):
    mariostate = 0
    mariolives = 3
    out = 0
    level = 1
    bullets = 0
    time = 0
    timer = 0

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.score = 0
        self._framechange = 40
        for i in range(1, self.width):
            for j in range(1, self.length):
                arr[i][j] = " "

        self.stringboard = self.return_stringboard()

    def return_stringboard(self):
        self.stringboard = ""
        for i in range(0, self.width):
            self.stringboard += "X"
            for j in range(0, self.length):
                self.stringboard += arr[i][j + config.frame_counter]
            self.stringboard += "X\n"
        cur_time = Board.timer - int(time.time()) + Board.time
        if cur_time == 0:
            print("TIME OUT!!")
            sys.exit()
        self.score = int(time.time()) - Board.time
        self.stringboard += "SCORE: " + \
            str(self.score) + "   LIVES: " + str(Board.mariolives) + "  TIMER: " + str(cur_time) + "\n"
        self.stringboard += "Press 'q' to exit\n"

        return self.stringboard

        # uncomment the following code and comment the above for colors
        
        # for i in range(0,self.width):
        #     self.stringboard+=Fore.YELLOW + "X"
        #     for j in range(0,self.length):
        #         if arr[i][j+config.frame_counter] == config._bricks:
        #             add = config._brickscolor + arr[i][j+config.frame_counter]
        #         elif arr[i][j+config.frame_counter] == config._floor:
        #             add = config._floorcolor + arr[i][j+config.frame_counter]
        #         elif arr[i][j+config.frame_counter] == config._coinbricks:
        #             add = config._coinbrickscolor + arr[i][j+config.frame_counter]

        #         elif arr[i][j+config.frame_counter] == config._mushroombricks:
        #             add = config._mushroombrickscolor + arr[i][j+config.frame_counter]
        #         elif arr[i][j+config.frame_counter] == config._coin:
        #             add = config._coincolor + arr[i][j+config.frame_counter]
        #         elif arr[i][j+config.frame_counter] == config._mushroom:
        #             add = config._mushroomcolor + arr[i][j+config.frame_counter]
        #         elif arr[i][j+config.frame_counter] == config._wall:
        #             add = config._wallcolor + arr[i][j+config.frame_counter]
        #         elif arr[i][j+config.frame_counter] == config._spring:
        #             add = config._springcolor + arr[i][j+config.frame_counter]
        #         elif arr[i][j+config.frame_counter] == config._enemy:
        #             add = config._enemycolor + arr[i][j+config.frame_counter]
        #         elif arr[i][j+config.frame_counter] == config._leftcornor:
        #             add = config._leftcornorcolor + arr[i][j+config.frame_counter]
        #         elif arr[i][j+config.frame_counter] == config._rightcornor:
        #             add = config._rightcornorcolor + arr[i][j+config.frame_counter]
        #         elif arr[i][j+config.frame_counter] == config._marioupper:
        #             add = config._rightcornorcolor + arr[i][j+config.frame_counter]
        #         elif arr[i][j+config.frame_counter] == config._mariolower:
        #             add = config._rightcornorcolor + arr[i][j+config.frame_counter]
        #         elif arr[i][j+config.frame_counter] == config._empty:
        #             add = config._emptycolor + arr[i][j+config.frame_counter]
        #         self.stringboard+=add
        #     self.stringboard+=Fore.YELLOW+"X\n"
        # cur_time = Board.timer - int(time.time())+Board.time
        # if cur_time == 0:
        #     print("TIME OUT!!")
        #     sys.exit()
        # self.score = int(time.time()) - Board.time
        # self.stringboard += "SCORE: " + str(self.score) + "   LIVES: " + str(Board.mariolives)+"  TIMER: "+str(cur_time)+"\n"
        # self.stringboard += "Press 'q' to exit\n"

        # return self.stringboard



    def print_array(self):
        self.update_bullets()
        self.update_mushies()
        self.update_enemies()
        self.update_bossenemies()
        self.update_stars()
        os.system('clear')
        self.stringboard = self.return_stringboard()
        sys.stdout.write(self.stringboard)

    def update_framecounter(self, y):
        if y > self._framechange + config.frame_counter:
            config.frame_counter = config.frame_counter + 1

    def clear_part(self, from_x, from_y, to_x, to_y):
        for i in range(from_x, to_x + 1):
            for j in range(from_y, to_y + 1):
                arr[i][j] = " "

    # all blocks are 2X2
    # in the following function, x and y are the coordinates of the obstacle
    # checks for the collsions in upward direction
    def collision_up_board_update(self, x, y, state):

        if arr[x][y] == config._spring:
            return 1
        elif arr[x][y] == config._bricks:
            if state == 1:
                brick_no = 0
                tempy = y
                while arr[x][tempy] == config._bricks:
                    tempy = tempy - 1
                    brick_no = brick_no + 1

                if brick_no % 2 == 0:
                    self.clear_part(x - 1, y - 1, x, y)
                else:
                    self.clear_part(x - 1, y, x, y + 1)
            return 1
        elif arr[x][y] == config._coinbricks:
            coinblock = obspow.Bricks_Coins()
            brick_no = 0
            tempy = y
            while arr[x][tempy] == config._coinbricks:
                tempy = tempy - 1
                brick_no = brick_no + 1
            if brick_no % 2 == 0:
                coinblock.spawn(x - 1, y - 1, x, y, config._bricks)
            else:
                coinblock.spawn(x - 1, y, x, y + 1, config._bricks)
            coinblock.on_hit_coins(x, y)
            return 1
        elif arr[x][y] == config._mushroombricks:
            mushroomblock = obspow.Bricks_Mushrooms()
            brick_no = 0
            tempy = y
            while arr[x][tempy] == config._mushroombricks:
                tempy = tempy - 1
                brick_no = brick_no + 1
            if brick_no % 2 == 0:
                mushroomblock.spawn(x - 1, y - 1, x, y, config._bricks)
            else:
                mushroomblock.spawn(x - 1, y, x, y + 1, config._bricks)
            mushroomblock.on_hit_mushroom(x, y)
            return 1
        elif arr[x][y] == config._starbricks:
            starblock = obspow.Bricks_Stars()
            brick_no = 0
            tempy = y
            while arr[x][tempy] == config._starbricks:
                tempy = tempy - 1
                brick_no = brick_no + 1
            if brick_no % 2 == 0:
                starblock.spawn(x - 1, y - 1, x, y, config._bricks)
            else:
                starblock.spawn(x - 1, y, x, y + 1, config._bricks)
            starblock.on_hit_star(x, y)
            return 1

    # returns 2 if enemy is to be destroyed
    # destroys enemies in downward direction
    def collision_down_board_update(self, x, y):
        if (arr[x][y] == config._bricks) or (arr[x][y] == config._coinbricks) or (
                arr[x][y] == config._mushroombricks) or (arr[x][y] == config._starbricks):
            return 1
        elif arr[x][y] == config._enemy:
            return 2

    def update_mushies(self):
        for mushies in config.mushrooms_list:
            Board.mariostate = mushies.update()

    def update_stars(self):
        for stars in config.stars_list:
            Board.bullets = stars.update()

    def update_bossenemies(self):
        for enemy in config.bossenemylist:
            enemy.update()

    def update_enemies(self):
        if Board.level == 2:
            for enemy in config.enemylist:
                enemy.update()
        else:
            for enemy in config.enemylist:
                enemy.update_ene_count += 1
                if enemy.speed == 1:
                    mod = 4
                elif enemy.speed == 2:
                    mod = 3
                elif enemy.speed == 3:
                    mod = 2
                else:
                    mod = 1
                if enemy.update_ene_count % mod == 0:
                    enemy.update()

    def update_bullets(self):
        for bullet in config.bullets_list:
            sc = bullet.update()
            if sc == 1:
                self.score += 1
            if sc == 3:
                self.score += 1
