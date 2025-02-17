again = "y"

while again == "y":
    firstVar = int(input("x = "))
    secondVar = int(input("y = "))

    operation = input("Enter the operation ( * / + - ): ")
    result = 0
    success = True

    match operation:
        case "*":
            result = firstVar * secondVar
        case "/":
            choice = input("With decimal point? (y/n): ")
            match choice:
                case "y":
                    result = firstVar / secondVar
                case "n":
                    result = firstVar // secondVar
        case "+":
            result = firstVar + secondVar
        case "-":
            result = firstVar - secondVar
        case _:
            print("Invalid operation")
            success = False
    if success:
        print(result)

    print()
    again = input("Try again? (y/n)")
