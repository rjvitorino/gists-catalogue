# 20241202-roll_call-gist

**Gist file**: [https://gist.github.com/rjvitorino/60a7b2df5fc473116f78f3049928f63c](https://gist.github.com/rjvitorino/60a7b2df5fc473116f78f3049928f63c)

**Description**: Cassidy's interview question of the week: a function that reverses the names in a list and puts them in alphabetical order!

## roll_call.py

```Python
from typing import List


def roll_call(names: List[str]) -> List[str]:
    """
    Reverses each name in the input list, then sorts the names alphabetically.

    Args:
        names (List[str]): A list of names to reverse and sort.

    Returns:
        List[str]: The reversed and alphabetically sorted names.
    """
    # Reverse each name and sort the list alphabetically
    return sorted(name[::-1] for name in names)


if __name__ == "__main__":
    # Example test cases
    assert roll_call(["yzneT", "ydissaC", "enimA"]) == ["Amine", "Cassidy", "Tenzy"]
    assert roll_call(
        [
            "rennoD",
            "nexiV",
            "recnarP",
            "temoC",
            "neztilB",
            "recnaD",
            "dipuC",
            "rehsaD",
            "hploduR",
        ]
    ) == [
        "Blitzen",
        "Comet",
        "Cupid",
        "Dancer",
        "Dasher",
        "Donner",
        "Prancer",
        "Rudolph",
        "Vixen",
    ]
    assert roll_call(["A", "B", "C"]) == ["A", "B", "C"]

    # Additional test cases
    assert roll_call([]) == []
    assert roll_call(["a", "b", "c"]) == ["a", "b", "c"]
    assert roll_call(["cc", "bb", "aa"]) == [
        "aa",
        "bb",
        "cc",
    ]

    print("All tests passed!")

```