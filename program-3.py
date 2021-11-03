print("\nWelcome to apple store!")

def user_change (money, apple):
    if money >= apple:
        change = money % apple
        apple_max = money // apple
        print(f"You can buy {apple_max} apple/s and your change is {change:,.2f}")

    else:
        money_short = apple - money
        print (f"Sorry, you do not have enough money to buy an apple. You need {money_short:.2f} PHP more.")

