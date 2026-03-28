import json
import os
from datetime import datetime, date, timedelta
import tkinter as tk
from tkinter import simpledialog
import random

GUESTS_FILE = 'guests.json'
HOTELS_FILE = 'hotels.json'
FLIGHTS_FILE = 'flights.json'
BOOKINGS_FILE = 'bookings.json'
ARCHIVES_FILE = 'archives.json'


def initialize_files():
    if not os.path.exists(GUESTS_FILE):
        with open(GUESTS_FILE, 'w') as f:
            json.dump([], f)
    
    if not os.path.exists(HOTELS_FILE):
        hotels = [
            {'hotel_id': 1, 'hotel_name': 'Grand Plaza', 'city': 'Mumbai', 'room_type': 'Single', 'price_per_night': 1000.00, 'total_rooms': 10, 'available_rooms': 10},
            {'hotel_id': 2, 'hotel_name': 'Grand Plaza', 'city': 'Mumbai', 'room_type': 'Double', 'price_per_night': 1500.00, 'total_rooms': 5, 'available_rooms': 5},
            {'hotel_id': 3, 'hotel_name': 'Royal Residency', 'city': 'Delhi', 'room_type': 'Deluxe Suite', 'price_per_night': 2500.00, 'total_rooms': 3, 'available_rooms': 3},
            {'hotel_id': 4, 'hotel_name': 'Royal Residency', 'city': 'Delhi', 'room_type': 'Family Suite', 'price_per_night': 3000.00, 'total_rooms': 4, 'available_rooms': 4},
            {'hotel_id': 5, 'hotel_name': 'Taj Heritage', 'city': 'Bangalore', 'room_type': 'Presidential Suite', 'price_per_night': 5000.00, 'total_rooms': 2, 'available_rooms': 2},
            {'hotel_id': 6, 'hotel_name': 'City Inn', 'city': 'Chennai', 'room_type': 'Standard Room', 'price_per_night': 800.00, 'total_rooms': 8, 'available_rooms': 8},
            {'hotel_id': 7, 'hotel_name': 'Business Hub', 'city': 'Hyderabad', 'room_type': 'Executive Room', 'price_per_night': 2000.00, 'total_rooms': 6, 'available_rooms': 6},
            {'hotel_id': 8, 'hotel_name': 'Paradise Resort', 'city': 'Goa', 'room_type': 'Honeymoon Suite', 'price_per_night': 4000.00, 'total_rooms': 2, 'available_rooms': 2},
            {'hotel_id': 9, 'hotel_name': 'Budget Stay', 'city': 'Pune', 'room_type': 'Budget Room', 'price_per_night': 600.00, 'total_rooms': 10, 'available_rooms': 10}
        ]
        with open(HOTELS_FILE, 'w') as f:
            json.dump(hotels, f, indent=4)
    
    if not os.path.exists(FLIGHTS_FILE):
        flights = [
            {'flight_id': 1, 'airline': 'Air India', 'from_city': 'Mumbai', 'to_city': 'Delhi', 'departure_time': '06:00', 'arrival_time': '08:00', 'price': 3500.00, 'total_seats': 150, 'available_seats': 150},
            {'flight_id': 2, 'airline': 'IndiGo', 'from_city': 'Mumbai', 'to_city': 'Bangalore', 'departure_time': '09:00', 'arrival_time': '11:00', 'price': 4000.00, 'total_seats': 180, 'available_seats': 180},
            {'flight_id': 3, 'airline': 'SpiceJet', 'from_city': 'Delhi', 'to_city': 'Mumbai', 'departure_time': '14:00', 'arrival_time': '16:00', 'price': 3200.00, 'total_seats': 150, 'available_seats': 150},
            {'flight_id': 4, 'airline': 'Vistara', 'from_city': 'Bangalore', 'to_city': 'Chennai', 'departure_time': '10:30', 'arrival_time': '11:30', 'price': 2500.00, 'total_seats': 120, 'available_seats': 120},
            {'flight_id': 5, 'airline': 'Air India', 'from_city': 'Chennai', 'to_city': 'Hyderabad', 'departure_time': '07:00', 'arrival_time': '08:30', 'price': 2800.00, 'total_seats': 140, 'available_seats': 140},
            {'flight_id': 6, 'airline': 'IndiGo', 'from_city': 'Hyderabad', 'to_city': 'Goa', 'departure_time': '12:00', 'arrival_time': '13:30', 'price': 3300.00, 'total_seats': 160, 'available_seats': 160},
            {'flight_id': 7, 'airline': 'SpiceJet', 'from_city': 'Goa', 'to_city': 'Pune', 'departure_time': '15:30', 'arrival_time': '16:45', 'price': 2200.00, 'total_seats': 130, 'available_seats': 130},
            {'flight_id': 8, 'airline': 'Vistara', 'from_city': 'Pune', 'to_city': 'Mumbai', 'departure_time': '18:00', 'arrival_time': '19:00', 'price': 2000.00, 'total_seats': 110, 'available_seats': 110},
            {'flight_id': 9, 'airline': 'Air India', 'from_city': 'Delhi', 'to_city': 'Bangalore', 'departure_time': '11:00', 'arrival_time': '13:30', 'price': 4500.00, 'total_seats': 170, 'available_seats': 170},
            {'flight_id': 10, 'airline': 'IndiGo', 'from_city': 'Bangalore', 'to_city': 'Mumbai', 'departure_time': '16:00', 'arrival_time': '18:00', 'price': 3800.00, 'total_seats': 180, 'available_seats': 180}
        ]
        with open(FLIGHTS_FILE, 'w') as f:
            json.dump(flights, f, indent=4)
    
    if not os.path.exists(BOOKINGS_FILE):
        with open(BOOKINGS_FILE, 'w') as f:
            json.dump({'hotel_bookings': [], 'flight_bookings': []}, f)
    
    if not os.path.exists(ARCHIVES_FILE):
        with open(ARCHIVES_FILE, 'w') as f:
            json.dump([], f)

