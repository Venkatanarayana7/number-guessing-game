import random

def play_game():
    # Asking difficulty level from user and set game parameters accordingly
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()

    # Set game parameters based on chosen difficulty
    if difficulty == "easy":
        max_range, max_attempts = 10, 7  # Easy: smaller range, more attempts
    elif difficulty == "medium":
        max_range, max_attempts = 15, 5  # Medium: medium range, medium attempts
    elif difficulty == "hard":
        max_range, max_attempts = 20, 3  # Hard: larger range, fewer attempts
    else:
        print()
    # Generating random target number for the player to guess
    target = random.randint(1, max_range)  # here in randint function range both endpoints are inclusive
    guesses = []
    initial_attempts = max_attempts  # Store initial attempts for display
    
    # Displays game information to player at initial
    print(f"\nGuess a number between 1 and {max_range}, You have total {max_attempts} attempts")

    # loop continues until the max_attempts are left
    while max_attempts > 0:
        remaining_attempts = max_attempts
        total_attempts = initial_attempts
        try:
            guess = int(input(f"Attempt {total_attempts - remaining_attempts + 1}/{total_attempts} - Your Guess: "))
        except ValueError:
            # Handles Non-numeric input values
            print("Please enter a valid number!")
            continue  # TO skip the next iteration, because we need integer to complete one attempt

        # storing guesses to display what we guess and decrement attempts for each iteration
        guesses.append(guess)
        max_attempts -= 1
  
        # check player guess correctly or not and giving a hint if they were far apart from guessing number
        if guess == target:
            print(f"Correct! You guessed it in {len(guesses)} attempts.")
            break  # exit if player wins
        elif guess > target:
            print("Too high!")
        else:
            print("Too low!")
    else:
        # this executes only after while loop ends normally
        # Prints what the target number and player guesses
        print(f"Game over! The number was {target}. Your guesses: {guesses}")

    # Return game results as dictionary
    return {target: guesses}

def display_game_history(game_history):
    # Display a formatted history of all games played
    """
    # Currently commented out because in our current
    # game flow, game_history can never be empty (player must play at least once.)
    # keep this for future feature where empty history might be possible.
    if not game_history:
        print("No game history available.")
        return
    """

    lines = []  # to store formatted lines for each game
    max_length = 0

    for target, guesses in game_history.items():
        line = f"Target: {target:02d} | Guesses: {guesses}"
        lines.append(line)
        current_length = len(line)
        # update maximum length for formatting
        if current_length > max_length:
            max_length = current_length

    # Ensure minimum width of 30 for the header
    header_width = max(max_length, 30)
    header = " GAME HISTORY GVN ".center(header_width, '=')

    print('\n' + header)
    for line in lines:
        print(line)  # Displays all games history line by line
    print("=" * header_width)  
    print('\nThanks for playing!')
    end_line = " GUVVALA VENKATA NARAYANA ".center(header_width, '*')
    print('\n' + end_line)  # Displays signature line

def get_user_choice():
    while True:
        print("\n" + "="*40)
        print("What would you like to do?")
        print("1. Play another game")
        print("2. View current game history")
        print("3. Quit and see final results")
        print("="*40)
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice in ('1', '2', '3'):
            return choice
        else:
            print("Please enter 1, 2, or 3")

def main():
    game_history = {}
    
    while True:  # main game loop
        # Play a game
        result = play_game()
        game_history.update(result)
        
        while True:
            choice = get_user_choice()
            
            if choice == '1':  # Play another game
                break  # Break inner loop to play again
            elif choice == '2':  # View current history
                print("\n" + "="*50)
                print("CURRENT GAME HISTORY")
                print("="*50)
                display_game_history(game_history)
                # Stay in menu after viewing history
            elif choice == '3':  # Quit
                print("\n" + "="*50)
                print("FINAL GAME RESULTS")
                print("="*50)
                display_game_history(game_history)
                return  # Exit main function completely

if __name__ == "__main__":
    main()

