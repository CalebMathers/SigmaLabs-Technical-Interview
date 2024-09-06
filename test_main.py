"""Tests for the main script."""

from main import calculate_score, assign_tiles, find_valid_word

TILES_DISTRIBUTION = {"E": 12, "A": 9, "I": 9, "O": 8, "N": 6, "R": 6,
                      "T": 6, "L": 4, "S": 4, "U": 4, "D": 4, "G": 3, "B": 2,
                      "C": 2, "M": 2, "P": 2, "F": 2, "H": 2, "V": 2,
                      "W": 2, "Y": 2, "K": 1, "J": 1, "X": 1, "Q": 1, "Z": 1}


def test_calculate_score_valid_input():
    """Tests that the correct score is returned given a valid word."""
    res = calculate_score("GUARDIAN")
    assert res == 10


def test_assign_tiles_returns_correct_list():
    """Tests that the assign tiles function returns a list of 7 strings."""
    res = assign_tiles(TILES_DISTRIBUTION)

    assert len(res) == 7
    assert isinstance(res, list)


def test_assign_tiles_takes_away_from_distribution():
    """Tests that when assigning tiles, the distribution dict is affected."""
    test_dict = {"E": 12}

    assign_tiles(test_dict)

    assert test_dict["E"] == 5


def test_find_valid_word_correct_word():
    """Tests that a word is returned from a tile set given."""
    res = find_valid_word(["G", "U", "A", "R", "D"])

    assert isinstance(res, str)
