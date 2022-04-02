"""Window class for creating window objects"""
import curses

class Window:
    """
    Creates game window objects
    """
    def __init__(self, y_size, x_size):
        self.y_size = y_size
        self.x_size = x_size
    