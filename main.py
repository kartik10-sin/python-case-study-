import random

n = random.randint(1, 100)

print("Number Guessing Game")
print("Number chosen by computer between 1 to 100")

while True:
    guess = int(input("Enter your guess: "))

    if guess == n:
        print("Correct guess")
        break
    elif guess < n:
        print("Too low")
    else:
        print("Too high")

