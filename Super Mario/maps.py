import config
import board
import creatures


class Mapp(object):
    def __init__(self):
        self.length = 400
        self.width = 35
        self.init_board()

    def spawn(self, from_x, from_y, to_x, to_y, denote):
        for i in range(from_x, to_x + 1):
            for j in range(from_y, to_y + 1):
                board.arr[i][j] = denote


class Maps1(Mapp):
    def __init__(self):
        Mapp.__init__(self)

    def init_board(self):
        for i in range(0, self.width):
            for j in range(0, self.length):
                board.arr[i][j] = " "
        for i in range(0, self.length):
            board.arr[self.width - 5][i] = 'X'
            board.arr[self.width - 4][i] = 'X'
            board.arr[self.width - 3][i] = 'X'
            board.arr[self.width - 2][i] = 'X'
            board.arr[self.width - 1][i] = 'X'
            board.arr[0][i] = 'X'
        board.arr[28][1] = config._marioupper
        board.arr[29][1] = config._mariolower

        self.spawn(23, 12, 24, 13, config._mushroombricks)
        self.spawn(23, 18, 24, 19, config._spring)
        self.spawn(23, 22, 24, 23, config._coinbricks)
        self.spawn(16, 22, 17, 23, config._coinbricks)
        self.spawn(28, 30, 29, 31, config._wall)
        ene1 = creatures.Enemy(29, 32, 2)
        # self.spawn(27,39,29,40,config._wall)
        ene2 = creatures.Enemy(29, 41, 3)
        self.spawn(26, 52, 29, 53, config._wall)
        # ene1 = creatures.Enemy(29,55,3)
        self.spawn(19, 56, 19, 65, config._bricks)
        self.spawn(18, 58, 18, 63, config._coin)
        # self.spawn(18,65,18,65,config._rightcornor)
        # ene2 = creatures.Enemy(18,64,2)
        self.spawn(12, 64, 12, 71, config._bricks)
        self.spawn(10, 66, 10, 70, config._coin)
        self.spawn(30, 72, 34, 82, config._empty)
        self.spawn(21, 89, 21, 122, config._bricks)
        self.spawn(20, 89, 20, 89, config._leftcornor)
        self.spawn(20, 122, 20, 122, config._rightcornor)
        self.spawn(13, 94, 14, 95, config._spring)
        self.spawn(13, 105, 14, 106, config._coinbricks)
        self.spawn(13, 116, 14, 117, config._coinbricks)
        self.spawn(6, 101, 6, 107, config._bricks)
        self.spawn(5, 101, 5, 101, config._leftcornor)
        self.spawn(5, 107, 5, 107, config._rightcornor)
        self.spawn(5, 102, 5, 106, config._coin)
        ene3 = creatures.Enemy(20, 120, 3)
        self.spawn(30, 137, 34, 170, config._empty)
        self.spawn(29, 135, 29, 136, config._floor)
        self.spawn(28, 137, 28, 138, config._floor)
        self.spawn(27, 139, 27, 140, config._floor)
        self.spawn(26, 141, 26, 149, config._floor)
        self.spawn(29, 171, 29, 172, config._spring)
        self.spawn(28, 169, 28, 170, config._floor)
        self.spawn(27, 167, 27, 168, config._floor)
        self.spawn(26, 150, 26, 157, config._floor)
        self.spawn(26, 158, 26, 166, config._floor)
        self.spawn(22, 151, 22, 155, config._coin)
        self.spawn(20, 180, 20, 197, config._bricks)
        self.spawn(19, 180, 19, 180, config._leftcornor)
        self.spawn(19, 197, 19, 197, config._rightcornor)
        self.spawn(19, 188, 19, 190, config._coin)
        ene5 = creatures.Enemy(19, 181, 2)
        ene6 = creatures.Enemy(19, 196, 2)
        self.spawn(13, 185, 14, 187, config._bricks)
        self.spawn(13, 188, 14, 191, config._coinbricks)
        self.spawn(13, 192, 14, 193, config._mushroombricks)
        self.spawn(13, 218, 13, 227, config._coin)
        self.spawn(14, 217, 14, 228, config._bricks)
        self.spawn(19, 210, 19, 219, config._coin)
        self.spawn(20, 209, 20, 220, config._bricks)
        self.spawn(19, 246, 19, 255, config._coin)
        self.spawn(20, 245, 20, 256, config._bricks)
        self.spawn(13, 238, 13, 247, config._coin)
        self.spawn(14, 237, 14, 248, config._bricks)
        ene7 = creatures.Enemy(22, 227, 4)
        ene8 = creatures.Enemy(22, 238, 4)
        self.spawn(17, 231, 22, 233, config._coin)
        self.spawn(28, 222, 29, 223, config._floor)
        self.spawn(28, 243, 29, 244, config._floor)
        ene9 = creatures.Enemy(29, 224, 4)
        self.spawn(24, 279, 29, 280, config._wall)
        self.spawn(24, 281, 29, 282, config._wall)
        self.spawn(28, 288, 29, 290, config._floor)
        self.spawn(26, 290, 29, 292, config._floor)
        self.spawn(24, 292, 29, 294, config._floor)
        self.spawn(22, 294, 29, 296, config._floor)
        self.spawn(20, 296, 29, 298, config._floor)
        self.spawn(20, 299, 29, 301, config._floor)
        self.spawn(22, 302, 29, 304, config._floor)
        self.spawn(28, 311, 29, 313, config._floor)
        self.spawn(26, 308, 29, 310, config._floor)
        self.spawn(24, 305, 29, 306, config._floor)


