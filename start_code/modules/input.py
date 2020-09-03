def first_user_input():
    choice = input("Select an option 1, 2, 3, 4, 5 or (Q)uit: ")
    return choice

def user_description():
    description = input("Enter task description to search for: ")
    return description

def time_taken():
    time = int(input("Enter task duration: "))
    return time

def add_already_made_task():
    task = input("Please enter task description: ")
    return task