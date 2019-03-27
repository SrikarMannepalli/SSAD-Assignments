import config
import board
# from common import mario as mario
# if direction is 1 goes in right direction


class Mushroom(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 0

    def appender(self):
        config.mushrooms_list.append(self)

    def update(self):
        state = 0
        if board.arr[self.x + 1][self.y] != config._empty:
            if board.arr[self.x + 1][self.y] == config._marioupper:
                state = 1
                board.arr[self.x][self.y] = config._empty
                config.mushrooms_list.remove(self)
                return state
            if self.direction == 1:
                if self.y == 97 + config.frame_counter:
                    self.direction = 0
                elif board.arr[self.x][self.y + 1] == config._empty:
                    board.arr[self.x][self.y] = config._empty
                    board.arr[self.x][self.y + 1] = config._mushroom
                    self.y = self.y + 1
                elif (board.arr[self.x][self.y + 1] == config._marioupper) or (board.arr[self.x][self.y + 1] == config._mariolower):
                    state = 1
                    board.arr[self.x][self.y] = config._empty
                    config.mushrooms_list.remove(self)
                else:
                    self.direction = 0
            else:
                if self.y == 1 + config.frame_counter:
                    self.direction = 1
                elif board.arr[self.x][self.y - 1] == config._empty:
                    board.arr[self.x][self.y] = config._empty
                    board.arr[self.x][self.y - 1] = config._mushroom
                    self.y = self.y - 1
                elif (board.arr[self.x][self.y - 1] == config._mariolower) or (board.arr[self.x][self.y - 1] == config._marioupper):
                    state = 1
                    board.arr[self.x][self.y] = " "
                    config.mushrooms_list.remove(self)
                else:
                    self.direction = 1
        else:
            board.arr[self.x][self.y] = config._empty
            if board.arr[self.x + 1][self.y] == config._marioupper:
                state = 1
                config.mushrooms_list.remove(self)
            else:
                board.arr[self.x + 1][self.y] = config._mushroom
                self.x = self.x + 1
                if self.x == 31:
                    config.mushrooms_list.remove(self)
                    board.arr[self.x][self.y] = config._empty

        return state


class Star(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 0

    def appender(self):
        config.stars_list.append(self)

    def update(self):
        state = 0
        if board.arr[self.x + 1][self.y] != config._empty:
            if board.arr[self.x + 1][self.y] == config._marioupper:
                state = 1
                board.arr[self.x][self.y] = config._empty
                config.stars_list.remove(self)
                return state
            if self.direction == 1:
                if self.y == 97 + config.frame_counter:
                    self.direction = 0
                elif board.arr[self.x][self.y + 1] == config._empty:
                    board.arr[self.x][self.y] = config._empty
                    board.arr[self.x][self.y + 1] = config._star
                    self.y = self.y + 1
                elif (board.arr[self.x][self.y + 1] == config._marioupper) or (board.arr[self.x][self.y + 1] == config._mariolower):
                    state = 1
                    board.arr[self.x][self.y] = config._empty
                    config.stars_list.remove(self)
                else:
                    self.direction = 0
            else:
                if self.y == 1 + config.frame_counter:
                    self.direction = 1
                elif board.arr[self.x][self.y - 1] == config._empty:
                    board.arr[self.x][self.y] = config._empty
                    board.arr[self.x][self.y - 1] = config._star
                    self.y = self.y - 1
                elif (board.arr[self.x][self.y - 1] == config._mariolower) or (board.arr[self.x][self.y - 1] == config._marioupper):
                    state = 1
                    board.arr[self.x][self.y] = " "
                    config.stars_list.remove(self)
                else:
                    self.direction = 1
        else:
            board.arr[self.x][self.y] = config._empty
            if board.arr[self.x + 1][self.y] == config._marioupper:
                state = 1
                config.stars_list.remove(self)
            else:
                board.arr[self.x + 1][self.y] = config._star
                self.x = self.x + 1
                if self.x == 31:
                    config.stars_list.remove(self)
                    board.arr[self.x][self.y] = config._empty

        return state


class Bullet(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 0
        self.appender()

    def appender(self):
        config.bullets_list.append(self)

    def update(self):
        score = 0
        if self.y + 1 == 97 + config.frame_counter:
            board.arr[self.x][self.y] = config._empty
            config.bullets_list.remove(self)
        elif board.arr[self.x][self.y + 1] == config._empty:
            board.arr[self.x][self.y] = config._empty
            board.arr[self.x][self.y + 1] = config._bullet
            self.y = self.y + 1
        elif board.arr[self.x][self.y + 1] == config._enemy:
            score = 1
            board.arr[self.x][self.y] = config._empty
            board.arr[self.x][self.y + 1] = config._empty
            for enemy in config.enemylist:
                if (enemy._x == self.x) and (enemy._y == self.y + 1):
                    config.enemylist.remove(enemy)
                    break
            config.bullets_list.remove(self)

        else:
            board.arr[self.x][self.y] = config._empty
            config.bullets_list.remove(self)

        return score
