"""
Tetromino Falls is terminal based game displayed in the browser.
"""
import time
from curses import wrapper




def print_welcome_text():
    """
    Prints welcome text to terminal for user and waits for 3 seconds before moving on.
    """
    file = open('welcome-msg.txt')
    message = file.read()
    print('\n\n\n' + message + '\n\n\n')
    file.close()
    time.sleep(3)

def get_user_name():
    """
    Gets the users name and checks the database for conflicting names.
    """
    try:
        name = input('Enter your name: ')
        if len(name) < 2 or len(name) > 12:
            raise ValueError(
                f'username must be at least 2 characters and no more than 12'
            )
    except ValueError as error:
        print(f'Invalid username entered: {error}, please try again.\n\n\n')
        return False
    return name

    
def main():
    """
    Main function calls all the necessary functions to run the game.
    """
    print('')


print_welcome_text()

# get and check user name, keep repeating until valid
USER_NAME = get_user_name()
if USER_NAME is False:
    while USER_NAME is False:
        USER_NAME = get_user_name()

main()
