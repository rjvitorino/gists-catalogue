from typing import Union

try:
    # Attempt to import the 'pint' library. If it is not available, set PINT_AVAILABLE to False.
    # To install 'pint', use the following command: pip install pint
    import pint

    PINT_AVAILABLE = True
except ImportError:
    PINT_AVAILABLE = False

# Define a dictionary to store unit conversion factors and symbols.
# Each entry maps a unit to a tuple containing:
# - the unit symbol for 'pint' (if available)
# - the conversion factor to millimeters
# - the conversion factor to inches
unit_map = {
    "mm": ("millimeter", 1, 0.0393701),
    "cm": ("centimeter", 10, 0.393701),
    "m": ("meter", 1000, 39.3701),
    "in": ("inch", 25.4, 1),
    "ft": ("foot", 304.8, 12),
}


def metric_to_imperial(value_in_mm: float) -> str:
    """
    Convert a value in millimeters to imperial units.

    Parameters:
    value_in_mm (float): The value in millimeters to be converted.

    Returns:
    str: The converted value in feet and inches.
    """
    total_inches = value_in_mm * unit_map["mm"][2]
    feet = int(total_inches // 12)
    inches = total_inches % 12
    return f"{feet}ft {inches:.2f}in"


def imperial_to_metric(value_in_inches: float) -> str:
    """
    Convert a value in inches to metric units.

    Parameters:
    value_in_inches (float): The value in inches to be converted.

    Returns:
    str: The converted value in meters, centimeters, and millimeters.
    """
    total_mm = value_in_inches * unit_map["in"][1]
    meters = int(total_mm // 1000)
    total_mm %= 1000
    centimeters = int(total_mm // 10)
    total_mm %= 10
    return f"{meters}m {centimeters}cm {total_mm:.2f}mm"


def convert_units(value: Union[int, float], unit: str) -> str:
    """
    Convert between metric and imperial units.

    Parameters:
    value (Union[int, float]): The numeric value to be converted.
    unit (str): The unit of the input value ('mm', 'cm', 'm', 'in', 'ft').

    Returns:
    str: The converted value in the target unit system.

    Note:
    This function tries to use the 'pint' library for unit conversion if it is available.
    'pint' provides a robust and flexible way to handle units and their conversions.
    To install 'pint', use the following command:
        pip install pint
    """
    if unit not in unit_map:
        raise ValueError(
            "Unsupported unit. Supported units are 'mm', 'cm', 'm', 'in', 'ft'."
        )

    if PINT_AVAILABLE:
        # If 'pint' is available, use it for conversions
        ureg = pint.UnitRegistry()
        unit_symbol, _, _ = unit_map[unit]

        # Create a quantity using 'pint' with the input value and input unit
        quantity = value * getattr(ureg, unit_symbol)

        if unit in ["mm", "cm", "m"]:
            inches = quantity.to(ureg.inch).magnitude
            return metric_to_imperial(inches * unit_map["in"][1])
        elif unit in ["in", "ft"]:
            mm = quantity.to(ureg.mm).magnitude
            return imperial_to_metric(mm * unit_map["mm"][2])
    else:
        # Get the conversion rates from the unit_map given the input unit
        _, to_mm, to_inch = unit_map[unit]
        # Convert input value to millimeters and inches
        value_in_mm = value * to_mm
        value_in_inches = value * to_inch

        if unit in ["mm", "cm", "m"]:
            return metric_to_imperial(value_in_mm)
        elif unit in ["in", "ft"]:
            return imperial_to_metric(value_in_inches)


# Example usage with assertions and debugging prints

result = convert_units(7, "ft")
print(f"convert_units(7, 'ft') -> {result}")
assert result == "2m 13cm 3.60mm"  # Expected: "2m 13cm 3.60mm"

result = convert_units(44, "cm")
print(f"convert_units(44, 'cm') -> {result}")
assert result == "1ft 5.32in"  # Expected: "1ft 5.32in"

result = convert_units(1000, "mm")
print(f"convert_units(1000, 'mm') -> {result}")
assert result == "3ft 3.37in"  # Expected: "3ft 3.37in"

result = convert_units(1, "m")
print(f"convert_units(1, 'm') -> {result}")
assert result == "3ft 3.37in"  # Expected: "3ft 3.37in"

result = convert_units(12, "in")
print(f"convert_units(12, 'in') -> {result}")
assert result == "0m 30cm 4.80mm"  # Expected: "0m 30cm 4.80mm"

result = convert_units(5.5, "ft")
print(f"convert_units(5.5, 'ft') -> {result}")
assert result == "1m 67cm 6.40mm"  # Expected: "1m 67cm 6.40mm"

result = convert_units(200, "cm")
print(f"convert_units(200, 'cm') -> {result}")
assert result == "6ft 6.74in"  # Expected: "6ft 6.74in"

result = convert_units(0.5, "m")
print(f"convert_units(0.5, 'm') -> {result}")
assert result == "1ft 7.69in"  # Expected: "1ft 7.69in"

result = convert_units(24, "in")
print(f"convert_units(24, 'in') -> {result}")
assert result == "0m 60cm 9.60mm"  # Expected: "0m 60cm 9.60mm"

result = convert_units(3.28, "ft")
print(f"convert_units(3.28, 'ft') -> {result}")
assert result == "0m 99cm 9.74mm"  # Expected: "0m 99cm 9.74mm"

# Edge case examples
result = convert_units(0, "cm")
print(f"convert_units(0, 'cm') -> {result}")
assert result == "0ft 0.00in"  # Expected: "0ft 0.00in"

result = convert_units(0, "in")
print(f"convert_units(0, 'in') -> {result}")
assert result == "0m 0cm 0.00mm"  # Expected: "0m 0cm 0.00mm"

result = convert_units(1000000, "mm")
print(f"convert_units(1000000, 'mm') -> {result}")
assert result == "3280ft 10.10in"  # Expected: "3280ft 10.10in"

result = convert_units(0.01, "cm")
print(f"convert_units(0.01, 'cm') -> {result}")
assert result == "0ft 0.00in"  # Expected: "0ft 0.00in"

print("All assertions passed.")
