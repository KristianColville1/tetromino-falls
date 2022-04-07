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


    def print_actions(self):
        """
        Asks the user what they would like to do next.
        Start the game, load instructions or exit.
        """
        try:
            print('\n\nHere are the options available:\n')
            print("\t\033[0;33mEnter '\033[31mp\033[0;33m' to play the game.")
            print("\tEnter '\033[31mi\033[0;33m' for instructions..")
            print("\tEnter '\033[31me\033[0;33m' to exit the program.\033[0m")
            user_decision = input('\n So what will it be?\n ')
            if user_decision not in ('p', 'i', 'e'):
                raise ValueError(
                    f"You need to enter something else as \033[36m{user_decision}\033[0m is invalid"
                )
        except ValueError as error:
            console.clear_console()
            print(f'\n\t\033[31mInvalid input received...\033[0m \n{error}, please try again')
            return False
        return user_decision


    def get_next_action(self):
        """
        Gets the users next action and will decide what route to take.
        Play the game, get instructions or exit program
        """
        # gets and checks the users decision on next actions
        console.clear_console()
        decision = self.print_actions()
        if decision is False:
            while decision is False:
                decision = self.print_actions()

        if decision == 'p':
            return True
        if decision == 'i':
            self.get_instructions()
        elif decision == 'e':
            exit_program()
