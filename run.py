"""
Tetromino Falls is terminal based game displayed in the browser.
"""
import time
import curses
from curses import wrapper
from curses.textpad import rectangle
from tetromino.tetromino.message import Message
from tetromino.tetromino.shape import Shape


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


def create_game_window():
    """
    Creates a game window object and returns the object to the caller.
    """
    game_screen = curses.newwin(19, 39, 2, 3)
    game_screen.border('|', '|', '.', '|')
    return game_screen


def main(full_window):
    """
    Main function calls all the necessary functions to run the game.
    """
    # calls to initialize curses
    start_curses()
    full_window.clear()
    game = create_game_window()
    shape = Shape()
    full_window.nodelay(True)
    y_axis, x_axis = 0, 14
    full_window.clear()
    while GAME_OVER is False:
        y_axis += 1
        if y_axis > 17:
            y_axis = 17
        if x_axis > 36:
            x_axis = 36
        elif x_axis < 1:
            x_axis = 1
        time.sleep(0.4)
        try:
            key = full_window.getkey()
        except:
            key = None
        if key == 'KEY_LEFT':
            x_axis -= 2
            if x_axis < 1:
                x_axis = 1
        elif key == 'KEY_RIGHT':
            x_axis += 2
            if x_axis > 35:
                x_axis = 35
        elif key == 'KEY_DOWN':
            y_axis += 1
            if y_axis > 17:
                y_axis = 17
        game.clear()
        game.addstr(y_axis, x_axis, '  ', shape.color)
        rectangle(game, 0, 0, 18, 37)
        game.move(18, 36)
        game.refresh()
    full_window.refresh()

GAME_OVER = False
start_game()