def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def write_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def get_password():
    r = tk.Tk()
    r.withdraw()
    password = simpledialog.askstring("Password", "Enter your password:", show='*')
    r.destroy()
    return password

def register_guest():
    guests = read_json(GUESTS_FILE)
    
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    
    
    if any(guest['email'] == email for guest in guests):
        print("Email already registered. Please login.")
        return
    
    password = get_password()
    
    guest_id = max([g['guest_id'] for g in guests], default=0) + 1
    
    new_guest = {
        'guest_id': guest_id,
        'first_name': first_name,
        'last_name': last_name,
        'phone_number': phone_number,
        'email': email,
        'password': password,
        'meal_booking': False,
        'taxi_booking': False,
        'experience_booking': False,
        'additional_info': ''
    }
    
    guests.append(new_guest)
    write_json(GUESTS_FILE, guests)
    print("Successfully registered. Kindly login.")

def archive(guest_id):
    guests = read_json(GUESTS_FILE)
    archives = read_json(ARCHIVES_FILE)
    
    guest = next((g for g in guests if g['guest_id'] == guest_id), None)
    
    if guest:
        archives.append({
            'guest_id': guest['guest_id'],
            'first_name': guest['first_name'],
            'last_name': guest['last_name'],
            'phone_number': guest['phone_number'],
            'email': guest['email'],
            'password': guest['password']
        })
        
        guests = [g for g in guests if g['guest_id'] != guest_id]
        
        write_json(GUESTS_FILE, guests)
        write_json(ARCHIVES_FILE, archives)

def login_guest():
    email = input("Enter your email: ")
    password = get_password()
    
    guests = read_json(GUESTS_FILE)
    guest = next((g for g in guests if g['email'] == email and g['password'] == password), None)
    
    if guest:
        return guest['guest_id']
    else:
        archives = read_json(ARCHIVES_FILE)
        archived_guest = next((a for a in archives if a['email'] == email and a['password'] == password), None)
        
        if archived_guest:
            print("Welcome back!")
            return archived_guest['guest_id']
        else:
            print("Invalid email or password.")
            return None

def reactivate_guest(guest_id):
    archives = read_json(ARCHIVES_FILE)
    guests = read_json(GUESTS_FILE)
    
    guest = next((a for a in archives if a['guest_id'] == guest_id), None)
    
    if guest:
        new_guest = {
            'guest_id': guest['guest_id'],
            'first_name': guest['first_name'],
            'last_name': guest['last_name'],
            'phone_number': guest['phone_number'],
            'email': guest['email'],
            'password': guest['password'],
            'meal_booking': False,
            'taxi_booking': False,
            'experience_booking': False,
            'additional_info': ''
        }
        
        guests.append(new_guest)
        archives = [a for a in archives if a['guest_id'] != guest_id]
        
        write_json(GUESTS_FILE, guests)
        write_json(ARCHIVES_FILE, archives)

