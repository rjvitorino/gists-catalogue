# 20241020-generate_circle-gist

**Gist file**: [https://gist.github.com/rjvitorino/042299e90a5e5f2a9dbdc26989d89d1e](https://gist.github.com/rjvitorino/042299e90a5e5f2a9dbdc26989d89d1e)

**Description**: Cassidoo's interview question of the week: a function that generates a valid SVG string for a circle given its radius, center position, and color.

## generate_circle.py

```Python
from xml.sax.saxutils import escape


def generate_circle(radius: int, center: tuple[int, int], color: str) -> str:
    """
    Generates a valid SVG string for a circle.

    Args:
        radius (int): The radius of the circle (must be positive).
        center (tuple[int, int]): The (x, y) center position of the circle.
        color (str): The fill color of the circle.

    Returns:
        str: A valid SVG string if inputs are valid.
    """
    x, y = center  # Unpacking for clarity

    if radius <= 0:
        raise ValueError("Radius must be a positive integer.")

    if any(coord < 0 for coord in (x, y)):
        raise ValueError("Center coordinates must be non-negative integers.")

    if not color.isalpha():
        raise ValueError("Color must be a valid string of alphabetic characters.")

    # Escaping the color string to avoid injection
    color_safe = escape(color)

    # The SVG’s width and height are calculated as twice the sum of the radius
    # and the respective x or y center value to ensure the circle fits in the SVG.
    svg_template = (
        f"<svg width='{(x + radius) * 2}' height='{(y + radius) * 2}'>"
        f"<circle cx='{x}' cy='{y}' r='{radius}' fill='{color_safe}'/>"
        f"</svg>"
    )

    return svg_template


if __name__ == "__main__":
    print(generate_circle(radius=50, center=(100, 100), color="blue"))
    # Output: <svg width='300' height='300'><circle cx='100' cy='100' r='50' fill='blue'/></svg>

    print(generate_circle(radius=30, center=(75, 50), color="red"))
    # Output: <svg width='210' height='160'><circle cx='75' cy='50' r='30' fill='red'/></svg>

    print(generate_circle(radius=20, center=(20, 20), color="green"))
    # Output: <svg width='80' height='80'><circle cx='20' cy='20' r='20' fill='green'/></svg>

    print(generate_circle(radius=10, center=(40, 40), color="yellow"))
    # Output: <svg width='100' height='100'><circle cx='40' cy='40' r='10' fill='yellow'/></svg>

    print(generate_circle(radius=15, center=(30, 60), color="purple"))
    # Output: <svg width='90' height='150'><circle cx='30' cy='60' r='15' fill='purple'/></svg>

    try:
        generate_circle(radius=-10, center=(100, 100), color="blue")
        # Output: Validation Error: Radius must be a positive integer.
    except ValueError as e:
        print(f"Validation Error: {e}")

    try:
        generate_circle(radius=30, center=(-75, 50), color="red")
        # Output: Validation Error: Center coordinates must be non-negative integers.
    except ValueError as e:
        print(f"Validation Error: {e}")

    try:
        generate_circle(radius=25, center=(50, 50), color="red123")
        # Output: Validation Error: Color must be a valid string of alphabetic characters.
    except ValueError as e:
        print(f"Validation Error: {e}")

    try:
        generate_circle(radius=0, center=(50, 50), color="black")
        # Output: Validation Error: Radius must be a positive integer.
    except ValueError as e:
        print(f"Validation Error: {e}")

```