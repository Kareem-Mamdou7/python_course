pizzaSize = input("Enter the size of the pizza (S/M/L): ")
price = 0

match pizzaSize:
    case "S":
        price = 15

    case "M":
        price = 20

    case "L":
        price = 25

    case default:
        print("Invalid pizza size")


choice = input("Add Pepperoni? Y/N: ")
if choice == "Y" and pizzaSize == "S":
    price += 2

elif choice == "Y" and (pizzaSize == "M" or pizzaSize == "L"):
    price += 3

choice = input("Add Extra Cheese? Y/N: ")
if choice == "Y":
    price += 1

print(f"Your final bill is: ${price}")
