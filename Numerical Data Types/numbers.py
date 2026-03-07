#Task 1:
# Follow these steps:
#   ● Create a new Python file in this folder called numbers.py.
#   ● Ask the user to enter three different integers.
# Then print out:
#   ○ The sum of all the numbers.
#   ○ The first number minus the second number.
#   ○ The third number is multiplied by the first number.
#   ○ The sum of all three numbers divided by the third number

#ask user for 3 different integers
first_int = int(input("Please enter an integer: "))
second_int = int(input("Please enter a different integer: "))
third_int = int(input("Please enter a different integer: "))

#print sum of all ints user gave
sum = str(first_int + second_int + third_int)
print("Total sum = " + sum)

#print the first integer minus the second integer
minus = str(first_int - second_int)
print("First integer minus the second integer: " + minus)

#print the third integer multiplied by the first integer
product = str(third_int * first_int)
print("Third integer multiplied by the first integer: " + product)

#print the sum of all three integers divided by the third integer
quotient = (first_int + second_int + third_int) / third_int
print("The total sum divided by the third integer: " + str(quotient))
