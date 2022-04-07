"""Handles printing text to terminal for Tetromino Falls"""
from tetromino.tetromino import console
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
        try:
            file = open('welcome-msg.txt', encoding='utf8')
            self.welcome = file.read()
            file.close()
            if self.welcome is None:
                raise IOError(
                    'An error occurred fetching the welcome message.. sorry about that..'
                )
        except IOError as error:
            console.clear_console()
            print(f'Oops something went wrong!\n\033[31m{error}\033[0m')

        return print('\n\n\n\033[31m' + self.welcome + '\033[0m\n\n\n')


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
