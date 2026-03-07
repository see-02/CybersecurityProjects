# Notes:
# 1. Use the following username and password to access the admin rights
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the
# program will look in your root directory for the text files.

# =====importing libraries===========
import os
from datetime import datetime, date


# =====functions=====================
def reg_user(user, new_password, confirmation):
    # Check if the new password and confirmed password are the same.
    if (new_password == confirmation) and (user not in
                                           username_password.keys()):
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[user] = new_password

        with open("user.txt", "a") as out_file:
            out_file.write(f"\n{user};{new_password}")

    # - Otherwise you present a relevant message.
    elif (new_password == confirmation) and (user in username_password.keys()):
        print("Username already exists. Please try a different username.")
    else:
        print("Passwords do not match.")


def add_task(task_username, task_title, task_description, due_date_time):
    # Create new task with the information given by user
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
        }
    # Add new_task to task_list and task_file
    task_list.append(new_task)
    with open("tasks.txt", "a") as task_file:
        str_attrs = [
            new_task['username'],
            new_task['title'],
            new_task['description'],
            new_task['due_date'].strftime(DATETIME_STRING_FORMAT),
            new_task['assigned_date'].strftime(DATETIME_STRING_FORMAT),
            "Yes" if new_task['completed'] else "No"
        ]
        separated_attrs = ";".join(str_attrs)
        task_file.write(f"\n{separated_attrs}")
    print("Task successfully added.")


def view_all():
    '''Run through data in task_list and print data out in a
    user-friendly manner'''
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += (
            f'''Date Assigned: \t '''
            f'''{t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n''')
        disp_str += (
            f'''Due Date: \t '''
            f'''{t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n''')
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)


