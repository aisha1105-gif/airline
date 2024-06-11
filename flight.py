import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import tkinter.font
import os
class AirlineReservationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Skyline Aviation Airways")
        # Creating a PhotoImage object from an image file
        icon = tk.PhotoImage(file="3.png")
        # Setting the icon using the iconphoto() method
        root.iconphoto(True, icon)
        self.root.configure(bg="sky blue")  # Set background color
        self.create_widgets()
        
    def create_widgets(self):
    # Load the image
       image = tk.PhotoImage(file="ari.png")

    # Create a label to display the image
       image_label = tk.Label(self.root, image=image, bg="Royal Blue")
       image_label.grid(row=0, columnspan=2, pady=10, sticky="nsew")  # Center align vertically and horizontally

    # Ensure the image doesn't get garbage collected
       image_label.image = image

    # Labels and Entry Widgets
       tk.Label(self.root, text="First Name", bg="white").grid(row=1, column=0, padx=10, pady=10, sticky="e")
       self.first_name = tk.Entry(self.root)
       self.first_name.grid(row=1, column=1, padx=10, pady=10, sticky="w")

       tk.Label(self.root, text="Last Name", bg="white").grid(row=2, column=0, padx=10, pady=10, sticky="e")
       self.last_name = tk.Entry(self.root)
       self.last_name.grid(row=2, column=1, padx=10, pady=10, sticky="w")

       tk.Label(self.root, text="Phone Number", bg="white").grid(row=4, column=0, padx=10, pady=10, sticky="e")
       self.phone = tk.Entry(self.root)
       self.phone.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    # Proceed Button
       tk.Button(self.root, text="Book", command=self.proceed, bg="#2196f3", fg="white").grid(row=8, columnspan=2, pady=10)

    # Exit button
       tk.Button(self.root, text="Exit", command=self.exit_program, bg="#4caf50", fg="white").grid(row=9, columnspan=2, pady=10)

    # Text label below the image
       text_label = tk.Label(self.root, text="Welcome to Skyline Aviation", bg="Royal Blue", fg="white", font=("Helvetica", 16))
       text_label.grid(row=10, columnspan=2, pady=10, sticky="nsew")  # Center align vertically and horizontally
    
    def proceed(self):
        # Execute the external script
        try:
            os.system('python flight_schedule.py')
        except Exception as e:
            messagebox.showerror("Error", f"Failed to proceed: {e}")

    def clear_fields(self):
        self.first_name.delete(0, tk.END)
        self.last_name.delete(0, tk.END)
        self.phone.delete(0, tk.END)

    def get_next_reservation_number(self):
        try:
            with open('reservation_number.txt', 'r') as file:
                content = file.read().strip()
                if content:
                    reservation_number = int(content)
                else:
                    reservation_number = 0
        except (FileNotFoundError, ValueError):
            reservation_number = 0

        reservation_number += 1

        with open('reservation_number.txt', 'w') as file:
            file.write(str(reservation_number))

        return reservation_number
    def exit_program(self):
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AirlineReservationForm(root)
    root.mainloop()
   
