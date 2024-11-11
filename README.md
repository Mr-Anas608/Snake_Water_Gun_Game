# Snake Water Gun Game

A simple Python game inspired by Rock-Paper-Scissors, where the player and computer each choose between Snake, Water, and Gun, and outcomes are determined based on predefined rules.

## Game Rules

The rules of the game are as follows:
- **Snake vs. Water**: Snake drinks the water, so Snake wins.
- **Water vs. Gun**: Water sinks the gun, so Water wins.
- **Gun vs. Snake**: Gun kills the snake, so Gun wins.
- **Tie**: If both choose the same, it’s a tie.

### Outcome Table

| User Choice | Computer Choice | Outcome        | Explanation                            |
|-------------|-----------------|----------------|----------------------------------------|
| `s`         | `w`             | User wins      | Snake drinks water, so Snake wins.     |
| `g`         | `s`             | User wins      | Gun kills the snake, so Gun wins.      |
| `w`         | `g`             | User wins      | Gun sinks in water, so Water wins.     |
| `w`         | `s`             | Computer wins  | Snake drinks water, so Snake wins.     |
| `s`         | `g`             | Computer wins  | Gun kills the snake, so Gun wins.      |
| `g`         | `w`             | Computer wins  | Gun sinks in water, so Water wins.     |
| `s`         | `s`             | Tie            | Both chose Snake, so it’s a tie.       |
| `g`         | `g`             | Tie            | Both chose Gun, so it’s a tie.         |
| `w`         | `w`             | Tie            | Both chose Water, so it’s a tie.       |

## How to Play

1. Run the game.
2. Enter your choice when prompted (`s` for Snake, `w` for Water, or `g` for Gun).
3. The computer will make a choice randomly, and the game will display the result.

## About the Project

This project is an introduction to Python programming, focusing on user input, conditional statements, and random number generation. It is designed as a beginner project for learning the basics of programming logic in Python.

## License

This project is open-source and free to use.