def view_mine():
    '''Run through data in task_list and keep track of the index of the
    user list as well as the original task list so we're able to call
    the corresponding data in the original task_list'''
    i = 0
    j = 0
    index_list = []
    # Print tasks only assigned to current user
    for t in task_list:
        if t['username'] == curr_user:
            disp_str = f"Task {i+1}: \t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += (f'''Date Assigned: \t '''
                         f'''{t['assigned_date'].strftime(
                             DATETIME_STRING_FORMAT)}\n''')
            disp_str += (f'''Due Date: \t '''
                         f'''{t['due_date'].strftime(
                             DATETIME_STRING_FORMAT)}\n''')
            disp_str += f"Task Description: \n {t['description']}\n"
            index_list.append(j)
            i += 1
            print(disp_str)
        j += 1
    # Ask user about editing the task they choose
    done = False
    while done is False:
        open_task = input('Type the corresponding task number to open it,\n'
                          'OR type -1 to go back to the main menu: ')
        try:
            open_task = int(open_task)
            # Leads back to main menu
            if open_task == -1:
                print("")
                break
            # Checks if task number is in list of tasks
            elif (index_list[open_task-1] in index_list):
                index = index_list[open_task-1]
                task_edit = task_list[index]
                # Option to mark task as completed (if not already)
                if task_edit['completed'] is False:
                    edit_task = input(
                        f'Would you like to mark Task {open_task} '
                        'as completed?\nOnce it is marked completed, '
                        'it cannot be edited. (Yes or no): ')
                    # User has chosen to mark task as completed
                    if edit_task.lower() == "yes":
                        task_edit['completed'] = "Yes"
                        with open("tasks.txt", "w") as task_file:
                            task_list_to_write = []
                            for t in task_list:
                                str_attrs = [
                                    t['username'],
                                    t['title'],
                                    t['description'],
                                    t['due_date'].strftime(
                                        DATETIME_STRING_FORMAT),
                                    t['assigned_date'].strftime(
                                        DATETIME_STRING_FORMAT),
                                    "Yes" if t['completed'] else "No"
                                ]
                                task_list_to_write.append(";".join(str_attrs))
                            task_file.write("\n".join(task_list_to_write))
                        print("Task updated.\n")
                    # User has chosen NOT to mark task as completed
                    # and is given the option to edit the task
                    if edit_task.lower() == "no":
                        done_editing = False
                        while done_editing is False:
                            answer = input(
                                'Which aspect would you like to edit?\n'
                                '1. Who it\'s assigned to\n'
                                '2. Due date\n'
                                '3. Exit editing\n'
                                'Please enter the corresponding number: ')
                            # User has chosen to change who task is assigned to
                            if answer == "1":
                                new_user = input(
                                    'Please enter the name of the new user: ')
                                task_edit['username'] = new_user
                                with open("tasks.txt", "w") as task_file:
                                    task_list_to_write = []
                                    for t in task_list:
                                        str_attrs = [
                                            t['username'],
                                            t['title'],
                                            t['description'],
                                            t['due_date'].strftime(
                                                DATETIME_STRING_FORMAT),
                                            t['assigned_date'].strftime(
                                                DATETIME_STRING_FORMAT),
                                            "Yes" if t['completed'] else "No"
                                        ]
                                        task_list_to_write.append(";".join(
                                            str_attrs))
                                    task_file.write("\n".join(
                                        task_list_to_write))
                                # Give user the option of editing more
                                continue_editing = input(
                                    'Task updated. '
                                    'Would you like to continue editing? ')
                                if continue_editing.lower() == "yes":
                                    done_editing = False
                                if continue_editing.lower() == "no":
                                    done_editing = True
                                # User didn't give yes or no answer
                                else:
                                    print("Unable to read answer.")
                            # User has chosen to edit the due date of the task
                            elif answer == "2":
                                while True:
                                    try:
                                        task_due_date = input(
                                            'Please enter new due date of task'
                                            ' (YYYY-MM-DD): ')
                                        due_date_time = datetime.strptime(
                                            task_due_date,
                                            DATETIME_STRING_FORMAT)
                                        task_edit['due_date'] = due_date_time
                                        with open(
                                                "tasks.txt", "w") as task_file:
                                            due_date_to_write = []
                                            for t in task_list:
                                                str_attrs = [
                                                    t['username'],
                                                    t['title'],
                                                    t['description'],
                                                    t['due_date'].strftime(
                                                        DATETIME_STRING_FORMAT
                                                        ),
                                                    t['assigned_date'
                                                      ].strftime(
                                                        DATETIME_STRING_FORMAT
                                                          ),
                                                    "Yes" if t['completed']
                                                    else "No"
                                                ]
                                                due_date_to_write.append(
                                                    ";".join(str_attrs))
                                            task_file.write("\n".join(
                                                due_date_to_write))
                                            continue_editing = input(
                                                            'Task updated. '
                                                            'Would you like to'
                                                            ' continue editing'
                                                            '? ')
                                            # Give user the option of
                                            # editing more
                                            if continue_editing.lower() == (
                                                    "yes"):
                                                done_editing = False
                                            if continue_editing.lower() == (
                                                    "no"):
                                                done_editing = True
                                            # User didn't give yes or no answer
                                            else:
                                                print("Unable to read answer.")
                                        break
                                    # User didn't give due date in correct
                                    # format
                                    except ValueError:
                                        print(
                                            'Invalid datetime format. '
                                            'Please use the format specified.')
                            # User has chosen to exit task editing
                            elif answer == "3":
                                done = True
                                break
                            # User did not give answer 1, 2, or 3
                            else:
                                print("Number not valid. Please try again.\n")
                # No option to edit task since task is marked as completed
                if task_edit['completed'] is True:
                    print('Since this task has been completed, '
                          'it cannot be edited.\n''')
            # Task number inputted by user is an int, but not in range
            else:
                open_task = input('The number you inputted is not assigned '
                                  'to a task.\nPlease enter a number '
                                  'corresponding to the task you want to edit'
                                  '\nOR type -1 to go back to the main menu: ')
        # Task number inputted by user is not an int
        except ValueError:
            open_task = input('Value entered is not a valid number.\n'
                              'Please enter a number corresponding to the task'
                              'you want to edit\nOR type -1 to go back to the'
                              ' main menu: ')


