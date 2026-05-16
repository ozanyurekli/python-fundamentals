# Number Guessing Game (Python Project)

## Overview
This is a command-line Number Guessing Game built using Python.

The player must guess a randomly generated number within a selected difficulty range. The game provides feedback after each guess and tracks performance across multiple rounds.

It also saves the best score using a JSON file so progress is not lost after closing the program.

---

## Features
- Random number generation
- Difficulty levels (Easy, Medium, Hard)
- Input validation (handles invalid inputs safely)
- Range checking
- Attempt counter
- Best score tracking
- Persistent storage using JSON file
- Replay system (play multiple rounds)

---

## Difficulty Levels
- Easy: 1 - 50
- Medium: 1 - 100
- Hard: 1 - 500

---

## How It Works

1. User selects a difficulty level
2. A random number is generated based on that range
3. User tries to guess the number
4. The game gives hints:
   - "Too high"
   - "Too low"
5. Attempts are counted
6. When the number is guessed:
   - Win message is shown
   - Best score is updated if improved
   - Score is saved to `score.json`
7. User can choose to play again

---

## Data Persistence

The best score is saved in a file called:
