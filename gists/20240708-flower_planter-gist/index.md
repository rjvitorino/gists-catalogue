# 20240708-flower_planter-gist

**Description**: Cassidoo's interview question of the week: a function that takes an array of integers representing the number of flowers planted in a line, and an integer k representing the number of additional flowers you want to plant. Return whether it's possible to plant all k flowers without planting any two flowers adjacent to each other.

## flower_planter.py

```Python
from typing import List

class FlowerPlanter:
    def __init__(self, garden: List[int]) -> None:
        """Initialise the garden with padded zeros at both ends."""
        self.garden = [0] + garden + [0]

    def has_enough_spaces(self, k: int) -> bool:
        """Check if there are enough spaces to plant k flowers without adjacent flowers."""
        available_spots, garden_length = 0, len(self.garden)

        for space in range(1, garden_length - 1):
            if self.garden[space] == 0 and self.garden[space - 1] == 0 and self.garden[space + 1] == 0:
                available_spots += 1
                # Place a flower to avoid adjacent placements
                self.garden[space] = 1
        
        return available_spots >= k

def can_plant_flowers(garden: List[int], k: int) -> bool:
    """Determine if k flowers can be planted without any two being adjacent.
    
    Args:
        garden (List[int]): The garden array where 1 represents a flower and 0 represents an empty spot.
        k (int): The number of flowers to be planted.
    
    Returns:
        bool: True if k flowers can be planted without adjacent flowers, False otherwise.
    """
    planter = FlowerPlanter(garden)
    return planter.has_enough_spaces(k)

if __name__ == "__main__":
    assert can_plant_flowers([1, 0, 0, 0, 1], 1) is True  # Can plant 1 flower
    assert can_plant_flowers([1, 0, 0, 0, 1], 2) is False  # Cannot plant 2 flowers
    assert can_plant_flowers([0, 0, 0, 0, 0], 3) is True  # Can plant 3 flowers
    assert can_plant_flowers([1, 0, 1, 0, 1], 1) is False  # Cannot plant any flowers
    assert can_plant_flowers([0, 0, 0], 1) is True  # Can plant 1 flower
    assert can_plant_flowers([0, 0, 0], 2) is True  # Can plant 2 flowers
    assert can_plant_flowers([0, 0, 0], 3) is False  # Cannot plant 3 flowers
    print("All tests passed.")

```