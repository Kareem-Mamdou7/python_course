def format_name(firstName, lastName):
    if firstName == "" or lastName == 0:
        print("You didn't provide a valid input")

    else:
        print(f"Result: {firstName.title()} {lastName.title()}")


firstName = input("Enter your First Name: ")
lastName = input("Enter your last Name: ")

format_name(firstName, lastName)
