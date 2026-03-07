# This example program is meant to demonstrate errors.
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.
#  animal = Lion
#  animal_type = "cub"
#  number_of_teeth = 16
#
#  full_spec = "This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth"
#
#  print full_spec
#*********************************************************************************************************************

# Added quotations to correctly assign the string to variable animal
# - syntax error
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

# Switched the places of number_of_teeth and animal_type to
# correctly display the string - logical error
# We don't want to literally print the names of the variables,
# so we need to add the f at the beginning of the variable to
# correctly print the data assigned to each variable - logical error
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"

# Added parentheses around full_spec to correctly print out full_spec
# -syntax error
print (full_spec)
