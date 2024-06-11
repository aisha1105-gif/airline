flights = [
    {
        "flight_number": "ABC123",
        "date": "2024-05-24",
        "time": "14:30",
        "destination": "New York",
        "airport_code": "JFK",
        "pilot": {"name": "John Doe", "role": "Pilot", "title": "Captain", "experience": "15 years", "email": "john.doe@example.com"},
        "air_hostess": {"name": "Emily Davis", "role": "Air Hostess", "title": "Senior Air Hostess", "experience": "12 years", "email": "emily.davis@example.com"}
    },
    {
        "flight_number": "DEF456",
        "date": "2024-05-25",
        "time": "08:45",
        "destination": "London",
        "airport_code": "LHR",
        "pilot": {"name": "Jane Smith", "role": "Pilot", "title": "First Officer", "experience": "10 years", "email": "jane.smith@example.com"},
        "air_hostess": {"name": "Anna Johnson", "role": "Air Hostess", "title": "Air Hostess", "experience": "5 years", "email": "anna.johnson@example.com"}
    },
    {
        "flight_number": "GHI789",
        "date": "2024-06-01",
        "time": "10:00",
        "destination": "Paris",
        "airport_code": "CDG",
        "pilot": {"name": "Mark Brown", "role": "Pilot", "title": "Captain", "experience": "20 years", "email": "mark.brown@example.com"},
        "air_hostess": {"name": "Laura Wilson", "role": "Air Hostess", "title": "Senior Air Hostess", "experience": "15 years", "email": "laura.wilson@example.com"}
    },
    {
        "flight_number": "JKL012",
        "date": "2024-06-02",
        "time": "15:30",
        "destination": "Tokyo",
        "airport_code": "HND",
        "pilot": {"name": "Michael Johnson", "role": "Pilot", "title": "First Officer", "experience": "8 years", "email": "michael.johnson@example.com"},
        "air_hostess": {"name": "Jessica White", "role": "Air Hostess", "title": "Air Hostess", "experience": "3 years", "email": "jessica.white@example.com"}
    },
    {
        "flight_number": "MNO345",
        "date": "2024-06-03",
        "time": "09:15",
        "destination": "Sydney",
        "airport_code": "SYD",
        "pilot": {"name": "David Miller", "role": "Pilot", "title": "Captain", "experience": "18 years", "email": "david.miller@example.com"},
        "air_hostess": {"name": "Sophia Lee", "role": "Air Hostess", "title": "Senior Air Hostess", "experience": "10 years", "email": "sophia.lee@example.com"}
    }
]

past_flights = [
    {
        "flight_number": "XYZ987",
        "date": "2024-05-24",
        "time": "12:30",
        "destination": "New York",
        "airport_code": "JFK",
        "pilot": {"name": "David", "role": "Pilot", "title": "Captain", "experience": "15 years", "email": "john.doe@example.com"},
        "air_hostess": {"name": "Jennifer Davis", "role": "Air Hostess", "title": "Senior Air Hostess", "experience": "12 years", "email": "emily.davis@example.com"}
    },
    {
        "flight_number": "PQR546",
        "date": "2024-05-25",
        "time": "08:30",
        "destination": "London",
        "airport_code": "LHR",
        "pilot": {"name": "Robert brown", "role": "Pilot", "title": "First Officer", "experience": "10 years", "email": "jane.smith@example.com"},
        "air_hostess": {"name": "Linda Johnson", "role": "Air Hostess", "title": "Air Hostess", "experience": "5 years", "email": "anna.johnson@example.com"}
    },
    {
        "flight_number": "STU123",
        "date": "2024-06-01",
        "time": "09:00",
        "destination": "Paris",
        "airport_code": "CDG",
        "pilot": {"name": "Michael", "role": "Pilot", "title": "Captain", "experience": "20 years", "email": "mark.brown@example.com"},
        "air_hostess": {"name": "Elizabeth", "role": "Air Hostess", "title": "Senior Air Hostess", "experience": "15 years", "email": "laura.wilson@example.com"}
    },
    {
        "flight_number": "VWX764",
        "date": "2024-06-02",
        "time": "15:00",
        "destination": "Tokyo",
        "airport_code": "HND",
        "pilot": {"name": "James William", "role": "Pilot", "title": "First Officer", "experience": "8 years", "email": "michael.johnson@example.com"},
        "air_hostess": {"name": "Susan hurds", "role": "Air Hostess", "title": "Air Hostess", "experience": "3 years", "email": "jessica.white@example.com"}
    },
    {
        "flight_number": "OPA321",
        "date": "2024-06-03",
        "time": "06:15",
        "destination": "Sydney",
        "airport_code": "SYD",
        "pilot": {"name": "Richard David", "role": "Pilot", "title": "Captain", "experience": "18 years", "email": "david.miller@example.com"},
        "air_hostess": {"name": "Mary lisa", "role": "Air Hostess", "title": "Senior Air Hostess", "experience": "10 years", "email": "sophia.lee@example.com"}
    }
]

def save_flights_to_file(flights, filename):
    with open(filename, 'w') as file:
        for flight in flights:
            file.write(f"Flight Number: {flight['flight_number']}\n")
            file.write(f"Date: {flight['date']}\n")
            file.write(f"Time: {flight['time']}\n")
            file.write(f"Destination: {flight['destination']}\n")
            file.write(f"Airport Code: {flight['airport_code']}\n")
            if flight['pilot']:
                file.write(f"Pilot:\n")
                file.write(f"  Name: {flight['pilot']['name']}\n")
                file.write(f"  Role: {flight['pilot']['role']}\n")
                file.write(f"  Title: {flight['pilot']['title']}\n")
                file.write(f"  Experience: {flight['pilot']['experience']}\n")
                file.write(f"  Email: {flight['pilot']['email']}\n")
            if flight['air_hostess']:
                file.write(f"Air Hostess:\n")
                file.write(f"  Name: {flight['air_hostess']['name']}\n")
                file.write(f"  Role: {flight['air_hostess']['role']}\n")
                file.write(f"  Title: {flight['air_hostess']['title']}\n")
                file.write(f"  Experience: {flight['air_hostess']['experience']}\n")
                file.write(f"  Email: {flight['air_hostess']['email']}\n")
            file.write("\n")

# Save available flights to file
save_flights_to_file(flights, "available_flights.txt")

# Save past flights to file
save_flights_to_file(past_flights, "past_flights.txt")