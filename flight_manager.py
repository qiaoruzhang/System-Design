"""
Title: INF452 Midterm Project
Course Name: INF452 Design Studio V: Coding
Instructor: Dr. Maher Elshakankiri
Student Name: Qiaoru Zhang
Student Number: 1004607758
Date Created: 2021/11/05
Last Updated: 2021/12/13

===== Module Description =====

This module contains the Passenger classes.
"""
from flight import *
# Import another file flight

from ticket import Ticket
# Import another file ticket

from time_in_strings import Time
# Import another file time_in_strings

from passenger import Passenger  # Import another file passenger


class FlightManager:
    # Define a class FlightManager

    """
    A class representing a Flight Manager.
    Each Flight Manager has one instance attributes flight_dictionary for
    the dictionary which store all the flights.The dictionary key is the flight,
    and the values are the flight related information. One instance attributes
    flight_passengers_dictionary for the dictionary to store all the passenger
    on this flight. One instance attributes route_dictionary for the dictionary
    to store all the route for all flight.One instance attributes route_list for
    the list to store all the route for all flight.

    === Public Attributes ===
    flight_dictionary: A dictionary which store all the flight.
    The dictionary key is the flight, and the values are the flight related
    information.
    flight_passengers_dictionary: A dictionary to store all the passenger on
    this flight.
    route_dictionary: A dictionary to store all the route for all flight.
    route_list: A list to store all the route for all flight.

    === Representation Variants ===
    - len(flight_dictionary) >= 0
    - len(flight_passengers_dictionary) >= 0

    === Sample Usage ===
    >>> flight_manager = FlightManager()
    >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
    >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
    >>> helicopter = Helicopter()
    >>> helicopter_capacity = helicopter.get_max_capacity()
    >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
    ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
    ...     helicopter_capacity)
    >>> flight_manager.add_flight(flight_helicopter)
    >>> flight_manager.print_flight_information(flight_helicopter)
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
    >>> passenger_jay = Passenger("Jay Chou","JC123456")
    >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
    >>> flight_manager.update_flight_seat(flight_helicopter,ticket_123)
    >>> flight_manager.print_flight_information(flight_helicopter)
    Flight Number:  AC123
    Origin City:  Montreal
    Destination City:  Toronto
    Departure Time:  2020 / 11 / 18  19:20
    Arrival Time:  2020 / 11 / 19  2:30
    Boarding Gate:  1A
    Flight Type:  Helicopter
    Total Seats Capacity:  2
    Seat Occupancy Rate:  50.0 %
    Current Seat Number Lists:  ['1A', '  ']
    """
    # Define public attributes type
    flight_dictionary: dict
    flight_passengers_dictionary: dict
    route_dictionary: dict
    route_list: list

    def __init__(self) -> None:
        """
        Initialize the flight_dictionary.
        """
        self.flight_dictionary = {}
        # Initialize flight_dictionary to be empty dictionary.

        self.flight_passengers_dictionary = {}
        # Initialize flight_passengers_dictionary to be empty dictionary.

        self.route_dictionary = {}
        # Initialize route_dictionary to be empty dictionary.

        self.route_list = []
        # Initialize route_list to be empty list.

    def add_flight(self, flight: Flight) -> None:
        """
        Add the flight to flight_dictionary.
        >>> flight_manager = FlightManager()
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_manager.add_flight(flight_helicopter)
        >>> flight_manager.get_flight_number(flight_helicopter)
        'AC123'
        """
        if flight not in self.flight_dictionary:
            # check if the given flight in the flight_dictionary or not.

            self.flight_dictionary[flight] \
                = flight.get_flight_information()
            # add the get_flight_information as value to the flight_dictionary.

    def return_flight(self, flight_number: str) -> Flight:
        """
        Return the related flight with the given flight number.
        >>> flight_manager = FlightManager()
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_manager.add_flight(flight_helicopter)
        >>> flight_manager.get_flight_number(flight_helicopter)
        'AC123'
        >>> flight_manager.return_flight('AC123').print_flight_information()
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
        for one_flight in self.flight_dictionary:
            # For each flight in the flight_dictionary.

            if one_flight.get_flight_number() == flight_number:
                # check if the flight number is same with the
                # given flight_number.

                return one_flight
                # if same, return the flight.

    def generate_route(self, flight: Flight) -> None:
        """
        Add the flight route to the route_list.
        >>> flight_manager = FlightManager()
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_manager.add_flight(flight_helicopter)
        >>> flight_manager.get_flight_number(flight_helicopter)
        'AC123'
        >>> flight_manager.generate_route(flight_helicopter)
        >>> print(*flight_manager.route_list)
        ['Montreal -> Toronto']
        """
        route_list = "{} -> {}".format(flight.get_origin_city(),
                                       flight.get_destination_city())
        # Generate the route_list with origin_city and destination_city

        if route_list not in self.route_dictionary:
            # If the route_list is not in the self.route_dictionary

            self.route_dictionary[route_list] = [flight]
            # create a list as the value for the route_list
            # add the route_list to the route_dictionary.

        else:
            # If the route_list is in the self.route_dictionary

            self.route_dictionary[route_list].append(flight)
            # add the route_list to the route_dictionary.

        if [route_list] not in self.route_list:
            # If the route_list is not in the self.route_list

            self.route_list.append([route_list])
            # add the route_list to the route_list.

    def generate_flight(self, selected_route: str) -> list[str]:
        """
        Return all the flight in flight_dictionary with the given route.
        >>> flight_manager = FlightManager()
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_manager.add_flight(flight_helicopter)
        >>> flight_manager.get_flight_number(flight_helicopter)
        'AC123'
        >>> flight_manager.generate_route(flight_helicopter)
        >>> print(*flight_manager.route_list)
        ['Montreal -> Toronto']
        >>> flight_manager.generate_flight('Montreal -> Toronto')
        ['AC123']
        """
        available_flight_list = []
        # Deine a empty list to contain all available flight number.

        if selected_route in self.route_dictionary:
            # if the route is in the route_dictionary

            for one_flight in self.route_dictionary[selected_route]:
                # for each flight in the route_dictionary with the route.

                available_flight_list.append(one_flight.get_flight_number())
                # Add the flight number to the available_flight_list.

        return available_flight_list
        # return the available_flight_list.

    def print_all_flight_list(self, selected_route: str) -> None:
        """
        Print all the flights in flight_dictionary with the given route.
        >>> flight_manager = FlightManager()
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_manager.add_flight(flight_helicopter)
        >>> flight_manager.get_flight_number(flight_helicopter)
        'AC123'
        >>> flight_manager.generate_route(flight_helicopter)
        >>> print(*flight_manager.route_list)
        ['Montreal -> Toronto']
        >>> flight_manager.print_all_flight_list('Montreal -> Toronto')
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
        <BLANKLINE>
        -----------------------------------------
        <BLANKLINE>
        """
        if selected_route in self.route_dictionary.keys():
            # If the route_list is not in the self.route_dictionary

            for one_flight in self.route_dictionary[selected_route]:
                # for each flight in the route_dictionary with the route.
                if one_flight is not None:
                    one_flight.print_flight_information()
                    print("\n-----------------------------------------\n")
                    # print each flight information.

    def add_passenger(self, flight: Flight, passenger: Passenger,
                      ticket: Ticket) -> None:
        """
        Add the passenger to flight.
        >>> flight_manager = FlightManager()
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_manager.add_flight(flight_helicopter)
        >>> flight_manager.get_flight_number(flight_helicopter)
        'AC123'
        """
        if flight in self.flight_dictionary:
            # check if the given flight in the flight_dictionary or not.

            flight_number = flight.get_flight_number()
            # get the flight number

            if flight_number not in self.flight_passengers_dictionary:
                # if the given flight_number not in the
                # flight_passengers_dictionary

                self.flight_passengers_dictionary[flight_number] = {}
                # create a empty dictionary as value.

                self.flight_passengers_dictionary[flight_number][flight] \
                    = flight.get_flight_information()
                # add the flight information to the
                # flight_passengers_dictionary.

            if passenger not in \
                    self.flight_passengers_dictionary[flight_number]:
                # if the given passenger not in the
                # flight_passengers_dictionary

                self.flight_passengers_dictionary[flight_number][passenger] \
                    = passenger.get_passenger_information()
                # add the passenger information to the
                # flight_passengers_dictionary.

            if ticket not in self.flight_passengers_dictionary[flight_number]:
                # if the given ticket not in the
                # flight_passengers_dictionary

                if ticket.flight.get_flight_number() == flight_number:
                    # if the ticket flight_number is same with the given
                    # flight number

                    self.flight_passengers_dictionary[flight_number][ticket] \
                        = ticket.get_ticket_information_dictionary()
                    # add the ticket information to the
                    # flight_passengers_dictionary.

    def update_flight_seat(self, flight: Flight, ticket: Ticket) -> None:
        """
        update the flight seat.
        >>> flight_manager = FlightManager()
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_manager.add_flight(flight_helicopter)
        >>> flight_manager.print_flight_current_seat_lists(flight_helicopter)
        ['1A', '2B']
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> flight_manager.update_flight_seat(flight_helicopter,ticket_123)
        >>> flight_manager.print_flight_current_seat_lists(flight_helicopter)
        ['1A', '  ']
        """
        if flight in self.flight_dictionary:
            # check if the given flight in the flight_dictionary or not.

            flight.update_flight_seat(ticket.seat_number)
            # update the flight seat.

        else:
            print("This flight is not in system.")

    def cancel_flight_seat(self, flight: Flight, ticket: Ticket) -> None:
        """
        cancel the flight ticket.
        >>> flight_manager = FlightManager()
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_manager.add_flight(flight_helicopter)
        >>> flight_manager.print_flight_current_seat_lists(flight_helicopter)
        ['1A', '2B']
        >>> passenger_jay = Passenger("Jay Chou","JC123456")
        >>> ticket_123 = Ticket("123","2B",passenger_jay,flight_helicopter)
        >>> flight_manager.update_flight_seat(flight_helicopter,ticket_123)
        >>> flight_manager.print_flight_current_seat_lists(flight_helicopter)
        ['1A', '  ']
        >>> flight_manager.cancel_flight_seat(flight_helicopter,ticket_123)
        >>> flight_manager.print_flight_current_seat_lists(flight_helicopter)
        ['1A', '2B']
        """
        if flight in self.flight_dictionary:
            # check if the given flight in the flight_dictionary or not.

            if ticket.get_ticket_check_in_status() is False:

                flight.cancel_flight_seat(ticket.seat_number)
                # cancel the flight seat.
            else:
                print("This Ticket is been checked in and "
                      "no longer could not be cancelled.")
        else:
            print("This flight is not in system.")

    def get_flight_number(self, flight: Flight) -> str:
        """
        Return the flight number in string format.
        >>> flight_manager = FlightManager()
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_manager.add_flight(flight_helicopter)
        >>> flight_manager.get_flight_number(flight_helicopter)
        'AC123'
        """
        if flight in self.flight_dictionary:
            # check if the given flight in the flight_dictionary or not.

            return flight.get_flight_number()
            # Return the flight number in string format.

        else:
            print("This flight is not in system.")

    def print_flight_current_seat_lists(self, flight: Flight) -> list[str]:
        """
        Return the current seat lists for this flight.
        >>> flight_manager = FlightManager()
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_manager.add_flight(flight_helicopter)
        >>> flight_manager.print_flight_current_seat_lists(flight_helicopter)
        ['1A', '2B']
        """
        if flight in self.flight_dictionary:
            # check if the given flight in the flight_dictionary or not.

            return flight.get_current_seat_number_lists()
            # Return the current_seat_number_lists.
        else:
            print("This flight is not in system.")

    def print_flight_information(self, flight: Flight) -> None:
        """
        print all flight related information about this flight.
        >>> flight_manager = FlightManager()
        >>> ac123departure_time = Time(2020,11,18,19,20).time_in_string()
        >>> ac123arrival_time = Time(2020,11,19,2,30).time_in_string()
        >>> helicopter = Helicopter()
        >>> helicopter_capacity = helicopter.get_max_capacity()
        >>> flight_helicopter = Flight("AC123","Montreal","Toronto",
        ...     ac123departure_time,ac123arrival_time,"1A",helicopter,
        ...     helicopter_capacity)
        >>> flight_manager.add_flight(flight_helicopter)
        >>> flight_manager.print_flight_information(flight_helicopter)
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
        if flight in self.flight_dictionary:
            # check if the given flight in the flight_dictionary or not.

            flight.print_flight_information()
            # Return the flight_information

        else:
            print("This flight is not in system.")

    def print_current_seats(self, flight: Flight) -> None:
        """
        Return a human-readable string representation of this flight seats.
        """
        if flight in self.flight_dictionary:
            # check if the given flight in the flight_dictionary or not.

            flight.print_current_seats()
            # Return the current_seats

        else:
            print("This flight is not in system.")


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
    flight_manager = FlightManager()
    # Initial a FlightManager

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
                                     "1A", ac1234helicopter,
                                     ac1234helicopter_capacity)
    # Initial a flight.

    flight_manager.add_flight(ac1234flight_helicopter)
    # add the flight to the flight_manager

    print("--------------------------------------------------------------------"
          "------------\n")
    flight_manager.print_flight_information(ac1234flight_helicopter)
    # print the flight information

    passenger_jay = Passenger("Jay Chou", "JC123456")
    # initial a Passenger

    ticket_123 = Ticket("123", "2B", passenger_jay, ac1234flight_helicopter)
    # initial a Ticket

    flight_manager.update_flight_seat(ac1234flight_helicopter, ticket_123)
    # update flight seat

    print("--------------------------------------------------------------------"
          "------------\n")
    print("After add one passenger Jay Chou to the flight.\n")
    flight_manager.print_flight_information(ac1234flight_helicopter)
    # print the flight information

    # Create flights and add then into system.
    # setup helicopter flights
    AC123departure_time = Time(2021, 11, 18, 19, 20).time_in_string()
    # Define the departure_time
    AC123arrival_time = Time(2021, 11, 19, 2, 30).time_in_string()
    # Define the arrival_time
    AC123helicopter = Helicopter()
    # initial a helicopter
    AC123helicopter_capacity = AC123helicopter.get_max_capacity()
    # calculate the helicopter capacity
    AC123flight_helicopter = Flight("AC123", "Montreal", "Toronto",
                                    AC123departure_time,
                                    AC123arrival_time, "1A",
                                    AC123helicopter,
                                    AC123helicopter_capacity)
    # Initial a flight.

    # Initial a flight.
    # setup small airliner flights
    SA123departure_time = Time(2021, 11, 18, 19, 20).time_in_string()
    # Define the departure_time
    SA123arrival_time = Time(2021, 11, 19, 2, 30).time_in_string()
    # Define the arrival_time
    SA123small_airliner = SmallAirliner()
    # initial a SmallAirliner
    SA123small_airliner_capacity = SA123small_airliner.get_max_capacity()
    # calculate the SmallAirliner capacity
    SA123flight_small_airliner = Flight("SA123", "Montreal", "Toronto",
                                        SA123departure_time,
                                        SA123arrival_time, "2A",
                                        SA123small_airliner,
                                        SA123small_airliner_capacity)
    # Initial a flight.

    # Initial a flight.
    # setup large airliner flights
    LA123departure_time = Time(2021, 11, 18, 19, 20).time_in_string()
    # Define the departure_time
    LA123arrival_time = Time(2021, 11, 19, 2, 30).time_in_string()
    # Define the arrival_time
    LA123large_airliner = LargeAirliner()
    # initial a LargeAirliner
    LA123large_airliner_capacity = LA123large_airliner.get_max_capacity()
    # calculate the LargeAirliner capacity
    LA123flight_large_airliner = Flight("LA123", "Montreal", "Toronto",
                                        LA123departure_time,
                                        LA123arrival_time, "3A",
                                        LA123large_airliner,
                                        LA123large_airliner_capacity)
    # Initial a flight.

    flight_manager.add_flight(AC123flight_helicopter)
    flight_manager.add_flight(SA123flight_small_airliner)
    flight_manager.add_flight(LA123flight_large_airliner)

    # generate route to the flight_manager
    flight_manager.generate_route(AC123flight_helicopter)
    flight_manager.generate_route(SA123flight_small_airliner)
    flight_manager.generate_route(LA123flight_large_airliner)

    flight_manager.print_all_flight_list('Montreal -> Toronto')
