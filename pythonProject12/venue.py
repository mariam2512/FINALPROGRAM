import pickle
import tkinter as tk
from tkinter import ttk
import os

class VenueManagmentGUI: # Generating a class to print the GUI
    def __init__(self, data_layer):
        self.data_layer = data_layer
        self.root = tk.Tk()
        self.root.geometry("500x400")
        self.root.title("Venue Management System")
        # Add labels and fields for entering venue id
        self.venue_id_label = tk.Label(self.root, text="Venue ID:")
        self.venue_id_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        self.venue_id_entry = tk.Entry(self.root)
        self.venue_id_entry.grid(row=0, column=1)
        # Add labels and fields for entering venue name
        self.name_venue_label = tk.Label(self.root, text="Name Venue:")
        self.name_venue_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.name_venue_entry = tk.Entry(self.root)
        self.name_venue_entry.grid(row=1, column=1)
        # Add labels and fields for entering venue address
        self.address_venue_label = tk.Label(self.root, text="Address Venue:")
        self.address_venue_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.address_venue_entry = tk.Entry(self.root)
        self.address_venue_entry.grid(row=2, column=1)
        # Add labels and fields for entering venue conteact
        self.contact_venue_label = tk.Label(self.root, text="Contact Venue:")
        self.contact_venue_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        self.contact_venue_entry = tk.Entry(self.root)
        self.contact_venue_entry.grid(row=3, column=1)
        # Add labels and fields for entering venue min guests
        self.min_guests_label = tk.Label(self.root, text="Minimum number of guests Venue:")
        self.min_guests_label.grid(row=4, column=0, sticky=tk.W, pady=5)
        self.min_guests_entry = tk.Entry(self.root)
        self.min_guests_entry.grid(row=4, column=1)
        # Add labels and fields for entering venue min guests
        self.max_guests_label = tk.Label(self.root, text="Maximum number of guests Venue:")
        self.max_guests_label.grid(row=5, column=0, sticky=tk.W, pady=5)
        self.max_guests_entry = tk.Entry(self.root)
        self.max_guests_entry.grid(row=5, column=1)

        # Create buttons adding venue to the GUI
        self.add_venue_button = tk.Button(self.root, text="Add venue", command=self.add_venue)
        self.add_venue_button.grid(row=6, column=0, pady=5)
        # Create buttons deleting venue from the GUI
        self.delete_venue_button = tk.Button(self.root, text="Delete venue", command=self.delete_venue)
        self.delete_venue_button.grid(row=6, column=1, pady=5)
        # Create buttons modifying venue to the GUI
        self.modify_venue_button = tk.Button(self.root, text="Modify venue", command=self.modify_venue)
        self.modify_venue_button.grid(row=7, column=0, pady=5)
        # Create buttons displaying venue to the GUI
        self.display_venue_details_button = tk.Button(self.root, text="Display venue Details", command=self.display_venue)
        self.display_venue_details_button.grid(row=7, column=1, pady=5)

        self.root.mainloop()

    def add_venue(self): # Adding venue to the attributes
        self.venue_id_entry.add_venue(tk.END, "Venue ID")
        self.name_venue_entry.add_venue(tk.END, "Name venue")
        self.address_venue_entry.add_venue(tk.END, "Address venue")
        self.contact_venue_entry.add_venue(tk.END, "Contact venue")
        self.min_guests_entry.add_venue(tk.END, "Minimum number of guests venue")
        self.max_guests_entry.add_venue(tk.END, "Maximum number of guests venue")

    def delete_venue(self): # Deleting venue from the attributes
        self.venue_id_entry.delete_venue(0, tk.END)
        self.name_venue_entry.delete_venue(0, tk.END)
        self.address_venue_entry.delete_venue(0, tk.END)
        self.contact_venue_entry.delete_venue(0, tk.END)
        self.min_guests_entry.delete_venue(0, tk.END)
        self.max_guests_entry.delete_venue(0, tk.END)

    def modify_venue(self): # Modifying venue to the attributes
        self.venue_id_entry.display_venue(0, tk.END)
        self.name_venue_entry.display_venue(0, tk.END)
        self.address_venue_entry.display_venue(0, tk.END)
        self.contact_venue_entry.display_venue(0, tk.END)
        self.min_guests_entry.display_venue(0, tk.END)
        self.max_guests_entry.display_venue(0, tk.END)

    def display_venue(self): # Displaying venue to the attributes
        venue_details = {
            "Venue ID": self.venue_id_entry.get(),
            "Name": self.name_venue_entry.get(),
            "Address": self.address_venue_entry.get(),
            "Contact Details": self.contact_venue_entry.get(),
            "Minimum Guests": self.min_guests_entry.get(),
            "Maximum Guests": self.max_guests_entry.get()
        }
        # Open a new window to show the venue details
        display_window = tk.Toplevel(self.root)
        display_window.title("Venue Details")
        # Open a treeview widget to show the venue details.
        venue_table = ttk.Treeview(display_window)
        venue_table['columns'] = tuple(venue_details.keys())
        for column in venue_table['columns']:
            venue_table.heading(column, text=column)
            venue_table.column(column, anchor='center')
        venue_table.grid(row=0, column=0, sticky='nsew')
        # Fill the table with the values taken from the venue_details
        venue_table.insert('', 'end', values=tuple(venue_details.values()))

        display_window.mainloop()

class Venue:
    def __init__(self, venueID, nameVenue, addressVenue, contactDetailsVenue):  # Attributes of class venue
        self.__venueID = venueID
        self.__nameVenue = nameVenue
        self.__addressVenue = addressVenue
        self.__contactDetailsVenue = contactDetailsVenue


    # Setter methods
    def setVenueID(self, venueID):
        self.__venueID = venueID

    def setNameVenue(self, nameVenue):
        self.__nameVenue = nameVenue

    def setAddressVenue(self, addressVenue):
        self.__addressVenue = addressVenue

    def setContactDetailsVenue(self, contactDetailsVenue):
        self.__contactDetailsVenue = contactDetailsVenue


    # Getter methods
    def getVenueID(self):
        return self.__venueID

    def getNameVenue(self):
        return self.__nameVenue

    def getAddressVenue(self):
        return self.__addressVenue

    def getContactDetailsVenue(self):
        return self.__contactDetailsVenue

class DataLayer: # Creating a class to input the pickle file
    def __init__(self, filename):
        self.filename = filename

    # Read all guests data from the pickle file
    def read_all_venue(self):
        if not os.path.exists(self.filename):
            return {}
        else:
            with open(self.filename, 'rb') as file:
                venue = pickle.load(file)
            return venue

    # Write guest data to the pickle file
    def write_venue_to_file(self, venue):
        with open(self.filename, 'wb') as f:
            pickle.dump(venue, f)

# Define the filename for the pickle file
filename = "venue.pkl"
# Create an instance of the DataLayer class
dt = DataLayer(filename)
# Initialize the VenueManagmentGUI using the DataLayer instance
management = VenueManagmentGUI(dt)