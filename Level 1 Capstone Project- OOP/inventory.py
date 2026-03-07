from tabulate import tabulate


# ========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return ("Country: " + self.country + " Code: " + self.code +
                " Product: " + self.product + " Cost: $" + str(self.cost)
                + " Quantity: " + str(self.quantity))


# =============Shoe list===========
"""
The list will be used to store a list of objects of shoes.
"""
shoe_list = []


# ==========Functions outside the class==============
def read_shoes_data():
    """
    This function will open the file inventory.txt and read the data
    from this file, then create a shoes object with this data and
    append this object into the shoes list. One line in this file
    represents data to create one object of shoes. You must use the
    try-except in this function for error handling. Remember to skip
    the first line using your code.
    """
    try:
        with open('inventory.txt', 'r') as file:
            shoe_data = file.read()[35:].split("\n")

        for s_str in shoe_data:
            shoe_attr = s_str.split(",")
            shoe_attr_country = shoe_attr[0]
            shoe_attr_code = shoe_attr[1]
            shoe_attr_product = shoe_attr[2]
            shoe_attr_cost = shoe_attr[3]
            shoe_attr_quantity = shoe_attr[4]
            curr_shoe = Shoe(shoe_attr_country, shoe_attr_code,
                             shoe_attr_product, shoe_attr_cost,
                             shoe_attr_quantity)
            shoe_list.append(curr_shoe)
    except FileNotFoundError:
        print("The file you are looking for does not exist.")


def capture_shoes(country, code, product, cost, quantity):
    """
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    """
    # Searching for any matching codes in existing shoe_list
    in_list = 0
    for s in shoe_list:
        if s.code == code:
            in_list = 1
            break
        elif s.code != code:
            pass
    if in_list == 1:
        print('''=====================
This shoe is already in inventory.
=====================''')
    else:
        # Adding new shoe to shoe_list and file
        try:
            with open('inventory.txt', 'a') as file:
                file.write(f"\n{country},{code},{product},{cost},{quantity}")
            print(f"Successfully added {product}s to the inventory!")
            curr_shoe = Shoe(country, code, product, cost, quantity)
            shoe_list.append(curr_shoe)
        except FileNotFoundError:
            print("The file you are looking for does not exist.")


def view_all():
    """
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organize your data in a table format
    by using Python’s tabulate module.
    """
    try:
        with open('inventory.txt', 'r') as file:
            shoe_data = file.read()[35:].split("\n")
        with open('inventory.txt', 'r') as file:
            headers = file.read()[0:34].split(",")
        shoes = []
        for str in shoe_data:
            shoe_attr = str.split(",")
            shoes.append(shoe_attr)
        print(tabulate(shoes, headers=headers))
    except FileNotFoundError:
        print("The file you are looking for does not exist.")


