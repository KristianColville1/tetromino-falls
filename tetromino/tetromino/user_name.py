"""This file handles the user input for user name creation"""
from better_profanity import profanity
from tetromino.tetromino import console

class User():
    """
    Creates a user name object.
    """
    def __init__(self):
        self.user_name = self.get_user_name()


    def get_user_name(self):
        """
        When called it allows the user to input a name.
        It checks for profanity and loops using recursion until valid.
        """
        try:
            name = input('Enter your name: ')
            self.user_name = name
            if len(name) < 4 or len(name) > 12:
                raise ValueError(
                    'username must be at least 4 characters\n and no more than 12'
                )
            if profanity.contains_profanity(name):
                raise ValueError(
                    '\033[31mProfanity detected\033[0m'
                )
            if self.definitely_no_profanity(name) is True:
                raise ValueError(
                    '\033[31mProfanity detected\033[0m'
                )
        except ValueError as error:
            console.clear_console()
            print(f'Invalid username entered: {error}, please try again.\n\n\n')
            self.get_user_name()

        return self.user_name


    def definitely_no_profanity(self, name):
        """
        Checks the users name string to see if profanity can be found.
        Returns True if profanity detected.
        """
        self.user_name = name
        letters_tested = ''
        for char in self.user_name:
            letters_tested += char
            if profanity.contains_profanity(letters_tested):
                return True

        try:
            file = open('exclude.json', encoding='utf8')
            profanity_list = file.read()
            for line in profanity_list:
                if line in self.user_name:
                    return True
        except IOError:
            print('\033[31mChecking profanity list failed...\033[0m')
        return False
