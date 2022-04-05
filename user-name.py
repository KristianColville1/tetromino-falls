"""This file handles the user input for user name creation"""
from better_profanity import profanity
import console

class User:
    """
    Creates a user name object.
    """
    def __init__(self):
        self.user_name = self.get_the_user_name()


    def get_the_user_name(self):
        """
        When called it allows the user to input a name.
        It checks for profanity and loops using recursion until valid.
        """
        try:
            name = input('Enter your name: ')
            if len(name) < 4 or len(name) > 12:
                raise ValueError(
                    'username must be at least 4 characters\n and no more than 12'
                )
        except ValueError as error:
            console.clear_console()
            print(f'Invalid username entered: {error}, please try again.\n\n\n')
            return False

        return name
