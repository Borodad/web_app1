import os

FILEPATH = os.path.join(os.getcwd(), "..\web_app1\todolist.txt")

def get_to_do_list(filepath=FILEPATH): # note use of default argument - which can be overridden
    with open(filepath, "r") as file_local:  # automatically closes file
        to_do_list_local = file_local.readlines()  # read each line
    return to_do_list_local

def write_to_do_list(to_do_list_local, filepath=FILEPATH): # note non-default argument has to go before default argument
    """Write the to-do items list to the text file.  No value returned"""
    with open(filepath, "w") as file_local:
        file_local.writelines(to_do_list_local) # note no need to return any values - will return 'none'

# print(__name__)
if __name__ == "__main__": # if functions is ran directly then print message.  __name__ is a hidden variable
    # and it's value is based on the file that calls/runs the code.  Here if functions is called directly __name__ will be __main__ otherwise
    # if it's ran from CLI_main.py its name will be set to to_do_list.modules.functions
    print("hello from functions")