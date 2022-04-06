"""Holds the game class for Tetromino Falls"""

class Game():
    """
    Creates a game object, specifically used to create the game grid.
    Deals with the curses module so y and x are written to match curses
    window objects.
    """
    def __init__(self, y_pos, x_pos, y_size, x_size):
        self.y_pos = y_pos
        self.x_pos = x_pos
        self.y_size = y_size
        self.x_size = x_size
        self.game_grid = self.create_game_grid()


    def create_game_grid(self):
        """
        Creates a game window of the specified size to view in a terminal
        window.
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
        