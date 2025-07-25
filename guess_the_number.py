import random

def guess_the_number():
    """
    A simple number guessing game where the player tries to guess
    a randomly generated number between 1 and 100.
    """
    print("🎮 Welcome to the Number Guessing Game! 🎮")
    print("=" * 40)
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    print()
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        try:
            # Get player's guess
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            # Check if the guess is correct
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                print(f"The number was {secret_number}")
                return True
            elif guess < secret_number:
                print("📈 Too low! Try a higher number.")
            else:
                print("📉 Too high! Try a lower number.")
                
            # Show remaining attempts
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"You have {remaining} attempts left.")
            print()
            
        except ValueError:
            print("❌ Please enter a valid number!")
            print()
    
    # Game over - ran out of attempts
    print(f"💀 Game Over! You've used all {max_attempts} attempts.")
    print(f"The number was {secret_number}")
    return False

def play_again():
    """Ask the player if they want to play again."""
    while True:
        choice = input("Would you like to play again? (y/n): ").lower().strip()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def main():
    """Main game loop."""
    games_played = 0
    games_won = 0
    
    while True:
        # Play a game
        won = guess_the_number()
        games_played += 1
        
        if won:
            games_won += 1
        
        # Show statistics
        print("\n" + "=" * 40)
        print("📊 GAME STATISTICS")
        print(f"Games played: {games_played}")
        print(f"Games won: {games_won}")
        if games_played > 0:
            win_rate = (games_won / games_played) * 100
            print(f"Win rate: {win_rate:.1f}%")
        print("=" * 40)
        
        # Ask if player wants to continue
        if not play_again():
            break
    
    print("\nThanks for playing! 👋")

if __name__ == "__main__":
    main()