def main_menu(guest_id):
    while True:
        print("\n****Planify****")
        print("1. Book Hotel")
        print("2. Book Flight")
        print("3. Cancel Hotel Booking")
        print("4. Cancel Flight Booking")
        print("5. Display My Hotel Bookings")
        print("6. Display My Flight Bookings")
        print("7. Check Hotel Amenities")
        print("8. Check Offers")
        print("9. Book Meals")
        print("10. Book Taxi Service")
        print("11. Book Experiences")
        print("12. Logout")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice == 1:
            book_hotel(guest_id)
        elif choice == 2:
            book_flight(guest_id)
        elif choice == 3:
            cancel_hotel_booking(guest_id)
        elif choice == 4:
            cancel_flight_booking(guest_id)
        elif choice == 5:
            display_hotel_bookings(guest_id)
        elif choice == 6:
            display_flight_bookings(guest_id)
        elif choice == 7:
            print('\nHotel Amenities:')
            print('• Free Wi-Fi - Unlimited high-speed internet available in all rooms')
            print('• Swimming Pool - Open from 6 AM to 10 PM')
            print('• Gym - Fully equipped gym available for guests')
            print('• 24/7 Room Service')
            print('• Complimentary Breakfast')
        elif choice == 8:
            print('\nCurrent Offers:')
            print('• 10% off on hotel stays longer than 3 nights')
            print('• Free breakfast with every hotel booking')
            print('• 5% off on round-trip flight bookings')
            print('• Combo deals: Book hotel + flight and save 15%')
        elif choice == 9:
            book_meal(guest_id)
        elif choice == 10:
            book_taxi(guest_id)
        elif choice == 11:
            book_experience(guest_id)
        elif choice == 12:
            archive_guest(guest_id)
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice.")

def archive_guest(guest_id):
    bookings = read_json(BOOKINGS_FILE)
    today = date.today()
    
    active_hotel_bookings = [b for b in bookings['hotel_bookings'] 
                             if b['guest_id'] == guest_id and 
                             datetime.strptime(b['check_out_date'], '%Y-%m-%d').date() >= today]
    
    active_flight_bookings = [b for b in bookings['flight_bookings']
                              if b['guest_id'] == guest_id and
                              datetime.strptime(b['travel_date'], '%Y-%m-%d').date() >= today]
    
    if not active_hotel_bookings and not active_flight_bookings:
        archive(guest_id)

