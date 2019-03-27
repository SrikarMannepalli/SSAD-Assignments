import config
import board
from time import sleep
import common

# all these in the same module have similar properties
# mario_x and mario_y have the coordinates of the upper '0'
#direction is 1 if right else 0


class Creature(object):
    def __init__(self, x, y, denote):
        self._state = 0
        self.jump_height = 0
        self.lives = 1
        self._x = x
        self._y = y
        self.denote = denote

    def spawn(self, old_x, old_y, x, y):
        self._x = x
        self._y = y
        board.arr[old_x][old_y] = config._empty
        board.arr[x][y] = self.denote


class BossEnemy(Creature):
    boss_dead = False
    boss_lives = 3

    def __init__(self, x, y, speed):
        Creature.__init__(self, x, y, "b")
        self.direction = 0
        self.speed = speed
        self.update_ene_count = 0
        self.lives = 3
        self.appender()

    def appender(self):
        config.bossenemylist.append(self)

    def update(self):
        if self.direction == 1:
            if board.arr[self._x + 1][self._y] == config._empty:
                config.bossenemylist.remove(self)
                board.arr[self._x][self._y] = config._empty
                return
            if self._y + 1 == 99 + config.frame_counter:
                self.direction = 0
                return
            if board.arr[self._x][self._y + 1] == config._empty:
                self.spawn(self._x, self._y, self._x, self._y + 1)
            elif board.arr[self._x][self._y + 1] == config._mariolower:
                board.arr[self._x][self._y] = config._empty
                common.mario.lives -= 1
                board.Board.out = 1
                common.mario._x = 28
                common.mario._y = 1
                config.bossenemylist.remove(self)
                board.arr[self._x][self._y] = config._empty
            else:
                self.direction = 0
        else:
            if board.arr[self._x + 1][self._y] == config._empty:
                config.bossenemylist.remove(self)
                board.arr[self._x][self._y] = config._empty
                return
            if self._y - 1 == 1 + config.frame_counter:
                self.direction = 1
                return
            if board.arr[self._x][self._y - 1] == config._empty:
                self.spawn(self._x, self._y, self._x, self._y - 1)
            elif board.arr[self._x][self._y - 1] == config._mariolower:
                board.arr[self._x][self._y] = config._empty
                common.mario.lives -= 1
                board.Board.out = 1
                common.mario._x = 28
                common.mario._y = 1
                config.bossenemylist.remove(self)
                board.arr[self._x][self._y] = config._empty
            else:
                self.direction = 1


class Enemy(Creature):
    def __init__(self, x, y, speed):
        Creature.__init__(self, x, y, "e")
        self.direction = 0
        self.speed = speed
        self.lives = 1
        self.update_ene_count = 0
        self.appender()

    def appender(self):
        config.enemylist.append(self)

    def update(self):
        if self.direction == 1:
            if board.arr[self._x + 1][self._y] == config._empty:
                config.enemylist.remove(self)
                board.arr[self._x][self._y] = config._empty
                return
            if self._y + 1 == 99 + config.frame_counter:
                self.direction = 0
                return
            if board.arr[self._x][self._y + 1] == config._empty:
                self.spawn(self._x, self._y, self._x, self._y + 1)
            elif board.arr[self._x][self._y + 1] == config._mariolower:
                board.arr[self._x][self._y] = config._empty

                if common.mario._state == 1:
                    board.arr[self._x][self._y + 1] = config._empty
                    board.arr[self._x - 1][self._y + 1] = config._empty
                    board.arr[self._x - 2][self._y + 1] = config._empty
                    common.mario._state = 0
                    board.Board.mariostate = 0
                else:
                    common.mario.lives -= 1
                    board.Board.out = 1
                    common.mario._x = 28
                    common.mario._y = 1

                config.enemylist.remove(self)
                board.arr[self._x][self._y] = config._empty
            else:
                self.direction = 0

        else:
            if board.arr[self._x + 1][self._y] == config._empty:
                config.enemylist.remove(self)
                board.arr[self._x][self._y] = config._empty
                return
            if self._y - 1 == 1 + config.frame_counter:
                self.direction = 1
                return
            if board.arr[self._x][self._y - 1] == config._empty:
                self.spawn(self._x, self._y, self._x, self._y - 1)
            elif board.arr[self._x][self._y - 1] == config._mariolower:
                board.arr[self._x][self._y] = config._empty

                if common.mario._state == 1:
                    board.arr[self._x][self._y - 1] = config._empty
                    board.arr[self._x - 1][self._y - 1] = config._empty
                    board.arr[self._x - 2][self._y - 1] = config._empty
                    common.mario._state = 0
                    common.mario.spawn(
                        self._x - 1, self._y - 1, self._x - 1, self._y - 1)
                    board.Board.mariostate = 0
                else:
                    common.mario.lives -= 1
                    board.Board.out = 1
                    common.mario._x = 28
                    common.mario._y = 1

                # config.enemylist.remove(self)
                board.arr[self._x][self._y] = config._empty

            else:
                self.direction = 1


