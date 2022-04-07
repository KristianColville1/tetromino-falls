"""Holds the game class for Tetromino Falls"""

class Game():
    """
    Creates a game object, specifically used to create the game grid.
    Deals with the curses module so y and x are written to match curses
    window objects.
    """
    def __init__(self, y_size, x_size):
        self.y_size = y_size
        self.x_size = x_size


    def create_game_grid(self):
        """
        When game window is created a tensor array is also created to represent
        the individual cells for rows and cols in the game window.
        Allows the ability to manipulate the board and store objects.
        """

        grid = []
        # for y rows insert x columns
        for _ in range(self.y_size):
            grid.append([])
        for i in grid:
            for _ in range(self.x_size):
                i.append([0])

        # returns a tensor array representing the game grid
        return grid
        