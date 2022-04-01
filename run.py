"""
Tetromino Falls is terminal based game displayed in the browser.
"""
import curses
from curses import wrapper

def main(stdscr):
    """
    Main function calls all the necessary functions to run the game.
    It is activated through the wrapper function call. It allows the
    window objects to be initilized.
    """
    stdscr = curses.initscr()



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
    blue = curses.color_pair(1)
    cyan = curses.color_pair(2)
    red = curses.color_pair(3)
    yellow = curses.color_pair(4)
    green = curses.color_pair(5)
    purple = curses.color_pair(6)
    white = curses.color_pair(7)

    # text colors with black bg
    blue_text = curses.color_pair(8)
    cyan_text = curses.color_pair(9)
    red_text = curses.color_pair(10)
    yellow_text = curses.color_pair(11)
    green_text = curses.color_pair(12)
    purple_text = curses.color_pair(13)
    white_text = curses.color_pair(14)

    file = open('welcome-msg.txt')
    text = file.read()
    file.close()

    stdscr.clear()
    stdscr.addstr(f'{text}', cyan_text)
    stdscr.addstr(20, 25, 'Created by Kristian Colville', yellow_text)
    stdscr.refresh()
    stdscr.getch()

# creates an object to initialize the curser objects using the main function
wrapper(main)