def book_hotel(guest_id):
    while True:
        print("\nSearch for a hotel:")
        print("1. By City")
        print("2. By Room Type")
        print("3. By Price Range")
        print("4. View All Available Hotels")
        print("5. Back to Main Menu")
        
        try:
            search_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input.")
            continue
        
        hotels = read_json(HOTELS_FILE)
        filtered_hotels = []
        
        if search_choice == 1:
            city = input("Enter city: ").strip()
            filtered_hotels = [h for h in hotels if h['available_rooms'] > 0 and 
                              h['city'].lower() == city.lower()]
        elif search_choice == 2:
            room_type = input("Enter room type: ").strip()
            filtered_hotels = [h for h in hotels if h['available_rooms'] > 0 and 
                              room_type.lower() in h['room_type'].lower()]
        elif search_choice == 3:
            try:
                min_price = float(input("Enter minimum price: "))
                max_price = float(input("Enter maximum price: "))
                filtered_hotels = [h for h in hotels if h['available_rooms'] > 0 and 
                                  min_price <= h['price_per_night'] <= max_price]
            except ValueError:
                print("Invalid price.")
                continue
        elif search_choice == 4:
            filtered_hotels = [h for h in hotels if h['available_rooms'] > 0]
        elif search_choice == 5:
            return
        else:
            print("Invalid choice.")
            continue
        
        if not filtered_hotels:
            print("No matching hotels found.")
            continue
        
        print("\nAvailable Hotels:")
        for hotel in filtered_hotels:
            print(f"Hotel ID: {hotel['hotel_id']}, Name: {hotel['hotel_name']}, City: {hotel['city']}, "
                  f"Type: {hotel['room_type']}, Price: ₹{hotel['price_per_night']}/night, "
                  f"Available Rooms: {hotel['available_rooms']}")
        
        try:
            hotel_id = int(input("\nEnter the hotel ID you want to book (or 0 to cancel): "))
        except ValueError:
            print("Invalid input.")
            continue
        
        if hotel_id == 0:
            return
        
        hotel = next((h for h in filtered_hotels if h['hotel_id'] == hotel_id), None)
        
        if not hotel:
            print("Invalid hotel ID selected.")
            continue
        
        check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
        check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
        
        try:
            check_in = datetime.strptime(check_in_date, '%Y-%m-%d').date()
            check_out = datetime.strptime(check_out_date, '%Y-%m-%d').date()
            
            if check_in < date.today():
                print("Check-in date cannot be in the past.")
                continue
            
            if check_out <= check_in:
                print("Check-out date must be after check-in date.")
                continue
        except ValueError:
            print("Invalid date format.")
            continue
        
        total_nights = (check_out - check_in).days
        total_cost = hotel['price_per_night'] * total_nights
        
        if total_nights > 3:
            discount = 0.10 * total_cost
            total_cost -= discount
            print(f"Discount applied: ₹{discount:.2f}")
        
    
        bookings = read_json(BOOKINGS_FILE)
        booking_id = max([b['booking_id'] for b in bookings['hotel_bookings']], default=0) + 1
        
        new_booking = {
            'booking_id': booking_id,
            'guest_id': guest_id,
            'hotel_id': hotel_id,
            'hotel_name': hotel['hotel_name'],
            'city': hotel['city'],
            'room_type': hotel['room_type'],
            'check_in_date': check_in_date,
            'check_out_date': check_out_date,
            'total_cost': total_cost
        }
        
        bookings['hotel_bookings'].append(new_booking)
        

        hotels = read_json(HOTELS_FILE)
        for h in hotels:
            if h['hotel_id'] == hotel_id:
                h['available_rooms'] -= 1
                break
        
        write_json(BOOKINGS_FILE, bookings)
        write_json(HOTELS_FILE, hotels)
        
        print(f"\nHotel booked successfully! Your booking ID is {booking_id}.")
        print(f"Total bill: ₹{total_cost:.2f}")
        break

def book_flight(guest_id):
    while True:
        print("\nSearch for a flight:")
        print("1. By Route (From City -> To City)")
        print("2. By Airline")
        print("3. By Price Range")
        print("4. View All Available Flights")
        print("5. Back to Main Menu")
        
        try:
            search_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input.")
            continue
        
        flights = read_json(FLIGHTS_FILE)
        filtered_flights = []
        
        if search_choice == 1:
            from_city = input("Enter departure city: ").strip()
            to_city = input("Enter destination city: ").strip()
            filtered_flights = [f for f in flights if f['available_seats'] > 0 and 
                               f['from_city'].lower() == from_city.lower() and
                               f['to_city'].lower() == to_city.lower()]
        elif search_choice == 2:
            airline = input("Enter airline name: ").strip()
            filtered_flights = [f for f in flights if f['available_seats'] > 0 and 
                               airline.lower() in f['airline'].lower()]
        elif search_choice == 3:
            try:
                min_price = float(input("Enter minimum price: "))
                max_price = float(input("Enter maximum price: "))
                filtered_flights = [f for f in flights if f['available_seats'] > 0 and 
                                   min_price <= f['price'] <= max_price]
            except ValueError:
                print("Invalid price.")
                continue
        elif search_choice == 4:
            filtered_flights = [f for f in flights if f['available_seats'] > 0]
        elif search_choice == 5:
            return
        else:
            print("Invalid choice.")
            continue
        
        if not filtered_flights:
            print("No matching flights found.")
            continue
        
        print("\nAvailable Flights:")
        for flight in filtered_flights:
            print(f"Flight ID: {flight['flight_id']}, Airline: {flight['airline']}, "
                  f"Route: {flight['from_city']} -> {flight['to_city']}, "
                  f"Departure: {flight['departure_time']}, Arrival: {flight['arrival_time']}, "
                  f"Price: ₹{flight['price']}, Available Seats: {flight['available_seats']}")
        
        try:
            flight_id = int(input("\nEnter the flight ID you want to book (or 0 to cancel): "))
        except ValueError:
            print("Invalid input.")
            continue
        
        if flight_id == 0:
            return
        
        flight = next((f for f in filtered_flights if f['flight_id'] == flight_id), None)
        
        if not flight:
            print("Invalid flight ID selected.")
            continue
        
        travel_date = input("Enter travel date (YYYY-MM-DD): ")
        
        try:
            travel_dt = datetime.strptime(travel_date, '%Y-%m-%d').date()
            
            if travel_dt < date.today():
                print("Travel date cannot be in the past.")
                continue
        except ValueError:
            print("Invalid date format.")
            continue
        
        try:
            num_passengers = int(input("Enter number of passengers: "))
            if num_passengers <= 0 or num_passengers > flight['available_seats']:
                print(f"Invalid number of passengers. Available seats: {flight['available_seats']}")
                continue
        except ValueError:
            print("Invalid input.")
            continue
        
        total_cost = flight['price'] * num_passengers
        
    
        bookings = read_json(BOOKINGS_FILE)
        booking_id = max([b['booking_id'] for b in bookings['flight_bookings']], default=0) + 1
        
        new_booking = {
            'booking_id': booking_id,
            'guest_id': guest_id,
            'flight_id': flight_id,
            'airline': flight['airline'],
            'from_city': flight['from_city'],
            'to_city': flight['to_city'],
            'departure_time': flight['departure_time'],
            'arrival_time': flight['arrival_time'],
            'travel_date': travel_date,
            'num_passengers': num_passengers,
            'total_cost': total_cost,
            'pnr': f"PNR{random.randint(100000, 999999)}"
        }
        
        bookings['flight_bookings'].append(new_booking)
        
        
        flights = read_json(FLIGHTS_FILE)
        for f in flights:
            if f['flight_id'] == flight_id:
                f['available_seats'] -= num_passengers
                break
        
        write_json(BOOKINGS_FILE, bookings)
        write_json(FLIGHTS_FILE, flights)
        
        print(f"\nFlight booked successfully! Your booking ID is {booking_id}.")
        print(f"PNR: {new_booking['pnr']}")
        print(f"Total bill: ₹{total_cost:.2f}")
        break

