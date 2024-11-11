# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from datetime import date
import random
from pydantic import Field
import json
import secrets

bookings = {
    "flights": [], 
    "accommodations": []  ,
    "attractions": [] 
}

emails = []

# apis to send emails
def send_booking_email(email: str, booking_details: dict) -> str:
    """Send an email with full booking details. The booking details must be a dictionary."""
    print(f"Sending email to {email}")
    email_booking = []
    value = {}
    if not isinstance(booking_details, dict ):
        value = booking_details.__dict__
    else:
        value = booking_details
    email_booking.append(value)
    
    message = f"Dear traveller, \n\nWe are happy to confirm your booking. Here are the details: \n\n{json.dumps(obj= value, indent=4)}\n\nHave a great trip!\n\nThe travel team"
    print(f"Email sent to {email} : { message}")
    emails.append(message)
    return f"Email sent to {email}"

# apis to get bookings
def get_bookings() -> dict:
    """Useful for getting bookings."""
    return bookings

# apis to find and book tickets
def find_attractions_tickets(attraction: str, number_of_people:int) -> dict:
    """Find tickets for an attraction for a given number of people."""
    return {
            "attraction": attraction,
            "date": date.today(),
            "price_pp": f"€{random.randrange(10, 50)}",
            "number_of_people": number_of_people
        }
    

def book_attraction_tickets(attraction: str, date: date, number_of_people: int) -> dict:
    """Book tickets for an attraction for a given number of people."""
    attraction_booking = {
        "attraction": attraction,
        "date": date,
        "number_of_people": number_of_people,
        "booking_reference": secrets.SystemRandom().randrange(1000, 9999)
    }

    bookings["attractions"].append(attraction_booking)

    return attraction_booking

# apis to find and book flights
def find_flights(
        origin: str, 
        destination:str, 
        date: date
        ) -> list[dict]:
    """Can find flights on a specific date between a departure and destination."""
    values : list[dict] = []
    for i in range(secrets.SystemRandom().randrange(3, 10)):
        values.append({
            "name": f"Flight {i}",
            "date": date,
            "origin": origin,
            "departure_time": f"{secrets.SystemRandom().randrange(3, 19)}:00",
            "price_pp": f"€{random.randrange(100, 1000)}",
            "destination": destination
        })
    
    return values

def book_flight(
        flight_name: str, 
        origin: str,
        destination: str,
        departure_date: date, 
        passengers: int
        ) -> dict:
    """Can book a flight on a date for any number of passengers. It returns the booking confirmation."""
    flight_booking ={
        "name": flight_name,
        "date": departure_date,
        "passengers": passengers,
        "origin": origin,
        "destination": destination,
        "booking_reference": secrets.SystemRandom().randrange(1000, 9999)
    }

    bookings["flights"].append(flight_booking)

    return flight_booking

# apis to find and book accommodations
def find_accommodations(
        location: str, 
        date: date
        ) -> list[dict]:
    """Can find accommodations for a given location and date."""
    values : list[dict] = []
    for i in range(secrets.SystemRandom().randrange(3, 10)):
        values.append(
            {
                "name": f"Accommodation {i}",
                "location": location,
                "date": date,
                "price_pn": f"€{random.randrange(100, 333)}",
            }
        )
           
    
    return values

def book_accommodation(
        accommodation_name: str, 
        check_in_date: date, 
        nights:int, 
        guests: int
        ) -> dict:
    """Can book accommodation for a group of guests on specific date and number on nights. It returns the booking confirmation including the booking reference."""
    accommodation_booking = {
        "name": accommodation_name,
        "date": check_in_date,
        "nights": nights,
        "guests": guests,
        "booking_reference": secrets.SystemRandom().randrange(1000, 9999)
    }

    bookings["accommodations"].append(accommodation_booking)

    return accommodation_booking
