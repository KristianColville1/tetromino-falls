"""
Tetromino Falls is terminal based game displayed in the browser.
"""
import curses
from curses import wrapper

# Initializes the curses objects
curses.initscr()

# Allows the curses colors to be accessed and used
curses.start_color()

# background curses color pairs initialized
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_CYAN)
curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)
curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_YELLOW)
curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_GREEN)
curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_WHITE)

# text curses color pairs initialized
curses.init_pair(8,  curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(9,  curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(10, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(11, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(12, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(13, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
curses.init_pair(14, curses.COLOR_WHITE, curses.COLOR_BLACK)

# background colors with white text assigned to constants
BLUE = curses.color_pair(1)
CYAN = curses.color_pair(2)
RED = curses.color_pair(3)
YELLOW= curses.color_pair(4)
GREEN = curses.color_pair(5)
PURPLE = curses.color_pair(6)
WHITE = curses.color_pair(7)

# text colors with black bg assigned to constants
BLUE_TEXT = curses.color_pair(8)
CYAN_TEXT = curses.color_pair(9)
RED_TEXT = curses.color_pair(10)
YELLOW_TEXT = curses.color_pair(11)
GREEN_TEXT = curses.color_pair(12)
PURPLE_TEXT = curses.color_pair(13)
WHITE_TEXT = curses.color_pair(14)

def print_welcome(welcome_window):
    """
    When called upon this function prints the first menu the user encounters.
    It waits for the user to press a key before moving on with the program.
    """
    file = open('welcome-msg.txt')
    text = file.read()
    file.close()

    welcome_window.addstr(f'{text}', CYAN_TEXT)
    welcome_window.addstr(18, 25, 'Created by Kristian Colville', YELLOW_TEXT)
    welcome_window.addstr(22, 15, 'Press any key to continue..', RED_TEXT)

    # gets the users input and exits this function
    welcome_window.getch()


def get_user_name():
    """
    Gets the users name and checks the data base for names entered.
    It returns the users name for displaying on the screen.
    """
    user = ''
    return user


def main(stdscr):
    """
    Main function calls all the necessary functions to run the game.
    It is activated through the wrapper function call. It allows the
    window objects to be initilized.
    """
    stdscr.clear()

    welcome_window = curses.newwin(29, 79)
    print_welcome(welcome_window)
    user = get_user_name()


# creates an object to initialize the curser objects using the main function
wrapper(main)
