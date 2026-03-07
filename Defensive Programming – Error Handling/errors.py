# This example program is meant to demonstrate errors.
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.
#  print "Welcome to the error program"
#      print "\n"
#
#   Variables declaring the user's age, casting the str to an int, and printing the result
#      age_Str == "24 years old" 
#      age = int(age_Str) 
#      print("I'm" + age + "years old.")
#
#   Variables declaring additional years and printing the total years of age
#      years_from_now = "3"
#      total_years = age + years_from_now
#
#  print "The total number of years:" + "answer_years"
#
# Variable to calculate the total amount of months from the total amount of years and printing the result
#  total_months = total * 12
#  print "In 3 years and 6 months, I'll be " + total_months + " months old"
#
#HINT, 330 months is the correct answer
#*******************************************************************************************************************

# This line below was highlighted before I even ran the program,
# so it's a syntax error
print ("Welcome to the error program") # Added parentheses around string

# This line below was highlighted before I even ran the program, 
# so it's a syntax error
print ("\n") # Fixed unexpected indent and added parentheses around
# string

# Variables declaring the user's age, casting the str to an int, 
# and printing the result

# Lines below was highlighted before I even ran the program, 
# so they were syntax errors

# Fixed unexpected indents on next few lines
# Commented out: age_Str = "24 years old"
    # Changed == to = so it would assign the string to age_Str
# Commented out: age = int(age_Str)
    # age = int(age_Str) caused runtime error because we tried to convert
    # string "24 years old" with non-integer characters to an integer
    # Also caused logical error since "years old" was already in
    # the string printed below
# Replaced commented out lines above with the line below
age = "24"
# Added spaces to make string below readable- logical error
print("I'm " + age + " years old.")

# Lines below was highlighted before I even ran the program, 
# so they were syntax errors

# Fixed unexpected indents on next few lines
years_from_now = 3 # Took away quotations so it would be an int
# -logical error

# Added line below to correctly calculate total years because
# we can't add a string and an int - runtime error
age = int(age)
total_years = age + years_from_now

# Line below was highlighted before I even ran the program,
# so it's a syntax error
# Added parentheses around string below
# Added spaces to make string below readable- logical error
# Took away quotations from answer_years to make string
# correct and readable - logical error
# Added line below because answer_years was not assigned
# -logical error
answer_years = str(total_years)
print ("The total number of years: " + answer_years)

# Variable to calculate the total amount of months from the 
# total amount of years and printing the result

# Lines below was highlighted before I even ran the program, 
# so they were syntax errors
# Variable "total" below wasn't defined, so changed to "total_years" 
# to be accurate
# Converted total_months into string so it can be printed in
# next line correctly -runtime error
# Added 6 to total_months to account for the extra 6 months
# we want in our answer (to get the correct 330 months)
total_months = str((total_years * 12) + 6)
# Added parentheses around strings below
print ("In 3 years and 6 months, I'll be " + total_months + " months old")

#HINT, 330 months is the correct answer
