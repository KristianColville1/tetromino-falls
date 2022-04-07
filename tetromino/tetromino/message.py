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
    
    