"""
Tetromino Falls is terminal based game displayed in the browser.
"""
import curses
from curses import wrapper


stdscr = curses.initscr()
curses.start_color()
# background curses colors initialized
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_CYAN)
curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)
curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_YELLOW)
curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_GREEN)
curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_WHITE)

# text curses colors initializes
curses.init_pair(8,  curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(9,  curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(10, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(11, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(12, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(13, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
curses.init_pair(14, curses.COLOR_WHITE, curses.COLOR_BLACK)

# background colors with white text
BLUE = curses.color_pair(1)
CYAN = curses.color_pair(2)
RED = curses.color_pair(3)
YELLOW= curses.color_pair(4)
GREEN = curses.color_pair(5)
PURPLE = curses.color_pair(6)
WHITE = curses.color_pair(7)

# text colors with black bg
BLUE_TEXT = curses.color_pair(8)
CYAN_TEXT = curses.color_pair(9)
RED_TEXT = curses.color_pair(10)
YELLOW_TEXT = curses.color_pair(11)
GREEN_TEXT = curses.color_pair(12)
PURPLE_TEXT = curses.color_pair(13)
WHITE_TEXT = curses.color_pair(14)

def main(stdscr):
    """
    Main function calls all the necessary functions to run the game.
    It is activated through the wrapper function call. It allows the
    window objects to be initilized.
    """
    stdscr.clear()

    welcome_window = curses.newwin(29, 79)
    file = open('welcome-msg.txt')
    text = file.read()
    file.close()

    welcome_window.addstr(f'{text}', CYAN_TEXT)
    welcome_window.addstr(24, 25, 'Created by Kristian Colville', YELLOW_TEXT)
    welcome_window.addstr(27, 15, 'Press any key to continue..', RED_TEXT)
    welcome_window.getch()

# creates an object to initialize the curser objects using the main function
wrapper(main)
