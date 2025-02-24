# 20250224-get_note_names-gist

**Gist file**: [https://gist.github.com/rjvitorino/a7cf16bf2ffc9b4bc3dd0fad1232f9b0](https://gist.github.com/rjvitorino/a7cf16bf2ffc9b4bc3dd0fad1232f9b0)

**Description**: Cassidy's interview question of the week: a function that, given a list of frequencies (in Hz), determines the closest musical note for each frequency based on the A440 pitch standard, indicating if the note is flat or sharp

## get_note_names.py

```Python
import math
from typing import List


def get_note_names(frequencies: List[float]) -> List[str]:
    """Convert frequencies to musical note names using A440 pitch standard.

    Takes a list of frequencies in Hz and returns their corresponding musical notes,
    indicating if they are sharp or flat relative to the standard pitch.

    Args:
        frequencies (List[float]): List of frequencies in Hz (e.g., [440.0, 466.16])

    Returns:
        List[str]: List of note descriptions with pitch accuracy indicators
                  Format: "This is [a/an] [NOTE][, but it's [sharp/flat]]"

    Examples:
        >>> get_note_names([440])
        ["This is an A"]
        >>> get_note_names([490])
        ["This is a B, but it's flat"]
        >>> get_note_names([440, 880, 1760])
        ["This is an A", "This is an A", "This is an A"]
    """

    # Constants for A440 tuning
    A4_FREQ: float = 440.0  # Standard concert pitch: A above middle C (A4) in Hz
    SEMITONES_PER_OCTAVE: int = 12  # Number of semitones in Western music octave
    PITCH_TOLERANCE: float = (
        0.01  # Acceptable frequency deviation (1 cent) before marking as sharp/flat
    )

    # Use tuple for immutable sequence
    NOTES: tuple[str, ...] = (
        "A",
        "A#",
        "B",
        "C",
        "C#",
        "D",
        "D#",
        "E",
        "F",
        "F#",
        "G",
        "G#",
    )
    VOWEL_NOTES: set[str] = {"A", "A#", "E", "F", "F#"}  # Notes that need "an"

    result: List[str] = []

    for freq in frequencies:
        # Calculate semitones from A4 (440 Hz) using logarithmic scale
        semitones: float = SEMITONES_PER_OCTAVE * math.log2(freq / A4_FREQ)
        rounded_semitones: int = round(semitones)

        # Get note name and expected frequency
        note: str = NOTES[rounded_semitones % SEMITONES_PER_OCTAVE]
        expected_freq: float = A4_FREQ * 2 ** (rounded_semitones / SEMITONES_PER_OCTAVE)

        # Determine pitch accuracy and add article
        article: str = "an" if note in VOWEL_NOTES else "a"
        base_text: str = f"This is {article} {note}"

        if abs(freq - expected_freq) < PITCH_TOLERANCE:
            result.append(base_text)  # Accurate note
        else:
            accuracy: str = "sharp" if freq > expected_freq else "flat"
            result.append(f"{base_text}, but it's {accuracy}")

    return result


if __name__ == "__main__":
    # Example fests
    assert get_note_names([440, 490, 524, 293.66]) == [
        "This is an A",
        "This is a B, but it's flat",
        "This is a C, but it's sharp",
        "This is a D",
    ]  # A4, B4 (flat), C5 (sharp), D4 (exact)

    # Test exact frequencies
    assert get_note_names([440]) == ["This is an A"]  # A4 (standard pitch)
    assert get_note_names([880]) == ["This is an A"]  # A5 (one octave up)
    assert get_note_names([220]) == ["This is an A"]  # A3 (one octave down)

    # Test sharp/flat detection
    assert get_note_names([490]) == ["This is a B, but it's flat"]  # B4 (flat)
    assert get_note_names([524]) == ["This is a C, but it's sharp"]  # C5 (sharp)
    assert get_note_names([293.66]) == ["This is a D"]  # D4 (exact)

    # Test multiple frequencies at once
    assert get_note_names([440, 880, 1760]) == [
        "This is an A",
        "This is an A",
        "This is an A",
    ]  # A4, A5, A6 (octave doubling)

    # Test vowel-starting notes
    assert get_note_names([466.16]) == ["This is an A#"]  # A#4 (exact)
    assert get_note_names([369.99]) == ["This is an F#"]  # F#4 (exact)
    assert get_note_names([329.63]) == ["This is an E"]  # E4 (exact)
    assert get_note_names([349.23]) == ["This is an F"]  # F4 (exact)

    print("All tests passed!")

```