def cancel_hotel_booking(guest_id):
    try:
        booking_id = int(input("Enter hotel booking ID to cancel: "))
    except ValueError:
        print("Invalid booking ID.")
        return
    
    bookings = read_json(BOOKINGS_FILE)
    booking = next((b for b in bookings['hotel_bookings'] 
                   if b['booking_id'] == booking_id and b['guest_id'] == guest_id), None)
    
    if not booking:
        print("Booking ID not found or does not belong to you.")
        return
    

    hotels = read_json(HOTELS_FILE)
    for h in hotels:
        if h['hotel_id'] == booking['hotel_id']:
            h['available_rooms'] += 1
            break
    

    bookings['hotel_bookings'] = [b for b in bookings['hotel_bookings'] 
                                   if b['booking_id'] != booking_id]
    
    write_json(BOOKINGS_FILE, bookings)
    write_json(HOTELS_FILE, hotels)
    
    print("Hotel booking cancelled successfully.")
    

    check_out = datetime.strptime(booking['check_out_date'], '%Y-%m-%d').date()
    if date.today() > check_out:
        archive_guest(guest_id)

def cancel_flight_booking(guest_id):
    try:
        booking_id = int(input("Enter flight booking ID to cancel: "))
    except ValueError:
        print("Invalid booking ID.")
        return
    
    bookings = read_json(BOOKINGS_FILE)
    booking = next((b for b in bookings['flight_bookings'] 
                   if b['booking_id'] == booking_id and b['guest_id'] == guest_id), None)
    
    if not booking:
        print("Booking ID not found or does not belong to you.")
        return
    
    
    flights = read_json(FLIGHTS_FILE)
    for f in flights:
        if f['flight_id'] == booking['flight_id']:
            f['available_seats'] += booking['num_passengers']
            break
    
   
    bookings['flight_bookings'] = [b for b in bookings['flight_bookings'] 
                                    if b['booking_id'] != booking_id]
    
    write_json(BOOKINGS_FILE, bookings)
    write_json(FLIGHTS_FILE, flights)
    
    print("Flight booking cancelled successfully.")
    
    
    travel_date = datetime.strptime(booking['travel_date'], '%Y-%m-%d').date()
    if date.today() > travel_date:
        archive_guest(guest_id)

def display_hotel_bookings(guest_id):
    bookings = read_json(BOOKINGS_FILE)
    hotel_bookings = [b for b in bookings['hotel_bookings'] if b['guest_id'] == guest_id]
    
    if not hotel_bookings:
        print("No hotel bookings found.")
        return
    
    print("\nYour Hotel Bookings:")
    for booking in hotel_bookings:
        print(f"\nBooking ID: {booking['booking_id']}")
        print(f"Hotel: {booking['hotel_name']}, City: {booking['city']}")
        print(f"Room Type: {booking['room_type']}")
        print(f"Check-in: {booking['check_in_date']}, Check-out: {booking['check_out_date']}")
        print(f"Total Cost: ₹{booking['total_cost']:.2f}")