def re_stock():
    """
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    """
    shoe = 0
    shoe_ids = []
    # Finds first least quantity in the shoe_list
    least_quantity = min(shoe_list, key=lambda s: s.quantity)
    # Checks for multiple least quantities
    for s in shoe_list:
        if s.quantity == least_quantity.quantity:
            shoe_ids.append(shoe)
        shoe += 1
    # Case where there is only one shoe with the least quantity
    if len(shoe_ids) == 1:
        shoe_id = shoe_ids[0]
        print("The shoes with the lowest stock is: " +
              str(shoe_list[shoe_id].product) + " with a quantity of " +
              str(least_quantity.quantity) + "\n")
        done = False
        while done is False:
            add_to_stock = input('Would you like to add to this stock? '
                                 '(Yes or no): ')
            # User has chosen to add to lowest stock
            if add_to_stock.lower() == "yes":
                quantity = input("How many " + str(shoe_list[shoe_id].product)
                                 + "s are you adding? ")
                try:
                    quantity = int(quantity)
                    new_quantity = least_quantity.quantity + quantity
                    shoe_list[shoe_id].quantity = new_quantity
                    new_shoe_list = []
                    # Rewrites file with updated quantity for shoe with
                    # least quantity
                    with open('inventory.txt', 'w') as file:
                        file.write("Country,Code,Product,Cost,Quantity\n")
                        for s in shoe_list:
                            shoe_attr = [s.country, s.code, s.product,
                                         str(s.cost), str(s.quantity)]
                            new_shoe_list.append(",".join(shoe_attr))
                        file.write("\n".join(new_shoe_list))
                    print("Quantity updated.\n")
                    done = True
                except ValueError:
                    print('You have not entered a valid number. '
                          'Please try again.\n')
            # User has chosen not to add to lowest stock
            elif add_to_stock.lower() == "no":
                print("Back to menu:\n")
                done = True
            else:
                print('You have not entered a valid answer. '
                      'Please try again.\n')
    # Case where there is more than one shoe with the least quantity
    elif len(shoe_ids) > 1:
        print("There are multiple shoes with the least quantity:\n")
        j = 0
        # Prints numbered list of shoes with lowest quantities
        for s in shoe_ids:
            shoe_id = shoe_ids[j]
            print(str(j+1) + ". " + str(shoe_list[shoe_id]))
            j += 1
        done = False
        while done is False:
            add_to_stock = input('Would you like to add to any of these '
                                 'stocks? (Yes or no): ')
            # User has chosen to add to a stock
            if add_to_stock.lower() == "yes":
                still_adding = True
                while still_adding is True:
                    # User is choosing to add stock to shoe with
                    # associated number as shown in list
                    which_shoe = input('Please enter the number '
                                       'associated with the shoe you '
                                       'would like to add to: ')
                    try:
                        which_shoe = int(which_shoe)
                        try:
                            shoe_id = shoe_ids[which_shoe-1]
                            # User tells how many shoes they're adding
                            # to the stock
                            quantity = input("How many " +
                                             str(shoe_list[shoe_id].product)
                                             + "s are you adding? ")
                            try:
                                quantity = int(quantity)
                                new_quantity = int(
                                    least_quantity.quantity) + quantity
                                # Quantity is updated in shoe_list
                                shoe_list[shoe_id].quantity = new_quantity
                                new_shoe_list = []
                                # Quantity is updated in text file
                                with open('inventory.txt', 'w') as file:
                                    file.write('Country,Code,Product,Cost,'
                                               'Quantity\n')
                                    for s in shoe_list:
                                        shoe_attr = [s.country, s.code,
                                                     s.product, str(s.cost),
                                                     str(s.quantity)]
                                        new_shoe_list.append(",".join(
                                                             shoe_attr))
                                    file.write("\n".join(new_shoe_list))
                                again = input('Quantity updated. Would you '
                                              'like to add to another shoe '
                                              'stock? (Yes or no): ')
                                # User has chosen to add to another
                                # shoe stock
                                if again.lower() == "yes":
                                    shoe_id = shoe_ids[which_shoe-1]
                                    shoe_ids.remove(shoe_id)
                                    # Case where all items in list were
                                    # updated
                                    if shoe_ids == []:
                                        print("All items were updated.")
                                        done = True
                                    # Case where there are still more
                                    # items with the least quantity
                                    else:
                                        print('Updated list of shoes with '
                                              'least quantity:')
                                        j = 0
                                        for s in shoe_ids:
                                            shoe_id = shoe_ids[j]
                                            print(str(j+1) + ". " +
                                                  str(shoe_list[shoe_id]))
                                            j += 1
                                        print("\n")
                                # User has chosen not to add to
                                # another shoe stock
                                elif again.lower() == "no":
                                    print("Back to menu:\n")
                                    still_adding = False
                                    done = True
                                else:
                                    print('You have not entered a valid '
                                          'answer. Please try again.\n')
                            except ValueError:
                                print('You have not entered a valid number. '
                                      'Please try again.\n')
                        except IndexError:
                            print("Number out of range. Please try again.\n")
                            still_adding = True
                    except ValueError:
                        print('You have not entered a valid number. Please try'
                              ' again.\n')
            # User has chosen not to add to any low stock
            elif add_to_stock.lower() == "no":
                print("Back to menu:")
                done = True
            else:
                print('You have not entered a valid answer. Please try again.'
                      '\n')