class Mario(Creature):
    def __init__(self, x, y):
        Creature.__init__(self, x, y, "m")
        self._state = 0
        self._upcount = 0
        self.jump_height = 8
        self.lives = 3
        self._x, self._y = self.spawn(x, y, x, y)

    def spawn(self, old_x, old_y, x, y):
        self._x = x
        self._y = y
        if self._state == 0:
            board.arr[old_x][old_y] = config._empty
            board.arr[old_x + 1][old_y] = config._empty
            board.arr[x][y] = config._marioupper
            board.arr[x + 1][y] = config._mariolower

        elif self._state == 1:
            board.arr[old_x][old_y] = config._empty
            board.arr[old_x + 1][old_y] = config._empty
            board.arr[old_x + 2][old_y] = config._empty
            board.arr[x][y] = config._marioupper
            board.arr[x + 1][y] = config._mariolower
            board.arr[x + 2][y] = config._mariolower

        common.scene.update_framecounter(y)

        return_coordinates = []
        return_coordinates.append(x)
        return_coordinates.append(y)
        common.scene.print_array()
        return return_coordinates

    def create_supermario(self):
        return_coordinates = []
        if board.arr[self._x - 1][self._y] == config._empty:
            board.arr[self._x - 1][self._y] = config._marioupper
            board.arr[self._x][self._y] = config._mariolower
            board.arr[self._x + 1][self._y] = config._mariolower
            return_coordinates.append(self._x - 1)
            return_coordinates.append(self._y)
        else:
            board.arr[self._x][self._y] = config._marioupper
            board.arr[self._x + 1][self._y] = config._mariolower
            board.arr[self._x + 2][self._y] = config._mariolower
            return_coordinates.append(self._x)
            return_coordinates.append(self._y)

        return return_coordinates

    def move(self, direction):
        if direction == "UP":
            self._upcount = self._upcount + 1
            try:
                if (board.arr[self._x + 2 + self._state][self._y]
                        == config._spring) and self._upcount == 1:
                    self.jump_height = 10
                    self._x, self._y = self.spawn(
                        self._x, self._y, self._x - 1, self._y)
                elif (board.arr[self._x + 2 + self._state][self._y] == config._bricks) or (board.arr[self._x + 2 + self._state][self._y] == config._coinbricks) or (board.arr[self._x + 2 + self._state][self._y] == config._starbricks) or (board.arr[self._x + 2 + self._state][self._y] == config._mushroombricks) and (self._upcount == 1):
                    self.jump_height = 8
                if (board.arr[self._x -
                              1][self._y] == config._bricks) or (board.arr[self._x -
                                                                           1][self._y] == config._coinbricks) or (board.arr[self._x -
                                                                                                                            1][self._y] == config._mushroombricks) or (board.arr[self._x -
                                                                                                                                                                                 1][self._y] == config._starbricks):
                    self._upcount = self.jump_height
                    ret = common.scene.collision_up_board_update(
                        self._x - 1, self._y, self._state)
                else:
                    if (board.arr[self._x -
                                  1][self._y] == config._empty) or (board.arr[self._x -
                                                                              1][self._y] == config._coin):
                        if board.arr[self._x - 1][self._y] == config._coin:
                            common.scene.score = common.scene.score + 1
                        self._x, self._y = self.spawn(
                            self._x, self._y, self._x - 1, self._y)
                    elif (board.arr[self._x - 1][self._y] == config._mushroom) and (self._state == 0):
                        self._state = 1
                        self._x, self._y = self.create_supermario()
                        for mushies in config.mushrooms_list:
                            if (mushies.x == self._x -
                                    1) and (mushies.y == self._y):
                                config.mushrooms_list.remove(mushies)
                                break
                        self._x, self._y = self.spawn(
                            self._x, self._y, self._x - 1, self._y)
                    elif (board.arr[self._x - 1][self._y] == config._star) and (board.Board.bullets == 0):
                        board.Board.bullets = 1
                        for stars in config.stars_list:
                            if (stars.x == self._x - 1) and (stars.y == self._y):
                                config.stars_list.remove(stars)
                                break
                        self._x, self._y = self.spawn(
                            self._x, self._y, self._x - 1, self._y)
            except IndexError:
                pass
            sleep(0.08)
            if self._upcount == self.jump_height:
                self._upcount = 0

        elif direction == "LEFT":
            if (board.arr[self._x][self._y -
                                   1] == config._coin) or (board.arr[self._x +
                                                                     1][self._y -
                                                                        1] == config._coin) or (board.arr[self._x +
                                                                                                          1 +
                                                                                                          self._state][self._y -
                                                                                                                       1] == config._coin):
                common.scene.score = common.scene.score + 1
                self._x, self._y = self.spawn(
                    self._x, self._y, self._x, self._y - 1)

            elif ((board.arr[self._x][self._y - 1] == config._mushroom) or (board.arr[self._x + 1][self._y - 1] == config._mushroom))and (self._state == 0):
                self._state = 1
                self._x, self._y = self.create_supermario()
                for mushies in config.mushrooms_list:
                    if (mushies.x == self._x - 1) and (mushies.y == self._y):
                        config.mushrooms_list.remove(mushies)
                        break
                self._x, self._y = self.spawn(
                    self._x, self._y, self._x, self._y - 1)

            elif ((board.arr[self._x][self._y - 1] == config._star) or (board.arr[self._x + 1][self._y - 1] == config._star))and (board.Board.bullets == 0):
                board.Board.bullets = 1
                for stars in config.stars_list:
                    if (stars.x == self._x - 1) and (stars.y == self._y):
                        config.stars_list.remove(stars)
                        break
                self._x, self._y = self.spawn(
                    self._x, self._y, self._x, self._y - 1)

            elif (board.arr[self._x][self._y - 1] == config._enemy):
                for enemies in config.enemylist:
                    if (enemies._x == self._x + 1 +
                            self._state) and (enemies._y == self._y - 1):
                        config.enemylist.remove(enemies)
                        board.arr[self._x][self._y + 1] = config._empty
                        board.Board.out = 1
                        self._x = 28
                        self._y = 1
                        break

            elif (board.arr[self._x][self._y - 1] == config._bossenemy):
                for enemies in config.bossenemylist:
                    if (enemies._x == self._x + 1 +
                            self._state) and (enemies._y == self._y - 1):
                        config.bossenemylist.remove(enemies)
                        board.arr[self._x][self._y + 1] = config._empty
                        board.Board.out = 1
                        self._x = 28
                        self._y = 1
                        break

            elif (board.arr[self._x][self._y - 1] == config._empty) and (board.arr[self._x + 1][self._y - 1] == config._empty) and ((board.arr[self._x + 1 + self._state][self._y - 1] == config._empty)):
                self._x, self._y = self.spawn(
                    self._x, self._y, self._x, self._y - 1)

        elif direction == "RIGHT":
            out = 0
            if (board.arr[self._x][self._y +
                                   1] == config._coin) or (board.arr[self._x +
                                                                     1][self._y +
                                                                        1] == config._coin) or (board.arr[self._x +
                                                                                                          1 +
                                                                                                          self._state][self._y +
                                                                                                                       1] == config._coin):
                common.scene.score = common.scene.score + 1
                self._x, self._y = self.spawn(
                    self._x, self._y, self._x, self._y + 1)
            elif ((board.arr[self._x][self._y + 1] == config._mushroom) or (board.arr[self._x + 1][self._y + 1] == config._mushroom))and (self._state == 0):
                self._state = 1
                self._x, self._y = self.create_supermario()
                for mushies in config.mushrooms_list:
                    if (mushies.x == self._x - 1) and (mushies.y == self._y):
                        config.mushrooms_list.remove(mushies)
                        break
                self._x, self._y = self.spawn(
                    self._x, self._y, self._x, self._y + 1)
            elif board.arr[self._x][self._y + 1] == config._enemy:
                out = 1
                for enemies in config.enemylist:
                    if (enemies._x == self._x + 1 +
                            self._state) and (enemies._y == self._y + 1):
                        config.enemylist.remove(enemies)
                        board.arr[self._x][self._y - 1] = config._empty
                        board.Board.out = 1
                        self._x = 28
                        self._y = 1
                        break
            elif (board.arr[self._x][self._y + 1] == config._bossenemy):
                for enemies in config.bossenemylist:
                    if (enemies._x == self._x + 1 +
                            self._state) and (enemies._y == self._y + 1):
                        config.bossenemylist.remove(enemies)
                        board.arr[self._x][self._y - 1] = config._empty
                        board.Board.out = 1
                        self._x = 28
                        self._y = 1
                        break

            elif (board.arr[self._x][self._y + 1] == config._empty) and (board.arr[self._x + 1][self._y + 1] == config._empty) and (board.arr[self._x + 1 + self._state][self._y + 1] == config._empty):
                self._x, self._y = self.spawn(
                    self._x, self._y, self._x, self._y + 1)

        elif direction == "DOWN":
            if board.arr[self._x + 2 + self._state][self._y] == config._coin:
                common.scene.score = common.scene.score + 1
                self._x, self._y = self.spawn(
                    self._x, self._y, self._x + 1, self._y)
            elif (board.arr[self._x + 2][self._y] == config._mushroom) and (self._state == 0):
                self.state = 1
                self._x, self._y = self.create_supermario()
                for mushies in config.mushrooms_list:
                    if (mushies.x == self._x - 1) and (mushies.y == self._y):
                        config.mushrooms_list.remove(mushies)
                        break
                self._x, self._y = self.spawn(
                    self._x, self._y, self._x + 1, self._y)
            elif (board.arr[self._x + 2 + self._state][self._y] == config._star) and (board.Board.bullets == 0):
                board.Board.bullets = 1
                for stars in config.stars_list:
                    if (stars.x == self._x - 1) and (stars.y == self._y):
                        config.stars_list.remove(stars)
                        break
                self._x, self._y = self.spawn(
                    self._x, self._y, self._x + 1, self._y)
            elif board.arr[self._x + 2 + self._state][self._y] == config._enemy:
                common.scene.score += 1
                for enemies in config.enemylist:
                    if (enemies._x == self._x + 2 +
                            self._state) and (enemies._y == self._y):
                        config.enemylist.remove(enemies)
                        break
                self._x, self._y = self.spawn(
                    self._x, self._y, self._x + 1, self._y)
            elif board.arr[self._x + 2 + self._state][self._y] == config._bossenemy:
                common.scene.score += 1
                for enemies in config.bossenemylist:
                    if (enemies._x == self._x + 2 +
                            self._state) and (enemies._y == self._y):
                        enemies.lives -= 1
                        if enemies.lives == 0:
                            BossEnemy.boss_dead = True
                            config.bossenemylist.remove(enemies)
                            self._x, self._y = self.spawn(
                                self._x, self._y, self._x + 1, self._y)
                            break
                        else:
                            if board.arr[self._x +
                                         1 +
                                         self._state][self._y -
                                                      1] == config._empty:
                                config.bossenemylist.remove(enemies)
                                board.arr[self._x + 2 +
                                          self._state][self._y] = config._empty
                                ene = BossEnemy(
                                    self._x + 2 + self._state, self._y - 1, 5)
                                BossEnemy.boss_lives -= 1
                                ene.lives = BossEnemy.boss_lives
                                break
                            else:
                                config.bossenemylist.remove(enemies)
                                board.arr[self._x + 2 +
                                          self._state][self._y] = config._empty
                                ene = BossEnemy(
                                    self._x + 2 + self._state, self._y + 1, 5)
                                BossEnemy.boss_lives -= 1
                                ene.lives = BossEnemy.boss_lives
                                break

            elif board.arr[self._x + 2 + self._state][self._y] == config._empty:
                self._x, self._y = self.spawn(
                    self._x, self._y, self._x + 1, self._y)
                if self._x > 30:
                    self.lives -= 1
                    board.Board.out = 1
                    self._x = 28
                    self._y = 1
                    return
