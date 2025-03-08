weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height**2)

if bmi < 18.5:
    print("Underweight")

elif bmi < 25:
    print("Normal")

elif bmi < 30:
    print("Overweight")
