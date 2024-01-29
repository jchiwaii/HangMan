import random
from word_list import word_list
from art import logo, stages

def get_word(difficulty):
    if difficulty == 'easy':
        return random.choice([(k, random.choice(v)) for k, v in word_list.items() if len(random.choice(v)) == 5])
    elif difficulty == 'medium':
        return random.choice([(k, random.choice(v)) for k, v in word_list.items() if len(random.choice(v)) > 5])
    else:
        return random.choice([(k, random.choice(v)) for k, v in word_list.items() if len(random.choice(v)) > 7])

def play_game(difficulty):
    category, chosen_word = get_word(difficulty)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6
    missed_guesses = 0
    hint_given = False

    print(logo)

    display = ["_" for _ in range(word_length)]
    guessed_letters = []

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        if guess in display:
            print(f"You've already guessed {guess}")

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                guessed_letters.append(guess)

        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            missed_guesses += 1
            if lives == 0:
                end_of_game = True
                print("You lose.")

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win.")

        print(stages[lives])

        if difficulty == 'easy' and "_" in display and lives > 0 and not hint_given:
            print(f"Hint: The word relates to '{category}'")
            print(f"Hint: The word starts with '{chosen_word[0]}'")
            print(f"Hint: The word ends with '{chosen_word[-1]}'")
            hint_given = True

        if difficulty == 'medium' and "_" in display and lives > 0 and missed_guesses == 1 and not hint_given:
            print(f"Hint: The word relates to '{category}'")
            print(f"Hint: The word starts with '{chosen_word[0]}'")
            hint_given = True

    print(f"The correct word was: {chosen_word}")
    return "_" not in display

def main():
    difficulty = input("Choose a difficulty. Type 'easy', 'medium', or 'hard': ")
    while True:
        won = play_game(difficulty)
        if won:
            print("Congratulations! You won!")
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != 'yes':
                break
            difficulty = input("Choose a difficulty. Type 'easy', 'medium', or 'hard': ")
        else:
            print("Better luck next time!")
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != 'yes':
                break

main()
