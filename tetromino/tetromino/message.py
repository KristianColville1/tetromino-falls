"""Handles printing text to terminal for Tetromino Falls"""

class Message():
    """
    Creates a message object that holds different methods for
    printing to terminal.
    """
    def __init__(self):
        self.welcome = self.get_welcome()
        self.instructions = self.get_instructions()
        self.goodbye = self.get_goodbye()


    def get_welcome(self):
        """
        Prints the welcome message to terminal when called.
        """
        return ''


    def get_instructions(self):
        """
        Prints the instructions to the terminal for the user when
        called for the Tetromino Falls game.
        """
        return ''


    def get_goodbye(self):
        """
        Prints the goodbye message to the terminal for the user for the
        Tetromino Falls game.
        """
        return ''
