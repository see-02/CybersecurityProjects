#Task 2:
# Follow these steps:
#     ● Create a new Python file in this folder called shopping.py.
#     ● Once this is done, ask the user to enter the names of three products
#     ● Now ask for the price of each product. Each product must have two
#     decimal values.
#     ● Calculate the total sum of all three products.
#     ● Calculate the average price of the three products. (Hint: look up the round()
#     function)
#     ● Then print out the following sentence after performing your calculations:
#     “The Total of [product1], [product2], [product3] is Rxx,xx and the average price of
#     the items is Rxx,xx.”
#*****************************************************************************************

#ask user for three products
product_1 = input("Please enter the name of a product: ")
product_2 = input("Please enter the name of another product: ")
product_3 = input("Please enter the name of another product: ")

#ask the price for each product
price_1 = input(f'''What is the price for {product_1}?
    Please make sure to include two decimal places: ''')
price_2 = input(f'''What is the price for {product_2}?
    Please make sure to include two decimal places: ''')
price_3 = input(f'''What is the price for {product_3}?
    Please make sure to include two decimal places: ''')

#calculate sum of all product prices
sum = float(price_1) + float(price_2) + float(price_3)

#calculate average of all product prices
average = sum / 3
avg_price = round(average,2)

sentence = f'''The total of {product_1}, {product_2}, and {product_3} is ${str(sum)}
and the average price of the items is ${str(avg_price)}'''

print(sentence)
