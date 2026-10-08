from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_parse_guess_accepts_bounds():
    assert parse_guess("1") == (True, 1, None)
    assert parse_guess("100") == (True, 100, None)


def test_parse_guess_rejects_out_of_range_values():
    assert parse_guess("-1")[0] is False
    assert parse_guess("101")[0] is False


def test_parse_guess_rejects_non_integer_input():
    assert parse_guess("400-")[0] is False
    assert parse_guess("1.5")[0] is False


def test_guess_direction_is_numeric():
    assert check_guess(9, 24) == "Too Low"
    assert check_guess(40, 24) == "Too High"
