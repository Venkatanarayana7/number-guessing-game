import random

def play_game():
    # Asking difficulty level from user and set game parameters accordingly
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()

    # Set game parameters based on chosen difficulty
    if difficulty == "easy":
        max_range, max_attempts = 10, 7  # Easy: smaller range, more attempts
    elif difficulty == "medium":
        max_range, max_attempts = 15, 5  # Medium: medium range, medium attempts
    else:
        max_range, max_attempts = 20, 3  # Hard: larger range, fewer attempts

    # Generating random target number for the player to guess
    target = random.randint(1, max_range)
    attempts = 0
    
    # Displays game information to player at initial
    print(f"\nGuess a number between 1 and {max_range}, You have {max_attempts} attempts")

    # Game loop
    while attempts < max_attempts:
        try:
            # Storing user input to guess as integer
            guess = int(input("Your Guess: "))
        except ValueError:
            # Handles Non-numeric input values
            print("Please enter a valid number!")
            continue

        attempts += 1
  
        # Check player guess correctly or not
        if guess == target:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break
        elif guess > target:
            print("Too high!")
        else:
            print("Too low!")
    else:
        # This executes only if while loop ends normally (player loses)
        print(f"Game over! The number was {target}.")

def main():
    while True:  # Loop runs until player wants to quit
        play_game()
        
        while True:  # Loop runs until enter yes or no
            replay = input("Play again? (yes/no): ").lower()
            if replay in ('yes', 'no'):
                break
            print("Please enter either 'yes' or 'no'")

        if replay == 'no':
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()
