# 20250210-nfl_numbers-gist

**Gist file**: [https://gist.github.com/rjvitorino/ae7ded09ef3c3e2d3e038129143e1052](https://gist.github.com/rjvitorino/ae7ded09ef3c3e2d3e038129143e1052)

**Description**: Cassidy's interview question of the week: a function that returns a list of numbers that an NFL player can choose from for their uniform, given the player's position, and an array of existing numbers on the team

## nfl_numbers.py

```Python
"""
NFL Uniform Number Management

Defines valid NFL uniform number ranges by position according to official regulations.
Provides utilities to validate and find available numbers for players.

Position Groups and Number Ranges:
Offense:
- QB (Quarterback): 1-19
- RB (Running Back): 20-49
- WR (Wide Receiver): 1-49, 80-89
- TE (Tight End): 1-49, 80-89
- OL (Offensive Line - C/G/T): 50-79

Defense:
- DL (Defensive Line - DT/DE): 50-79, 90-99
- LB (Linebacker - MLB/OLB): 0-59, 90-99
- DB (Defensive Back - CB/S): 20-49

Special Teams:
- K (Kicker), P (Punter), LS (Long Snapper): 1-19

Main components:
- NFL_NUMBER_RANGES: Maps position groups to allowed number ranges
- POSITION_TO_CATEGORY: Maps position codes to their categories
- available_numbers(): Returns valid available numbers for a position
"""

from typing import Dict, List, TypedDict


class PositionRange(TypedDict):
    """
    TypedDict for position ranges

    Attributes:
        positions: List of positions
        range: List of numbers
    """

    positions: List[str]
    range: List[int]


# Dictionary mapping position categories to allowed number ranges and positions
# Each entry contains a list of position codes and their valid uniform numbers
# Used to validate and look up valid numbers for NFL players by position
NFL_NUMBER_RANGES: Dict[str, PositionRange] = {
    "Quarterbacks, Punters, Kickers": {
        "positions": ["QB", "P", "K"],
        "range": list(range(1, 20)),
    },
    "Running Backs, Defensive Backs": {
        "positions": ["RB", "DB"],
        "range": list(range(20, 50)),
    },
    "Wide Receivers": {
        "positions": ["WR"],
        "range": list(range(1, 50)) + list(range(80, 90)),
    },
    "Tight Ends": {
        "positions": ["TE"],
        "range": list(range(1, 50)) + list(range(80, 90)),
    },
    "Offensive Line": {"positions": ["C", "G", "T"], "range": list(range(50, 80))},
    "Defensive Line": {
        "positions": ["DT", "DE"],
        "range": list(range(50, 80)) + list(range(90, 100)),
    },
    "Linebackers": {
        "positions": ["LB", "OLB", "MLB"],
        "range": list(range(0, 60)) + list(range(90, 100)),
    },
    "Special Teams": {
        "positions": ["K", "P", "LS"],
        "range": list(range(1, 20)),  # Mostly overlapping with QBs
    },
}

# Create a mapping from position codes (e.g. 'QB', 'WR') to their category names
# This allows efficient lookup of valid number ranges for a position without
# having to search through the NFL_NUMBER_RANGES dictionary each time
POSITION_TO_CATEGORY: Dict[str, str] = {
    position: category
    for category, data in NFL_NUMBER_RANGES.items()
    for position in data["positions"]
}


def available_numbers(position: str, existing_numbers: List[int]) -> List[int]:
    """
    Get available numbers for a position, using position acronym (e.g. 'QB', 'WR').

    Args:
        position: Position acronym (e.g. 'QB', 'WR')
        existing_numbers: List of already existing numbers on the team

    Returns:
        List of available numbers in sorted order
    """
    if position not in POSITION_TO_CATEGORY:
        raise ValueError(f"Unknown position: {position}")
    return sorted(
        set(NFL_NUMBER_RANGES[POSITION_TO_CATEGORY[position]]["range"])
        - set(existing_numbers)
    )


if __name__ == "__main__":
    test_cases = [
        ("QB", [1, 2, 3, 10, 19], list(range(4, 10)) + list(range(11, 19))),
        ("WR", [1, 2, 81], list(range(3, 50)) + [80, 82, 83, 84, 85, 86, 87, 88, 89]),
        (
            "LB",
            [50, 51, 95],
            list(range(0, 50))
            + list(range(52, 60))
            + [90, 91, 92, 93, 94, 96, 97, 98, 99],
        ),
        ("TE", [1, 85, 88], list(range(2, 50)) + [80, 81, 82, 83, 84, 86, 87, 89]),
        ("DB", [20, 21, 45], list(range(22, 45)) + list(range(46, 50))),
        ("DT", [50, 90, 99], list(range(51, 80)) + list(range(91, 99))),
        (
            "C",
            [50, 60, 70],
            list(range(51, 60)) + list(range(61, 70)) + list(range(71, 80)),
        ),
        ("P", [1, 2], list(range(3, 20))),
        ("LS", [40], list(range(1, 20))),  # Testing invalid number for position
        ("OLB", [0, 59, 90], list(range(1, 59)) + list(range(91, 100))),
    ]

    for position, used_numbers, expected in test_cases:
        result = available_numbers(position, used_numbers)
        assert (
            result == expected
        ), f"Failed for {position}: expected {expected}, got {result}"

    print("All checks passed!")

```