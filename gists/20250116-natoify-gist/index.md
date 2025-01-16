# 20250116-natoify-gist

**Gist file**: [https://gist.github.com/rjvitorino/217bca150a775b34c363b873ba915bbb](https://gist.github.com/rjvitorino/217bca150a775b34c363b873ba915bbb)

**Description**: Cassidy's interview question of the week: a translation function for the NATO phonetic alphabet

## natoify.py

```Python
"""
NATO phonetic alphabet converter.

This module converts text into NATO phonetic alphabet
representation, handling special cases like decimal points and quotation marks.
"""

from typing import Dict, List, Optional

# Core NATO phonetic alphabet mapping
NATO_PHONETIC_ALPHABET: Dict[str, str] = {
    # Letters
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliet",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu",
    # Punctuation
    ".": "Stop",
    ",": "Comma",
    "-": "Dash",
    "/": "Slant",
    "(": "Brackets On",
    ")": "Brackets Off",
    ":": "Colon",
    ";": "Semi-colon",
    "!": "Exclamation Mark",
    "?": "Question Mark",
    "'": "Apostrophe",
}

# Number words in order
NUMBER_WORDS = [
    "Zero",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
]

# Add numbers to the NATO phonetic alphabet
NATO_PHONETIC_ALPHABET.update({str(i): word for i, word in enumerate(NUMBER_WORDS)})


def natoify(text: str) -> str:
    """Convert text to NATO phonetic alphabet representation.

    Args:
        text: Input text to convert

    Returns:
        Space-separated NATO phonetic representation

    Examples:
        >>> natoify("SOS")
        'Sierra Oscar Sierra'
        >>> natoify("3.14")
        'Three Decimal One Four'
        >>> natoify('Hello "World"')
        'Hotel Echo Lima Lima Oscar Quote Whiskey Oscar Romeo Lima Delta Unquote'
    """

    def handle_special_cases(char: str, index: int, chars: List[str]) -> Optional[str]:
        """Handle special cases for NATO phonetic alphabet conversion.

        Special cases:
        - Double quotes alternate between "Quote" and "Unquote"
        - Periods between digits become "Decimal"
        """
        if char == '"':
            prev_quotes = chars[:index].count('"')
            return "Quote" if prev_quotes % 2 == 0 else "Unquote"

        if char == "." and _is_decimal_point(index, chars):
            return "Decimal"

        return None

    def _is_decimal_point(index: int, chars: List[str]) -> bool:
        """Check if a period at the given index is a decimal point between digits."""
        return (
            index > 0
            and index < len(chars) - 1
            and chars[index - 1].isdigit()
            and chars[index + 1].isdigit()
        )

    result = []
    chars = list(text)

    for i, char in enumerate(chars):
        # Handle special cases first
        if special := handle_special_cases(char, i, chars):
            result.append(special)
            continue

        # Convert regular characters using NATO alphabet
        if nato_word := NATO_PHONETIC_ALPHABET.get(char.upper()):
            result.append(nato_word)

    return " ".join(result)


def main() -> None:
    """Run test cases to validate the natoify function."""
    # Basic conversion tests
    assert (
        natoify("hello world")
        == "Hotel Echo Lima Lima Oscar Whiskey Oscar Romeo Lima Delta"
    )
    assert (
        natoify("3spooky5me")
        == "Three Sierra Papa Oscar Oscar Kilo Yankee Five Mike Echo"
    )
    assert natoify("") == ""
    assert natoify("A") == "Alpha"
    assert natoify("PyThOn") == "Papa Yankee Tango Hotel Oscar November"

    # Number and special character tests
    assert natoify("123") == "One Two Three"
    assert natoify("3.14") == "Three Decimal One Four"
    assert natoify("Hi!@#") == "Hotel India Exclamation Mark"
    assert (
        natoify('Say "Hello"')
        == "Sierra Alpha Yankee Quote Hotel Echo Lima Lima Oscar Unquote"
    )

    # Multiple word test
    assert natoify("SOS HELP") == "Sierra Oscar Sierra Hotel Echo Lima Papa"

    print("All checks passed!")


if __name__ == "__main__":
    main()

```