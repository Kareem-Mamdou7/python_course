score = int(input("Enter your score: "))

if score <= 50 and score >= 0:
  print("Oh, better luck next time!")

elif score <= 150:
  print("Congratulations! You got a Wooden Rabbit")

elif score <= 180:
  print("Congratulations! You got a Wafer-thin mint")

elif score <= 200:
  print("Congratulations! You got a penguin")

else: 
  print("Invalid Score")