def display_flight_bookings(guest_id):
    bookings = read_json(BOOKINGS_FILE)
    flight_bookings = [b for b in bookings['flight_bookings'] if b['guest_id'] == guest_id]
    
    if not flight_bookings:
        print("No flight bookings found.")
        return
    
    print("\nYour Flight Bookings:")
    for booking in flight_bookings:
        print(f"\nBooking ID: {booking['booking_id']}")
        print(f"PNR: {booking['pnr']}")
        print(f"Airline: {booking['airline']}")
        print(f"Route: {booking['from_city']} -> {booking['to_city']}")
        print(f"Travel Date: {booking['travel_date']}")
        print(f"Departure: {booking['departure_time']}, Arrival: {booking['arrival_time']}")
        print(f"Passengers: {booking['num_passengers']}")
        print(f"Total Cost: ₹{booking['total_cost']:.2f}")

def active_booking(guest_id):
    bookings = read_json(BOOKINGS_FILE)
    today = date.today()
    
    active_hotels = [b for b in bookings['hotel_bookings'] 
                     if b['guest_id'] == guest_id and 
                     datetime.strptime(b['check_out_date'], '%Y-%m-%d').date() > today]
    
    active_flights = [b for b in bookings['flight_bookings']
                      if b['guest_id'] == guest_id and
                      datetime.strptime(b['travel_date'], '%Y-%m-%d').date() >= today]
    
    return len(active_hotels) > 0 or len(active_flights) > 0

def book_meal(guest_id):
    if not active_booking(guest_id):
        print("You must have an active booking to book meals.")
        return
    
    try:
        num_people = int(input("Enter the number of people: "))
    except ValueError:
        print("Invalid input.")
        return
    
    meal_preference = input("Enter meal preference (Veg/Non-Veg): ")
    
    guests = read_json(GUESTS_FILE)
    for guest in guests:
        if guest['guest_id'] == guest_id:
            guest['meal_booking'] = True
            guest['additional_info'] += f"Meals booked: {num_people} people, Preference: {meal_preference}; "
            break
    
    write_json(GUESTS_FILE, guests)
    print(f"{num_people} meals booked successfully with preference: {meal_preference}.")

def book_taxi(guest_id):
    if not active_booking(guest_id):
        print("You must have an active booking to book a taxi.")
        return
    
    taxi_type = input("Enter taxi type (e.g., Sedan, SUV): ")
    pickup_time = input("Enter pickup time (HH:MM): ")
    
    guests = read_json(GUESTS_FILE)
    for guest in guests:
        if guest['guest_id'] == guest_id:
            guest['taxi_booking'] = True
            guest['additional_info'] += f"Taxi booked: {taxi_type} at {pickup_time}; "
            break
    
    write_json(GUESTS_FILE, guests)
    print(f"{taxi_type} taxi booked successfully for {pickup_time}.")

def book_experience(guest_id):
    if not active_booking(guest_id):
        print("You must have an active booking to book experiences.")
        return
    
    experience = input("Enter the experience you want to book (e.g., City Tour, Adventure Sports): ")
    experience_time = input("Enter the time for the experience (HH:MM): ")
    
    guests = read_json(GUESTS_FILE)
    for guest in guests:
        if guest['guest_id'] == guest_id:
            guest['experience_booking'] = True
            guest['additional_info'] += f"Experience booked: {experience} at {experience_time}; "
            break
    
    write_json(GUESTS_FILE, guests)
    print(f"{experience} experience booked successfully for {experience_time}.")

def main():
    print("Initializing Planify...")
    initialize_files()
    print("System ready!")
    
    while True:
        print("\n****Welcome to Planify****")
        print("1. Register Guest")
        print("2. Login")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice == 1:
            register_guest()
        elif choice == 2:
            guest_id = login_guest()
            if guest_id:
                guests = read_json(GUESTS_FILE)
                if not any(g['guest_id'] == guest_id for g in guests):
                    reactivate_guest(guest_id)
                main_menu(guest_id)
        elif choice == 3:
            print("Thank you for using Planify. Have a great journey!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
