# 20250311-piano_largest_interval-gist

**Gist file**: [https://gist.github.com/rjvitorino/f6d034793e748887f3e066468b04f3c0](https://gist.github.com/rjvitorino/f6d034793e748887f3e066468b04f3c0)

**Description**: Cassidy's interview question of the week: a function that takes a list of piano keys played in sequence and returns the largest interval (in semitones) between any two consecutive keys.

## piano_largest_interval.py

```Python
"""
Finds the largest interval in semitones between consecutive piano notes.
Supports both a standard library implementation and an optimized version
using the `mido` library (if installed).

USAGE:
    - If `mido` is installed (`pip install mido` or `uv pip install mido`), it will use it automatically.
    - If `mido` is not available, it falls back to a pure Python implementation.
"""

import itertools
from typing import Iterable, Iterator, List, Tuple

# Try to import `mido` for MIDI note conversion. If unavailable, use a manual approach.
try:
    from mido import note_to_midi

    def get_semitone_index(note: str) -> int:
        """
        Convert a piano note to its semitone index using `mido`.

        Args:
            note: Piano note in format like 'C4'

        Returns:
            Semitone index where A0 = 0
        """
        return note_to_midi(note) - 21  # MIDI note 21 corresponds to A0

except ImportError:
    # Standard library fallback
    NOTE_OFFSETS = {
        "A": 0,
        "A#": 1,
        "Bb": 1,
        "B": 2,
        "C": 3,
        "C#": 4,
        "Db": 4,
        "D": 5,
        "D#": 6,
        "Eb": 6,
        "E": 7,
        "F": 8,
        "F#": 9,
        "Gb": 9,
        "G": 10,
        "G#": 11,
        "Ab": 11,
    }

    def get_semitone_index(note: str) -> int:
        """
        Convert a piano note to its semitone index using a pure Python approach.

        Args:
            note: Piano note in format like 'C4'

        Returns:
            Semitone index where A0 = 0

        Raises:
            ValueError: If note format is invalid
        """
        for index, char in enumerate(note):
            if char.isdigit():  # Find where the octave starts
                note_name = note[:index]
                octave = int(note[index:])
                break
        else:
            raise ValueError(f"Invalid note format: {note}")

        base_offset = NOTE_OFFSETS[note_name]

        # Adjust octave for notes before C (A and B need to be in previous octave)
        if note_name in ["A", "A#", "Bb", "B"]:
            octave += 1

        # Calculate total semitones from A0
        return base_offset + ((octave - 1) * 12)


def pairwise(iterable: Iterable[int]) -> Iterator[Tuple[int, int]]:
    """
    Return consecutive pairs from an iterable.

    Args:
        iterable: Input sequence

    Returns:
        Iterator yielding pairs like (a, b), (b, c), (c, d), ...
    """
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def find_largest_interval(notes: List[str]) -> int:
    """
    Find the largest interval in semitones between consecutive piano notes.

    Args:
        notes: List of piano notes in format like 'C4'

    Returns:
        Largest interval in semitones between any consecutive notes
    """
    semitone_values = list(map(get_semitone_index, notes))
    intervals = [abs(b - a) for a, b in pairwise(semitone_values)]
    return max(intervals)


if __name__ == "__main__":
    test_cases = [
        # Example test cases
        (["A0", "C1", "G1", "C2"], 7),
        (["C4", "G4", "C5", "G3"], 17),
        (["E2", "C3", "G3", "C8"], 53),
        # Chromatic sequences
        (["C4", "C#4", "D4", "D#4"], 1),  # All intervals are 1 semitone
        (["C4", "D4", "E4", "F4"], 2),  # All intervals are 2 semitones
        # Octave jumps
        (["C4", "C5", "C6", "C7"], 12),  # All intervals are 1 octave
        (["A0", "A1", "A2", "A3"], 12),  # All intervals are 1 octave
        # Mixed intervals
        (
            ["C4", "E4", "G4", "C5"],
            5,
        ),  # Major third (4), minor third (3), perfect fourth (5)
        (
            ["C4", "F4", "B4", "C5"],
            6,
        ),  # Perfect fourth (5), augmented fourth (6), minor second (1)
        # Extreme ranges
        (["A0", "C8"], 87),  # Largest possible interval on piano
        (["C1", "G1", "C2", "G2"], 7),  # Repeating pattern of perfect fifths
        # Accidentals
        (["C4", "F#4", "B4", "C5"], 6),  # Including sharp notes
        (["C4", "Eb4", "Ab4", "C5"], 5),  # Including flat notes
    ]

    for notes, expected in test_cases:
        assert find_largest_interval(notes) == expected

    print("All tests passed!")

```