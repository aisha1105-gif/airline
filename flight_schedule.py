import tkinter as tk
from tkinter import messagebox, ttk

def add_reservation():
    base_cost = 20000
    additional_cost_per_passenger = 10000

    destination = destination_var.get()
    flight_class = classs_var.get()
    passenger_count = int(passenger_count_var.get())

    if flight_class == "Business Class":
        total_cost = base_cost + (additional_cost_per_passenger * passenger_count)
    else:
        total_cost = base_cost * passenger_count

    total_cost_var.set(total_cost)

    reservation = {
        "Destination": destination,
        "Departure Date": departure_date_var.get(),
        "Passenger Name": full_name_var.get(),
        "Passport Number": passport_number_var.get(),
        "Passenger Number": passenger_count_var.get(),
        "Class": classs_var.get(),
        "Seat Preference": seat_preference_var.get(),
        "Payment Method": payment_method_var.get(),
        "Total Cost": total_cost
    }
    reservations.append(reservation)
    save_reservations()
    messagebox.showinfo("Success", "Reservation added successfully!")

def view_reservations():
    view_window = tk.Toplevel(root)
    view_window.title("View Reservations")
    text = tk.Text(view_window)
    text.pack(expand=True, fill=tk.BOTH)

    for idx, reservation in enumerate(reservations, start=1):
        text.insert(tk.END, f"Reservation {idx}\n")
        for key, value in reservation.items():
            text.insert(tk.END, f"{key}: {value}\n")
        text.insert(tk.END, "-"*30 + "\n")

def update_reservation():
    update_window = tk.Toplevel(root)
    update_window.title("Update Reservation")
    
    tk.Label(update_window, text="Enter Reservation Number to update:").grid(row=0, column=0)
    reservation_number_entry = tk.Entry(update_window)
    reservation_number_entry.grid(row=0, column=1)
    
    def submit_update():
        idx = int(reservation_number_entry.get()) - 1
        if 0 <= idx < len(reservations):
            reservations[idx] = {
                "Destination": destination_var.get(),
                "Departure Date": departure_date_var.get(),
                "Passenger Name": full_name_var.get(),
                "Passport Number": passport_number_var.get(),
                "Passenger Number": passenger_count_var.get(),
                "Class": classs_var.get(),
                "Seat Preference": seat_preference_var.get(),
                "Payment Method": payment_method_var.get(),
                "Total Cost": total_cost_var.get()
            }
            save_reservations()
            messagebox.showinfo("Success", "Reservation updated successfully!")
            update_window.destroy()
        else:
            messagebox.showerror("Error", "Invalid reservation number!")
    
    tk.Button(update_window, text="Update", command=submit_update).grid(row=1, columnspan=2)

def delete_reservation():
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Reservation")

    tk.Label(delete_window, text="Enter Reservation Number to delete:").grid(row=0, column=0)
    reservation_number_entry = tk.Entry(delete_window)
    reservation_number_entry.grid(row=0, column=1)

    def submit_delete():
        idx = int(reservation_number_entry.get()) - 1
        if 0 <= idx < len(reservations):
            reservations.pop(idx)
            save_reservations()
            messagebox.showinfo("Success", "Reservation deleted successfully!")
            delete_window.destroy()
        else:
            messagebox.showerror("Error", "Invalid reservation number!")
    
    tk.Button(delete_window, text="Delete", command=submit_delete).grid(row=1, columnspan=2)

def save_reservations():
    with open('airline_reservations.txt', 'w') as file:
        for reservation in reservations:
            for key, value in reservation.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")

def load_reservations():
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
                        reservations.append(reservation)
                        reservation = {}
            if reservation:
                reservations.append(reservation)
    except FileNotFoundError:
        pass

def show_available_flights():
    show_flight_details("available_flights.txt", "Available Flights")

def show_past_flights():
    show_flight_details("past_flights.txt", "Past Flights")

def show_flight_details(filename, title):
    flight_details_window = tk.Toplevel(root)
    flight_details_window.title(title)
    text = tk.Text(flight_details_window)
    text.pack(expand=True, fill=tk.BOTH)

    try:
        with open(filename, 'r') as file:
            text.insert(tk.END, file.read())
    except FileNotFoundError:
        text.insert(tk.END, "No flights available.")

def confirm_ticket():
    try:
        confirmation = messagebox.askquestion("Confirm Ticket", "Do you want to confirm this ticket?")
        if confirmation == "yes":
            destination = destination_var.get()
            destination_matches = False
            with open("available_flights.txt", "r") as file:
                for line in file:
                    if destination in line:
                        destination_matches = True
                        break

            user_details = {
                "Destination": destination,
                "Departure Date": departure_date_var.get(),
                "Passenger Name": full_name_var.get(),
                "Passenger Number": passenger_count_var.get(),
                "Passport Number": passport_number_var.get(),
                "Class": classs_var.get(),
                "Seat Preference": seat_preference_var.get(),
                "Payment Method": payment_method_var.get(),
                "Total Cost": total_cost_var.get()
            }

            filename = f"{user_details['Passenger Name']}_boarding_pass.txt"
            with open(filename, mode='w') as file:
                for key, value in user_details.items():
                    file.write(f"{key}: {value}\n")

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

