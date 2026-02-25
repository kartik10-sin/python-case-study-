import random

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
