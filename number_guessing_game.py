import random
def play_game():
    # Asking difficulty level from user and set game parameters accordingly
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()

    # Set game parameters based on chosen difficulty
    if difficulty == "easy":
        max_range, max_attempts = 10, 7 # Easy: smaller range, more attempts
    elif difficulty == "medium":
        max_range, max_attempts = 15, 5 # Medium: medium range, medium attempts
    else :
        max_range, max_attempts = 20, 3 # Hard: larger range , fewer attempts

    # Generating random target number for the player to guess
    target = random.randint(1, max_range) # here in randint function range both endpoints are inclusive
    guesses = []
    
    # Displays game information to player at initial
    print(f"\nGuess a number between 1 and {max_range} , Here your have total {max_attempts} attempts")

    # loop continues until the max_attemps are left
    while max_attempts > 0 :
        try:
            # Storing user input to guess as integer
            guess = int(input("Your Guess: "))
        except ValueError:
            # Handles Non-numeric input values
            print("Please enter a valid number!")
            continue # TO skip the next iteration , becuase of need to enter integer to complete one attempt

        # storing guesses to display what we guess and dicrement attempts for each iteration
        guesses.append(guess)
        max_attempts -= 1
  
        # check player guess correctly or not and giving a hint if they were far apart from guessing number
        if guess == target:
            print(f"Correct! You guessed it in {len(guesses)} attempts.")
            break # exit if player wins
        elif guess > target:
            print("Too high!")
        else:
            print("Too low!")
    else:
        # this executes only after while loop ends normally
        # Prints what the target number and player guesses
        print(f"Game over! The number was {target}. Your guesses:{guesses}")

    # Return game results as dictionary
    return {target : guesses}

def display_game_history(game_history):
    # Diplay a formatted history of all games played
    """
    # Currently commented out because in our current
    # game flow, game_history can never be empty (player must play at least once.)
    # keep this for future feature where empty history might be possible.
    if not game_history:
        print("No game history available.")
        return
    """

    lines = [] # to store formatted lines for each game
    max_length = 0

    for target, guesses in game_history.items():
        line = f"Target: {target:02d} | Guesses: {guesses}"
        lines.append(line)
        current_length = len(line)
        # update maximum length for formmatting
        if current_length > max_length:
            max_length = current_length

    # Ensure minimum width of 30 for the header
    header_width = max(max_length, 30)
    header = " GAME HISTORY GVN ".center(header_width, '=')

    print('\n' + header)
    for line in lines:
        print(line) # Displays all games history line by line
    print("=" * header_width)  
    print('\nThanks for playing!')
    end_line = " GUVVALA VENKATA NARAYANA ".center(header_width, '*')
    print('\n' + end_line) # Displays signature line


# def func to ask to play agin 

def main():
    game_history = {}
    while True: # loop runs until you want to quit game 
        result = play_game()
        game_history.update(result)


        while True: # loop runs  until enter yes or no
            replay = input("Play agin? (yes/no): ").lower()
            if replay in ('yes', 'no'):
                break
            print("Please enter either 'yes' or 'no' ")


        if replay == 'no':
            display_game_history(game_history)
            break
    
if __name__ == "__main__":
    main()
    
