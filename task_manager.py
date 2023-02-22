# =====importing libraries===========
# This is the section where libraries are imported
from datetime import date
from colorama import Fore
from colorama import Style
from datetime import datetime
import os.path


# This function called when the user selects 'r' to register a user.
def reg_user():
    while True:
        new_username = input("Please enter your username: ")
        new_password = input("Please enter your password: ")
        confirm_password = input("Please confirm your password: ")

        # Checking if username exists in the file
        if new_username in login_dict:
            print("This username already exists. Try again.")
            continue
        if new_password == confirm_password:
            with open("user.txt", "a") as new_file:
                new_file.write("\n")
                new_file.write(new_username + ", " + new_password)
            break
        else:
            print("Passwords don't match. Try again.")
            continue


# This function called when the user selects 'a' to add new task to task.txt file.
def add_task():
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


# This function called when the user selects 'va' to read all the tasks listed in 'tasks.txt' and
# print to the console in the format of Output 2
def view_all():
    with open("tasks.txt", "r") as read_tasks:
        lines = read_tasks.readlines()

        straight_line = "⸻" * 36
        for task_number, task in enumerate(lines, 1):
            task_list = task.replace("\n", "").split(", ")
            # Ref: color of output https: // pypi.org / project / colorama /
            print(f"""{Fore.BLUE}
{straight_line}
Task number:         {task_number}
Task:                {task_list[1]}
Assigned to:         {task_list[0]}
Date assigned:       {task_list[3]}
Due date:            {task_list[4]}
Task Complete?       {task_list[5]}
Task description:                              
 {task_list[2]}
{straight_line}{Style.RESET_ALL}""")


# This function called when the user selects 'vm' to view all the tasks listed in 'tasks.txt'
# that have been assigned to them and able to edit tasks
def view_mine():
    with open("tasks.txt", "r") as read_tasks:
        lines = read_tasks.readlines()
        list_number = []
        straight_line = "⸻" * 36
        for task_number, task in enumerate(lines, 1):
            task_list = task.replace("\n", "").split(", ")
            # Ref: color of output https: // pypi.org / project / colorama /
            if username_input == task_list[0]:
                list_number.append(task_number)
                print(f"""{Fore.BLUE}
{straight_line}
Task number:         {task_number}
Task:                {task_list[1]}
Assigned to:         {task_list[0]}
Date assigned:       {task_list[3]}
Due date:            {task_list[4]}
Task Complete?       {task_list[5]}
Task description:                              
 {task_list[2]}
{straight_line}{Style.RESET_ALL}""")

        while True:
            spec_task = int(input("Select a task by entering a task number ('-1' to return to the main menu): "))
            if spec_task == -1:
                menu()
                break
            if spec_task in list_number:
                edit_lines = lines[spec_task - 1]
                split_lines = edit_lines.split(", ")
                if split_lines[-1] == "Yes\n":
                    print("This task has already been completed and cannot be amended.\n")
                    menu()
                    break
                else:
                    edit_lines = lines[spec_task - 1]
                break
            else:
                print("This task number doesn't exist or has been assigned to different user.")
                continue

        while True:
            change = int(input("""Select one of the following Options below:
1 - Mark the task as complete
2 - Edit the task
""").lower())

            if change <= 0 or change >= 3:
                print("This option is not available.")
                continue
            elif change == 1:
                split_lines = edit_lines.split(", ")

                split_lines[-1] = "Yes\n"
                new_task = ", ".join(split_lines)
                lines[spec_task - 1] = new_task
                print("The task has been successfully completed.\n")

                with open("tasks.txt", "w") as file1:
                    for line1 in lines:
                        file1.write(line1)
                    break

            # Edit username of the person to whom the task is assigned to or the due date of the task can be edited
            else:
                edit = int(input("""Select one of the following Options below:
1 - Edit username of the person to whom the task is assigned to
2 - Edit the due date of the task
""").lower())

                # Change username of the person to whom the task is assigned to
                if edit <= 0 or edit >= 3:
                    print("This option is not available.")
                    continue
                elif edit == 1:
                    new_user = input("Enter new username of person to whom the task is assigned to: ")
                    split_lines = edit_lines.split(", ")

                    split_lines[0] = new_user
                    new_user1 = ", ".join(split_lines)
                    lines[spec_task - 1] = new_user1
                    print("The task has been successfully amended.\n")

                    with open("tasks.txt", "w") as file2:
                        for line2 in lines:
                            file2.write(line2)
                        break

                # Change the due date of the task
                else:
                    while True:
                        new_dd = input("Please enter new due date of the task formatted yyyy-mm-dd): ")
                        date_format = "%Y-%m-%d"
                        res = True
                        try:
                            res = bool(datetime.strptime(new_dd, date_format))
                        except ValueError:
                            res = False
                        if res:
                            break
                        else:
                            print("Incorrect date format.")
                            continue
                    new_dd = new_dd.split("-")
                    year, month, day = [int(item) for item in new_dd]
                    new_dd_f = date(year, month, day).strftime("%d %b %Y")

                    split_lines = edit_lines.split(", ")


                    split_lines[4] = new_dd_f
                    new_due_date = ", ".join(split_lines)
                    lines[spec_task - 1] = new_due_date
                    print("The task has been successfully amended.\n")

                    with open("tasks.txt", "w") as file3:
                        for line3 in lines:
                            file3.write(line3)
                        break


