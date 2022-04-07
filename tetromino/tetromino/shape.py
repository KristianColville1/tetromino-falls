"""Class shape generates the game objects for Tetromino falls"""
import random
import curses

class Shape():
    """
    When called it will produce a random shape and color for the game.
    """
    SHAPES = {
    'I':[
            [[1],['b'],['c'],['d']],
            [[1],['b'],['c'],['d']],
            [[1],['b'],['c'],['d']],
            [[1],['b'],['c'],['d']],
            ],
    'J':[
            [['a'],[1],['c'],['d']],
            [['a'],[1],['c'],['d']],
            [[1],[1],['c'],['d']],
            [['a'],['b'],['c'],['d']],
            ],
    'L':[
            [[1],['b'],['c'],['d']],
            [[1],['b'],['c'],['d']],
            [[1],[1],['c'],['d']],
            [['a'],['b'],['c'],['d']],
            ],
    'O':[
            [['a'],['b'],['c'],['d']],
            [['a'],[1],[1],['d']],
            [['a'],[1],[1],['d']],
            [['a'],['b'],['c'],['d']],
            ],
    'T':[
            [[1],[1],[1],['d']],
            [['a'],[1],['c'],['d']],
            [['a'],['b'],['c'],['d']],
            [['a'],['b'],['c'],['d']],
            ],
    'S':[
            [['a'],[1],[1],['d']],
            [[1],[1],['c'],['d']],
            [['a'],['b'],['c'],['d']],
            [['a'],['b'],['c'],['d']],
            ],
    'Z':[
            [[1],[1],['c'],['d']],
            [['a'],[1],[1],['d']],
            [['a'],['b'],['c'],['d']],
            [['a'],['b'],['c'],['d']],
            ],
}


    def __init__(self):
        self.color = self.get_color()


    def get_shape(self):
        """
        Returns a random shape to use as game objects in
        Tetromino Falls.
        """
        keys = ['I', 'J', 'L', 'O', 'T', 'S', 'Z']
        rand_shape = self.SHAPES[keys[random.randrange(7)]]
        return rand_shape

    def get_color(self):
        """
        Returns a random color to use on game objects in
        Tetromino Falls.
        """
        # initializes the game objects
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
        curses.init_pair(8, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(9, curses.COLOR_CYAN, curses.COLOR_BLACK)
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

        colors = [blue, cyan, red, yellow, green, purple, white]
        color = colors[random.randrange(7)]
        return color
