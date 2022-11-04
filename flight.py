"""
Student Name: Qiaoru Zhang
Date Created: 2021/11/05
Last Updated: 2021/12/13

===== Module Description =====

This module contains the Passenger classes.
"""
from typing import Union
# Import Union

from time_in_strings import Time

# Import another file time_in_strings

alphabet_list = ["A", "B", "C", "D", "E", "F"]


# Define an alphabet list


class Helicopter:
    # Define a class Helicopter

    """
    A class representing a helicopter flight.Each helicopter class has
    three private attributes:which are _class_name for the name for this flight
    in string format,_small_airliner_ticket_price for the flight price for
    flight. _small_airliner_max_capacity for the maximum capacity for flight.

    === Private Attributes ===
    _class_name: The name for this flight in string format.
    _helicopter_ticket_price: The flight price for flight.
    _helicopter_max_capacity: The maximum capacity for flight.

    === Representation Variants ===
    - account_balance is a valid float >= 0

    === Sample Usage ===
    >>> helicopter = Helicopter()
    >>> helicopter.get_class_name()
    'Helicopter'
    >>> helicopter.get_ticket_price()
    180.0
    >>> helicopter.get_max_capacity()
    2
    """
    # Define private attributes type
    _helicopter_ticket_price: float
    _helicopter_max_capacity: int
    _class_name: str

    def __init__(self) -> None:
        """
        Initialize the Helicopter Class.
        """
        self._helicopter_ticket_price = 180.0
        # Initialize _helicopter_ticket_price to be 180.0

        self._helicopter_max_capacity = 2
        # Initialize _helicopter_max_capacity to be 2

        self._class_name = "Helicopter"
        # Initialize _class_name to be "Helicopter"

    def get_ticket_price(self) -> float:
        """
        return this flight ticket price in float format.
        >>> helicopter = Helicopter()
        >>> helicopter.get_ticket_price()
        180.0
        """
        return self._helicopter_ticket_price
        # Return the _helicopter_ticket_price in float format.

    def get_max_capacity(self) -> int:
        """
        return this flight max capacity in int format.
        >>> helicopter = Helicopter()
        >>> helicopter.get_max_capacity()
        2
        """
        return self._helicopter_max_capacity
        # Return the _helicopter_max_capacity in float format.

    def get_class_name(self) -> str:
        """
        return this flight name in str format.
        >>> helicopter = Helicopter()
        >>> helicopter.get_class_name()
        'Helicopter'
        """
        return self._class_name
        # Return the _class_name in float format.


class SmallAirliner:
    # Define a class SmallAirliner
    """
    A class representing a Small Airliner flight. Each Small Airliner class has
    three private attributes:which are _class_name for the name for this flight
    in string format,_small_airliner_ticket_price for the flight price for
    flight. _small_airliner_max_capacity for the maximum capacity for flight.

    === Private Attributes ===
    _class_name: The name for this flight in string format.
    _small_airliner_ticket_price: The flight price for flight.
    _small_airliner_max_capacity: The maximum capacity for flight.

    === Representation Variants ===
    - account_balance is a valid float >= 0

    === Sample Usage ===
    >>> small_airliner = SmallAirliner()
    >>> small_airliner.get_class_name()
    'Small Airliner'
    >>> small_airliner.get_ticket_price()
    1200.0
    >>> small_airliner.get_max_capacity()
    12
    """
    # Define private attributes type
    _small_airliner_ticket_price: float
    _small_airliner_max_capacity: int
    _class_name: str

    def __init__(self) -> None:
        """
        Initialize the Small Airliner Class.
        """
        self._small_airliner_ticket_price = 1200.0
        # Initialize _helicopter_ticket_price to be 1200.0

        self._small_airliner_max_capacity = 12
        # Initialize _helicopter_max_capacity to be 12

        self._class_name = "Small Airliner"
        # Initialize _class_name to be "Small Airliner"

    def get_ticket_price(self) -> float:
        """
        return this flight ticket price in float format.
        >>> small_airliner = SmallAirliner()
        >>> small_airliner.get_ticket_price()
        1200.0
        """
        return self._small_airliner_ticket_price
        # Return the _small_airliner_ticket_price in float format.

    def get_max_capacity(self) -> int:
        """
        return this flight max capacity in float format.
        >>> small_airliner = SmallAirliner()
        >>> small_airliner.get_max_capacity()
        12
        """
        return self._small_airliner_max_capacity
        # Return the _small_airliner_max_capacity in float format.

    def get_class_name(self) -> str:
        """
        return this flight name in str format.
        >>> small_airliner = SmallAirliner()
        >>> small_airliner.get_class_name()
        'Small Airliner'
        """
        return self._class_name
        # Return the _class_name in float format.


