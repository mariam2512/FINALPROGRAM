import pickle
import tkinter as tk
from tkinter import ttk
import os

class GuestManagmentGUI: # Generating a class to print the GUI
    def __init__(self, data_layer):
        self.data_layer = data_layer
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("Guest Management System")
        # Add labels and fields for entering guest id
        self.guest_label = tk.Label(self.root, text="Guest ID:")
        self.guest_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        self.guest_entry = tk.Entry(self.root)
        self.guest_entry.grid(row=0, column=1)
        # Add labels and fields for entering guest name
        self.name_guest_label = tk.Label(self.root, text="Name Guest:")
        self.name_guest_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.name_guest_entry = tk.Entry(self.root)
        self.name_guest_entry.grid(row=1, column=1)
        # Add labels and fields for entering guest address.
        self.address_guest_label = tk.Label(self.root, text="Address Guest:")
        self.address_guest_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.address_guest_entry = tk.Entry(self.root)
        self.address_guest_entry.grid(row=2, column=1)
        # Add labels and fields for entering guest contact details.
        self.contact_details_guest_label = tk.Label(self.root, text="Contact details Guest:")
        self.contact_details_guest_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        self.contact_details_guest_entry = tk.Entry(self.root)
        self.contact_details_guest_entry.grid(row=3, column=1)

        # Create buttons adding guest to the GUI
        self.add_guest_button = tk.Button(self.root, text="Add guest", command=self.add_guest)
        self.add_guest_button.grid(row=4, column=0, pady=5)
        # Create buttons deleting guest from the GUI
        self.delete_guest_button = tk.Button(self.root, text="Delete guest", command=self.delete_guest)
        self.delete_guest_button.grid(row=4, column=1, pady=5)
        # Create buttons modifying guest to the GUI
        self.modify_guest_button = tk.Button(self.root, text="Modify guest", command=self.modify_guest)
        self.modify_guest_button.grid(row=5, column=0, pady=5)
        # Create buttons displaying guest to the GUI
        self.display_guest_details_button = tk.Button(self.root, text="Display guest Details",command=self.display_guest)
        self.display_guest_details_button.grid(row=5, column=1, pady=5)

        self.root.mainloop()

    def add_guest(self): # Adding guest to the attributes
        self.guest_entry.add_guest(tk.END, "Guest ID")
        self.name_guest_entry.add_guest(tk.END, "Name guest")
        self.address_guest_entry.add_guest(tk.END, "Address guest")
        self.contact_details_guest_entry.add_guest(tk.END, "Contact details guest")

    def delete_guest(self): # Deleting guest from the attributes
        self.guest_entry.delete_guest(0, tk.END)
        self.name_guest_entry.delete_guest(0, tk.END)
        self.address_guest_entry.delete_guest(0, tk.END)
        self.contact_details_guest_entry.delete_guest(0, tk.END)

    def modify_guest(self): # Modifying guest to the attributes
        self.guest_entry.modify_guest(0, tk.END)
        self.name_guest_entry.modify_guest(0, tk.END)
        self.address_guest_entry.modify_guest(0, tk.END)
        self.contact_details_guest_entry.modify_guest(0, tk.END)

    def display_guest(self): # Displaying guest to the attributes
        guest_details = {
            "Guest ID": self.guest_entry.get(),
            "Name": self.name_guest_entry.get(),
            "Address": self.address_guest_entry.get(),
            "Contact Details": self.contact_details_guest_entry.get(),
        }
        # Open a new window to show the guest details.
        display_window = tk.Toplevel(self.root)
        display_window.title("Guest Details")
        # Open a treeview widget to show the guest details.
        guest_table = ttk.Treeview(display_window)
        guest_table['columns'] = tuple(guest_details.keys())
        for column in guest_table['columns']:
            guest_table.heading(column, text=column)
            guest_table.column(column, anchor='center')
        guest_table.grid(row=0, column=0, sticky='nsew')
        # Fill the table with the values taken from the guest_details
        guest_table.insert('', 'end', values=tuple(guest_details.values()))

        display_window.mainloop()

class Guest:
    def __init__(self, guestID, nameGuest, addressGuest, contactDetailsGuest): # Attributes of class guest
        self.__guestID = guestID
        self.__nameGuest = nameGuest
        self.__addressGuest = addressGuest
        self.__contactDetailsGuest = contactDetailsGuest


    # Setter methods
    def setGuestID(self, guestID):
        self.__guestID = guestID

    def setNameGuest(self, nameGuest):
        self.__nameGuest = nameGuest

    def setAddressGuest(self, addressGuest):
        self.__addressGuest = addressGuest

    def setContactDetailsGuest(self, contactDetailsGuest):
        self.__contactDetailsGuest = contactDetailsGuest


    # Getter methods
    def getGuestID(self):
        return self.__guestID

    def getNameGuest(self):
        return self.__nameGuest

    def getAddressGuest(self):
        return self.__addressGuest

    def getContactDetailsGuest(self):
        return self.__contactDetailsGuest

class DataLayer: # Creating a class to input the pickle file
    def __init__(self, filename):
        self.filename = filename

    # Read all guests data from the pickle file
    def read_all_guests(self):
        if not os.path.exists(self.filename):
            return {}
        else:
            with open(self.filename, 'rb') as file:
                guests = pickle.load(file)
            return guests

    # Write guest data to the pickle file
    def write_guests_to_file(self, guests):
        with open(self.filename, 'wb') as f:
            pickle.dump(guests, f)

# Define the filename for the pickle file
filename = "guests.pkl"
# Create an instance of the DataLayer class
dt = DataLayer(filename)
# Initialize the GuestManagmentGUI using the DataLayer instance
management = GuestManagmentGUI(dt)