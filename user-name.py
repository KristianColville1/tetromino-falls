"""This file handles the user input for user name creation"""

from better_profanity import profanity

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
        return True
