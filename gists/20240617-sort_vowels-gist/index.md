# 20240617-sort_vowels-gist

**Gist file**: [https://gist.github.com/rjvitorino/dfef5433066c061954d29d1b15202290](https://gist.github.com/rjvitorino/dfef5433066c061954d29d1b15202290)

**Description**: Cassidoo's interview question of the week: a function that takes a list of names and returns the names sorted by the number of vowels in each name in descending order. If two names have the same number of vowels, sort them alphabetically.

## sort_vowels.py

```Python
from typing import List

def count_vowels(name: str) -> int:
    """Helper function to count the number of vowels in a name."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in name if char in vowels)


def clean_names(names: List[str]) -> None:
    """Helper function to remove non-string elements from the list."""
    return [name for name in names if isinstance(name, str)]


def sort_names(names: List[str]) -> List[str]:
    """
    Sort names by the number of vowels in descending order.
    If two names have the same number of vowels, sort them alphabetically.
    """
    names = clean_names(names)
    return sorted(names, key=lambda name: (-count_vowels(name), name))


if __name__ == "__main__":
    names1 = ["Goku", "Vegeta", "Piccolo", "Gohan"]
    names2 = ["Edward", "Alphonse", "Roy", "Winry"]
    names3 = ["John", 123, "Doe"]

    sorted_names1 = sort_names(names1)
    sorted_names2 = sort_names(names2)
    sorted_names3 = sort_names(names3)

    # Expected results based on the number of vowels and alphabetical order
    expected_sorted_names1 = ["Piccolo", "Vegeta", "Gohan", "Goku"]
    expected_sorted_names2 = ["Alphonse", "Edward", "Roy", "Winry"]
    expected_sorted_names3 = ["Doe", "John"]

    # Verify if the function's output matches the expected results
    assert sorted_names1 == expected_sorted_names1, f"Expected {expected_sorted_names1}, but got {sorted_names1}"
    print(sorted_names1)  # Output: ["Piccolo", "Vegeta", "Gohan", "Goku"]
    assert sorted_names2 == expected_sorted_names2, f"Expected {expected_sorted_names2}, but got {sorted_names2}"
    print(sorted_names2)  # Output: ["Alphonse", "Edward", "Roy", "Winry"]
    assert sorted_names3 == expected_sorted_names3, f"Expected {expected_sorted_names3}, but got {sorted_names3}"
    print(sorted_names3)  # Output: ["Doe", "John"]

```