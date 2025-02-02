# from functions import get_to_do_list, write_to_do_list # module
# from to_do_list.modules import functions
import functions # my module
import time # standard module


now = time.strftime("%d-%m-%Y %H:%M:%S")
print("It is now: ", now)
while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip() # remove white space

    # note that 'case' is not used as it cannot accept expressions e.g. case "add" in user_action
    if user_action.startswith("add"): #instead of using 'in'
    # if "add" in user_action:   # replaced by .startswith method
        to_do = user_action[4:] #4: is a list slicing operation - start at index 4

        to_do_list = functions.get_to_do_list() # function call to custom function using default argument

        to_do_list.append(to_do + "\n")

        functions.write_to_do_list(to_do_list) # filepath is now a default arg, but to_do_list isn't

    elif user_action.startswith("show"):
        # file = open("todolist.txt","r")
        # to_do_list = file.readlines()
        # file.close()

        to_do_list = functions.get_to_do_list() # function call to custom function

        # This for loop is a way to remove the \n ie break line from the to do list
        # new_to_do_list = []

        # for each_item in to_do_list:
        #    stripped_item = each_item.strip('\n')
        #    new_to_do_list.append(stripped_item)

        # This is a 'list comprehension' or 'inline for loop' - another shorter way to remove the \n
        #new_to_do_list = [item.strip('\n') for item in to_do_list]


        # Another way to remove the \n from each item is to do it directly
        # for index, each_item in enumerate(new_to_do_list):
        for index, each_item in enumerate(to_do_list):
            each_item = each_item.strip('\n')
            row = f"{index + 1}- {each_item}" # "f-string"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) # string slice
            number = int(number) - 1 # convert to index - as starts at 0

            to_do_list = functions.get_to_do_list() # function call to custom function

            new_to_do = input("enter the new to do:")
            to_do_list[number] = new_to_do + "\n"

            functions.write_to_do_list(to_do_list)
        except ValueError: # this is an error type - must be specified
            print("Your command is not valid")
            continue # restart the while loop

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:]) # string slice

            to_do_list = functions.get_to_do_list() # function call to custom function

            index = number - 1
            to_do_to_be_removed = to_do_list[index].strip("\n")
            to_do_list.pop(index) # "pop" removes an item

            functions.write_to_do_list(to_do_list)

            message = f"To do {to_do_to_be_removed} was removed"
            print(message)
        except IndexError: # try to complete a number that is out of range
            print("This number is outside the list")
            continue # restart from the while loop

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid")

print("Bye!")








