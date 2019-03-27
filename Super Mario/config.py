import os
import errno
import termios
import time
import fcntl
from colorama import Fore
import sys

# character representation of objects
_floor = "X"
_coin = "o"
_mushroom = "M"
_bricks = "#"
_coinbricks = "O"
_mushroombricks = "?"
_wall = "X"
_empty = " "
_marioupper = "0"
_mariolower = "|"
_spring = "!"
_enemy = "e"
_leftcornor = "<"
_rightcornor = ">"
_star = "*"
_starbricks = "@"
_bossenemy = "b"
_bullet = "-"

# uncomment following code for colors
'''
_floorcolor = Fore.YELLOW
_coincolor = Fore.YELLOW
_mushroomcolor = Fore.CYAN
_coinbrickscolor = Fore.WHITE
_mushroombrickscolor = Fore.CYAN
_brickscolor = Fore.RED
_wallcolor = Fore.GREEN
_springcolor = Fore.MAGENTA
_enemycolor = Fore.WHITE
_leftcornorcolor = Fore.YELLOW
_rightcornorcolor = Fore.YELLOW
_mariolowercolor = Fore.WHITE
_mariouppercolor = Fore.WHITE
_emptycolor  = Fore.BLACK
'''


mushrooms_list = []
enemylist = []
bossenemylist = []
stars_list = []
bullets_list = []
# state 0:normal mario
# state 1:super mario


frame_counter = 0

timeout_value = 0.1
TERMIOS = termios


def timeout(seconds, error_message=os.strerror(errno.ETIME)):
    import signal
    from functools import wraps

    def decorator(func):
        def _handle_timeout(signum, frame):
            raise Exception(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.setitimer(signal.ITIMER_REAL, seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)
    return decorator


@timeout(timeout_value)
def getkey():
    fd = sys.stdin.fileno()
    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

    try:
        while True:
            try:
                c = sys.stdin.read(1)
                break
            except IOError:
                pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
    return c
