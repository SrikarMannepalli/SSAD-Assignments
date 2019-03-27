import random
from sys import argv, stdout
import datetime
import time
import config
import board
import obspow
import common
import powerups
from common import mario
import creatures
import maps
import os
import sys

# the game is run from here


def main():
    os.system('clear')
    game_over = 0
    print("w is for moving up")
    print("a is for moving left")
    print("d is for moving right")
    print("s is for bullets in level 2")
    while True:
        level = input("Choose a level. 1 or 2: ")
        if level == "1":
            board.Board.level = 1
            board.Board.timer = 250
            map1 = maps.Maps1()
            break
        elif level == "2":
            board.Board.level = 2
            board.Board.timer = 450
            map1 = maps.Maps2()
            break
        else:
            print("Enter valid level.")
    board.Board.time = int(time.time())
    common.scene.print_array()
    count = 0
    while True:
        if common.mario.lives < 3 and board.Board.out == 1:
            count += 1
            board.Board.out = 0
            config.mushrooms_list[:] = []
            config.enemylist[:] = []
            config.bossenemylist[:] = []
            config.frame_counter = 0
            del map1
            if level == "1":
                map1 = maps.Maps1()
            else:
                map1 = maps.Maps2()
            del common.mario
            common.mario = creatures.Mario(28, 1)
            common.mario.lives -= count
            common.mario.state = 0
            if common.mario.lives == 0:
                game_over = 1
            board.Board.mariolives = common.mario.lives
            board.Board.mariostate = common.mario.state
            common.scene.print_array()

        if level == "2" and creatures.BossEnemy.boss_dead:
            if(common.mario._y == 313):
                print("YOU WON!!")
                game_over = 1
        elif level == "1":
            if(common.mario._y >= 313):
                print("YOU WON!!")
                game_over = 1
        if board.arr[common.mario._x + 2 +
                     common.mario._state][mario._y] == config._spring:
            common.mario.move("UP")
        pressed_key = config.getkey()
        if pressed_key == 'w' or 0 < common.mario._upcount < common.mario.jump_height:
            if pressed_key == 'w':
                if (board.arr[common.mario._x +
                              2 +
                              common.mario._state][common.mario._y] != config._empty) and (board.arr[common.mario._x +
                                                                                                     2 +
                                                                                                     common.mario._state][common.mario._y] != config._coin) and (board.arr[common.mario._x +
                                                                                                                                                                           2 +
                                                                                                                                                                           common.mario._state][common.mario._y] != config._mushroom):
                    common.mario.move("UP")
            else:
                common.mario.move("UP")
        if pressed_key == 'a':
            common.mario.move("LEFT")
            time.sleep(0.08)
        elif pressed_key == 'd' and game_over != 1:
            common.mario.move("RIGHT")
            time.sleep(0.08)

        elif pressed_key == 's':
            powerups.Bullet(
                common.mario._x + 1 + common.mario._state,
                common.mario._y + 1)
        elif pressed_key == 'q' or game_over == 1:
            break

        if common.mario._upcount == 0:
            common.mario.move("DOWN")
            time.sleep(0.08)

        if common.mario._state == 0 and board.Board.mariostate == 1:
            common.mario._state = 1
            common.mario._x, common.mario._y = common.mario.create_supermario()

        board.Board.mariolives = common.mario.lives
        common.scene.print_array()


if __name__ == '__main__':
    main()
