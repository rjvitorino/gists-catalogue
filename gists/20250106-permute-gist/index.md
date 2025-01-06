# 20250106-permute-gist

**Gist file**: [https://gist.github.com/rjvitorino/293230bb5af9e418ed1710b9c698e586](https://gist.github.com/rjvitorino/293230bb5af9e418ed1710b9c698e586)

**Description**: Cassidy's interview question of the week: a function that generates all possible permutations of a given string

## permute.py

```Python
from typing import List
from itertools import permutations


def permute(text: str) -> List[str]:
    """
    Generate all unique permutations of the input string.

    Uses Python's built-in itertools.permutations for efficient generation
    of all possible arrangements of characters. Duplicate permutations
    (from repeated characters) are removed.

    Args:
        text: The string to generate permutations for

    Returns:
        List of all unique permutations of the input string

    Examples:
        >>> permute('abc')
        ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
        >>> permute('ab')
        ['ab', 'ba']
        >>> permute('a')
        ['a']
        >>> permute('aa')
        ['aa']
        >>> permute('')
        []
    """
    if not text:
        return []

    return sorted(set("".join(p) for p in permutations(text)))


def main():
    """Validate the permute function with test cases."""
    # Test empty string
    assert permute("") == [], "Empty string should return empty list"

    # Test single character
    assert permute("a") == ["a"], "Single character should return list with one element"

    # Test two characters
    assert permute("ab") == [
        "ab",
        "ba",
    ], "Two characters should return two permutations"

    # Test three characters
    assert permute("abc") == [
        "abc",
        "acb",
        "bac",
        "bca",
        "cab",
        "cba",
    ], "Three characters should return six permutations"

    # Test with repeated characters
    assert permute("aa") == [
        "aa"
    ], "Repeated characters should return unique permutations only"

    print("All checks passed!")


if __name__ == "__main__":
    main()

```