def generate_report():
    # Generating task overview report
    tot_tasks = 0
    uncompleted = 0
    completed = 0
    overdue = 0

    # Counting types of task to include in report
    for t in task_list:
        tot_tasks += 1
        if t['completed'] is False:
            uncompleted += 1
            if (date.today().strftime(DATETIME_STRING_FORMAT) >
                    t['due_date'].strftime(DATETIME_STRING_FORMAT)):
                overdue += 1
        if t['completed'] is True:
            completed += 1
    # Calculating percentages
    percent_incomplete = float(uncompleted/tot_tasks) * 100
    percent_overdue = float(overdue/tot_tasks) * 100
    # Creating dictionary of new task
    new_task_ov = {
        "total tasks": str(tot_tasks),
        "uncompleted tasks": str(uncompleted),
        "completed tasks": str(completed),
        "overdue tasks": str(overdue),
        "percentage of tasks incomplete": str(
            round(percent_incomplete, 2)) + "%",
        "percentage of tasks overdue": str(round(percent_overdue, 2)) + "%"
        }

    # Add new_task_ov to task_ov_list and task_ov_file
    task_ov_list.append(new_task_ov)
    with open("task_overview.txt", "w") as task_ov_file:
        task_ov_to_write = []
        for t in task_ov_list:
            str_attrs = [
                t['total tasks'],
                t['uncompleted tasks'],
                t['completed tasks'],
                t['overdue tasks'],
                t['percentage of tasks incomplete'],
                t['percentage of tasks overdue']
            ]
            task_ov_to_write.append(";".join(str_attrs))
        task_ov_file.write("\n".join(task_ov_to_write))
    print("\nTask overview successfully added.")

    # Print task overview in user-friendly manner
    print(f'Total tasks: \t\t {str(tot_tasks)}\n'
          f'Uncompleted Tasks: \t {str(uncompleted)}\n'
          f'Completed Tasks: \t {str(completed)}\n'
          f'Overdue Tasks: \t\t {str(overdue)}\n'
          'Percentage of uncompleted tasks: '
          f'{str(round(percent_incomplete, 2))}%\n'
          f'Percentage of overdue tasks: \t'
          f'{str(round(percent_overdue, 2))}%\n')

    # Generate user overview report
    total_users = 0
    tasks = []
    due = []
    task_per_user = []
    overdue = []
    completed = []
    user = []

    # Count and calculate types of tasks per user
    for u in username_password.keys():
        user.append(u)
        total_users += 1
        tasks_per_user = 0
        due_per_user = 0
        overdue_per_user = 0
        completed_per_user = 0
        for t in task_list:
            # Check if username is assigned to tasks
            if u == t['username']:
                tasks_per_user += 1
                # Check if corresponding task is completed
                if t['completed'] is False:
                    due_per_user += 1
                    # Check if task is overdue
                    if (date.today().strftime(DATETIME_STRING_FORMAT) >
                            t['due_date'].strftime(DATETIME_STRING_FORMAT)):
                        overdue_per_user += 1
                if t['completed'] is True:
                    completed_per_user += 1
            # Case if user has at least one task
            if tasks_per_user != 0:
                percent_ttp_user = round(
                    float(tasks_per_user/tot_tasks * 100), 2)
                percent_complete_per_user = round(float(
                    completed_per_user/tasks_per_user * 100), 2)
                percent_due_per_user = round(
                    float(due_per_user/tasks_per_user * 100), 2)
                percentage_overdue_per_user = round(float(
                    overdue_per_user/tasks_per_user * 100), 2)
            # Case if user doesn't have any tasks assigned to them
            else:
                percent_ttp_user = 0
                percent_complete_per_user = 0
                percent_due_per_user = 0
                percentage_overdue_per_user = 0
        # Adding each value to it's corresponding list
        tasks.append(tasks_per_user)
        due.append(percent_due_per_user)
        task_per_user.append(percent_ttp_user)
        overdue.append(percentage_overdue_per_user)
        completed.append(percent_complete_per_user)
    # Change lists to string for easier storage in user_overview.txt
    tot_tasks_p_user = ','.join(str(x) for x in tasks)
    due_tasks_p_user = ','.join(str(x) for x in due)
    per_tasks_p_user = ','.join(str(x) for x in task_per_user)
    per_overdue_p_user = ','.join(str(x) for x in overdue)
    per_complete_p_user = ','.join(str(x) for x in completed)
    # Create the user overview dictionary
    new_user_ov = {
        "total tasks": str(tot_tasks),
        "total users": str(total_users),
        "total tasks for user": tot_tasks_p_user,
        "percentage of total tasks for user":  per_tasks_p_user,
        "percentage of tasks complete for user": per_complete_p_user,
        "percentage of tasks due": due_tasks_p_user,
        "percentage of tasks overdue": per_overdue_p_user
        }
    # Add new_user_ov to user_ov_list and user_ov_file
    user_ov_list.append(new_user_ov)
    with open("user_overview.txt", "w") as user_ov_file:
        user_ov_to_write = []
        for u in user_ov_list:
            str_attrs = [
                u['total tasks'],
                u['total users'],
                u['total tasks for user'],
                u['percentage of total tasks for user'],
                u['percentage of tasks complete for user'],
                u['percentage of tasks due'],
                u['percentage of tasks overdue']
            ]
            user_ov_to_write.append(";".join(str_attrs))
        user_ov_file.write("\n".join(user_ov_to_write))
    print("\nUser overview successfully added.")
    # Print user overview in a user-friendly manner
    print(f'''Total number of tasks: \t {str(tot_tasks)}
Total number of users: \t {str(total_users)}''')
    k = 0
    for u in user:
        print("User: " + u)
        print("\tTotal tasks:\t\t\t\t" + str(tasks[k]))
        print("\tPercentage of total tasks:\t\t" + str(task_per_user[k]) + "%")
        print('\tPercentage of their tasks completed:\t'
              + str(completed[k]) + '%')
        print("\tPercentage of their tasks due:\t\t" + str(due[k]) + "%")
        print("\tPercentage of their tasks overdue:\t" + str(overdue[k]) + "%")
        k += 1


