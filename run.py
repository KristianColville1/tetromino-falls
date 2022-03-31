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

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    stdscr.addstr(3, 7, '  ', curses.color_pair(1))
    stdscr.addstr(3, 8, '  ', curses.color_pair(1))
    stdscr.addstr(3, 9, '  ', curses.color_pair(1))
    stdscr.addstr(3, 10, '  ', curses.color_pair(1))
    stdscr.refresh()
    stdscr.getch()

# creates an object to initialize the curser objects using the main function
wrapper(main)
