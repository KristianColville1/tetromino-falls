"""This file handles the user input for user name creation"""
from better_profanity import profanity
import console

class User():
    """
    Creates a user name object.
    """
    def __init__(self):
        self.user_name = self._get_user_name()


    def _get_user_name(self):
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
            if profanity.contains_profanity(name):
                raise ValueError(
                    '\033[31mProfanity detected\033[0m'
                )
            self.user_name = name
        except ValueError as error:
            console.clear_console()
            print(f'Invalid username entered: {error}, please try again.\n\n\n')
            self._get_user_name()

        return self.user_name
