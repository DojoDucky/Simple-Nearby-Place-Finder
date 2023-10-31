import sqlite3
import tkinter as tk
from tkinter import ttk

class Location:
    def __init__(self):
        self.connection = sqlite3.connect('placesData.db')
        self.cursor = self.connection.cursor()

    def load_location(self, placeType):
        self.cursor.execute("""
        SELECT *
        FROM locations
        WHERE place_type = ?;
        """, (placeType,))
        result = self.cursor.fetchall()

        if result:
            placeType, placeName, placeAddress, priceRange = result[0]
            self.placeType = placeType
            self.placeName = placeName
            self.placeAddress = placeAddress
            self.priceRange = priceRange
        else:
            print("Location not found")

    def __str__(self):
        return f"Place Type: {self.placeType}\nPlace Name: {self.placeName}\nPlace Address: {self.placeAddress}\nPrice Range: {self.priceRange}"

    def display_all_places_by_type(self, placeType):
        self.cursor.execute("""
        SELECT *
        FROM locations
        WHERE place_type = ?;
        """, (placeType,))
        results = self.cursor.fetchall()

        if results:
            result_text = f"Displaying all places of type '{placeType}':\n"
            for result in results:
                placeType, placeName, placeAddress, priceRange = result
                result_text += f"Place Type: {placeType}\nPlace Name: {placeName}\nPlace Address: {placeAddress}\nPrice Range: {priceRange}\n\n"
            return result_text
        else:
            return f"No places of type '{placeType}' found"

def show_places():
    place_type = entry.get().strip().title()
    result_text = p1.display_all_places_by_type(place_type)
    display_text.config(state=tk.NORMAL)
    display_text.delete("1.0", tk.END)
    display_text.insert(tk.END, result_text)
    display_text.config(state=tk.DISABLED)

p1 = Location()

# Create a Tkinter window
root = tk.Tk()
root.title("Place Locator")

# Create a style
style = ttk.Style()
style.configure("TFrame", background="#FDF3E7")  # Light beige background
style.configure("TLabel", background="#FDF3E7", font=("Arial", 12))
style.configure("TButton", background="#FF6B6B", foreground="black", font=("Arial", 12))  # Red button with white text
style.configure("TEntry", font=("Arial", 12))

# Create input and display widgets
frame = ttk.Frame(root, style="TFrame")
input_label = ttk.Label(frame, text="Enter the place type:")
entry = ttk.Entry(frame)
display_text = tk.Text(frame, wrap=tk.WORD, height=20, width=50)  # Adjust the height and width here
display_text.config(state=tk.DISABLED)
show_button = ttk.Button(frame, text="Show Places", command=show_places)

# Pack widgets
frame.pack(padx=20, pady=20)
input_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry.grid(row=0, column=1, padx=10, pady=10)
show_button.grid(row=1, columnspan=2, pady=20)
display_text.grid(row=2, columnspan=2)

root.mainloop()
