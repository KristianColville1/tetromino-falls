"""Handles printing text to terminal for Tetromino Falls"""
import time
from tetromino.tetromino import console
class Message:
    """
    Creates a message object that holds different methods for
    printing to terminal.
    """
    def __init__(self):
        self.welcome = self.get_welcome()
        self.get_next_action = self.get_next_action()

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

        try:
            print('\n\n\n\033[31m' + self.welcome + '\033[0m\n\n\n')
            input('\t\t\t\033[36mHit enter to continue...\033[0m')
        except ValueError:
            self.get_welcome()
        return True


    def get_instructions(self):
        """
        Prints the instructions to the terminal for the user when
        called for the Tetromino Falls game.
        """
        print('\033[0;33m')
        try:
            console.clear_console()
            file = open('instructions.txt', encoding='utf8')
            instructions = file.read()
            file.close()
            try:
                read_instructions = input('\033[31m\nEnter "y" and hit enter to continue: \033[0m')
                if read_instructions not in ('Y', 'y'):
                    raise ValueError(
                        '\033[36m\nEnter the letter y for yes or n for no\n\033[0m'
                    )
            except ValueError as error:
                print(error)
                time.sleep(2)
                console.clear_console()
            if instructions is None:
                raise IOError(
                    "Failed to read instructions from welcome.txt..."
                )
        except IOError as error:
            console.clear_console()
            print(f'\033[31m\n{error}\033[0m')
        return print(f"{instructions}\033[0m")


    def get_goodbye(self):
        """
        Prints the goodbye message to the terminal for the user for the
        Tetromino Falls game.
        """
        return ''


    def get_next_action(self):
        """
        Prints options to terminal for user to decide what route to take
        in Tetromino Falls program.
        """
        return ''