class Maps2(Mapp):
    def __init__(self):
        Mapp.__init__(self)

    def init_board(self):
        for i in range(0, self.width):
            for j in range(0, self.length):
                board.arr[i][j] = " "
        for i in range(0, self.length):
            board.arr[self.width - 5][i] = 'X'
            board.arr[self.width - 4][i] = 'X'
            board.arr[self.width - 3][i] = 'X'
            board.arr[self.width - 2][i] = 'X'
            board.arr[self.width - 1][i] = 'X'
            board.arr[0][i] = 'X'
        board.arr[28][1] = config._marioupper
        board.arr[29][1] = config._mariolower

        self.spawn(23, 12, 24, 13, config._mushroombricks)
        self.spawn(23, 16, 24, 25, config._bricks)
        self.spawn(23, 18, 24, 19, config._spring)
        self.spawn(23, 22, 24, 23, config._starbricks)
        self.spawn(16, 22, 17, 23, config._coinbricks)
        self.spawn(28, 30, 29, 31, config._wall)
        ene1 = creatures.Enemy(29, 26, 2)
        self.spawn(27, 39, 29, 40, config._wall)
        self.spawn(26, 52, 29, 53, config._wall)
        self.spawn(19, 56, 19, 65, config._bricks)
        self.spawn(18, 56, 18, 56, config._leftcornor)
        self.spawn(18, 65, 18, 65, config._rightcornor)
        ene2 = creatures.Enemy(18, 64, 2)
        self.spawn(12, 64, 12, 71, config._bricks)
        self.spawn(10, 66, 10, 70, config._coin)
        self.spawn(30, 72, 34, 82, config._empty)
        self.spawn(21, 89, 21, 122, config._bricks)
        self.spawn(20, 89, 20, 89, config._leftcornor)
        self.spawn(20, 122, 20, 122, config._rightcornor)
        self.spawn(13, 94, 14, 95, config._coinbricks)
        self.spawn(13, 105, 14, 106, config._coinbricks)
        self.spawn(13, 116, 14, 117, config._coinbricks)
        self.spawn(6, 101, 6, 107, config._bricks)
        self.spawn(5, 101, 5, 101, config._leftcornor)
        self.spawn(5, 107, 5, 107, config._rightcornor)
        self.spawn(5, 102, 5, 106, config._coin)
        ene3 = creatures.Enemy(20, 120, 2)
        ene4 = creatures.Enemy(20, 91, 2)
        self.spawn(30, 137, 34, 170, config._empty)
        self.spawn(29, 135, 29, 136, config._floor)
        self.spawn(28, 137, 28, 138, config._floor)
        self.spawn(27, 139, 27, 140, config._floor)
        self.spawn(26, 141, 26, 149, config._floor)
        self.spawn(29, 171, 29, 172, config._spring)
        self.spawn(28, 169, 28, 170, config._floor)
        self.spawn(27, 167, 27, 168, config._floor)
        self.spawn(26, 158, 26, 166, config._floor)
        self.spawn(22, 151, 22, 155, config._coin)
        self.spawn(20, 180, 20, 197, config._bricks)
        self.spawn(19, 180, 19, 180, config._leftcornor)
        self.spawn(19, 197, 19, 197, config._rightcornor)
        self.spawn(19, 188, 19, 190, config._coin)
        ene5 = creatures.Enemy(19, 181, 2)
        ene6 = creatures.Enemy(19, 196, 3)
        self.spawn(13, 185, 14, 187, config._bricks)
        self.spawn(13, 188, 14, 193, config._coinbricks)
        self.spawn(14, 217, 14, 228, config._bricks)
        self.spawn(20, 209, 20, 220, config._bricks)
        self.spawn(23, 226, 23, 239, config._bricks)
        self.spawn(22, 226, 22, 226, config._leftcornor)
        self.spawn(22, 239, 22, 239, config._rightcornor)
        self.spawn(20, 245, 20, 256, config._bricks)
        self.spawn(14, 237, 14, 248, config._bricks)
        ene7 = creatures.Enemy(22, 227, 4)
        ene8 = creatures.Enemy(22, 238, 4)
        self.spawn(17, 231, 22, 231, config._coin)
        self.spawn(17, 232, 22, 232, config._coin)
        self.spawn(28, 222, 29, 223, config._floor)
        self.spawn(28, 243, 29, 244, config._floor)
        ene9 = creatures.Enemy(29, 224, 4)
        self.spawn(28, 288, 29, 290, config._floor)
        self.spawn(26, 290, 29, 292, config._floor)
        self.spawn(24, 292, 29, 294, config._floor)
        self.spawn(22, 294, 29, 296, config._floor)
        self.spawn(20, 296, 29, 298, config._floor)
        self.spawn(20, 299, 29, 301, config._floor)
        self.spawn(22, 302, 29, 304, config._floor)
        self.spawn(28, 311, 29, 313, config._floor)
        self.spawn(26, 308, 29, 310, config._floor)
        self.spawn(24, 305, 29, 306, config._floor)
        ene10 = creatures.BossEnemy(29, 286, 5)