def return_ticket():
    try:
        if not reservations:
            messagebox.showinfo("Return Ticket", "No tickets to return.")
            return

        messagebox.showinfo("Return Ticket", "Booked Tickets:\n" + '\n'.join([f"{i+1}. {reservation['Passenger Name']}, {reservation['Departure Date']}" for i, reservation in enumerate(reservations)]))
        index = int(passenger_name_entry.get()) - 1
        if 0 <= index < len(reservations):
            returned_ticket = reservations.pop(index)
            save_reservations()
            messagebox.showinfo("Return Ticket", "Your ticket has been returned successfully.")
        else:
            messagebox.showerror("Error", "Invalid ticket index.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid index.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("Skyline Aviation Airways")
icon = tk.PhotoImage(file="3.png")
root.iconphoto(True, icon)
root.configure(bg="sky blue")

# Variables
destination_var = tk.StringVar()
departure_date_var = tk.StringVar()
full_name_var = tk.StringVar()
passenger_count_var = tk.StringVar()
passport_number_var = tk.StringVar()
classs_var = tk.StringVar()
seat_preference_var = tk.StringVar()
payment_method_var = tk.StringVar()
total_cost_var = tk.StringVar(value="0.0")

# Data
reservations = []
load_reservations()

# UI
frame = tk.Frame(root, bg="sky blue")
frame.pack(padx=10, pady=10)

# Flight Information
flight_info_frame = tk.LabelFrame(frame, text="Flight Information", bg="sky blue")
flight_info_frame.grid(row=0, column=0, padx=10, pady=5)

tk.Label(flight_info_frame, text="Destination:", bg="sky blue").grid(row=0, column=0, sticky=tk.W)
destination_entry = tk.Entry(flight_info_frame, textvariable=destination_var)
destination_entry.grid(row=0, column=1)

tk.Label(flight_info_frame, text="Departure Date:", bg="sky blue").grid(row=1, column=0, sticky=tk.W)
departure_date_entry = tk.Entry(flight_info_frame, textvariable=departure_date_var)
departure_date_entry.grid(row=1, column=1)

# Passenger Information
passenger_info_frame = tk.LabelFrame(frame, text="Passenger Information", bg="sky blue")
passenger_info_frame.grid(row=1, column=0, padx=10, pady=5)

tk.Label(passenger_info_frame, text="Passenger Name:", bg="sky blue").grid(row=0, column=0, sticky=tk.W)
full_name_entry = tk.Entry(passenger_info_frame, textvariable=full_name_var)
full_name_entry.grid(row=0, column=1)

tk.Label(passenger_info_frame, text="Number of Passengers", bg="sky blue").grid(row=1, column=0, sticky=tk.W)
passenger_count_entry = tk.Entry(passenger_info_frame, textvariable=passenger_count_var)
passenger_count_entry.grid(row=1, column=1)

tk.Label(passenger_info_frame, text="Passport Number:", bg="sky blue").grid(row=2, column=0, sticky=tk.W)
passport_number_entry = tk.Entry(passenger_info_frame, textvariable=passport_number_var)
passport_number_entry.grid(row=2, column=1)

tk.Label(passenger_info_frame, text="Class:", bg="sky blue").grid(row=3, column=0, sticky=tk.W)
classes = ['Economy Class', 'Business Class']
classs_entry = ttk.Combobox(passenger_info_frame, textvariable=classs_var, values=classes)
classs_entry.grid(row=3, column=1)

tk.Label(passenger_info_frame, text="Seat Preference:", bg="sky blue").grid(row=4, column=0, sticky=tk.W)
seat_preferences = ['Window Seat', 'Aisle Seat', 'Middle Seat']
seat_preference_entry = ttk.Combobox(passenger_info_frame, textvariable=seat_preference_var, values=seat_preferences)
seat_preference_entry.grid(row=4, column=1)

# Payment Information
tk.Label(frame, text="Payment Method:", bg="sky blue").grid(row=3, column=0, sticky=tk.W)
payment_options = ["Credit Card", "Debit Card", "Cash", "Online Payment", "Bank Transfer"]
payment_menu = ttk.Combobox(frame, textvariable=payment_method_var, values=payment_options)
payment_menu.grid(row=3, column=1)

# Total Cost
tk.Label(frame, text="Total Cost:", bg="sky blue").grid(row=4,column=0, sticky=tk.W)
tk.Label(frame, textvariable=total_cost_var, bg="sky blue").grid(row=4, column=1, sticky=tk.W)

# Buttons
buttons_frame = tk.Frame(frame, bg='sky blue')
buttons_frame.grid(row=5, column=0, pady=10)

add_button = tk.Button(buttons_frame, text="Add Reservation", command=add_reservation, bg="#4caf50", fg="white")
add_button.grid(row=0, column=0, padx=5)

update_button = tk.Button(buttons_frame, text="Update Reservation", command=update_reservation, bg="#4caf50", fg="white" )
update_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(buttons_frame, text="Delete Reservation", command=delete_reservation, bg="#4caf50", fg="white")
delete_button.grid(row=0, column=2, padx=5)

view_button = tk.Button(buttons_frame, text="View Reservations", command=view_reservations, bg="#4caf50", fg="white")
view_button.grid(row=0, column=3, padx=5)

available_flights_button = tk.Button(buttons_frame, text="Available Flights", command=show_available_flights, bg="#4caf50", fg="white")
available_flights_button.grid(row=0, column=4, padx=5)

past_flights_button = tk.Button(buttons_frame, text="Past Flights", command=show_past_flights, bg="#4caf50", fg="white")
past_flights_button.grid(row=0, column=5, padx=5)

confirm_button = tk.Button(buttons_frame, text="Confirm Ticket", command=confirm_ticket, bg="#4caf50", fg="white")
confirm_button.grid(row=1, column=0, padx=5)

return_button = tk.Button(buttons_frame, text="Return Ticket", command=return_ticket, bg="#4caf50", fg="white")
return_button.grid(row=1, column=1, padx=5)

root.mainloop()
