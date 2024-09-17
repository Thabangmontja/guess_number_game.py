import random

def guess_number_game():
    print("I'm thinking of a number between 1 and 10. Can you guess it?")
    
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    guess = None
    attempts = 0  # Counter for the number of guesses
    
    while guess != secret_number:
        try:
            # Get user's guess and increment the attempt counter
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Use match case to handle the guess comparison
            match guess:
                case _ if guess == secret_number:
                    print(f"Congratulations, you guessed it in {attempts} attempts!")
                case _ if guess > secret_number:
                    print("Oops, your guess is a bit high. Try again!")
                case _ if guess < secret_number:
                    print("Nope, your guess is a bit low. Give it another shot!")
        except ValueError:
            print("Please enter a valid number!")
    
    # Offer to play again
    play_again = input("Play again? (yes/no): ").lower()
    if play_again == 'yes':
        guess_number_game()  # Restart the game if the user wants to play again
    else:
        print("Thanks for playing!")

# Run the game for the first time
guess_number_game()