# ======end of functions=============
DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3],
                                           DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4],
                                                DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


# Create task_overview.txt if it doesn't exist
if not os.path.exists("task_overview.txt"):
    with open("task_overview.txt", "w") as default_file:
        pass

with open("task_overview.txt", 'r') as task_ov_file:
    task_ov_data = task_ov_file.read().split("\n")
    task_ov_data = [t for t in task_ov_data if t != ""]

task_ov_list = []
for to_str in task_ov_data:
    curr_nt = {}

    # Split by semicolon and manually add each component
    task_ov_components = to_str.split(";")
    curr_nt['total tasks'] = task_ov_components[0]
    curr_nt['uncompleted tasks'] = task_ov_components[1]
    curr_nt['completed tasks'] = task_ov_components[2]
    curr_nt['overdue tasks'] = task_ov_components[3]
    curr_nt['percentage of tasks incomplete'] = task_ov_components[4]
    curr_nt['percentage of tasks overdue'] = task_ov_components[5]

    task_ov_list.append(curr_nt)


# Create user_overview.txt if it doesn't exist
if not os.path.exists("user_overview.txt"):
    with open("user_overview.txt", "w") as default_file:
        pass

with open("user_overview.txt", 'r') as user_ov_file:
    user_ov_data = user_ov_file.read().split("\n")
    user_ov_data = [t for t in user_ov_data if t != ""]

user_ov_list = []
for u_str in user_ov_data:
    current = {}

    # Split by semicolon and manually add each component
    user_ov_components = u_str.split(";")
    current['total tasks'] = user_ov_components[0]
    current['total users'] = user_ov_components[1]
    current['total tasks for user'] = user_ov_components[2]
    current['percentage of total tasks for user'] = user_ov_components[3]
    current['percentage of tasks complete for user'] = user_ov_components[4]
    current['percentage of tasks due'] = user_ov_components[5]
    current['percentage of tasks overdue'] = user_ov_components[5]

    user_ov_list.append(current)

# ====Login Section====
'''This code reads usernames and password from the user.txt file to
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
ds - Display statistics
e - Exit
: ''').lower()
    # Registering a user
    if menu == 'r':
        '''Add a new user to the user.txt file'''
        # - Request input of a new username
        new_username = input("New Username: ")

        # - Request input of a new password
        new_password = input("New Password: ")

        # - Request input of password confirmation.
        confirm_password = input("Confirm Password: ")

        # Call reg_user to check password and register user
        reg_user(new_username, new_password, confirm_password)
    # Adding a task
    elif menu == 'a':
        '''Allow a user to add a new task to task.txt file
            Prompt a user for the following:
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and
             - the due date of the task.'''
        # Check if username given exists
        while True:
            task_username = input("Name of person assigned to task: ")
            if task_username not in username_password.keys():
                print("User does not exist. Please enter a valid username")
            else:
                break
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")
        # Make sure due date is in correct form
        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date,
                                                  DATETIME_STRING_FORMAT)
                break
            except ValueError:
                print('Invalid datetime format.\n'
                      'Please use the format specified')
        add_task(task_username, task_title, task_description, due_date_time)
    # View all tasks
    elif menu == 'va':
        '''Reads the task from task.txt file and prints to the console in the
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
        view_all()
    # View my tasks
    elif menu == 'vm':
        '''Reads the task from task.txt file and prints to the console in the
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
        view_mine()
    # Generate reports
    elif menu == 'gr':
        '''Generates reports viewing information about tasks and users'''
        generate_report()
    # Display statistics
    elif menu == 'ds' and curr_user == 'admin':
        '''If the user is an admin they can display statistics about number of
        users and tasks.'''
        generate_report()
    # Exit menu
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    # User has not entered a valid answer
    else:
        print("You have made a wrong choice, Please Try again")
