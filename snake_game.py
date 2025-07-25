import pygame
import random
import json
import os
from enum import Enum

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)
DARK_GREEN = (0, 128, 0)

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class Difficulty(Enum):
    EASY = {"speed": 8, "name": "Easy", "multiplier": 1}
    NORMAL = {"speed": 12, "name": "Normal", "multiplier": 1.5}
    HARD = {"speed": 16, "name": "Hard", "multiplier": 2}

class GameMode(Enum):
    CLASSIC = {"name": "Classic", "walls": False, "obstacles": False}
    WALLS = {"name": "Walls", "walls": True, "obstacles": False}
    OBSTACLES = {"name": "Obstacles", "walls": False, "obstacles": True}
    EXTREME = {"name": "Extreme", "walls": True, "obstacles": True}

class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game - Advanced Edition")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # Game state
        self.reset_game()
        self.difficulty = Difficulty.NORMAL
        self.game_mode = GameMode.CLASSIC
        self.high_scores = self.load_high_scores()
        self.paused = False
        
    def reset_game(self):
        """Reset the game to initial state."""
        # Snake starting position (center of screen)
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        self.snake = [(start_x, start_y)]
        self.direction = Direction.RIGHT
        self.next_direction = Direction.RIGHT
        
        # Game stats
        self.score = 0
        self.level = 1
        self.food_eaten = 0
        self.food_position = self.generate_food()
        self.obstacles = []
        self.walls = []
        
        # Level progression
        self.food_for_next_level = 5
        
    def generate_food(self):
        """Generate food at a random position not occupied by snake or obstacles."""
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in self.snake and (x, y) not in self.obstacles:
                return (x, y)
    
    def generate_obstacles(self, count):
        """Generate random obstacles for obstacle modes."""
        obstacles = []
        for _ in range(count):
            while True:
                x = random.randint(1, GRID_WIDTH - 2)
                y = random.randint(1, GRID_HEIGHT - 2)
                pos = (x, y)
                if (pos not in self.snake and pos != self.food_position and 
                    pos not in obstacles):
                    obstacles.append(pos)
                    break
        return obstacles
    
    def generate_walls(self):
        """Generate walls around the border for wall modes."""
        walls = []
        # Top and bottom walls
        for x in range(GRID_WIDTH):
            walls.append((x, 0))
            walls.append((x, GRID_HEIGHT - 1))
        # Left and right walls
        for y in range(GRID_HEIGHT):
            walls.append((0, y))
            walls.append((GRID_WIDTH - 1, y))
        return walls
    
    def move_snake(self):
        """Move the snake in the current direction."""
        self.direction = self.next_direction
        head_x, head_y = self.snake[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx, head_y + dy)
        
        # Check for collisions
        if self.check_collision(new_head):
            return False
        
        self.snake.insert(0, new_head)
        
        # Check if food is eaten
        if new_head == self.food_position:
            self.score += 10 * self.difficulty.value["multiplier"] * self.level
            self.food_eaten += 1
            self.food_position = self.generate_food()
            
            # Check for level up
            if self.food_eaten >= self.food_for_next_level:
                self.level_up()
        else:
            # Remove tail if no food eaten
            self.snake.pop()
        
        return True
    
    def check_collision(self, position):
        """Check if the given position results in a collision."""
        x, y = position
        
        # Check bounds (only if not in wall mode - walls handle bounds)
        if not self.game_mode.value["walls"]:
            if x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT:
                return True
        else:
            # In wall mode, going out of bounds is handled by wall collision
            if x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT:
                return True
        
        # Check self collision
        if position in self.snake:
            return True
        
        # Check wall collision
        if position in self.walls:
            return True
        
        # Check obstacle collision
        if position in self.obstacles:
            return True
        
        return False
    
    def level_up(self):
        """Increase the level and add obstacles/challenges."""
        self.level += 1
        self.food_for_next_level = 5 + (self.level - 1) * 2
        
        # Add obstacles in obstacle modes
        if self.game_mode.value["obstacles"]:
            new_obstacles = self.generate_obstacles(self.level - 1)
            self.obstacles.extend(new_obstacles)
    
    def handle_input(self, event):
        """Handle keyboard input."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.direction != Direction.DOWN:
                self.next_direction = Direction.UP
            elif event.key == pygame.K_DOWN and self.direction != Direction.UP:
                self.next_direction = Direction.DOWN
            elif event.key == pygame.K_LEFT and self.direction != Direction.RIGHT:
                self.next_direction = Direction.LEFT
            elif event.key == pygame.K_RIGHT and self.direction != Direction.LEFT:
                self.next_direction = Direction.RIGHT
            elif event.key == pygame.K_SPACE:
                self.paused = not self.paused
            elif event.key == pygame.K_r:
                self.reset_game()
                if self.game_mode.value["walls"]:
                    self.walls = self.generate_walls()
                if self.game_mode.value["obstacles"]:
                    self.obstacles = self.generate_obstacles(2)
    
    def draw_grid(self):
        """Draw a subtle grid for better visibility."""
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, GRAY, (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, GRAY, (0, y), (WINDOW_WIDTH, y))
    
    def draw_snake(self):
        """Draw the snake with a gradient effect."""
        for i, (x, y) in enumerate(self.snake):
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            if i == 0:  # Head
                pygame.draw.rect(self.screen, DARK_GREEN, rect)
                pygame.draw.rect(self.screen, GREEN, rect, 2)
            else:  # Body
                color_intensity = max(100, 255 - i * 10)
                color = (0, color_intensity, 0)
                pygame.draw.rect(self.screen, color, rect)
    
    def draw_food(self):
        """Draw the food with a pulsing effect."""
        x, y = self.food_position
        rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(self.screen, RED, rect)
        pygame.draw.rect(self.screen, YELLOW, rect, 2)
    
    def draw_obstacles(self):
        """Draw obstacles."""
        for x, y in self.obstacles:
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(self.screen, PURPLE, rect)
    
    def draw_walls(self):
        """Draw walls."""
        for x, y in self.walls:
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(self.screen, BLUE, rect)
    
    def draw_ui(self):
        """Draw the user interface."""
        # Score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Level
        level_text = self.font.render(f"Level: {self.level}", True, WHITE)
        self.screen.blit(level_text, (10, 50))
        
        # Food progress
        progress = self.food_eaten % self.food_for_next_level
        progress_text = self.small_font.render(f"Progress: {progress}/{self.food_for_next_level}", True, WHITE)
        self.screen.blit(progress_text, (10, 90))
        
        # Difficulty and mode
        diff_text = self.small_font.render(f"Difficulty: {self.difficulty.value['name']}", True, WHITE)
        self.screen.blit(diff_text, (10, 110))
        
        mode_text = self.small_font.render(f"Mode: {self.game_mode.value['name']}", True, WHITE)
        self.screen.blit(mode_text, (10, 130))
        
        # High score
        high_score = self.get_high_score()
        high_text = self.small_font.render(f"High Score: {high_score}", True, WHITE)
        self.screen.blit(high_text, (10, 150))
        
        # Controls
        controls = [
            "Controls:",
            "Arrow Keys - Move",
            "SPACE - Pause",
            "R - Restart"
        ]
        for i, control in enumerate(controls):
            control_text = self.small_font.render(control, True, WHITE)
            self.screen.blit(control_text, (WINDOW_WIDTH - 150, 10 + i * 20))
        
        if self.paused:
            pause_text = self.font.render("PAUSED", True, YELLOW)
            text_rect = pause_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
            self.screen.blit(pause_text, text_rect)
    
    def load_high_scores(self):
        """Load high scores from file."""
        try:
            if os.path.exists("high_scores.json"):
                with open("high_scores.json", "r") as f:
                    return json.load(f)
        except:
            pass
        return {}
    
    def save_high_scores(self):
        """Save high scores to file."""
        try:
            with open("high_scores.json", "w") as f:
                json.dump(self.high_scores, f)
        except:
            pass
    
    def get_high_score(self):
        """Get the high score for current difficulty and mode."""
        key = f"{self.difficulty.value['name']}_{self.game_mode.value['name']}"
        return self.high_scores.get(key, 0)
    
    def update_high_score(self):
        """Update high score if current score is higher."""
        key = f"{self.difficulty.value['name']}_{self.game_mode.value['name']}"
        current_high = self.high_scores.get(key, 0)
        if self.score > current_high:
            self.high_scores[key] = self.score
            self.save_high_scores()
            return True
        return False
    
    def show_game_over(self):
        """Show game over screen."""
        is_high_score = self.update_high_score()
        
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        game_over_text = self.font.render("GAME OVER!", True, RED)
        score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
        level_text = self.font.render(f"Level Reached: {self.level}", True, WHITE)
        
        if is_high_score:
            high_score_text = self.font.render("NEW HIGH SCORE!", True, YELLOW)
            self.screen.blit(high_score_text, (WINDOW_WIDTH//2 - high_score_text.get_width()//2, WINDOW_HEIGHT//2 - 60))
        
        restart_text = self.small_font.render("Press R to restart or ESC to quit", True, WHITE)
        
        # Center all text
        self.screen.blit(game_over_text, (WINDOW_WIDTH//2 - game_over_text.get_width()//2, WINDOW_HEIGHT//2 - 20))
        self.screen.blit(score_text, (WINDOW_WIDTH//2 - score_text.get_width()//2, WINDOW_HEIGHT//2 + 20))
        self.screen.blit(level_text, (WINDOW_WIDTH//2 - level_text.get_width()//2, WINDOW_HEIGHT//2 + 60))
        self.screen.blit(restart_text, (WINDOW_WIDTH//2 - restart_text.get_width()//2, WINDOW_HEIGHT//2 + 100))
    
    def show_menu(self):
        """Show the main menu."""
        menu_running = True
        selected_difficulty = 1  # Default to Normal
        selected_mode = 0  # Default to Classic
        
        difficulties = list(Difficulty)
        modes = list(GameMode)
        
        while menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected_difficulty = (selected_difficulty - 1) % len(difficulties)
                    elif event.key == pygame.K_DOWN:
                        selected_difficulty = (selected_difficulty + 1) % len(difficulties)
                    elif event.key == pygame.K_LEFT:
                        selected_mode = (selected_mode - 1) % len(modes)
                    elif event.key == pygame.K_RIGHT:
                        selected_mode = (selected_mode + 1) % len(modes)
                    elif event.key == pygame.K_RETURN:
                        self.difficulty = difficulties[selected_difficulty]
                        self.game_mode = modes[selected_mode]
                        self.reset_game()
                        if self.game_mode.value["walls"]:
                            self.walls = self.generate_walls()
                        if self.game_mode.value["obstacles"]:
                            self.obstacles = self.generate_obstacles(2)
                        menu_running = False
                    elif event.key == pygame.K_ESCAPE:
                        return False
            
            self.screen.fill(BLACK)
            
            # Title
            title_text = self.font.render("SNAKE GAME - ADVANCED EDITION", True, GREEN)
            self.screen.blit(title_text, (WINDOW_WIDTH//2 - title_text.get_width()//2, 50))
            
            # Difficulty selection
            diff_title = self.font.render("Difficulty (UP/DOWN):", True, WHITE)
            self.screen.blit(diff_title, (WINDOW_WIDTH//2 - diff_title.get_width()//2, 150))
            
            for i, diff in enumerate(difficulties):
                color = YELLOW if i == selected_difficulty else WHITE
                diff_text = self.small_font.render(diff.value['name'], True, color)
                self.screen.blit(diff_text, (WINDOW_WIDTH//2 - diff_text.get_width()//2, 180 + i * 30))
            
            # Mode selection
            mode_title = self.font.render("Game Mode (LEFT/RIGHT):", True, WHITE)
            self.screen.blit(mode_title, (WINDOW_WIDTH//2 - mode_title.get_width()//2, 300))
            
            for i, mode in enumerate(modes):
                color = YELLOW if i == selected_mode else WHITE
                mode_text = self.small_font.render(mode.value['name'], True, color)
                self.screen.blit(mode_text, (WINDOW_WIDTH//2 - mode_text.get_width()//2, 330 + i * 30))
            
            # Instructions
            instructions = [
                "ENTER - Start Game",
                "ESC - Quit",
                "",
                "Game Modes:",
                "Classic - Basic snake game",
                "Walls - Walls around the border",
                "Obstacles - Random obstacles appear",
                "Extreme - Walls + Obstacles"
            ]
            
            for i, instruction in enumerate(instructions):
                inst_text = self.small_font.render(instruction, True, WHITE)
                self.screen.blit(inst_text, (50, 450 + i * 20))
            
            pygame.display.flip()
            self.clock.tick(60)
        
        return True
    
    def run(self):
        """Main game loop."""
        if not self.show_menu():
            return
        
        running = True
        game_over = False
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if game_over:
                            running = False
                        else:
                            if not self.show_menu():
                                running = False
                    elif event.key == pygame.K_r and game_over:
                        game_over = False
                        self.reset_game()
                        if self.game_mode.value["walls"]:
                            self.walls = self.generate_walls()
                        if self.game_mode.value["obstacles"]:
                            self.obstacles = self.generate_obstacles(2)
                    else:
                        self.handle_input(event)
            
            if not game_over and not self.paused:
                if not self.move_snake():
                    game_over = True
            
            # Draw everything
            self.screen.fill(BLACK)
            self.draw_grid()
            self.draw_walls()
            self.draw_obstacles()
            self.draw_food()
            self.draw_snake()
            self.draw_ui()
            
            if game_over:
                self.show_game_over()
            
            pygame.display.flip()
            self.clock.tick(self.difficulty.value["speed"])
        
        pygame.quit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
