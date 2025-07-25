import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_player_choice():
    """Get the player's choice with input validation."""
    valid_choices = ['rock', 'paper', 'scissors', 'r', 'p', 's']
    
    while True:
        choice = input("Choose rock, paper, or scissors (or r/p/s): ").lower().strip()
        
        if choice in valid_choices:
            # Convert short forms to full names
            if choice == 'r':
                return 'rock'
            elif choice == 'p':
                return 'paper'
            elif choice == 's':
                return 'scissors'
            else:
                return choice
        else:
            print("❌ Invalid choice! Please enter rock, paper, scissors, or r/p/s")

def determine_winner(player_choice, computer_choice):
    """Determine the winner of the game."""
    if player_choice == computer_choice:
        return "tie"
    
    winning_combinations = {
        'rock': 'scissors',      # rock crushes scissors
        'paper': 'rock',         # paper covers rock
        'scissors': 'paper'      # scissors cut paper
    }
    
    if winning_combinations[player_choice] == computer_choice:
        return "player"
    else:
        return "computer"

def display_choices(player_choice, computer_choice):
    """Display the choices made by both players."""
    choice_emojis = {
        'rock': '🪨',
        'paper': '📄',
        'scissors': '✂️'
    }
    
    print(f"\nYou chose: {choice_emojis[player_choice]} {player_choice.capitalize()}")
    print(f"Computer chose: {choice_emojis[computer_choice]} {computer_choice.capitalize()}")

def play_round():
    """Play a single round of Rock, Paper, Scissors."""
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    
    display_choices(player_choice, computer_choice)
    
    result = determine_winner(player_choice, computer_choice)
    
    if result == "tie":
        print("🤝 It's a tie!")
        return "tie"
    elif result == "player":
        print("🎉 You win this round!")
        return "player"
    else:
        print("🤖 Computer wins this round!")
        return "computer"

def play_again():
    """Ask if the player wants to play again."""
    while True:
        choice = input("\nPlay another round? (y/n): ").lower().strip()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def main():
    """Main game loop for Rock, Paper, Scissors."""
    print("🎮 Welcome to Rock, Paper, Scissors! 🎮")
    print("=" * 40)
    print("Rules:")
    print("🪨 Rock crushes Scissors")
    print("📄 Paper covers Rock") 
    print("✂️ Scissors cut Paper")
    print("=" * 40)
    
    player_score = 0
    computer_score = 0
    ties = 0
    
    while True:
        print(f"\n📊 Score - You: {player_score} | Computer: {computer_score} | Ties: {ties}")
        print("-" * 40)
        
        result = play_round()
        
        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1
        else:
            ties += 1
        
        if not play_again():
            break
    
    # Final results
    print("\n" + "=" * 40)
    print("🏆 FINAL RESULTS")
    print(f"Your wins: {player_score}")
    print(f"Computer wins: {computer_score}")
    print(f"Ties: {ties}")
    
    total_games = player_score + computer_score + ties
    if total_games > 0:
        if player_score > computer_score:
            print("🎉 You are the overall winner!")
        elif computer_score > player_score:
            print("🤖 Computer is the overall winner!")
        else:
            print("🤝 It's an overall tie!")
    
    print("Thanks for playing! 👋")

if __name__ == "__main__":
    main()
