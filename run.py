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
    print('\n\n\n\033[31m' + message + '\033[0m\n\n\n')
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
                'username must be at least 2 characters and no more than 12'
            )
    except ValueError as error:
        print(f'Invalid username entered: {error}, please try again.\n\n\n')
        return False
    return name


def what_next_user():
    """
    Asks the user what they would like to do next.
    Start the game, load instructions or exit.
    """
    try:
        print(f'\n\nWhat do you want to do {USER_NAME}.')
        print("Enter 'p' to play the game.")
        print("Enter 'i' for instructions..")
        print("Enter 'e' to exit the program.")
        user_decision = input('f\n So What do you want to do next {USER_NAME}?\n ')
        if user_decision in ('p', 'i', 'e'):
            raise ValueError(
                f'Look buddy, you need to enter something else {user_decision} is not valid'
            )
    except ValueError as error:
        print(f'Invalid data received... {error}, please try again')
        return False
    return user_decision

def get_next_action():
    """
    Gets the users next action and will decide what route to take.
    Play the game, get instructions or exit program
    """
    # gets and checks the users decision on next actions
    decision = what_next_user()
    if decision is False:
        while decision is False:
            decision = what_next_user()

    if decision is 'p':
        start_game()
    elif decision is 'i':
        get_instructions()
    else:
        exit_program()

def start_game():
    
def get_instructions():

def exit_program():

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

get_next_action()

main()
