"""Main script for technical interview."""

import random

LETTER_SCORES = {"E": 1, "A": 1, "I": 1, "O": 1,
                 "N": 1, "R": 1, "T": 1, "L": 1, "S": 1, "U": 1,
                 "D": 2, "G": 2, "B": 3, "C": 3, "M": 3, "P": 3,
                 "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4, "K": 5,
                 "J": 8, "X": 8, "Q": 10, "Z": 10}

TILES_DISTRIBUTION = {"E": 12, "A": 9, "I": 9, "O": 8, "N": 6, "R": 6,
                      "T": 6, "L": 4, "S": 4, "U": 4, "D": 4, "G": 3, "B": 2,
                      "C": 2, "M": 2, "P": 2, "F": 2, "H": 2, "V": 2, "W": 2,
                      "Y": 2, "K": 1, "J": 1, "X": 1, "Q": 1, "Z": 1}


def calculate_score(word: str) -> int:
    """Returns the score for a given word."""
    score = 0

    for letter in word:
        score += LETTER_SCORES[letter]

    return score


def assign_tiles(tiles_distribution: dict) -> list[str]:
    """Returns a list of seven tiles each being a letter of the alphabet."""
    tiles = []

    for i in range(7):
        new_tile = random.choice(list(tiles_distribution.keys()))
        tiles_distribution[new_tile] -= 1
        tiles.append(new_tile)

    return tiles


def find_valid_word(tiles: list[str]) -> str:
    """Returns a string that can be made from the given tile list."""
    words = []
    with open(file="dictionary.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip())

    tiles_word = "".join(tiles)

    for word in words:
        if tiles_word.lower() == word:
            return word


if __name__ == "__main__":
    print(find_valid_word(["A", "A"]))
