"""
Game Launcher - Choose which game to play!
"""
import subprocess
import sys
import os

def run_game(game_file):
    """Run a specific game file."""
    try:
        # Get the Python executable path for the virtual environment
        python_exe = r"C:/Users/nirma/Desktop/python game/.venv/Scripts/python.exe"
        subprocess.run([python_exe, game_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running game: {e}")
    except FileNotFoundError:
        print(f"Game file not found: {game_file}")

def main():
    """Main launcher menu."""
    print("🎮 Welcome to Python Game Collection! 🎮")
    print("=" * 50)
    print()
    print("Available Games:")
    print("1. 🐍 Snake Game (Advanced Edition)")
    print("   - Multiple difficulty levels (Easy, Normal, Hard)")
    print("   - 4 Game modes (Classic, Walls, Obstacles, Extreme)")
    print("   - Level progression system")
    print("   - High score tracking")
    print("   - Pause/Resume functionality")
    print()
    print("2. 🔢 Guess the Number")
    print("   - Classic number guessing game")
    print("   - Statistics tracking")
    print("   - Multiple rounds")
    print()
    print("3. ✂️ Rock Paper Scissors")
    print("   - Play against computer")
    print("   - Score tracking")
    print("   - Multiple rounds")
    print()
    print("4. 🚪 Exit")
    print()
    
    while True:
        try:
            choice = input("Select a game (1-4): ").strip()
            
            if choice == "1":
                print("\n🐍 Starting Snake Game...")
                print("Controls:")
                print("- Arrow keys to move")
                print("- SPACE to pause")
                print("- R to restart")
                print("- ESC to return to menu")
                print("\nHave fun! 🎉")
                run_game("snake_game.py")
                
            elif choice == "2":
                print("\n🔢 Starting Guess the Number...")
                run_game("guess_the_number.py")
                
            elif choice == "3":
                print("\n✂️ Starting Rock Paper Scissors...")
                run_game("rock_paper_scissors.py")
                
            elif choice == "4":
                print("\n👋 Thanks for playing!")
                break
                
            else:
                print("❌ Invalid choice! Please enter 1, 2, 3, or 4.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Thanks for playing!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
