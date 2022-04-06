"""
Tetromino Falls is terminal based game displayed in the browser.
"""

import time
import sys
import curses
import random
from curses import wrapper
import console
from user_name import User


# tetromino shapes


def print_welcome_text():
    """
    Prints welcome text to terminal for user and waits for 3 seconds before moving on.
    """
    try:
        file = open('welcome-msg.txt', encoding='utf8')
        message = file.read()
        print('\n\n\n\033[31m' + message + '\033[0m\n\n\n')
        file.close()
        if len(message) < 1:
            raise IOError(
                'An error occurred fetching the welcome message.. sorry about that..'
            )
    except IOError as error:
        console.clear_console()
        print(f'Oops something went wrong!\n\033[31m{error}\033[0m')
    # time.sleep(3)


def get_user_name():
    """
    Gets the users name and checks the database for conflicting names.
    """



def what_next_user():
    """
    Asks the user what they would like to do next.
    Start the game, load instructions or exit.
    """
    try:
        print(f'\n\nHere are the options available {USER_NAME.user_name}:\n')
        print("\t\033[0;33mEnter '\033[31mp\033[0;33m' to play the game.")
        print("\tEnter '\033[31mi\033[0;33m' for instructions..")
        print("\tEnter '\033[31me\033[0;33m' to exit the program.\033[0m")
        user_decision = input(f'\n So what will it be {USER_NAME.user_name}?\n ')
        if user_decision not in ('p', 'i', 'e'):
            raise ValueError(
                f"""You need to enter something else as \033[36m{user_decision}\033[0m is invalid"""
            )
    except ValueError as error:
        console.clear_console()
        print(f'\n\t\033[31mInvalid input received...\033[0m \n{error}, please try again')
        return False
    return user_decision

def get_next_action():
    """
    Gets the users next action and will decide what route to take.
    Play the game, get instructions or exit program
    """
    # gets and checks the users decision on next actions
    console.clear_console()
    decision = what_next_user()
    if decision is False:
        while decision is False:
            decision = what_next_user()

    if decision == 'p':
        start_game()
    elif decision == 'i':
        get_instructions()
    else:
        exit_program()

def start_game():
    """
    Starts the game calls the main function.
    """
    wrapper(main)


def get_instructions():
    """
    When called it will get instructions on how to play the game.
    """
    print('\033[0;33m')
    try:
        console.clear_console()
        file = open('instructions.txt', encoding='utf8')
        instructions = file.read()
        file.close()
        print(f"{instructions}\033[0m")
        try:
            read_instructions = input('\033[31m\nEnter "y" and hit enter to continue: \033[0m')
            if read_instructions not in ('Y', 'y'):
                raise ValueError(
                    '\033[36m\nEnter the letter y for yes or n for no\n\033[0m'
                )
        except ValueError as error:
            print(error)
            time.sleep(2)
            console.clear_console()
            get_instructions()
        if len(instructions) < 1:
            raise IOError(
                "Failed to read instructions from welcome.txt..."
            )
    except IOError as error:
        console.clear_console()
        print(f'\033[31m\n{error}\033[0m')
    get_next_action()


def exit_program():
    """
    Exits the program if the user decides to quit the game.
    Loops using recursion until valid input is entered.
    """
    try:
        check_input = 'Are you absolutely sure you want to exit the program? y/n '
        user_decision = input(f'\033[0;31m{check_input}:\033[0m')
        if user_decision not in ('y', 'n'):
            raise ValueError(
                f'\n\033[31m{user_decision}\033[0m is not valid input, try again...\n'
            )
        if user_decision == 'n':
            get_next_action()
        elif user_decision == 'y':
            console.clear_console()
            thanks_for_playing()
            sys.exit()
    except ValueError as error:
        print(f'{error}')
        exit_program()


def thanks_for_playing():
    """
    When the user decides to quit the game this message is displayed in the terminal.
    """
    try:
        file = open('goodbye.txt', encoding='utf8')
        message = file.read()
        console.clear_console()
        print(message)
        time.sleep(4)
        file.close()
        if file is None:
            raise IOError(
                'The thank you message failed to display...'
            )
    except IOError as error:
        print(f"An error has occurred..\n {error}")


def start_curses():
    """
    Initializes the curses objects.
    Specifically allows the colors to be used and windows to be created.
    Returns the colors after curses color pairs are initialized.
    """



def create_game_grid():
    """
    Creates a tensor array for the game grid for Tetromino Falls.
    """
    # this grid tensor is composed of a 3D array
    # the idea is to use 1s and 0s to manipulate the board output

    # i tested a nested for loop with 3 loops and the results show
    # that there is 860 arrays within the tensor holding the value 0

    # every square in the tetromino shape will contain 2 values
    # 860 / 2 is 430, so there are 430 positions to manipulate through

    # 21 rows with 41 cols
    grid_tensor = []
    for row in range(21):
        grid_tensor.append([])
        for _ in range(41):
            grid_tensor[row].append([0])
    return grid_tensor


def check_user_input():
    """
    Checks user input to game.
    """


def main(stdscr):
    """
    Main function calls all the necessary functions to run the game.
    """
    # calls to initialize curses
    start_curses()

    stdscr.clear()
    stdscr.refresh()
    y_axis, x_axis = 0, 1
    g_win = curses.newwin(21, 41, 1, 3)
    stdscr.nodelay(True)
    
    # while the game is not over clear the screen,
    # add a shape formated as sequential strings,
    # add the values in at column 16 of the game window,
    # for each array within the 2d arrays,
    # assign letter checker to zero,
    # for the value in the 1d array
    # Add the index of the value to the col num,
    # begin letter checker and build up shape object
    # get input and refresh.
    while True:
        g_win.clear()
        for two_arr in shape:
            x_axis = 16
            for one_arr in two_arr:
                for val in one_arr:
                    x_axis += one_arr.index(val) + 1
                    if val == 1:
                        # a space is used for each value, it makes them more square in terminal
                        g_win.addstr(y_axis, x_axis, ' ', color)
            y_axis += 1
        try:
            key = stdscr.getkey()
            if key == 'KEY_RIGHT':
                if x_axis < 37:
                    x_axis += 1
            elif key == 'KEY_LEFT':
                if x_axis > 3:
                    x_axis -= 1
            elif key == 'KEY_DOWN':
                if y_axis < 20:
                    y_axis += 1
            elif key == 'KEY_UP':
                y_axis -= 1
        except:
            key = None
        if y_axis < 21:
            y_axis -= 3
        if y_axis == 21:
            y_axis = 0
            shape = get_random_shape()
            shape = rotate_shape(shape)
            color = colors[random.randrange(6)]
        g_win.border('|', '|', ' ', '|')
        time.sleep(.3)
        g_win.refresh()

    #


print_welcome_text()

# get and check user name, keep repeating until valid
USER_NAME = User()
print(USER_NAME.user_name)

get_next_action()