class LargeAirliner:
    # Define a class LargeAirliner

    """
    A class representing a Large Airliner flight.Each Large Airliner class has
    three private attributes:which are _class_name for the name for this flight
    in string format,_small_airliner_ticket_price for the flight price for
    flight. _small_airliner_max_capacity for the maximum capacity for flight.

    === Private Attributes ===
    _class_name: The name for this flight in string format.
    _helicopter_ticket_price: The flight price for flight.
    _helicopter_max_capacity: The maximum capacity for flight.

    === Representation Variants ===
    - account_balance is a valid float >= 0

    === Sample Usage ===
    >>> large_airliner = LargeAirliner()
    >>> large_airliner.get_class_name()
    'Large Airliner'
    >>> large_airliner.get_ticket_price()
    3200.0
    >>> large_airliner.get_max_capacity()
    18
    """
    # Define private attributes type
    _large_airliner_ticket_price: float
    _large_airliner_max_capacity: int
    _class_name: str

    def __init__(self) -> None:
        """
        Initialize the Large Airliner Class.
        """
        self._large_airliner_ticket_price = 3200.0
        # Initialize _helicopter_ticket_price to be 3200.0

        self._large_airliner_max_capacity = 18
        # Initialize _helicopter_max_capacity to be 18

        self._class_name = "Large Airliner"
        # Initialize _class_name to be "Large Airliner"

    def get_ticket_price(self) -> float:
        """
        return this flight ticket price in float format.
        >>> large_airliner = LargeAirliner()
        >>> large_airliner.get_ticket_price()
        3200.0
        """
        return self._large_airliner_ticket_price
        # Return the _large_airliner_ticket_price in float format.

    def get_max_capacity(self) -> int:
        """
        return this flight max capacity in float format.
        >>> large_airliner = LargeAirliner()
        >>> large_airliner.get_max_capacity()
        18
        """
        return self._large_airliner_max_capacity
        # Return the _large_airliner_max_capacity in float format.

    def get_class_name(self) -> str:
        """
        return this flight name in str format.
        >>> large_airliner = LargeAirliner()
        >>> large_airliner.get_class_name()
        'Large Airliner'
        """
        return self._class_name
        # Return the _class_name in float format.


