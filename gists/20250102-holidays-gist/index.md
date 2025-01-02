# 20250102-holidays-gist

**Gist file**: [https://gist.github.com/rjvitorino/4a8356707be032b82fa419ca37b5f283](https://gist.github.com/rjvitorino/4a8356707be032b82fa419ca37b5f283)

**Description**: Cassidy's interview question of the week: given a year, a script that determines weekdays and dates for US holidays (New Year's, Easter, Memorial Day, Independence Day, Thanksgiving, Christmas)

## holidays.py

```Python
from datetime import date, timedelta
from enum import Enum
from dataclasses import dataclass
from typing import Optional

WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


@dataclass
class HolidayInfo:
    """Information about a holiday."""

    name: str
    month: int
    day: Optional[int] = None
    weekday: Optional[int] = None  # 0=Monday, 6=Sunday
    week_of_month: Optional[int] = None  # 1=first, -1=last
    fixed_weekday: Optional[str] = None  # Holidays always falling on the same weekday


class Holiday(Enum):
    """Enumeration of supported holidays with their date information."""

    NEW_YEARS_DAY = HolidayInfo("New Year's Day", month=1, day=1)
    INDEPENDENCE_DAY = HolidayInfo("Independence Day", month=7, day=4)
    CHRISTMAS_DAY = HolidayInfo("Christmas Day", month=12, day=25)
    THANKSGIVING = HolidayInfo(
        "Thanksgiving Day", month=11, week_of_month=4, fixed_weekday="Thursday"
    )  # 4th Thursday of November
    MEMORIAL_DAY = HolidayInfo(
        "Memorial Day", month=5, weekday=0, week_of_month=-1
    )  # Last Monday of May
    EASTER = HolidayInfo(
        "Easter Sunday", month=0, day=0
    )  # Special case, requires calculation


class HolidayCalculator:
    """Calculator for determining dates and weekdays of various holidays."""

    def get_holiday_date(self, holiday: Holiday, year: int) -> date:
        """Get the date for a specific holiday in a given year."""
        info = holiday.value

        # Special case for Easter
        if holiday == Holiday.EASTER:
            return self._calculate_easter(year)

        if info.day:  # Fixed date holiday
            return date(year, info.month, info.day)

        # Convert fixed_weekday to weekday number if specified
        weekday = (
            WEEKDAYS.index(info.fixed_weekday) if info.fixed_weekday else info.weekday
        )
        if weekday is not None and info.week_of_month is not None:
            return self._get_weekday_based_date(
                year, info.month, weekday, info.week_of_month
            )

        raise ValueError(f"Unable to calculate date for {holiday.name}")

    def get_holiday_weekday(self, holiday: Holiday, year: int) -> str:
        """Get the weekday name for a specific holiday in a given year."""
        info = holiday.value
        if info.fixed_weekday:
            return info.fixed_weekday
        return WEEKDAYS[self.get_holiday_date(holiday, year).weekday()]

    @staticmethod
    def _get_weekday_based_date(
        year: int, month: int, weekday: int, week_of_month: int
    ) -> date:
        """Calculate date for holidays based on weekday and week of month."""
        first_day = date(year, month, 1)

        if week_of_month == -1:  # Last occurrence
            last_day = (
                date(year, month + 1, 1) if month < 12 else date(year + 1, 1, 1)
            ) - timedelta(days=1)
            day = last_day
            while day.weekday() != weekday:
                day -= timedelta(days=1)
            return day

        # Find first occurrence of weekday
        day = first_day + timedelta(days=(weekday - first_day.weekday() + 7) % 7)
        # Add weeks as needed
        return day + timedelta(weeks=week_of_month - 1)

    def _calculate_easter(self, year: int) -> date:
        """Calculate Easter Sunday using Butcher's Algorithm.

        This algorithm calculates Easter Sunday's date for any year in the Gregorian calendar.
        Easter falls on the first Sunday following the first ecclesiastical full moon
        that occurs on or after March 21.
        """
        golden_year = year % 19  # Position in the 19-year Metonic cycle
        century = year // 100
        year_in_century = year % 100

        # Calculate corrections
        leap_years = century // 4  # Number of leap years
        non_leap = century % 4
        lunar_correction = (century + 8) // 25
        solar_correction = (century - lunar_correction + 1) // 3

        # Calculate moon phase
        moon_phase = (
            19 * golden_year + century - leap_years - solar_correction + 15
        ) % 30

        # Calculate Sunday date
        century_leap_years = year_in_century // 4
        sunday_offset = (
            32
            + 2 * non_leap
            + 2 * century_leap_years
            - moon_phase
            - (year_in_century % 4)
        ) % 7

        # Calculate Easter date
        lunar_offset = (golden_year + 11 * moon_phase + 22 * sunday_offset) // 451

        # Final date calculation
        month = (moon_phase + sunday_offset - 7 * lunar_offset + 114) // 31
        day = ((moon_phase + sunday_offset - 7 * lunar_offset + 114) % 31) + 1

        return date(year, month, day)


def get_holiday_weekday(holiday: Holiday, year: int) -> str:
    """Get the weekday name for any holiday in a given year."""
    return HolidayCalculator().get_holiday_weekday(holiday, year)


def get_holiday_date(holiday: Holiday, year: int) -> str:
    """Get the ISO formatted date for any holiday in a given year."""
    return HolidayCalculator().get_holiday_date(holiday, year).isoformat()


def new_years_day(year: int) -> str:
    """Get the weekday name for New Year's Day of the given year.

    This is an example of how to create a simple, specific holiday function
    while leveraging the more flexible underlying implementation.
    """
    return get_holiday_weekday(Holiday.NEW_YEARS_DAY, year)


def main():
    # Original requirement test
    assert new_years_day(2024) == "Monday"
    assert new_years_day(2025) == "Wednesday"

    # More comprehensive tests
    assert get_holiday_weekday(Holiday.NEW_YEARS_DAY, 2024) == "Monday"
    assert get_holiday_weekday(Holiday.CHRISTMAS_DAY, 2024) == "Wednesday"
    assert get_holiday_weekday(Holiday.INDEPENDENCE_DAY, 2024) == "Thursday"
    assert get_holiday_date(Holiday.MEMORIAL_DAY, 2024) == "2024-05-27"
    assert get_holiday_date(Holiday.THANKSGIVING, 2024) == "2024-11-28"
    assert get_holiday_date(Holiday.EASTER, 2024) == "2024-03-31"

    # Assertions for 2025
    assert get_holiday_weekday(Holiday.NEW_YEARS_DAY, 2025) == "Wednesday"
    assert get_holiday_weekday(Holiday.CHRISTMAS_DAY, 2025) == "Thursday"
    assert get_holiday_weekday(Holiday.INDEPENDENCE_DAY, 2025) == "Friday"
    assert get_holiday_date(Holiday.MEMORIAL_DAY, 2025) == "2025-05-26"
    assert get_holiday_date(Holiday.THANKSGIVING, 2025) == "2025-11-27"
    assert get_holiday_date(Holiday.EASTER, 2025) == "2025-04-20"

    print("All checks passed!")


if __name__ == "__main__":
    main()

```