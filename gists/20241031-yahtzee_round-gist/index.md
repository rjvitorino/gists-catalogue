# 20241031-yahtzee_round-gist

**Gist file**: [https://gist.github.com/rjvitorino/6d1722037fd3d12f5042dd32d14a40c3](https://gist.github.com/rjvitorino/6d1722037fd3d12f5042dd32d14a40c3)

**Description**: Cassidoo's interview question of the week: a function that implements a round of the game Yahtzee, where 5 dice are randomly rolled, and the function returns what options the user has to score more than 0 points.

## yahtzee_round.py

```Python
import random
from collections import Counter
from typing import List, Dict


def roll_dice(num_dice: int = 5) -> List[int]:
    """Rolls a specified number of dice and returns their values as a list.

    Args:
        num_dice (int): The number of dice to roll (default is 5).

    Returns:
        List[int]: A list of integers representing the dice roll.
    """
    return [random.randint(1, 6) for _ in range(num_dice)]


def get_yahtzee_options(dice: List[int]) -> List[str]:
    """Determines scoring options for a given dice roll in Yahtzee - https://en.m.wikipedia.org/wiki/Yahtzee

    Args:
        dice (List[int]): A list of integers representing the dice roll.

    Returns:
        List[str]: A list of scoring options available for the roll.
    """
    counts = Counter(dice)
    unique_dice = set(dice)
    options = [f"{value}s" for value in range(1, 7) if counts[value] > 0]

    # Check for scoring options based on counts
    max_count = max(counts.values())
    if max_count >= 3:
        options.append("three of a kind")
    if max_count >= 4:
        options.append("four of a kind")
    if sorted(counts.values()) == [2, 3]:
        options.append("full house")

    # Define straights
    small_straights = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]
    large_straights = [{1, 2, 3, 4, 5}, {2, 3, 4, 5, 6}]

    # Check for straights
    if any(straight.issubset(unique_dice) for straight in small_straights):
        options.append("small straight")
    if unique_dice in large_straights:
        options.append("large straight")

    if max_count == 5:
        options.append("yahtzee")

    options.append("chance")
    return options


def assert_options(
    dice_roll: List[int], expected_options: List[str], test_name: str = ""
) -> None:
    """Asserts that the options returned by get_options for a given dice roll match the expected options.

    Compares the options in a set-like manner to disregard ordering and provides a detailed error message
    if the assertion fails.

    Args:
        dice_roll (List[int]): The list of dice values being tested.
        expected_options (List[str]): The expected scoring options for the dice roll.
        test_name (str): An optional name for the test case to help identify failures.
    """
    actual_options = get_yahtzee_options(dice_roll)
    assert set(actual_options) == set(
        expected_options
    ), f"{test_name} failed: expected {expected_options} but got {actual_options}"


def test_get_options():
    """Test cases to validate scoring options for the Yahtzee game."""
    # Define straights
    small_straights = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]
    large_straights = [{1, 2, 3, 4, 5}, {2, 3, 4, 5, 6}]

    # Provided examples from Cassidy
    assert_options(
        [2, 2, 3, 3, 3],
        ["2s", "3s", "full house", "three of a kind", "chance"],
        "Test case 1",
    )
    assert_options(
        [2, 3, 4, 2, 2], ["2s", "3s", "4s", "three of a kind", "chance"], "Test case 2"
    )
    assert_options(
        [4, 3, 6, 3, 5],
        ["3s", "4s", "5s", "6s", "small straight", "chance"],
        "Test case 3",
    )

    # Additional test cases
    assert get_yahtzee_options([2, 2, 2, 3, 4]) == [
        "2s",
        "3s",
        "4s",
        "three of a kind",
        "chance",
    ]
    assert get_yahtzee_options([1, 1, 1, 1, 1]) == [
        "1s",
        "three of a kind",
        "four of a kind",
        "yahtzee",
        "chance",
    ]

    # Three of a Kind
    assert "three of a kind" in get_yahtzee_options([3, 3, 3, 4, 5])
    assert "three of a kind" not in get_yahtzee_options([1, 2, 3, 4, 5])

    # Four of a Kind
    assert "four of a kind" in get_yahtzee_options([4, 4, 4, 4, 2])
    assert "four of a kind" not in get_yahtzee_options([1, 1, 1, 2, 3])

    # Full House
    assert "full house" in get_yahtzee_options([5, 5, 5, 2, 2])
    assert "full house" not in get_yahtzee_options([1, 1, 2, 2, 3])

    # Small Straight
    assert any(straight.issubset(set([1, 2, 3, 4, 6])) for straight in small_straights)
    assert any(straight.issubset(set([2, 3, 4, 5, 6])) for straight in small_straights)
    assert not any(
        straight.issubset(set([1, 1, 3, 4, 6])) for straight in small_straights
    )

    # Large Straight
    assert any(set([1, 2, 3, 4, 5]) == straight for straight in large_straights)
    assert any(set([2, 3, 4, 5, 6]) == straight for straight in large_straights)
    assert not any(set([1, 2, 3, 4, 6]) == straight for straight in large_straights)

    # Yahtzee
    assert "yahtzee" in get_yahtzee_options([6, 6, 6, 6, 6])
    assert "yahtzee" not in get_yahtzee_options([6, 6, 6, 6, 5])

    # Chance
    assert "chance" in get_yahtzee_options([1, 2, 3, 4, 5])
    assert "chance" in get_yahtzee_options([5, 5, 5, 5, 5])

    print("All test cases passed!")


def yahtzee_round() -> Dict[str, List[int]]:
    """Simulates a single round of Yahtzee, rolling dice and determining scoring options.

    Returns:
        Dict[str, List[int]]: A dictionary containing the dice roll and scoring options.
    """
    dice = roll_dice()
    options = get_yahtzee_options(dice)
    return {"dice": dice, "options": options}


if __name__ == "__main__":
    test_get_options()
    print(yahtzee_round())

```