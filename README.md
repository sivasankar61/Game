# 🐍 Snake Water Gun Game (Python)

A simple command-line game built using Python where the user plays **Snake-Water-Gun** against the computer.

This project is a beginner-friendly mini game to practice:
- Python basics
- Conditional statements
- Dictionaries
- Random module
- Input validation

---

## 🎮 Game Rules

- 🐍 Snake drinks 💧 Water → Snake wins
- 💧 Water drowns 🔫 Gun → Water wins
- 🔫 Gun kills 🐍 Snake → Gun wins
- Same choice → Draw

---

## 🧠 How It Works

- The computer randomly selects one option using `random.choice()`
- The user enters:
  - `s` → Snake
  - `w` → Water
  - `g` → Gun
- The program compares both choices and declares the winner.

---

## 📂 Project Structure

```
snake-water-gun/
│
├── game.py
└── README.md
```

## 🖥️ Example Output

```
Enter your choice (s for snake, w for water, g for gun): s
You chose Snake
Computer chose Water
You Win!
```

---

## 📜 Source Code

```python
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
```

---

## 🚀 Features

- Random computer choice
- User input validation
- Clean and simple logic
- Beginner-friendly structure

---

## 👨‍💻 Author

Siva Sankar

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
