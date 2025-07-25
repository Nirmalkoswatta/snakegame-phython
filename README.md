# Snake Game Python 🐍

An advanced Snake game implementation in Python with multiple difficulty levels, game modes, and features. This project also includes bonus games: Number Guessing and Rock Paper Scissors.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Pygame](https://img.shields.io/badge/pygame-required-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🎮 Features

- **Advanced Snake Game** with multiple difficulties and game modes
- **Level progression system** with increasing challenges
- **High score tracking** with persistent storage
- **Multiple game modes**: Classic, Walls, Obstacles, and Extreme
- **Bonus games**: Number Guessing and Rock Paper Scissors

### Snake Game Difficulty Levels:
| Difficulty | Speed | Score Multiplier | Description |
|------------|-------|------------------|-------------|
| Easy | 8 FPS | 1x | Perfect for beginners |
| Normal | 12 FPS | 1.5x | Balanced gameplay |
| Hard | 16 FPS | 2x | Fast-paced challenge |

### Game Modes:
| Mode | Features | Challenge Level |
|------|----------|----------------|
| Classic | Traditional snake game | ⭐ |
| Walls | Border walls block movement | ⭐⭐ |
| Obstacles | Random obstacles appear | ⭐⭐⭐ |
| Extreme | Walls + Obstacles | ⭐⭐⭐⭐ |

## 🎮 Controls

**Snake Game:**
- `Arrow Keys` - Move snake
- `SPACE` - Pause/Resume
- `R` - Restart game
- `ESC` - Return to menu

**Menu Navigation:**
- `UP/DOWN` - Select difficulty
- `LEFT/RIGHT` - Select game mode
- `ENTER` - Start game

## 📊 Scoring System

Score = Base Points (10) × Difficulty Multiplier × Current Level

**Example:** In Hard mode at Level 3: `10 × 2 × 3 = 60 points per food`

## 🏆 High Score System

- Separate high scores for each difficulty/mode combination
- Automatically saved to `high_scores.json`
- Persistent across game sessions

## 🎯 Bonus Games

### 🔢 Guess the Number
- Random number between 1-100
- 7 attempts to guess correctly
- Statistics tracking
- Hints for each guess

### ✂️ Rock Paper Scissors
- Classic game against computer
- Score tracking (wins/losses/ties)
- Multiple rounds
- Overall winner determination

## 📁 Project Structure

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Nirmalkoswatta/snakegame-phython.git
   cd snakegame-phython
   ```

2. **Install dependencies:**
   ```bash
   pip install pygame
   ```

3. **Run the game launcher:**
   ```bash
   python game_launcher.py
   ```

   Or run individual games:
   ```bash
   python snake_game.py
   python guess_the_number.py
   python rock_paper_scissors.py
   ```

## 🎯 Game Modes & Difficulty

```
snakegame-phython/
├── snake_game.py          # 🐍 Advanced Snake game
├── guess_the_number.py    # 🔢 Number guessing game
├── rock_paper_scissors.py # ✂️ Rock Paper Scissors
├── game_launcher.py       # 🚀 Main launcher script
├── high_scores.json       # 🏆 High scores (auto-generated)
├── README.md             # 📖 Documentation
└── LICENSE               # ⚖️ MIT License
```

## 🛠️ Technical Details

- **Language:** Python 3.7+
- **Graphics Library:** Pygame
- **Architecture:** Object-oriented design
- **Features:** JSON-based high score persistence
- **Platform:** Cross-platform (Windows, macOS, Linux)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🐛 Known Issues

- None currently reported

## 📝 Changelog

### v1.0.0 (2025-07-26)
- Initial release
- Advanced Snake game with 4 modes and 3 difficulties
- High score system
- Bonus games included
- Complete documentation

## 🎯 Future Enhancements

- [ ] Multiplayer snake game
- [ ] Online leaderboards
- [ ] Sound effects and music
- [ ] Additional game modes
- [ ] Mobile version

## � License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Nirmal Koswatta**
- GitHub: [@Nirmalkoswatta](https://github.com/Nirmalkoswatta)

## 🙏 Acknowledgments

- Inspired by the classic Snake game
- Built with Python and Pygame
- Thanks to the open-source community

## 📞 Support

If you have any questions or need help, please:
1. Check the documentation above
2. Open an issue on GitHub
3. Make sure Python 3.7+ and Pygame are properly installed

---

⭐ **Star this repository if you found it helpful!** ⭐
