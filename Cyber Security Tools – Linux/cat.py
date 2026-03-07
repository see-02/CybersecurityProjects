#!/usr/bin/python3
# remember to give this file execute permissions
import sys
# stdin is sys.stdin
no_files = True


# function for if stdin is specified
def std_in():
    # handle stdin here
    i = 1
    while i < len(sys.argv):
        print(sys.argv[i])
        i += 1


# function for if some sort of file is specified
def infile(file):
    # Make sure to type "python cat.py" before file name
    try:
        with open(file, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        return no_files is True


# this if statement basically tells Python to do this first if
# we're running it from the command line
if __name__ == "__main__":
    # check somehow if we're reading from stdin or from a file
    # hint: how many arguments are there?
    if len(sys.argv) == 2:
        infile(sys.argv[1])
    # if we have more than one argument
    elif len(sys.argv) > 2:
        i = 1
        while i < len(sys.argv):
            infile(sys.argv[i])
            i += 1
        if no_files is True:
            std_in()
    else:
        print("No arguments given.")
