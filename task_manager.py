# =====importing libraries===========
# This is the section where you will import libraries
from datetime import date
from colorama import Fore
from colorama import Style
from datetime import datetime

# ====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''

with open("user.txt", "r") as file:
    lines = file.readlines()
    login_dict = {}
    for line in lines:
        # Split the line on comma and space and strip the whitespaces
        username, password = line.replace("\n", "").split(", ")
        password = password.strip()
        login_dict[username] = password

    while True:
        username_input = input("Please enter your username: ")
        password_input = input("Please enter your password: ")
        if username_input not in login_dict:
            print("Username is not valid.")
        # Mentor's guidance with keys and values in dictionary
        elif username_input in login_dict and password_input not in login_dict[username_input]:
            print("Password is not valid")
        # Menu will be displayed if the username and password are both correct
        else:
            print("You are now logged in")
            break

while True:
    # Presenting the menu to the user and
    # Making sure that the user input is converted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r':
        pass
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''

        while True:
            new_username = input("Please enter your username: ")
            new_password = input("Please enter your password: ")
            confirm_password = input("Please confirm your password: ")
            # Checking if username exists in the file
            if new_username in login_dict:
                print("This username already exists. Try again.")
            if new_password == confirm_password:
                with open("user.txt", "a") as file:
                    file.write("\n")
                    file.write(new_username + ", " + new_password)
                break
            else:
                print("Passwords don't match. Try again.")

    elif menu == 'a':
        pass
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''

        print("Please enter the following:")
        person_username = input("A username of the person whom the task is assigned to: ")
        title = input("A title of a task: ")
        description = input("A description of the task: ")
        # Check if the user enters due date in correct format
        # https://www.geeksforgeeks.org/python-validate-string-date-format/
        while True:
            due_date = input("The due date of the task formatted yyyy-mm-dd): ")
            date_format = "%Y-%m-%d"
            res = True
            try:
                res = bool(datetime.strptime(due_date, date_format))
            except ValueError:
                res = False
            if res:
                break
            else:
                print("Incorrect date format.")
                continue
        due_date = due_date.split("-")
        # Ref: create date from user input https://bobbyhadz.com/blog/python-input-date
        year, month, day = [int(item) for item in due_date]
        due_date_f = date(year, month, day).strftime("%d %b %Y")

        today = date.today()
        # Date format https://www.geeksforgeeks.org/formatting-dates-in-python/
        assigned_date = today.strftime("%d %b %Y")
        completed = "No"
        new_task = (person_username + ", " + title + ", " + description + ", " + assigned_date + ", "
                    + due_date_f + ", " + completed)

        with open("tasks.txt", "a") as file1:
            file1.write("\n")
            file1.write(new_task)

    elif menu == 'va':
        pass
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''
        with open("tasks.txt", "r") as file1:
            lines = file1.readlines()
            straight_line = "⸻" * 36
            for line in lines:
                person_username, title, description, assigned_date, due_date_f, completed = line.replace("\n",
                                                                                                         "").split(", ")
                # Ref: color of output https: // pypi.org / project / colorama /
                print(f"""{Fore.BLUE}
{straight_line}
Task:                {title}
Assigned to:         {person_username}
Date assigned:       {assigned_date}
Due date:            {due_date_f}
Task Complete?       {completed}
Task description:    
 {description}
{straight_line}{Style.RESET_ALL}""")

    elif menu == 'vm':
        pass
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''
        with open("tasks.txt", "r") as file1:
            lines = file1.readlines()
            straight_line = "⸻" * 36
            for line in lines:
                person_username, title, description, assigned_date, due_date_f, completed = line.replace("\n",
                                                                                                         "").split(", ")
                if username_input == person_username:
                    print(f"""{Fore.BLUE}
{straight_line}
Task:                {title}
Assigned to:         {person_username}
Date assigned:       {assigned_date}
Due date:            {due_date_f}
Task Complete?       {completed}
Task description:    
 {description}
 {straight_line}{Style.RESET_ALL}""")


    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
