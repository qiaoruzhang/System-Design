"""
Title: INF452 Midterm Project
Course Name: INF452 Design Studio V: Coding
Instructor: Dr. Maher Elshakankiri
Student Name: Qiaoru Zhang
Student Number: 1004607758
Date Created: 2021/11/05
Last Updated: 2021/11/07

===== Module Description =====

This module contains the Passenger classes.
"""


class Time:
    # Define a class Time
    """
    A class representing a Time.

    === Private Attributes ===
    _year: the year of the time.
    _month: the month of the time.
    _day: the day of the time.
    _hour: the hour of the time.
    _second: the second of the time.

    === Representation Variants ===
    - _year is a valid int >= 0
    - _month is a valid int >= 0
    - _day is a valid int >= 0
    - _hour is a valid int >= 0
    - _second is a valid int >= 0

    === Sample Usage ===
    >>> time = Time(2020,11,18,19,20)
    >>> time.time_in_string()
    '2020 / 11 / 18  19:20'
    """
    # Define public attributes type
    _year: int
    _month: int
    _day: int
    _hour: int
    _second: int

    def __init__(self, year_number: int, month_number: int, day_number: int,
                 hour_number: int, second_number: int) -> None:
        """
        Create a new time with unique <year_number>,
        <month_number>, <day_number>, <hour_number>, <second_number>.
        >>> time = Time(2020,11,18,19,20)
        """
        self._year = year_number
        # Initialize _year to be the given year_number.

        self._month = month_number
        # Initialize _month to be the given month_number.

        self._day = day_number
        # Initialize _day to be the given day_number.

        self._hour = hour_number
        # Initialize _hour to be the given hour_number.

        self._second = second_number
        # Initialize _second to be the given second_number.

    def time_in_string(self) -> str:
        """
        >>> time = Time(2020,11,18,19,20)
        >>> time.time_in_string()
        '2020 / 11 / 18  19:20'
        """
        return "{} / {} / {}  {}:{}".format(self._year,
                                            self._month,
                                            self._day,
                                            self._hour,
                                            self._second)
        # Get the time in string format.


if __name__ == "__main__":

    import doctest

    doctest.testmod()

    print("Title: INF452 Midterm Project")
    print("Course Name: INF452 Design Studio V: Coding")
    print("Instructor: Dr. Maher Elshakankiri")
    print("Student Name: Qiaoru Zhang")
    print("Student Number: 1004607758")
    print("--------------------------------------------------------------------"
          "------------\n")

    time = Time(2020, 11, 18, 19, 20)
    # Initialize a new Time.

    time.time_in_string()
    # Get the time in string format.
