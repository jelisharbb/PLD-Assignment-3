print("\nWelcome to Fruit Market! \nHere is the pricelist: \nApple = 20 \nOrange = 25")

def apple_quantity():
    apple = int(input("\nHow many apples do you want to buy? "))
    return apple

def orange_quantity():
    orange = int(input("How many oranges do you want to buy? "))
    return orange

def apple_price_per_piece():
    apple_price = 20
    return apple_price

def orange_price_per_piece():
    orange_price = 25
    return orange_price

def total_price():
    apple = (apple_quantity() * apple_price_per_piece())
    orange = (orange_quantity() * orange_price_per_piece())
    overall_price = (apple + orange)
    receipt(overall_price)

def receipt(overall_price):
    print(f"\nThe total amount is {overall_price:,.2f} PHP.\n")

total_price()