# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

class Email:
    # Declare the class variable, with default value, for emails.
    def __init__(email, email_address, subject_line, email_content):
        email.email_address = email_address
        email.subject_line = subject_line
        email.email_content = email_content
    # Initialise the instance variables for emails.
    has_been_read = False

    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(email):
        email.has_been_read = True


# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []

# --- Functions --- #
# Build out the required functions for your program.


def populate_inbox(inbox):
    # Create 3 sample emails and add it to the Inbox list.
    first_email = Email("martin4@email.com", "Here's the Update",
                        'Hey!\nTurns out that Martha didn\'t need the '
                        'report after all. If you could send\nlast week\'s '
                        'report again, that should suffice.\n\nThanks,\n'
                        'Martin')
    first_email.has_been_read = False
    second_email = Email("localStore@email.com", "Big Sale!",
                         'Great news!\nWe are holding out biggest sale '
                         'yet! Head on over to Local Store to save big\n'
                         'on all sorts of your favorite items.')
    second_email.has_been_read = False
    third_email = Email("grandmaJo@email.com", "Funny Update",
                        'Hey, sweetie!\nI saw this beautiful sunset outside'
                        ' today and thought of you. How are you doing?\nHow is'
                        ' your family? My dog loves the weather now that '
                        'it\'s so warm outside. Maybe\nwe can video chat '
                        'again soon.'
                        '\n\nLove,\nGramma')
    third_email.has_been_read = False
    inbox.append(first_email)
    inbox.append(second_email)
    inbox.append(third_email)


def list_emails():
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    i = 0
    while i < len(inbox):
        print(str(i) + "\t" + inbox[i].subject_line)
        i += 1


def read_email(index):
    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    print("Subject: " + inbox[index].subject_line)
    print("From: " + inbox[index].email_address)
    print("To: You\n")
    print(inbox[index].email_content)
    print("\n")
    inbox[index].has_been_read = True


# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.

# Fill in the logic for the various menu operations.
menu = True
populate_inbox(inbox)

while True:
    user_choice = input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: ''')
    print("\n")
    if user_choice == "1":
        # add logic here to read an email
        print("Displayed below are your emails:")
        list_emails()
        reading = True
        while reading is True:
            choose_email = input("Please enter the corresponding number "
                                 "of the email you would like to read: ")
            print("\n")
            if choose_email == "0":
                read_email(0)
                print(f"Email from {inbox[0].email_address} marked as read\n")
                more_reading = input("Would you like to read another email? ")
                if more_reading.lower() == "yes":
                    reading = True
                elif more_reading.lower() == "no":
                    reading = False
                else:
                    print("Unable to read request. Please try again.")
                    reading = True
            elif choose_email == "1":
                read_email(1)
                print(f"Email from {inbox[1].email_address} marked as read\n")
                more_reading = input("Would you like to read another email? ")
                if more_reading.lower() == "yes":
                    reading = True
                elif more_reading.lower() == "no":
                    reading = False
            elif choose_email == "2":
                read_email(2)
                print(f"Email from {inbox[2].email_address} marked as read\n")
                more_reading = input("Would you like to read another email? ")
                if more_reading.lower() == "yes":
                    reading = True
                elif more_reading.lower() == "no":
                    reading = False
            else:
                print("Number not recognized. Please try again.")
    elif user_choice == "2":
        # add logic here to view unread emails
        print("Here are your unread emails:\n")
        k = 0
        while k < len(inbox):
            if inbox[k].has_been_read is False:
                read_email(k)
                k += 1
            else:
                k += 1
        print("End of unread emails.")
    elif user_choice == "3":
        # add logic here to quit application
        print("Exiting application. Thank you!")
        menu = False
        break
    else:
        print("Oops - incorrect input.")
