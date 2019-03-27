import config
import board
import powerups


class Obstacle(object):
    def __init__(self, denote):
        self.is_destroyable = False
        self.is_scorable = False
        self.mushroom_out = False

    def spawn(self, from_x, from_y, to_x, to_y, denote):
        for i in range(from_x, to_x + 1):
            for j in range(from_y, to_y + 1):
                board.arr[i][j] = denote

    def clear_obs(from_x, from_y, to_x, to_y):
        for i in range(from_x, to_x + 1):
            for j in range(from_y, to_y + 1):
                board.arr[i][j] = config._empty


class Coins(Obstacle):
    def __init__(self, denote=config._coin):
        Obstacle.__init__(self, denote)
        self.is_destroyable = True
        self.is_scorable = True


class Bricks_Coins(Obstacle):
    def __init__(self, denote=config._coinbricks):
        Obstacle.__init__(self, denote)
        self.is_scorable = True
        self.mushroom_out = False
        self.is_a_coin = True
        self.is_not_a_mushroom = False

    def on_hit_coins(self, hit_x, hit_y):
        if self.is_scorable:
            self.spawn(hit_x - 2, hit_y, hit_x - 2, hit_y, config._coin)
            self.is_scorable = False


class Bricks_Mushrooms(Obstacle):
    def __init__(self, denote=config._mushroombricks):
        Obstacle.__init__(self, denote)
        self.is_scorable = False
        self.mushroom_out = True
        self.is_a_mushroom = True
        self.is_not_a_coin = False

    def on_hit_mushroom(self, hit_x, hit_y):
        if self.mushroom_out:
            self.spawn(hit_x - 2, hit_y, hit_x - 2, hit_y, config._mushroom)
            mush = powerups.Mushroom(hit_x - 2, hit_y)
            mush.appender()
            self.mushroom_out = False


class Bricks_Stars(Obstacle):
    def __init__(self, denote=config._starbricks):
        Obstacle.__init__(self, denote)
        self.is_scorable = False
        self.mushroom_out = False
        self.is_a_mushroom = False
        self.is_not_a_coin = False
        self.star_out = True

    def on_hit_star(self, hit_x, hit_y):
        if self.star_out:
            self.spawn(hit_x - 2, hit_y, hit_x - 2, hit_y, config._star)
            star_pow = powerups.Star(hit_x - 2, hit_y)
            star_pow.appender()
            self.star_out = False


class Spring(Obstacle):
    def __init__(self, denote=config._spring):
        Obstacle.__init__(self, denote)
        self.movable = True


class Mushroom(Obstacle):
    def __init__(self, denote=config._mushroom):
        Obstacle.__init__(self, denote)
        self.is_destroyable = True
