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
    game_screen = curses.newwin(19, 39, 2, 35)
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
    new_shape = Shape()
    color = new_shape.get_color()
    new_shape = new_shape.get_shape()
    
    full_window.nodelay(True)
    y_axis, x_axis = 0, 14
    full_window.clear()
    
    while GAME_OVER is False:
        y_axis += 1
        if y_axis > 20:
            y_axis = 20
        if x_axis > 30:
            x_axis = 30
        elif x_axis < 3:
            x_axis = 3
        time.sleep(.5)
        try:
            key = game.getkey()
        except:
            key = None
        if key == 'KEY_LEFT':
            x_axis -= 2
            if x_axis < 3:
                x_axis = 3
        elif key == 'KEY_RIGHT':
            x_axis += 2
            if x_axis > 30:
                x_axis = 30
        elif key == 'KEY_DOWN':
            y_axis += 1
            if y_axis > 20:
                y_axis = 20
        full_window.clear()
        letter_checker = 0
        r_count = 1
        c_count = 1
        for two_d in new_shape:
            for one_d in two_d:
                for val in one_d:
                    if val == 1:
                        full_window.addstr(y_axis + r_count, x_axis + c_count, '  ', color)
            r_count +=1
        rectangle(full_window, 0, 2, 21, 32)
        full_window.move(18, 38)
        full_window.refresh()
    full_window.refresh()

GAME_OVER = False
start_game()
