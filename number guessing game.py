
import random

def number_guessing_game():
    print("=" * 40)
    print("       NUMBER GUESSING GAME")
    print("=" * 40)
    print("I have selected a number between 1 and 100.")
    print("Can you guess it?")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("\nEnter your guess (1-100): "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try a bigger number.")
            elif guess > secret_number:
                print("Too high! Try a smaller number.")
            else:
                print(f"\nCorrect! You guessed it in {attempts} attempts.")
                break

        except ValueError:
            
            print("Invalid input! Please enter a whole number.")

    print("Thanks for playing!")


if __name__ == "__main__":

    number_guessing_game()

