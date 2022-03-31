"""
Tetromino Falls is terminal based game displayed in the browser.
"""

import curses
from curses import wrapper




stdscr = curses.initscr()
def main(stdscr):
    """
    Main function calls all the necessary functions to run the game.
    """
    stdscr.clear()
    
    # curses colors initialized
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_CYAN)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_YELLOW)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_WHITE)

    # color constants
    BLUE = curses.color_pair(1)
    CYAN = curses.color_pair(2)
    RED = curses.color_pair(3)
    YELLOW = curses.color_pair(4)
    GREEN = curses.color_pair(5)
    PURPLE = curses.color_pair(6)
    WHITE = curses.color_pair(7)
    
    stdscr.addstr(3, 7, '  ', PURPLE)
    stdscr.addstr(2, 7, '  ', PURPLE)
    stdscr.addstr(3, 9, '  ', PURPLE)
    stdscr.addstr(3, 10, '  ', PURPLE)
    stdscr.refresh()
    stdscr.getch()

# creates an object to initialize the curser objects using the main function
wrapper(main)
