
from abc import ABC, abstractmethod


# Base class
class Passenger(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_discount(self):
        pass

    @abstractmethod
    def get_type(self):
        pass


# Inheritance
class RegularPassenger(Passenger):
    def get_discount(self):
        return 0.0

    def get_type(self):
        return "Regular"


class StudentPassenger(Passenger):
    def get_discount(self):
        return 0.10

    def get_type(self):
        return "Student"


# Flight class
class Flight:
    def __init__(self, code, airline, source, destination, seats, fare):
        self.code = code
        self.airline = airline
        self.source = source
        self.destination = destination
        self.__available_seats = seats
        self.fare = fare

    @property
    def available_seats(self):
        return self.__available_seats

    def display(self):
        print(
            f"{self.code} | {self.airline} | "
            f"{self.source} to {self.destination} | "
            f"Seats: {self.available_seats} | Fare: Rs.{self.fare}"
        )

    def has_seats(self, count):
        return count <= self.__available_seats

    def reserve_seats(self, count):
        if self.has_seats(count):
            self.__available_seats -= count
            return True
        return False


# Booking class
class Booking:
    def __init__(self, booking_id, flight, passenger, tickets):
        self.booking_id = booking_id
        self.flight = flight
        self.passenger = passenger
        self.tickets = tickets

        self.subtotal = flight.fare * tickets
        self.discount = self.subtotal * passenger.get_discount()
        self.total = self.subtotal - self.discount

    def display_summary(self):
        print("\nBooking confirmed!")
        print("Booking ID:", self.booking_id)
        print("Flight:", self.flight.code)
        print("Route:", self.flight.source, "to", self.flight.destination)
        print("Airline:", self.flight.airline)
        print("Passenger:", self.passenger.name)
        print("Age:", self.passenger.age)
        print("Passenger type:", self.passenger.get_type())
        print("Tickets:", self.tickets)
        print("Base fare per ticket: Rs.", self.flight.fare)
        print("Subtotal: Rs.", self.subtotal)
        print(
            f"Discount ({self.passenger.get_discount() * 100:.0f}%): "
            f"Rs. {self.discount:.2f}"
        )
        print(f"Final amount: Rs. {self.total:.2f}")


# Main system class
class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("PN101", "Kiran Air", "Pune", "Delhi", 20, 4000),
            Flight("MB202", "Sky Air", "Mumbai", "Bengaluru", 25, 3500),
            Flight("PN303", "Kiran Air", "Pune", "Hyderabad", 15, 3000)
        ]
        self.bookings = []
        self.next_booking_id = 1001

    def display_flights(self):
        print("\nAvailable Flights")
        for flight in self.flights:
            flight.display()

    def find_flight(self, code):
        for flight in self.flights:
            if flight.code.lower() == code.lower():
                return flight
        return None

    def validate_details(self, flight, name, age, tickets):
        if flight is None:
            print("Error: Flight code does not exist.")
            return False

        if not name.strip():
            print("Error: Passenger name cannot be blank.")
            return False

        if age <= 0:
            print("Error: Age must be greater than zero.")
            return False

        if tickets <= 0:
            print("Error: Ticket count must be greater than zero.")
            return False

        if not flight.has_seats(tickets):
            print("Booking failed: Not enough seats available.")
            return False

        return True

    def book_flight(self):
        code = input("Enter flight code: ").strip()
        flight = self.find_flight(code)

        name = input("Enter passenger name: ").strip()

        try:
            age = int(input("Enter age: "))
            passenger_type = input(
                "Passenger type (Regular/Student): "
            ).strip().lower()
            tickets = int(input("Enter number of tickets: "))
        except ValueError:
            print("Error: Age and ticket count must be valid integers.")
            return

        if passenger_type == "regular":
            passenger_class = RegularPassenger
        elif passenger_type == "student":
            passenger_class = StudentPassenger
        else:
            print("Error: Choose Regular or Student.")
            return

        if not self.validate_details(flight, name, age, tickets):
            return

        passenger = passenger_class(name, age)

        # Update seats only after validation succeeds
        if flight.reserve_seats(tickets):
            booking = Booking(
                f"BK{self.next_booking_id}",
                flight,
                passenger,
                tickets
            )

            self.bookings.append(booking)
            self.next_booking_id += 1
            booking.display_summary()

    def view_booking(self):
        if not self.bookings:
            print("No confirmed bookings found.")
        else:
            self.bookings[-1].display_summary()

    def run(self):
        print("Welcome to Kiran Air Booking")

        while True:
            print("\n1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.display_flights()
            elif choice == "2":
                self.book_flight()
            elif choice == "3":
                self.view_booking()
            elif choice == "4":
                print("Thank you for using Kiran Air Booking!")
                break
            else:
                print("Invalid choice. Please select 1 to 4.")


# Create object and start application
if __name__ == "__main__":
    system = FlightBookingSystem()
    system.run()
