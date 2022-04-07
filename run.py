"""
Tetromino Falls is terminal based game displayed in the browser.
"""
import time
import curses
import random
from curses import wrapper
from tetromino.tetromino.game import Game
from tetromino.tetromino.message import Message
from tetromino.tetromino.shape import Shape
from tetromino.tetromino.user_name import User

def start_game():
    """
    Starts the game calls the main function.
    """
    tetromino = Message()
    tetromino.get_next_action()
    wrapper(main)


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


def drop_new_shape():
    """
    Handles the array conversion to print a shape to the terminal.
    """

def format_shape(shape):
    """
    Takes a shape and converts its arrays into printable strings for
    the game. Returns an array holding the string values to be printed.
    """
    shape_strings = shape
    return shape_strings


def start_curses():
    """
    Initializes the curses objects.
    Specifically allows the colors to be used and windows to be created.
    Returns the colors after curses color pairs are initialized.
    """
    curses.initscr()
    curses.start_color()


def clear_then_refresh(window):
    """
    Clears a curses window object and refreshes the screen.
    """
    window.clear()
    window.refresh()


def main(full_window):
    """
    Main function calls all the necessary functions to run the game.
    """
    # calls to initialize curses
    start_curses()
    clear_then_refresh(full_window)

    shape = Shape()
    shape_strings = format_shape(shape)

    game = Game(20, 36)
    full_window.getkey()
    time.sleep(5)


start_game()
