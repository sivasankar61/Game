
import random

computer = random.choice([-1, 0, 1])

youstr = input("Enter your choice (s for snake, w for water, g for gun): ")

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

if youstr not in youDict:
    print("Invalid input! Please choose s, w, or g.")
    exit()

you = youDict[youstr]

print(f"You chose {reverseDict[you]}")
print(f"Computer chose {reverseDict[computer]}")

result = you - computer

if result == 0:
    print("It's a Draw!")
elif result == 1 or result == -2:
    print("You Win!")
else:
    print("You Lose!")
