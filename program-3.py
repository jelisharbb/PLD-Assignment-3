print("\nWelcome to apple store!")

def user_change (money, apple):
    if money >= apple:
        change = money % apple
        apple_max = money // apple
        print(f"\nYou can buy {apple_max:.0f} apple/s and your change is {change:,.2f} PHP. \nThank you! \n")

    else:
        money_short = apple - money
        print (f"\nSorry, you do not have enough money to buy an apple. You need {money_short:.2f} PHP more.")

money = float(input("\nHow much money do you have? "))
apple = int(input("How much does one apple cost? "))

user_change (money, apple)