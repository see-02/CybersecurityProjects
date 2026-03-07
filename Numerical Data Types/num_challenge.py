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
