# Write a program that displays a logical error
# (be as creative as possible!)

item = input("What item do you need from the store? ")
price = input("How much does the " + item + ''' cost?
Exclude the dollar sign: ''')
money = input("How much cash do you have? Exclude the dollar sign: ")

# Calculate money left over after buying item
money_left = float(money) -  float(price)

# Supposed to print out the money left after buying item,
# but it prints out the money the user has total instead
# It runs and has no runtime or syntax errors, but since
# it doesn't print out the expected result, it's a logical
# error
print ("You need $" + price + " to buy the " + item 
+ ", so you'll have $" + money + " left after buying it.")
