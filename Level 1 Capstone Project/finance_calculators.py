import math

# Output instructions for user
print('''investment - to calculate the amount of interest
you'll earn on your investment
bond       - to calculate the amount you'll have to pay
on a home loan\n''')

user_decision = input('''Enter either \"investment\" or \"bond\" from
the menu above to proceed: ''')

# Changes user input to improve readability
user_answer = user_decision.lower()

# Chooses calculation based on which answer user gave
if user_answer == "investment":
    print("\nYou chose " + user_answer + ".")

    #Collecting information from user
    money_amount = float(input('''Please enter the amount of money that
you are depositing (no dollar sign is needed): '''))
    interest_rate = float(input('''Please enter the interest rate
percentage (no percent sign is needed): '''))
    years = int(input('''Please enter the number of years you plan on
investing: '''))
    interest = input('''Do you want simple or compound interest? ''')
    interest = interest.lower()

    # Calculating based on user's info and answer
    if interest == "simple":
        simple = money_amount * (1 + (interest_rate/100) * years)
        simple_interest = str(round(simple, 2))
        print("Calculating your simple interest, it will be $" +
              simple_interest)
    elif interest == "compound":
        compound = money_amount * math.pow((1 + (interest_rate/100)), years)
        compound_interest = str(round(compound, 2))
        print("Calculating your compound interest, it will be $" +
              compound_interest)
    else: print('''We are unable to read your request.
Please try again.''')

elif user_answer == "bond":
    print("\nYou chose " + user_answer + ".")

    # Collecting information from user
    house_value = float(input('''Please enter the present value of
your house: '''))
    bond_interest = float(input("Please enter the interest rate: "))
    months = int(input('''Please enter the number of months you plan
to repay the bond: '''))

    # Calculating based on users info
    bond_interest = (bond_interest/100)/12
    repayment = ((bond_interest) * house_value)/(1 -
                (1 + (bond_interest))**(-months))
    monthly_repayment = str(round(repayment, 2))
    print("Your monthly repayment will be $" + monthly_repayment)

else:
    print('''\nWe are unable to read your request.
Please try again.''')
