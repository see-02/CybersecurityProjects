import os


# ===Functions========
def solve(num1, operator, num2):
    if operator == '+':
        answer = num1 + num2
        return answer
    elif operator == '-':
        answer = num1 - num2
        return answer
    elif operator == '/':
        try:
            answer = num1/num2
            return answer
        except ZeroDivisionError:
            print("Can't divide by zero!\n")
    elif operator == '*':
        answer = num1 * num2
        return answer


def add_to_equations(equation):
    equation_list.append(equation)
    with open("equations.txt", "w") as file:
        file.write("\n".join(equation_list))


# Create equations.txt if it doesn't exist
if not os.path.exists("equations.txt"):
    with open("equations.txt", "w") as default_file:
        pass

# Make sure the input is in the correct form
correct_form = False
equation_list = []

while correct_form is False:
    num1 = input('''Welcome to the calculator!
You will enter a number, an operation, then another number.\n
Operations can be:
\tmultiplication (*)
\tdivision (/)
\taddition (+)
\tsubtraction (-)\n
Type "e" for your first number to see all past equations.
Enter the first number in your equation: ''')

    if num1 == "e":
        f = open("equations.txt", "r")
        print(f.read())

    else:
        operator = input('''Please enter the operator (eg. "+" or "/): ''')
        num2 = input('''Enter the second number in your equation: ''')

        if (operator == "+" or operator == "-" or
                operator == "/" or operator == "*"):
            try:
                number1 = int(num1)
            except ValueError:
                print('''\n//////////////////
First number is not recognized.
Please try again.\n//////////////////\n''')
                continue
            if isinstance(number1, int) is True:
                try:
                    number2 = int(num2)
                except ValueError:
                    print('''\n//////////////////
Second number is not recognized.
Please try again.\n//////////////////\n''')
                    continue
                if isinstance(number2, int) is True:
                    answer = solve(number1, operator, number2)
                    equation = (f'{number1} {operator} {number2} = {answer}')
                    print(equation + "\n")
                    add_to_equations(equation)
        else:
            print('''\n//////////////////
Operator is not recognized.
Please try again.\n//////////////////\n''')
