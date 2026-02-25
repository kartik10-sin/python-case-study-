import random

# -----------------------
# Number Guessing Game
# -----------------------

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


# -----------------------
# Word Scrambler Game
# -----------------------

words = ["python", "jupyter", "colab", "programming", "scramble", "developer"]

selected_word = random.choice(words)
word_list = list(selected_word)

random.shuffle(word_list)
scrambled = ''.join(word_list)

print("\nWelcome to the Word Scrambler Game!")
print(f"Unscramble the word: {scrambled}")

while True:
    guess = input("Your guess: ").lower()

    if guess == selected_word:
        print(f"Congratulations! You unscrambled the word '{selected_word}'.")
        break
    else:
        print("Incorrect. Try again!")
