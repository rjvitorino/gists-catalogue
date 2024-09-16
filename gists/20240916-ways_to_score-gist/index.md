# 20240916-ways_to_score-gist

**Gist file**: [https://gist.github.com/rjvitorino/8d5ece780024c66c6d434e48e1615a67](https://gist.github.com/rjvitorino/8d5ece780024c66c6d434e48e1615a67)

**Description**: Cassidy's interview question of the week: a function to determine the number of unique ways an American Football team can achieve exactly n points 

## ways_to_score.py

```Python
def ways_to_score(total_points: int) -> int:
    """
    Calculate the number of unique ways in American Football 🏈 to score exactly total_points
    using combinations of touchdowns (6 points), field goals (3 points), and safeties (2 points).

    :param total_points: An integer representing the total points to score.
    :return: The number of unique ways to score exactly total_points.
    """

    # ways[i] will hold the number of ways to score exactly i points.
    ways = [0] * (total_points + 1)

    # There is exactly one way to score 0 points: by not scoring at all.
    ways[0] = 1

    # Possible scores: touchdowns (6), field goals (3), safeties (2)
    score_options = [6, 3, 2]

    # Fill the ways array by calculating the number of ways to achieve each score.
    for score in score_options:
        for points in range(score, total_points + 1):
            ways[points] += ways[points - score]

    return ways[total_points]


# 5 points: Only 1 way (1 field goal + 1 safety)
assert ways_to_score(5) == 1, "Test case for total_points=5 failed"

# 7 points: Only 1 way (1 field goal + 2 safeties)
assert ways_to_score(7) == 1, "Test case for total_points=7 failed"

# 9 points: 3 ways (3 field goals OR 1 touchdown + 1 field goal OR 1 field goal + 3 safeties)
assert ways_to_score(9) == 3, "Test case for total_points=9 failed"

# 10 points: 3 ways (1 touchdown + 2 safeties OR 2 field goals + 2 safeties OR 5 safeties)
assert ways_to_score(10) == 3, "Test case for total_points=10 failed"

# 11 points: 3 ways (1 touchdown + 1 field goal + 1 safety OR 3 field goals + 1 safety OR 4 safeties + 1 field goal)
assert ways_to_score(11) == 3, "Test case for total_points=11 failed"

# 12 points: 6 ways (2 touchdowns OR 1 touchdown + 2 field goals OR 1 touchdown + 3 safeties OR 4 field goals OR 2 field goals + 3 safeties OR 6 safeties)
assert ways_to_score(12) == 6, "Test case for total_points=12 failed"

# 14 points: 6 ways (2 touchdowns + 1 safety OR 1 touchdown + 2 field goals + 1 safety OR 1 touchdown + 4 safeties OR 4 field goals + 1 safety OR 2 field goals + 4 safeties OR 7 safeties)
assert ways_to_score(14) == 6, "Test case for total_points=14 failed"

# 20 points: 10 ways (3 touchdowns + 1 safety OR 2 touchdowns + 2 field goals + 1 safety OR 2 touchdowns + 4 safeties OR 1 touchdown + 4 field goals + 1 safety OR 1 touchdown + 2 field goals + 4 safeties OR 1 touchdown + 7 safeties OR 6 field goals + 1 safety OR 4 field goals + 4 safeties OR 2 field goals + 7 safeties OR 10 safeties)
assert ways_to_score(20) == 10, "Test case for total_points=20 failed"

print("All test cases passed!")

```