# This function will generate reports
def generate_reports():
    count_no = 0
    count_yes = 0
    count_overdue = 0

    # task_overview.txt should contain:
    with open("tasks.txt", "r") as file:
        # 1. The total number of tasks that have been generated and tracked using the task_manager.py
        lines = file.readlines()
        number_of_tasks = len(lines)

        # 2. Total number of completed tasks
        for task in lines:
            task_list = task.replace("\n", "").split(", ")
            if task_list[5] == 'No':
                count_no += 1

            # 3. Total number of uncompleted tasks
            else:
                count_yes += 1

            # 4. Total number of tasks that haven't been completed and that are overdue
            if task_list[5] == 'No' and (task_list[4] < task_list[3]):
                count_overdue += 1

        # 5. The % of tasks that incomplete
        incomplete_rep = (count_no * 100) / number_of_tasks
        # 6. The % of tasks that are overdue
        overdue_rep = (count_overdue * 100) / number_of_tasks

    with open("task_overview.txt", "w") as file4:
        file4.write(f"The total number of: ")
        file4.write(f"\n    1. tasks that have been generated and tracked using the task_manager.py is "
                    f"{number_of_tasks}.")
        file4.write(f"\n    2. completed tasks is {count_yes}.")
        file4.write(f"\n    3. uncompleted tasks is {count_no}.")
        file4.write(f"\n    4. tasks that haven't been completed and that are overdue is {count_overdue}.")
        file4.write(f"\nThe percentage of tasks that incomplete is {round(incomplete_rep, 1)}%.")
        file4.write(f"\nThe percentage of tasks that are overdue is {round(overdue_rep, 1)}%.")

    # user_overview.txt should contain:
    # 1. The total number of users registered with task_manager.py.
    count = {}
    users = []
    for user in lines:
        user_list = user.split(", ")
        users.append(user_list[0])

    for user in users:
        if user in count:
            count[user] += 1
        else:
            count[user] = 1
    len(count)

    # 2. The total number of tasks that have been generated and tracked using task_manager.py.
    with open("user_overview.txt", "w") as file5:
        file5.write(f"Total number of registered users:    {len(count)}\n")
        file5.write(f"Total number of tasks:               {number_of_tasks}\n")

        # For each user also describe:
        # 1. The total number of tasks assigned to that user.
        for user in login_dict.keys():
            count_task = 0
            perc = 0
            count_yes1 = 0
            perc_compl = 0
            count_no1 = 0
            perc_uncompl = 0
            overdue = 0
            perc_overdue = 0

            file5.write("---------------------------------------------------\n")
            file5.write(f"Username: {user}\n")
            file5.write("---------------------------------------------------\n")

            for line in lines:
                task_list = line.replace("\n", "").split(", ")

                if task_list[0] == user:

                    count_task += 1
                    # 2. The percentage of the total number of tasks that have been assigned to that user
                    perc = count_task * 100 / number_of_tasks

                    # 3. The percentage of the tasks assigned to that user that have been completed
                    if task_list[5] == 'Yes':
                        count_yes1 += 1
                        perc_compl = count_yes1 * 100 / number_of_tasks

                    # 4. The percentage of the tasks assigned to that user that must still be completed
                    else:
                        count_no1 += 1
                        perc_uncompl = count_no1 * 100 / number_of_tasks

                        # 5. The percentage of the tasks assigned to that user that have not yet been completed
                        # and are overdue
                        if task_list[3] > task_list[4]:
                            overdue += 1
                            perc_overdue = overdue * 100 / number_of_tasks

            file5.write(f"Total tasks assigned:                                 {count_task}\n")
            file5.write(f"Percentage of assigned tasks:                         {round(perc, 1)}%\n")
            file5.write(f"Percentage of completed tasks assigned:               {round(perc_compl, 1)}%\n")
            file5.write(f"Percentage of uncompleted tasks assigned:             {round(perc_uncompl, 1)}%\n")
            file5.write(f"Percentage of incomplete and overdue tasks assigned:  {round(perc_overdue, 1)}%\n")


