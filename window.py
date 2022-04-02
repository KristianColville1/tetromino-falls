"""Window class for creating window objects"""
import curses

class Window:
    """
    Creates game window objects
    """
    
    # class variables
    # # Initializes the curses objects
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
    
    def __init__(self, y_size, x_size, y_pos, x_pos):
        """
        Creates a game window of the specified size on instantiation and
        positions it at the desired location. X and Y are reversed to match 
        how curses work with window objects.
        """
        self.y_size = y_size
        self.x_size = x_size
        self.y_pos = y_pos
        self.x_pos = x_pos
    
    def display_game_window(self):
        """
        Displays the game window.
        """
        return self