def search_shoe(code):
    """
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    """
    t = 0
    for s in shoe_list:
        if s.code == code:
            t = 1
            print("Shoe information:\n" + str(s))
        else:
            pass
    if t == 0:
        print("There is not a shoe with that code.")


def value_per_item():
    """
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    """
    shoes = []
    for s in shoe_list:
        shoe_value = []
        cost = s.cost
        quantity = float(s.quantity)
        value = cost * quantity
        shoe_value.append(s.product)
        shoe_value.append(cost)
        shoe_value.append(quantity)
        shoe_value.append(value)
        shoes.append(shoe_value)
    headers = ["Product", "Cost per item", "Quantity", "Total Value"]
    print(tabulate(shoes, headers=headers))


def highest_qty():
    """
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    """
    shoe = 0
    shoe_ids = []
    # Finds first greatest quantity in the shoe_list
    greatest_quantity = max(shoe_list, key=lambda s: s.quantity)
    # Checks for multiple greatest quantities
    for s in shoe_list:
        if s.quantity == greatest_quantity.quantity:
            shoe_ids.append(shoe)
        shoe += 1
    # Case where there is just one shoe with greatest quantity
    if len(shoe_ids) == 1:
        shoe_id = shoe_ids[0]
        print("The " + str(shoe_list[shoe_id].product) + "s are now on sale!")
    # Case where there are more than one shoe with greatest quantity
    elif len(shoe_ids) > 1:
        print("There are multiple shoes on sale!\n")
        j = 0
        for s in shoe_ids:
            shoe_id = shoe_ids[j]
            print(str(shoe_list[shoe_id].product) + "s")
            j += 1


# ==========Main Menu=============
"""
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
"""
# Reads text file to shoe_list
read_shoes_data()
menu = True
while menu is True:
    print('''\nWelcome to the inventory menu!
=============================
1. View all shoes in inventory
2. Add new shoe to inventory
3. Restock lowest stock(s)
4. Search for an existing shoe in inventory
5. Calculate total value for each shoe in stock
6. See which shoes are high in stock and on sale
7. Exit menu
=============================''')
    menu_choice = input('Please enter the number of the action you would like'
                        ' to take: ')
    # User has chosen to view all shoes in inventory
    if menu_choice == "1":
        view_all()
    # User has chosen to add new shoe to inventory
    elif menu_choice == "2":
        country = input("What is the country of the product? ")
        code = input("What is the code of the product? ")
        product = input("What is the name of the product? ")
        cost_is_int = False
        while cost_is_int is False:
            cost = input("What is the cost of the product? ")
            cost = cost.strip('$')
            try:
                is_cost_an_int = int(cost)
                cost_is_int = True
            except ValueError:
                print("Please enter the cost as an integer.")
        correct_quantity = False
        while correct_quantity is False:
            quantity = input(f'Please enter the number of {product}s that'
                             ' you are putting in inventory: ')
            try:
                is_quantity_an_int = float(quantity)
                correct_quantity = True
            except ValueError:
                print("Please enter the quantity as a float.")
        capture_shoes(country, code, product, cost, quantity)
    # User has chosen to restock lowest stocks in inventory
    elif menu_choice == "3":
        re_stock()
    # User has chosen to search for a shoe in inventory
    elif menu_choice == "4":
        shoe_code = input('Please enter the code of the shoe you are '
                          'searching for: ')
        search_shoe(shoe_code)
    # User has chosen to calculate total value for each shoe in stock
    elif menu_choice == "5":
        value_per_item()
    # User has chosen to see which items are highest in stock/on sale
    elif menu_choice == "6":
        highest_qty()
    # User has chosen to exit out of menu
    elif menu_choice == "7":
        print("Thank you. Bye!")
        menu = False
    else:
        print("Answer not recognized. Please try again.")
