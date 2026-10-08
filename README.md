# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🎯 Project

A number guessing game built with Streamlit. The player chooses a difficulty, guesses the secret number, and receives higher/lower hints while keeping track of attempts and score. This project investigates and repairs bugs in the game's state, hint logic, and input handling.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the game: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

The repaired game stores round data in Streamlit session state, validates guesses, and uses reusable functions from `logic_utils.py`. Run the tests with `python -m pytest tests`.

## 📝 Document Your Experience

- [x] The game lets a player guess a hidden number, receive directional hints, and track a score.
- [x] Bugs found: misleading high/low hints, mixed numeric/string comparisons, no 1–100 input validation, and stale game/input state across rounds.
- [x] Fixes: moved game logic to `logic_utils.py`, compared numeric values consistently, validated whole-number guesses within 1–100, reset round state and the input widget, and preserved feedback through reruns.

## 🎮 Demo Walkthrough

Example round with Normal difficulty and the debug secret set to 50:

1. The player enters `40`; the game reports that the guess is too low and to guess higher.
2. The player enters `70`; the game reports that the guess is too high and to guess lower.
3. The player enters `50`; the game reports a win and displays the final score.
4. The player selects **New Game**; attempts, score, history, and the guess field reset for the next round.
5. An input such as `-1`, `101`, or `400-` displays an error instead of being scored as a guess.

## 🧪 Test Results

```
$ .venv\Scripts\python.exe -m pytest tests
tests\test_game_logic.py .......                                         [100%]
============================== 7 passed in 0.06s ==============================
```

## 🚀 Stretch Features

- No stretch features completed.
