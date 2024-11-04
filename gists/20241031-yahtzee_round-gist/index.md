# 20241031-yahtzee_round-gist

**Gist file**: [https://gist.github.com/rjvitorino/6d1722037fd3d12f5042dd32d14a40c3](https://gist.github.com/rjvitorino/6d1722037fd3d12f5042dd32d14a40c3)

**Description**: Cassidoo's interview question of the week: a function that implements a round of the game Yahtzee, where 5 dice are randomly rolled, and the function returns what options the user has to score more than 0 points.

## yahtzee_round.py

```Python
import random
from collections import Counter
from typing import List, Dict


def roll_dice(num_dice: int = 5) -> List[int]:
    """
    Rolls a specified number of dice and returns their values as a list.

    Args:
        num_dice (int): The number of dice to roll (default is 5).

    Returns:
        List[int]: A list of integers representing the values rolled by the dice.
    """
    return [random.randint(1, 6) for _ in range(num_dice)]


def get_yahtzee_options(dice: List[int]) -> List[str]:
    """
    Determines scoring options for a given dice roll in Yahtzee.

    Args:
        dice (List[int]): A list of integers representing the values rolled by the dice.

    Returns:
        List[str]: A list of strings representing the possible scoring options for the roll.
    """
    counts = Counter(dice)
    unique_dice = set(dice)
    max_count = max(counts.values())
    options = [f"{value}s" for value in counts]

    # Define straights
    SMALL_STRAIGHTS = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]
    LARGE_STRAIGHTS = [{1, 2, 3, 4, 5}, {2, 3, 4, 5, 6}]

    # Add options based on max count and specific patterns
    if max_count >= 3:
        options.append("three of a kind")
    if max_count >= 4:
        options.append("four of a kind")
    if sorted(counts.values()) == [2, 3]:
        options.append("full house")
    if any(straight.issubset(unique_dice) for straight in SMALL_STRAIGHTS):
        options.append("small straight")
    if unique_dice in LARGE_STRAIGHTS:
        options.append("large straight")
    if max_count == 5:
        options.append("yahtzee")

    options.append("chance")
    return options


def assert_options(
    dice_roll: List[int], expected_options: List[str], test_name: str = ""
) -> None:
    """
    Asserts that the options returned by get_yahtzee_options match the expected options.

    Args:
        dice_roll (List[int]): The list of dice values being tested.
        expected_options (List[str]): The expected scoring options for the given dice roll.
        test_name (str): An optional name for the test case to help identify failures.

    Raises:
        AssertionError: If the actual options do not match the expected options.
    """
    actual_options = get_yahtzee_options(dice_roll)
    assert set(actual_options) == set(
        expected_options
    ), f"{test_name} failed: expected {expected_options} but got {actual_options}"


def test_get_options() -> None:
    """
    Runs multiple test cases to validate the get_yahtzee_options function.

    Ensures that all expected scoring options for various dice rolls are correctly returned.
    """
    test_cases = [
        (
            [2, 2, 3, 3, 3],
            ["2s", "3s", "full house", "three of a kind", "chance"],
            "Test case 1",
        ),
        (
            [2, 3, 4, 2, 2],
            ["2s", "3s", "4s", "three of a kind", "chance"],
            "Test case 2",
        ),
        (
            [4, 3, 6, 3, 5],
            ["3s", "4s", "5s", "6s", "small straight", "chance"],
            "Test case 3",
        ),
        (
            [2, 2, 2, 3, 4],
            ["2s", "3s", "4s", "three of a kind", "chance"],
            "Test case 4",
        ),
        (
            [1, 1, 1, 1, 1],
            ["1s", "three of a kind", "four of a kind", "yahtzee", "chance"],
            "Test case 5",
        ),
        # Additional test cases
        (
            [3, 3, 3, 4, 5],
            ["3s", "4s", "5s", "three of a kind", "chance"],
            "Three of a Kind - present",
        ),
        (
            [1, 2, 3, 4, 5],
            [
                "1s",
                "2s",
                "3s",
                "4s",
                "5s",
                "small straight",
                "large straight",
                "chance",
            ],
            "Straight case",
        ),
        (
            [1, 1, 1, 2, 3],
            ["1s", "2s", "3s", "three of a kind", "chance"],
            "Three of a Kind - partial",
        ),
        (
            [4, 4, 4, 4, 2],
            ["4s", "2s", "three of a kind", "four of a kind", "chance"],
            "Four of a Kind - present",
        ),
        (
            [5, 5, 5, 2, 2],
            ["5s", "2s", "full house", "three of a kind", "chance"],
            "Full House - present",
        ),
        ([1, 1, 2, 2, 3], ["1s", "2s", "3s", "chance"], "Full House - not present"),
        (
            [1, 2, 3, 4, 6],
            ["1s", "2s", "3s", "4s", "6s", "small straight", "chance"],
            "Small straight - present",
        ),
        (
            [2, 3, 4, 5, 6],
            [
                "2s",
                "3s",
                "4s",
                "5s",
                "6s",
                "small straight",
                "large straight",
                "chance",
            ],
            "Large straight - present",
        ),
        (
            [6, 6, 6, 6, 6],
            ["6s", "three of a kind", "four of a kind", "yahtzee", "chance"],
            "Yahtzee - present",
        ),
        (
            [6, 6, 6, 6, 5],
            ["6s", "5s", "three of a kind", "four of a kind", "chance"],
            "Yahtzee - not present",
        ),
    ]

    for dice_roll, expected, name in test_cases:
        assert_options(dice_roll, expected, name)

    print("All test cases passed!")


def yahtzee_round() -> Dict[str, List[int]]:
    """
    Simulates a single round of Yahtzee and returns the dice roll and scoring options.

    Returns:
        Dict[str, List[int]]: A dictionary containing the dice roll and possible scoring options.
    """
    dice = roll_dice()
    options = get_yahtzee_options(dice)
    return {"dice": dice, "options": options}


if __name__ == "__main__":
    test_get_options()
    print(yahtzee_round())

```