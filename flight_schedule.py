import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os

class AirlineReservation:
    def __init__(self, root):
        self.root = root
        self.root.title("Airline Reservation Form")
        # Creating a PhotoImage object from an image file
        icon = tk.PhotoImage(file="3.png")
        # Setting the icon using the iconphoto() method
        root.iconphoto(True, icon)
        self.reservations = []
        self.load_reservations()
        self.create_widgets()
    def create_widgets(self):
        frame = tk.Frame(self.root, bg="sky blue")  # Set background color
        frame.pack(padx=10, pady=10)

        # Flight Information
        flight_info_frame = tk.LabelFrame(frame, text="Flight Information", bg="sky blue")  # Set background color
        flight_info_frame.grid(row=0, column=0, padx=10, pady=5)

        tk.Label(flight_info_frame, text="Destination:", bg="sky blue").grid(row=0, column=0, sticky=tk.W)
        self.destination = tk.StringVar()
        destination_entry = tk.Entry(flight_info_frame, textvariable=self.destination)
        destination_entry.grid(row=0, column=1)

        tk.Label(flight_info_frame, text="Departure Date:", bg="sky blue").grid(row=1, column=0, sticky=tk.W)
        self.departure_date = tk.StringVar()
        departure_date_entry = tk.Entry(flight_info_frame, textvariable=self.departure_date)
        departure_date_entry.grid(row=1, column=1)

        # Passenger Information
        passenger_info_frame = tk.LabelFrame(frame, text="Passenger Information", bg="sky blue")  # Set background color
        passenger_info_frame.grid(row=1, column=0, padx=10, pady=5)

        tk.Label(passenger_info_frame, text="Passenger Name:", bg="sky blue").grid(row=0, column=0, sticky=tk.W)
        self.full_name = tk.StringVar()
        full_name_entry = tk.Entry(passenger_info_frame, textvariable=self.full_name)
        full_name_entry.grid(row=0, column=1)
        
        tk.Label(passenger_info_frame, text="Number of Passengers", bg="sky blue").grid(row=1, column=0, sticky=tk.W)
        self.passenger_count=tk.StringVar()
        passenger_count_entry = tk.Entry(passenger_info_frame, textvariable=self.passenger_count)
        passenger_count_entry.grid(row=1, column=1)

        tk.Label(passenger_info_frame, text="Passport Number:", bg="sky blue").grid(row=2, column=0, sticky=tk.W)
        self.passport_number = tk.StringVar()
        passport_number_entry = tk.Entry(passenger_info_frame, textvariable=self.passport_number)
        passport_number_entry.grid(row=2, column=1)
        
        tk.Label(passenger_info_frame, text="Class:", bg="sky blue").grid(row=3, column=0, sticky=tk.W)
        self.classs = tk.StringVar()
        classes=['Economy Class','Business Class']
        classs_entry = ttk.Combobox(passenger_info_frame, textvariable=self.classs, values=classes)
        classs_entry.grid(row=3, column=1)

        tk.Label(passenger_info_frame, text="Seat Preference:", bg="sky blue").grid(row=4, column=0, sticky=tk.W)
        self.seat_preference = tk.StringVar()
        seatpre=['Window Seat','Aisle Seat','Middle Seat']
        seat_preference_entry = ttk.Combobox(passenger_info_frame, textvariable=self.seat_preference, values=seatpre)
        seat_preference_entry.grid(row=4, column=1)

        # Payment Information
        tk.Label(frame, text="Payment Method:", bg="sky blue").grid(row=3, column=0, sticky=tk.W)
        self.payment_method = tk.StringVar()
        payment_options = ["Credit Card", "Debit Card", "Cash", "Online Payment", "Bank Transfer"]
        self.payment_menu = ttk.Combobox(frame, textvariable=self.payment_method, values=payment_options)
        self.payment_menu.grid(row=3, column=1)

        # Total Cost
        tk.Label(frame, text="Total Cost:", bg="sky blue").grid(row=4,column=0, sticky=tk.W)
        self.total_cost_var = tk.StringVar(value="0.0")
        tk.Label(frame, textvariable=self.total_cost_var, bg="sky blue").grid(row=4, column=1, sticky=tk.W)

        # Buttons
        buttons_frame = tk.Frame(frame, bg='sky blue')  # Set background color
        buttons_frame.grid(row=5, column=0, pady=10)

        self.add_button = tk.Button(buttons_frame, text="Add Reservation", command=self.add_reservation, bg="#4caf50", fg="white")
        self.add_button.grid(row=0, column=0, padx=5)

        self.update_button = tk.Button(buttons_frame, text="Update Reservation", command=self.update_reservation,bg="#4caf50", fg="white" )
        self.update_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(buttons_frame, text="Delete Reservation", command=self.delete_reservation, bg="#4caf50", fg="white")
        self.delete_button.grid(row=0, column=2, padx=5)

        self.view_button = tk.Button(buttons_frame, text="View Reservations", command=self.view_reservations, bg="#4caf50", fg="white")
        self.view_button.grid(row=0, column=3, padx=5)

        self.available_flights_button = tk.Button(buttons_frame, text="Available Flights", command=self.show_available_flights, bg="#4caf50", fg="white")
        self.available_flights_button.grid(row=0, column=4, padx=5)

        self.past_flights_button = tk.Button(buttons_frame, text="Past Flights", command=self.show_past_flights, bg="#4caf50", fg="white")
        self.past_flights_button.grid(row=0, column=5, padx=5)

        self.confirm_button = tk.Button(buttons_frame, text="Confirm Ticket", command=self.confirm_ticket, bg="#4caf50", fg="white")
        self.confirm_button.grid(row=1, column=0, padx=5)

        self.return_button = tk.Button(buttons_frame, text="Return Ticket", command=self.return_ticket, bg="#4caf50", fg="white")
        self.return_button.grid(row=1, column=1, padx=5)

    def add_reservation(self):
    # Calculate total cost based on destination, class, and number of passengers
       base_cost = 20000  # Base cost for the flight
       additional_cost_per_passenger = 10000  # Additional cost per passenger

       destination = self.destination.get()
       flight_class = self.classs.get()
       passenger_count = int(self.passenger_count.get())

       if flight_class == "Business Class":
        total_cost = base_cost + (additional_cost_per_passenger * passenger_count)
       else:
        total_cost = base_cost * passenger_count

       self.total_cost_var.set(total_cost)

    # Now add the reservation as before
       reservation = {
        "Destination": destination,
        "Departure Date": self.departure_date.get(),
        "Passenger Name": self.full_name.get(),
        "Passport Number": self.passport_number.get(),
        "Passenger Number": self.passenger_count.get(),
        "Class": self.classs.get(),
        "Seat Preference": self.seat_preference.get(),
        "Payment Method": self.payment_method.get(),
        "Total Cost": total_cost
    }
       self.reservations.append(reservation)
       self.save_reservations()
       messagebox.showinfo("Success", "Reservation added successfully!")
    def view_reservations(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Reservations")
        text = tk.Text(view_window)
        text.pack(expand=True, fill=tk.BOTH)

        for idx, reservation in enumerate(self.reservations, start=1):
            text.insert(tk.END, f"Reservation {idx}\n")
            for key, value in reservation.items():
                text.insert(tk.END, f"{key}: {value}\n")
            text.insert(tk.END, "-"*30 + "\n")

    def update_reservation(self):
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Reservation")
        
        tk.Label(update_window, text="Enter Reservation Number to update:").grid(row=0, column=0)
        reservation_number_entry = tk.Entry(update_window)
        reservation_number_entry.grid(row=0, column=1)
        
        def submit_update():
            idx = int(reservation_number_entry.get()) - 1
            if 0 <= idx < len(self.reservations):
                self.reservations[idx] = {
                    "Destination": self.destination.get(),
                    "Departure Date": self.departure_date.get(),
                    "Passenger Name": self.full_name.get(),
                    "Passport Number": self.passport_number.get(),
                    "Passenger Number":self.passenger_count.get(),
                    "Class": self.classs.get(),
                    "Seat Preference": self.seat_preference.get(),
                    "Payment Method": self.payment_method.get(),
                    "Total Cost": self.total_cost_var.get()
                }
                self.save_reservations()
                messagebox.showinfo("Success", "Reservation updated successfully!")
                update_window.destroy()
            else:
                messagebox.showerror("Error", "Invalid reservation number!")
        
        tk.Button(update_window, text="Update", command=submit_update).grid(row=1, columnspan=2)

    def delete_reservation(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Reservation")

        tk.Label(delete_window, text="Enter Reservation Number to delete:").grid(row=0, column=0)
        reservation_number_entry = tk.Entry(delete_window)
        reservation_number_entry.grid(row=0, column=1)

        def submit_delete():
            idx = int(reservation_number_entry.get()) - 1
            if 0 <= idx < len(self.reservations):
                self.reservations.pop(idx)
                self.save_reservations()
                messagebox.showinfo("Success", "Reservation deleted successfully!")
                delete_window.destroy()
            else:
                messagebox.showerror("Error", "Invalid reservation number!")
        
        tk.Button(delete_window, text="Delete", command=submit_delete).grid(row=1, columnspan=2)

    def save_reservations(self):
        with open('airline_reservations.txt', 'w') as file:
            for reservation in self.reservations:
                for key, value in reservation.items():
                    file.write(f"{key}: {value}\n")
                file.write("\n")

    def load_reservations(self):
        try:
            with open('airline_reservations.txt', 'r') as file:
                reservation = {}
                for line in file:
                    line = line.strip()
                    if line:
                        if ": " in line:
                            key, value = line.split(': ', 1)
                            reservation[key] = value
                    else:
                        if reservation:
                            self.reservations.append(reservation)
                            reservation = {}
                if reservation:  # Ensure the last reservation is added
                    self.reservations.append(reservation)
        except FileNotFoundError:
            pass

    def show_available_flights(self):
        self.show_flight_details("available_flights.txt", "Available Flights")

    def show_past_flights(self):
        self.show_flight_details("past_flights.txt", "Past Flights")

    def show_flight_details(self, filename, title):
        flight_details_window = tk.Toplevel(self.root)
        flight_details_window.title(title)
        text = tk.Text(flight_details_window)
        text.pack(expand=True, fill=tk.BOTH)

        try:
            with open(filename, 'r') as file:
                text.insert(tk.END, file.read())
        except FileNotFoundError:
            text.insert(tk.END, "No flights available.")

    def confirm_ticket(self):
     try:
        confirmation = messagebox.askquestion("Confirm Ticket", "Do you want to confirm this ticket?")
        if confirmation == "yes":
            # Check if entered destination matches any available flights
            destination = self.destination.get()
            destination_matches = False
            with open("available_flights.txt", "r") as file:
                for line in file:
                    if destination in line:
                        destination_matches = True
                        break

            # Combining user details and saving in a file with user's name
            user_details = {
                "Destination": destination,
                "Departure Date": self.departure_date.get(),
                "Passenger Name": self.full_name.get(),
                "Passenger Number":self.passenger_count.get(),
                "Passport Number": self.passport_number.get(),
                "Class": self.classs.get(),
                "Seat Preference": self.seat_preference.get(),
                "Payment Method": self.payment_method.get(),
                "Total Cost": self.total_cost_var.get()
            }

            # Save to file with user's name as filename (boarding pass)
            filename = f"{user_details['Passenger Name']}_boarding_pass.txt"
            with open(filename, mode='w') as file:
                # Write user details
                for key, value in user_details.items():
                    file.write(f"{key}: {value}\n")

                # If destination does not match available flights, include flight details
                if not destination_matches:
                    file.write("\nFlight Details:\n")
                    with open("available_flights.txt", "r") as available_flights_file:
                        file.write(available_flights_file.read())

            messagebox.showinfo("Ticket Confirmation", "Your ticket has been confirmed.")
            return True
        else:
            messagebox.showinfo("Ticket Confirmation", "Ticket confirmation cancelled.")
            return False
     except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return False
    def return_ticket(self):
        try:
            if not self.reservations:
                messagebox.showinfo("Return Ticket", "No tickets to return.")
                return

            # Show booked tickets for selection
            messagebox.showinfo("Return Ticket", "Booked Tickets:\n" + '\n'.join([f"{i+1}. {reservation['Passenger Name']}, {reservation['Departure Date']}" for i, reservation in enumerate(self.reservations)]))
            index = int(passsengername.get()) - 1
            if 0 <= index < len(self.reservations):
                # Return the selected ticket
                returned_ticket = self.reservations.pop(index)
                self.save_reservations()  # Update reservations after returning ticket
                messagebox.showinfo("Return Ticket", "Your ticket has been returned successfully.")
            else:
                messagebox.showerror("Error", "Invalid ticket index.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid index.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="sky blue")
    app = AirlineReservation(root)
    root.mainloop()
