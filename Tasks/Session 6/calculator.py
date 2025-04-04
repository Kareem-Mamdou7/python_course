def add(firstNum, secondNum):
    return firstNum + secondNum


def subtract(firstNum, secondNum):
    return firstNum - secondNum


def multiply(firstNum, secondNum):
    return firstNum * secondNum


def divide(firstNum, secondNum):
    return firstNum / secondNum


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    firstNum = float(input("Enter the First Number to operate on\n"))

    shouldContinue = True

    while shouldContinue:
        secondNum = float(input("Enter the Second Number to operate on\n"))

        for operation in operations:
            print(operation)

        operation = input("Enter desired Operation\n")

        calculationFun = operations[operation]
        result = calculationFun(firstNum, secondNum)

        print(f"{firstNum} {operation} {secondNum} = {result}")

        choice = input(f"Continue Calculating using {result}? (y/n)\n")

        if choice == "y":
            firstNum = result

        else:
            shouldContinue = False
            print("*" * 50)
            calculator()


calculator()
