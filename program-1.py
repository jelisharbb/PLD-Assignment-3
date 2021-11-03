# define first the three functions

def user_name():
    name = input("What is your name? ")
    return name

def user_age():
    age = input("How old are you? ")
    return age

def user_address():
    address = input("Where do you live? ")
    return address

def complete_details():
    userName = user_name()
    userAge = user_age()
    userAddress = user_address()
    completeDetails (userName, userAge, userAddress)

def completeDetails(username_, userage_, useraddress_):
    print(f"Hi, my name is {username_}. I am {userage_} years old. I live in {useraddress_}.")


complete_details() 