class Flight:
    # Define a class Flight
    """
    A class representing a flight.
    Each flight has one instance attributes flight_id for the flight ID of this
    flight.One instance attributes origin_city for the he departure city of this
    flight.One instance attributes destination_city for the he destination city
    of this flight.One instance attributes departure_time for the he departure
    time of this flight.One instance attributes arrival_time for the
    departure time of this flight.One instance attributes boarding_gate for the
    boarding gate of this flight.One instance attributes flight_type for the
    flight type of this flight, which are Helicopter, Small airliner and
    Large airliner.One instance attributes total_seats_capacity for the he total
    number of seats of this flight，there are three different flight which
    Helicopter only has two seats,Small airliner has 12 seats, and Large
    airliner has 18 seats.One instance attributes seat_occupancy_rate for the
    rate of how many seats have been booked.One instance attributes
    current_seat_number_lists for the list contains the current available
    seats number.One instance attributes flight_information_dictionary for the
    dictionary to store all flight information.

    === Private Attributes ===
    flight_id: The flight ID of this flight.
    origin_city: The departure city of this flight.
    destination_city: The destination city of this flight.
    flight_type: The flight type of this flight, which are Helicopter,
                 Small airliner and Large airliner.
    total_seats_capacity: The total number of seats of this flight，there
                          are three different flight which Helicopter
                          only has two seats,Small airliner has 30 seats,
                          and Large airliner has 100 seats.
    seat_occupancy_rate: The rate of how many seats have been booked.

    === Public Attributes ===
    departure_time: The departure time of this flight.
    arrival_time: The departure time of this flight.
    boarding_gate: The boarding gate of this flight.
    current_seat_number_lists: A list contains the current available
                               seats number.
    flight_information_dictionary: The dictionary to store all flight
                                    information.

    === Representation Variants ===
    - _total_seats_capacity is a valid int >= 0

    === Sample Usage ===
    >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
    >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
    >>> helicopter = Helicopter()
    >>> helicopter_capacity = helicopter.get_max_capacity()
    >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
    ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
    ...     helicopter_capacity)
    >>> flight_helicopter.get_flight_number()
    'AC123'
    >>> flight_helicopter.get_origin_city()
    'Montreal'
    >>> flight_helicopter.get_destination_city()
    'Toronto'
    >>> flight_helicopter.get_departure_time()
    '2020 / 11 / 18  19:20'
    >>> flight_helicopter.get_arrival_time()
    '2020 / 11 / 19  2:30'
    >>> flight_helicopter.get_boarding_gate()
    '1A'
    >>> flight_helicopter.get_flight_type()
    'Helicopter'
    >>> flight_helicopter.get_total_seats_capacity()
    2
    >>> flight_helicopter.get_current_seat_number_lists()
    ['1A', '2B']
    >>> flight_helicopter.print_flight_information()
    Flight Number:  AC123
    Origin City:  Montreal
    Destination City:  Toronto
    Departure Time:  2020 / 11 / 18  19:20
    Arrival Time:  2020 / 11 / 19  2:30
    Boarding Gate:  1A
    Flight Type:  Helicopter
    Total Seats Capacity:  2
    Seat Occupancy Rate:  0.0 %
    Current Seat Number Lists:  ['1A', '2B']
    """
    # Define private and public attributes type
    _flight_number: str
    _origin_city: str
    _destination_city: str
    departure_time: str
    arrival_time: str
    boarding_gate: str
    _flight_type: Union[Helicopter, SmallAirliner, LargeAirliner]
    _total_seats_capacity: int
    _seat_occupancy_rate: str
    current_seat_number_lists: list
    flight_information_dictionary: dict

    def __init__(self, flight_number: str, origin_city: str,
                 destination_city: str,
                 departure_time: str, arrival_time: str,
                 boarding_gate: str,
                 flight_type: Union[Helicopter, SmallAirliner,
                                    LargeAirliner],
                 total_seats_capacity: int
                 ) -> None:
        """
        Create a new flight with unique <flight_number>,
        <origin_city>, <destination_city>, <departure_time>
        , <arrival_time>, <boarding_gate>, <flight_type>
        , <total_seats_capacity>.

        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> print(flight_helicopter._flight_number)
        AC123
        >>> print(flight_helicopter._origin_city)
        Montreal
        >>> print(flight_helicopter._destination_city)
        Toronto
        >>> print(flight_helicopter.departure_time)
        2020 / 11 / 18  19:20
        >>> print(flight_helicopter.arrival_time)
        2020 / 11 / 19  2:30
        >>> print(flight_helicopter.boarding_gate)
        1A
        >>> print(flight_helicopter._flight_type.get_class_name())
        Helicopter
        >>> print(flight_helicopter._total_seats_capacity)
        2
        >>> print(flight_helicopter.current_seat_number_lists)
        ['1A', '2B']
        """
        self._flight_number = flight_number
        # Initialize _flight_number to be the given flight_number.

        self._origin_city = origin_city
        # Initialize _origin_city to be the given origin_city.

        self._destination_city = destination_city
        # Initialize _destination_city to be the given destination_city.

        self.boarding_gate = boarding_gate
        # Initialize boarding_gate to be the given boarding_gate.

        self._flight_type = flight_type
        # Initialize _flight_type to be the given flight_type.

        self._total_seats_capacity = total_seats_capacity
        # Initialize _flight_type to be the given flight_type.

        self.departure_time = departure_time
        # Initialize departure_time to be the given departure_time.

        self.arrival_time = arrival_time
        # Initialize arrival_time to be the given arrival_time.

        number_list = list(range(1, self._total_seats_capacity + 1))
        # Generate a number list which from 1 to the self._total_seats_capacity.

        self.current_seat_number_lists = []
        # Define a list to contains all the current seat numbers.

        alphabet_list_copy = alphabet_list[:]
        # Aliasing a the alphabet_list defined in the beginning of file.

        if isinstance(self._flight_type, Helicopter):
            # Check if the flight type is Helicopter

            for index in range(len(number_list)):
                # get the index of the number_list in the range of the list
                # length.

                one_seats_number = "{}{}".format(number_list[index],
                                                 alphabet_list_copy[index])
                # Generate the string format of the seat number, which the first
                # string is the number and the second string is the word.

                self.current_seat_number_lists.append(one_seats_number)
                # Add the string format of the seat number to
                # current_seat_number_lists

        else:
            # if the flight type is  SmallAirliner or LargeAirliner.

            for index in range(len(number_list)):
                # get the index of the number_list in the range of the list
                # length.

                alphabet_list_copy.extend(alphabet_list_copy * (
                        self._total_seats_capacity // len(alphabet_list_copy)
                        + 1))
                # Extend the aliased list to be the same length as the
                # self._total_seats_capacity

                one_seats_number = "{}{}".format(number_list[index],
                                                 alphabet_list_copy[index])
                # Generate the string format of the seat number, which the first
                # string is the number and the second string is the word.

                self.current_seat_number_lists.append(one_seats_number)
                # Add the string format of the seat number to
                # current_seat_number_lists

        self._seat_occupancy_rate = "0.0 %"
        # Initialize the _seat_occupancy_rate is 0.0 %.

        self.flight_information_dictionary = {
            "flight_number": self._flight_number,
            "origin_city": self._origin_city,
            "destination_city": self._destination_city,
            "departure_time": self.departure_time,
            "arrival_time": self.arrival_time,
            "boarding_gate": self.boarding_gate,
            "flight_type": self._flight_type,
            "total_seats_capacity": self._total_seats_capacity,
            "seat_occupancy_rate": self._seat_occupancy_rate,
            "current_seat_number_lists": self.current_seat_number_lists
        }
        # Add all the related value and keys to the
        # flight_information_dictionary.

    def get_flight_number(self) -> str:
        """
        The getter function to return the flight's <_flight_number>.
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_helicopter.get_flight_number()
        'AC123'
        """
        return self._flight_number
        # return the flight's <_flight_number>.

    def get_origin_city(self) -> str:
        """
        The getter function to return the flight's <_origin_city>.
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_helicopter.get_origin_city()
        'Montreal'
        """
        return self._origin_city
        # return the flight's <_origin_city>.

    def get_destination_city(self) -> str:
        """
        The getter function to return the flight's <_destination_city>.
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_helicopter.get_destination_city()
        'Toronto'
        """
        return self._destination_city
        # return the flight's <_destination_city>.

    def get_departure_time(self) -> str:
        """
        The getter function to return the flight's <departure_time>.
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_helicopter.get_departure_time()
        '2020 / 11 / 18  19:20'
        """
        return self.departure_time
        # return the flight's <departure_time>.

    def get_arrival_time(self) -> str:
        """
        The getter function to return the flight's <arrival_time>.
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_helicopter.get_arrival_time()
        '2020 / 11 / 19  2:30'
        """
        return self.arrival_time
        # return the flight's <arrival_time>.

    def get_boarding_gate(self) -> str:
        """
        The getter function to return the flight's <boarding_gate>.
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_helicopter.get_boarding_gate()
        '1A'
        """
        return self.boarding_gate
        # return the flight's <boarding_gate>.

    def get_flight_type(self) -> str:
        """
        The getter function to return the flight's <_flight_type> in string
        format.
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_helicopter.get_flight_type()
        'Helicopter'
        """
        return self._flight_type.get_class_name()
        # return the flight's <_flight_type>.

    def get_flight_price(self) -> float:
        """
        The getter function to return the flight's <ticket_price>.
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_helicopter.get_flight_type()
        'Helicopter'
        >>> flight_helicopter.get_flight_price()
        180.0
        """
        return self._flight_type.get_ticket_price()
        # return the flight's <ticket_price>.

    def get_total_seats_capacity(self) -> int:
        """
        The getter function to return the flight's <max_capacity>.
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_helicopter.get_total_seats_capacity()
        2
        """
        return self._flight_type.get_max_capacity()
        # return the flight's <max_capacity>.

    def get_current_seat_number_lists(self) -> list[str]:
        """
        The getter function to return the flight's <current_seat_number_lists>.
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_helicopter.get_current_seat_number_lists()
        ['1A', '2B']
        """
        return self.current_seat_number_lists
        # return the flight's <current_seat_number_lists>.

    def get_flight_mileage(self) -> float:
        """
        The getter function to return the flight's distance.
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_helicopter.get_current_seat_number_lists()
        ['1A', '2B']
        """
        if self.get_origin_city() == "Toronto" and \
                self.get_destination_city() == "Montreal":
            return 554.0
        elif self.get_origin_city() == "Montreal" and \
                self.get_destination_city() == "Toronto":
            return 533.0

    def update_flight_seat(self, seat_number: str) -> None:
        """
        Update the booked seat in this flight with the given string.
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_helicopter.get_current_seat_number_lists()
        ['1A', '2B']
        >>> flight_helicopter.update_flight_seat('2B')
        >>> flight_helicopter.get_current_seat_number_lists()
        ['1A', '  ']
        """
        for seat_index in range(len(self.current_seat_number_lists)):
            # generate the list index between 0 and the length of the
            # current_seat_number_lists

            if self.current_seat_number_lists[seat_index] == seat_number:
                # if the current item in the list with the seat_index has the
                # same string with the given seat_number.

                if len(seat_number) == 2:
                    # if the given seat_number length is 2.

                    self.current_seat_number_lists[seat_index] = '  '
                    # Replace the string to be '  '.

                else:
                    # if the given seat_number length is 3.

                    self.current_seat_number_lists[seat_index] = '   '
                    # Replace the string to be '   '.

        calculate_rate = \
            self.current_seat_number_lists.count('  ') / len(
                self.current_seat_number_lists) * 100
        # calculate how many empty string exit in the list.

        self._seat_occupancy_rate = "{} %".format(calculate_rate)
        # replace the _seat_occupancy_rate to the calculate_rate.

    def cancel_flight_seat(self, seat_number: str) -> None:
        """
        Update the booked seat in this flight.
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_helicopter.get_current_seat_number_lists()
        ['1A', '2B']
        >>> flight_helicopter.update_flight_seat('2B')
        >>> flight_helicopter.get_current_seat_number_lists()
        ['1A', '  ']
        >>> flight_helicopter._seat_occupancy_rate
        '50.0 %'
        >>> flight_helicopter.cancel_flight_seat('2B')
        >>> flight_helicopter.get_current_seat_number_lists()
        ['1A', '2B']
        >>> flight_helicopter._seat_occupancy_rate
        '0.0 %'
        """

        seat_first_char = int(seat_number[:-1])
        # Get the number string of given seat number.

        for seat_index in range(len(self.current_seat_number_lists)):
            # generate the list index between 0 and the length of the
            # current_seat_number_lists

            find_string = self.current_seat_number_lists[seat_index]
            # find the item in the list that with the seat_index.

            if not any(char.isdigit() for char in find_string):
                # check if the find_string is empty string.

                first_char = \
                    int(self.current_seat_number_lists[seat_index - 1][:-1])
                # Find the previous string's number

                if first_char == (seat_first_char - 1):
                    # check if the previous string's number is less than the
                    # the number string of given seat number.

                    self.current_seat_number_lists[seat_index] = seat_number
                    # replace the item in the list with the seat_index to
                    # given seat_number.

        calculate_rate = \
            (self.current_seat_number_lists.count('  ') +
             self.current_seat_number_lists.count('   ')) / len(
                self.current_seat_number_lists) * 100
        # calculate how many empty string exit in the list.

        self._seat_occupancy_rate = "{} %".format(calculate_rate)
        # replace the _seat_occupancy_rate to the calculate_rate.

    def get_flight_information(self) -> dict:
        """
        Return the passenger related information in dictionary format.
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> information_dictionary = flight_helicopter.get_flight_information()
        >>> information_dictionary["flight_number"]
        'AC123'
        """
        return self.flight_information_dictionary
        # return the flight's <flight_information_dictionary>.

    def print_flight_information(self) -> None:
        """
        Return the flight related information.
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_helicopter.print_flight_information()
        Flight Number:  AC123
        Origin City:  Montreal
        Destination City:  Toronto
        Departure Time:  2020 / 11 / 18  19:20
        Arrival Time:  2020 / 11 / 19  2:30
        Boarding Gate:  1A
        Flight Type:  Helicopter
        Total Seats Capacity:  2
        Seat Occupancy Rate:  0.0 %
        Current Seat Number Lists:  ['1A', '2B']
        """
        print('Flight Number: ', self._flight_number)
        print('Origin City: ', self._origin_city)
        print('Destination City: ', self._destination_city)
        print('Departure Time: ', self.departure_time)
        print('Arrival Time: ', self.arrival_time)
        print('Boarding Gate: ', self.boarding_gate)
        print('Flight Type: ', self._flight_type.get_class_name())
        print('Total Seats Capacity: ', self._total_seats_capacity)
        print('Seat Occupancy Rate: ', self._seat_occupancy_rate)
        print('Current Seat Number Lists: ', self.current_seat_number_lists)
        # return the flight's related information.

    def print_current_seats(self) -> None:
        """
        Return a human-readable string representation of this flight seats.
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        """
        if not isinstance(self._flight_type, Helicopter):
            # check if the flight type is Helicopter or not.
            print("--------------------------------------------")
            print("           Flight", self._flight_number, "Seats Table")
            print("--------------------------------------------")
            # Display the seats list table

            print(" ", end=' ')
            for one_letter in alphabet_list:
                # for each letter in alphabet_list

                print("   ", one_letter, end='  ')
                # print the letter

            print(" ", end=' ')
            print("\n--------------------------------------------")

            number_of_rows = self._total_seats_capacity // 6
            # count number of rows for this table

            number_of_columns = 6
            # define number of columns for this table

            # Display the flight seats.
            for one_row_number in range(number_of_rows):
                # for each row number in the row number range

                print(one_row_number + 1, "|", end=' ')
                # print the letter each row number in the row number range

                for one_column_number in range(number_of_columns):
                    # for each column number in the row number range

                    if (
                            one_column_number + one_row_number * number_of_columns + 1) <= 9:
                        # check if the number is less than 9.

                        print("", format(
                            self.current_seat_number_lists[
                                one_column_number + one_row_number * number_of_columns]),
                              end=' || ')
                        # print the item in the current_seat_number_lists with
                        # the number index.

                    else:
                        # check if the number is larger than 9.

                        print(format(
                            self.current_seat_number_lists[
                                one_column_number + one_row_number * number_of_columns]),
                            end=' || ')
                        # print the item in the current_seat_number_lists with
                        # the number index.
                print()

        else:
            print("--------------------------------------------")
            print("           Flight", self._flight_number, "Seats Table")
            print("--------------------------------------------")
            # Display the seats list table
            print(" ", end=' ')
            for one_letter in range(len(alphabet_list)):
                # for each letter in alphabet_list

                if one_letter < 2:
                    # check is the letter is less than 2.

                    print("        ", alphabet_list[one_letter],
                          end='            ')

            print(" ", end=' ')
            print("\n--------------------------------------------")
            number_of_rows = 1
            # define number of row for this table

            number_of_columns = 2
            # define number of column for this table

            # Display the flight seats.
            for one_row_number in range(number_of_rows):
                # for each row number in the row number range

                print(one_row_number + 1, "|", end=' ')
                # print the letter each row number in the row number range

                for one_column_number in range(number_of_columns):
                    # for each column number in the row number range

                    print("     ", format(
                        self.current_seat_number_lists[
                            one_column_number + one_row_number * number_of_columns]),
                          end='         ||   ')
                    # print the item in the current_seat_number_lists with
                    # the number index.

                print()


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

    print('\nTesting helicopter:')
    ac1234departure_time = Time(2020, 11, 18, 19, 20).time_in_string()
    # Define the departure_time

    ac1234arrival_time = Time(2020, 11, 19, 2, 30).time_in_string()
    # Define the arrival_time

    ac1234helicopter = Helicopter()
    # initial a helicopter

    ac1234helicopter_capacity = ac1234helicopter.get_max_capacity()
    # calculate the helicopter capacity

    ac1234flight_helicopter = Flight("AC123", "Montreal", "Toronto",
                                     ac1234departure_time, ac1234arrival_time,
                                     "1A",
                                     ac1234helicopter,
                                     ac1234helicopter_capacity)
    # Initial a flight.

    ac1234flight_helicopter.get_flight_number()
    # get the flight number.

    ac1234flight_helicopter.get_origin_city()
    # get the flight's origin_city.

    ac1234flight_helicopter.get_destination_city()
    # get the flight's destination_city.

    ac1234flight_helicopter.get_departure_time()
    # get the flight's departure_time.

    ac1234flight_helicopter.get_arrival_time()
    # get the flight's arrival_time.

    ac1234flight_helicopter.get_boarding_gate()
    # get the flight's boarding_gate.

    ac1234flight_helicopter.get_flight_type()
    # get the flight's flight_type.

    ac1234flight_helicopter.get_total_seats_capacity()
    # get the flight's total_seats_capacity.

    ac1234flight_helicopter.get_current_seat_number_lists()
    # get the flight's current_seat_number_lists.

    ac1234flight_helicopter.print_flight_information()
    # get the flight's flight_information.
