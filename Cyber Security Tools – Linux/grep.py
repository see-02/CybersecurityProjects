#!/usr/bin/python3
# remember to give this file execute permissions
import sys
# stdin is sys.stdin


def match(haystack, needle):
    # all of grep's brains
    # haystack is where you're looking, needle is what you're looking for
    # remember that you only need to do a simple match
    no_matches = True
    try:
        with open(haystack, 'r') as file:
            words = []
            for line in file:
                for word in line.split():
                    words.append(word)
            for word in words:
                if word == needle:
                    print(f"\"{needle}\" found in {haystack}")
                    no_matches = False
            if no_matches is True:
                print(f"\"{needle}\" not found in {haystack}")
    except FileNotFoundError:
        return


# this if statement basically tells Python to do this first if we're
# running it from the command line
if __name__ == "__main__":
    # here, figure out if you're reading from a file or from stdin
    # based on where you're reading from, you're going to pass either
    # sys.stdin or a file to match()
    # hint: how many arguments are there?
    if len(sys.argv) == 2:
        print("Enter a word and a file to search")
    # if we have more than one argument
    elif len(sys.argv) > 2:
        i = 1
        while i+1 < len(sys.argv):
            match(sys.argv[i+1], sys.argv[i])
            i += 1
    else:
        print("No arguments given.")
