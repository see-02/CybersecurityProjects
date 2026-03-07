#Challenge:
# Use this opportunity to extend yourself by completing an optional challenge
# activity.
# Follow these steps:
#   ● Create a new file called challenge.py.
#   ● Write Python code to take the name of a user's favourite restaurant and
#   store it in a variable called string_fav.
#   ● Below this, write a statement to take in the user's favourite number. Use
#   casting to store it in an integer variable called int_fav.
#   ● Print out both of these using two separate print statements below what
#   you have written. Be careful!
#   ● Once this is working, try to cast string_fav to an integer. What happens?
#   Add a comment in your code to explain why this is.


#ask user's favorite restaurant and store it
string_fav = input("What is the name of your favorite restaurant? ")

#ask user's favorite number and store it
int_fav = input("What is your favorite number? ")

#print restaurant and number on different lines
print(string_fav)
print(int_fav)

#cast restaurant variable to int
print(int(string_fav))

#doesn't work- this gives a valueError because there
#isn't valid characters that can be integers
