from typing import List

class FlowerPlanter:
    def __init__(self, garden: List[int]) -> None:
        """Initialise the garden with padded zeros at both ends."""
        self.garden = [0] + garden + [0]

    def has_enough_spaces(self, k: int) -> bool:
        """Check if there are enough spaces to plant k flowers without adjacent flowers."""
        if k == 0:  # Early return
            return True

        available_spots, garden_length = 0, len(self.garden)

        for space in range(1, garden_length - 1):
            is_current_space_empty = self.garden[space] == 0
            is_previous_space_empty = self.garden[space - 1] == 0
            is_next_space_empty = self.garden[space + 1] == 0

            if is_current_space_empty and is_previous_space_empty and is_next_space_empty:
                available_spots += 1
                # Place a flower to avoid adjacent placements
                self.garden[space] = 1
                if available_spots >= k:  # Early exit
                    return True
        
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
