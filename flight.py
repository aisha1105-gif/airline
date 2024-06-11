import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import tkinter.font
import os

def create_widgets(root):
    # Load the image
    image = tk.PhotoImage(file="ari.png")

    # Create a label to display the image
    image_label = tk.Label(root, image=image, bg="sky Blue")
    image_label.grid(row=0, columnspan=2, pady=10, sticky="nsew")  # Center align vertically and horizontally

    # Ensure the image doesn't get garbage collected
    image_label.image = image

    # Labels and Entry Widgets
    tk.Label(root, text="First Name", bg="sky blue").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    first_name = tk.Entry(root)
    first_name.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    tk.Label(root, text="Last Name", bg="sky blue").grid(row=3, column=0, padx=10, pady=10, sticky="e")
    last_name = tk.Entry(root)
    last_name.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    tk.Label(root, text="Phone Number", bg="sky blue").grid(row=5, column=0, padx=10, pady=10, sticky="e")
    phone = tk.Entry(root)
    phone.grid(row=5, column=1, padx=10, pady=10, sticky="w")

    # Proceed Button
    tk.Button(root, text="Book", command=lambda: proceed(first_name, last_name, phone), bg="#2196f3", fg="white").grid(row=9, columnspan=2, pady=10)

    # Exit button
    tk.Button(root, text="Exit", command=exit_program, bg="#4caf50", fg="white").grid(row=10, columnspan=2, pady=10)

    # Text label below the image
    text_label = tk.Label(root, text="Welcome to Skyline Aviation", bg="Royal Blue", fg="white", font=("Helvetica", 16))
    text_label.grid(row=1, columnspan=2, pady=10, sticky="nsew")  # Center align vertically and horizontally

def proceed(first_name, last_name, phone):
    try:
        os.system('python flight_schedule.py')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to proceed: {e}")

def exit_program():
    root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Skyline Aviation Airways")
    icon = tk.PhotoImage(file="3.png")
    root.iconphoto(True, icon)
    root.configure(bg="sky blue")  # Set background color
    create_widgets(root)
    root.mainloop()
   
   
