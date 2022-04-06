"""Used to clear console when called"""
import os

# Taken from delfstack https://www.delftstack.com/howto/python/python-clear-console/
def clear_console():
    """Clears the terminal screen when called."""
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
