def get_range_for_difficulty(difficulty: str):
    """Return the inclusive number range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an integer guess from 1 through 100.

    Returns: (ok, guess_int, error_message)
    """
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        value = int(raw)
    except ValueError:
        return False, None, "Enter a whole number."

    # Keep invalid guesses from affecting the game state.
    if not 1 <= value <= 100:
        return False, None, "Guess must be between 1 and 100."

    return True, value, None


def check_guess(guess, secret):
    """Compare a guess with the secret and return its outcome."""
    # Direct integer comparisons avoid the earlier string-based hint inversion.
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
