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

    MAIN_BG = curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK)
    stdscr.addstr(10, 10, '\33[44m hello', MAIN_BG)
    stdscr.refresh()
    stdscr.getch()

# creates an object to initialize the curser objects using the main function
wrapper(main)