# This function will display statistics
def display_statistics():
    # the reports generated are read from task_overview.txt and user_overview.txt and displayed on the screen info
    # Ref: check if file exists:
    # https: // www.pythontutorial.net / python - basics / python - check - if -file - exists /
    if os.path.exists('task_overview.txt'):
        with open("task_overview.txt", "r") as file3:
            lines = file3.read().splitlines()
            straight_line = "⸻" * 36
            print(straight_line)
            print("TASK OVERVIEW:")
            print(straight_line)
            for line in lines:
                print(line)
            print(straight_line)

    if os.path.exists('user_overview.txt'):
        with open("user_overview.txt", "r") as file3:
            lines = file3.read().splitlines()
            straight_line = "⸻" * 36
            print("USER OVERVIEW:")
            print(straight_line)
            for line in lines:
                print(line)
            print(straight_line)

    # If these text files don’t exist (because the user has not selected to generate
    # them yet), first call the code to generate the text files
    else:
        generate_reports()
        if os.path.exists('task_overview.txt'):
            with open("task_overview.txt", "r") as file3:
                lines = file3.read().splitlines()
                straight_line = "⸻" * 36
                print(straight_line)
                print("TASK OVERVIEW:")
                print(straight_line)
                for line in lines:
                    print(line)
                print(straight_line)

        if os.path.exists('user_overview.txt'):
            with open("user_overview.txt", "r") as file3:
                lines = file3.read().splitlines()
                straight_line = "⸻" * 36
                print("USER OVERVIEW:")
                print(straight_line)
                for line in lines:
                    print(line)
                print(straight_line)


# This function will display menu and return user's choice
def menu():
    while True:
        if username_input == "admin":
            # Presenting the privilege menu to the user 'admin'
            user_menu = input('''Select one of the following Options below:
r -  Registering a user
a -  Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e -  Exit
: ''').lower()
        # Presenting the menu for registered users who have limited access
        else:
            user_menu = input('''Select one of the following Options below:
a -  Adding a task
va - View all tasks
vm - View my task
e -  Exit
: ''').lower()

        if user_menu == 'r' and username_input == "admin":
            pass
            reg_user()
            continue
        elif user_menu == 'a':
            pass
            add_task()
            continue
        elif user_menu == 'va':
            pass
            view_all()
            continue
        elif user_menu == 'vm':
            pass
            view_mine()
            continue
        elif user_menu == 'gr' and username_input == "admin":
            pass
            generate_reports()
            continue
        elif user_menu == 'ds' and username_input == "admin":
            pass
            display_statistics()
            continue
        elif user_menu == 'e':
            print('Goodbye!!!')
            exit()
        else:
            print("You have made a wrong choice, Please Try again")
            continue
        return user_menu


# ====Login Section====
# This section will allow a user to login.
with open("user.txt", "r") as file_l:
    lines_l = file_l.readlines()
    login_dict = {}
    for line_l in lines_l:
        username, password = line_l.replace("\n", "").split(", ")
        password = password.strip()
        login_dict[username] = password
    while True:
        username_input = input("Please enter your username: ")
        password_input = input("Please enter your password: ")
        if username_input not in login_dict:
            print("Username is not valid.")
        elif username_input in login_dict and password_input not in login_dict[username_input]:
            print("Password is not valid")
        else:
            print("You are now logged in\n")
            break

    menu()
