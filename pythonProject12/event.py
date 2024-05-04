import pickle
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import os

class EventManagementGUI: # Generating a class to print the GUI
    def __init__(self, data_layer):
        self.data_layer = data_layer
        self.root = tk.Tk()
        self.root.geometry("600x600")
        self.root.title("Event Management System")
        # Add labels and fields for entering event id
        self.id_label = tk.Label(self.root, text="ID:")
        self.id_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        self.id_entry = tk.Entry(self.root)
        self.id_entry.grid(row=0, column=1)
        # Add labels and fields for entering event type
        self.type_label = tk.Label(self.root, text="Type:")
        self.type_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.type_entry = tk.Entry(self.root)
        self.type_entry.grid(row=1, column=1)
        # Add labels and fields for entering event theme
        self.theme_label = tk.Label(self.root, text="Theme:")
        self.theme_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.theme_entry = tk.Entry(self.root)
        self.theme_entry.grid(row=2, column=1)
        # Add labels and fields for entering event date
        self.date_label = tk.Label(self.root, text="Date:")
        self.date_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        self.date_entry = tk.Entry(self.root)
        self.date_entry.grid(row=3, column=1)
        # Add labels and fields for entering event time
        self.time_label = tk.Label(self.root, text="Time:")
        self.time_label.grid(row=4, column=0, sticky=tk.W, pady=5)
        self.time_entry = tk.Entry(self.root)
        self.time_entry.grid(row=4, column=1)
        # Add labels and fields for entering event duration
        self.duration_label = tk.Label(self.root, text="Duration:")
        self.duration_label.grid(row=5, column=0, sticky=tk.W, pady=5)
        self.duration_entry = tk.Entry(self.root)
        self.duration_entry.grid(row=5, column=1)
        # Add labels and fields for entering event address
        self.address_label = tk.Label(self.root, text="Venue Address:")
        self.address_label.grid(row=6, column=0, sticky=tk.W, pady=5)
        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(row=6, column=1)
        # Add labels and fields for entering event catering company
        self.catering_label = tk.Label(self.root, text="Catering Company:")
        self.catering_label.grid(row=7, column=0, sticky=tk.W, pady=5)
        self.catering_entry = tk.Entry(self.root)
        self.catering_entry.grid(row=7, column=1)
        # Add labels and fields for entering event cleaning company
        self.cleaning_label = tk.Label(self.root, text="Cleaning Company:")
        self.cleaning_label.grid(row=8, column=0, sticky=tk.W, pady=5)
        self.cleaning_entry = tk.Entry(self.root)
        self.cleaning_entry.grid(row=8, column=1)
        # Add labels and fields for entering event decorations company
        self.decorations_label = tk.Label(self.root, text="Decorations Company:")
        self.decorations_label.grid(row=9, column=0, sticky=tk.W, pady=5)
        self.decorations_entry = tk.Entry(self.root)
        self.decorations_entry.grid(row=9, column=1)
        # Add labels and fields for entering event entertainment company
        self.entertainment_label = tk.Label(self.root, text="Entertainment Company:")
        self.entertainment_label.grid(row=10, column=0, sticky=tk.W, pady=5)
        self.entertainment_entry = tk.Entry(self.root)
        self.entertainment_entry.grid(row=10, column=1)
        # Add labels and fields for entering event furniture supply company
        self.furniture_label = tk.Label(self.root, text="Furniture Supply Company:")
        self.furniture_label.grid(row=11, column=0, sticky=tk.W, pady=5)
        self.furniture_entry = tk.Entry(self.root)
        self.furniture_entry.grid(row=11, column=1)
        # Add labels and fields for entering event invoice
        self.invoice_label = tk.Label(self.root, text="Invoice:")
        self.invoice_label.grid(row=12, column=0, sticky=tk.W, pady=5)
        self.invoice_entry = tk.Entry(self.root)
        self.invoice_entry.grid(row=12, column=1)
        # Create buttons adding event to the GUI
        self.add_button = tk.Button(self.root, text="Add Event", command=self.add_event)
        self.add_button.grid(row=13, column=0, pady=5)
        # Create buttons deleting event from the GUI
        self.delete_button = tk.Button(self.root, text="Delete Event", command=self.delete_event)
        self.delete_button.grid(row=13, column=1, pady=5)
        # Create buttons modifying event to the GUI
        self.modify_button = tk.Button(self.root, text="Modify Event", command=self.modify_event)
        self.modify_button.grid(row=14, column=0, pady=5)
        # Create buttons displaying event to the GUI
        self.display_button = tk.Button(self.root, text="Display Event Details", command=self.display_event)
        self.display_button.grid(row=14, column=1, pady=5)
        # Create buttons displaying guest to event to the GUI
        self.display_button = tk.Button(self.root, text="Add Guest", command=self.guest_event)
        self.display_button.grid(row=14, column=5, pady=5)

        self.root.mainloop()

    def add_event(self): # Adding event to the attributes
        self.id.add_event(0, tk.END)
        self.type.add_event(0, tk.END)
        self.theme.add_event(0, tk.END)
        self.Date.add_event(0, tk.END)
        self.Time.add_event(0, tk.END)
        self.Duration.add_event(0, tk.END)
        self.VenueAddress.add_event(0, tk.END)
        self.CateringCompany.add_event(0, tk.END)
        self.CleaningCompany.add_event(0, tk.END)
        self.DecorationsCompany.add_event(0, tk.END)
        self.EntertainmentCompany.add_event(0, tk.END)
        self.FurnitureSupplyCompany.add_event(0, tk.END)
        self.Invoice.add_event(0, tk.END)

    def delete_event(self):# Deleting event from the attributes
        self.id.delete_event(0, tk.END)
        self.type.delete_event(0, tk.END)
        self.Theme.delete_event(0, tk.END)
        self.Date.delete_event(0, tk.END)
        self.Time.delete_event(0, tk.END)
        self.Duration.delete_event(0, tk.END)
        self.VenueAddress.delete_event(0, tk.END)
        self.CateringCompany.delete_event(0, tk.END)
        self.CleaningCompany.delete_event(0, tk.END)
        self.DecorationsCompany.delete_event(0, tk.END)
        self.EntertainmentCompany.delete_event(0, tk.END)
        self.FurnitureSupplyCompany.delete_event(0, tk.END)
        self.Invoice.delete_event(0, tk.END)

    def modify_event(self): # Modifying event to the attributes
        self.ID.modify_event(0, tk.END)
        self.Type.modify_event(0, tk.END)
        self.Theme.modify_event(0, tk.END)
        self.Date.modify_event(0, tk.END)
        self.Time.modify_event(0, tk.END)
        self.Duration.modify_event(0, tk.END)
        self.VenueAddress.modify_event(0, tk.END)
        self.CateringCompany.modify_event(0, tk.END)
        self.CleaningCompany.modify_event(0, tk.END)
        self.DecorationsCompany.modify_event(0, tk.END)
        self.EntertainmentCompany.modify_event(0, tk.END)
        self.FurnitureSupplyCompany.modify_event(0, tk.END)
        self.Invoice.modify_event(0, tk.END)

    def guest_event(self): # Adding guest to event  to the attributes
        self.ID.guest_event(0, tk.END)
        self.Type.guest_event(0, tk.END)
        self.Theme.guest_event(0, tk.END)
        self.Date.guest_event(0, tk.END)
        self.Time.guest_event(0, tk.END)
        self.Duration.guest_event(0, tk.END)
        self.VenueAddress.guest_event(0, tk.END)
        self.CateringCompany.guest_event(0, tk.END)
        self.CleaningCompany.guest_event(0, tk.END)
        self.DecorationsCompany.guest_event(0, tk.END)
        self.EntertainmentCompany.guest_event(0, tk.END)
        self.FurnitureSupplyCompany.guest_event(0, tk.END)
        self.Invoice.guest_event(0, tk.END)

    def display_event(self): #Displaying event to the getter function
        event_details = {
            "ID": self.id_entry.get(),
            "Type": self.type_entry.get(),
            "Theme": self.theme_entry.get(),
            "Date": self.date_entry.get(),
            "Time": self.time_entry.get(),
            "Duration": self.duration_entry.get(),
            "VenueAddress": self.address_entry.get(),
            "CateringCompany": self.catering_entry.get(),
            "CleaningCompany": self.cleaning_entry.get(),
            "DecorationsCompany": self.decorations_entry.get(),
            "EntertainmentCompany": self.entertainment_entry.get(),
            "FurnitureSupplyCompany": self.furniture_entry.get(),
            "Invoice": self.invoice_entry.get()}

        # Create a new window to display event details
        display_window = tk.Toplevel(self.root)
        display_window.title("Event Details")

        # Create a Treeview widget to display event details
        event_table = ttk.Treeview(display_window)
        event_table['columns'] = tuple(event_details.keys())
        for column in event_table['columns']:
            event_table.heading(column, text=column)
            event_table.column(column, anchor='center')
        event_table.grid(row=0, column=0, sticky='nsew')

        # Insert event details into the table
        event_table.insert('', 'end', values=tuple(event_details.values()))

        # Add a button to display all events
        display_all_button = tk.Button(display_window, text="Display All Events", command=self.display_all_events)
        display_all_button.grid(row=1, column=0, pady=5)

        display_window.mainloop()

    def display_all_events(self):
        all_events = [ #test cases
            Event("20247", "Wedding", "Black", "03-05-2024", "15:00", "3 hours", "Jumeirah St.", "20247", "Friends",
                  "Mara Catering", "DXB shiner", "DXB celebrations Co.", "Pixuol"),
            Event("1345", "Graduation", "Pink", "02-05-2024", "17:00", "7 hours", "Shakhbout St.", "683", "Family",
                  "Nowbl Catering", "Mitusbishi Co.", "2XL Co.", "Gaming arcade"),
        ]

        # Create a new window to display all events
        display_window = tk.Toplevel(self.root)
        display_window.title("All Events")

        # Create a Treeview widget to display events in a tabular format
        event_table = ttk.Treeview(display_window, columns=(
        'ID', 'Type', 'Theme', 'Date', 'Time', 'Duration', 'Address', 'Caterer', 'Cleaner', 'Decorator', 'Entertainer',
        'Furniture', 'Invoice'), show='headings')

        event_table.heading('ID', text='ID')
        event_table.heading('Type', text='Type')
        event_table.heading('Theme', text='Theme')
        event_table.heading('Date', text='Date')
        event_table.heading('Time', text='Time')
        event_table.heading('Duration', text='Duration')
        event_table.heading('Address', text='Address')
        event_table.heading('Caterer', text='Caterer')
        event_table.heading('Cleaner', text='Cleaner')
        event_table.heading('Decorator', text='Decorator')
        event_table.heading('Entertainer', text='Entertainer')
        event_table.heading('Furniture', text='Furniture')
        event_table.heading('Invoice', text='Invoice')

        # Insert each event into the table
        for event in all_events:
            event_table.insert('', 'end', values=(
            event.getEventID(), event.getType(), event.getTheme(), event.getDate(), event.getTime(),
            event.getDuration(), event.getVenueAddress(), event.getCateringCompany(), event.getCleaningCompany(),
            event.getDecorationsCompany(), event.getEntertainmentCompany(), event.getFurnitureSupplyCompany(),
            event.getInvoice()))

        event_table.pack(padx=10, pady=10, fill="both", expand=True)

        display_window.mainloop()

class EventTable:
    def __init__(self, data_layer):
        self.data_layer = data_layer
        self.root = tk.Tk()
        self.root.geometry('800x600')
        self.root.title("Event Details")

        self.table = ttk.Treeview(self.root, columns=('ID', 'Type', 'Theme', 'Date', 'Time', 'Duration', 'Venue Address', 'Catering Company', 'Cleaning Company','Decorations Company', 'Entertainment Company', 'Furniture Supply Company', 'Invoice'), show='headings')

        self.table.heading('ID', text='ID')
        self.table.heading('Type', text='Type')
        self.table.heading('Theme', text='Theme')
        self.table.heading('Date', text='Date')
        self.table.heading('Time', text='Time')
        self.table.heading('Duration', text='Duration')
        self.table.heading('Venue Address', text='Venue Address')
        self.table.heading('Catering Company', text='Catering Company')
        self.table.heading('Cleaning Company', text='Cleaning Company')
        self.table.heading('Decorations Company', text='Decorations Company')
        self.table.heading('Entertainment Company', text='Entertainment Company')
        self.table.heading('Furniture Supply Company', text='Furniture Supply Company')
        self.table.heading('Invoice', text='Invoice')
        self.table.pack(pady=20)

        events = self.data_layer.read_events()
        for event in events.items():
            self.table.insert('', 'end', values=(id, events.getEventID(), events.getType(), events.getTheme(), events.getDate(), events.getTime(),events.getDuration(), events.getVenueAddress(), events.getClientID(), events.getGuestList(),events.getCateringCompany(), events.getCleaningCompany(), events.getDecorationsCompany(),events.getEntertainmentCompany(), events.getFurnitureSupplyCompany(), events.getInvoice()))
            self.root.mainloop()

class Event:
    def __init__(self, eventID="", type="", theme="", date="", time="", duration="", venueAddress="", clientID="", guestList="", cateringCompany="",
                 cleaningCompany="", decorationsCompany="", entertainmentCompany="", furnitureSupplyCompany="", invoice=""):

        self.__eventID = eventID
        self.__type = type
        self.__theme = theme
        self.__date = date
        self.__time = time
        self.__duration = duration
        self.__venueAddress = venueAddress
        self.__clientID = clientID
        self.__guestList = guestList
        self.__cateringCompany = cateringCompany
        self.__cleaningCompany = cleaningCompany
        self.__decorationsCompany = decorationsCompany
        self.__entertainmentCompany = entertainmentCompany
        self.__furnitureSupplyCompany = furnitureSupplyCompany
        self.__invoice = invoice

    # Set methods

    def setEventID(self, eventID):
        self.__eventID = eventID

    def setType(self, type):
        self.__type = type

    def setTheme(self, theme):
        self.__theme = theme

    def setDate(self, date):
        self.__date = date

    def setTime(self, time):
        self.__time = time

    def setDuration(self, duration):
        self.__duration = duration

    def setVenueAddress(self, venueAddress):
        self.__venueAddress = venueAddress

    def setClientID(self, clientID):
        self.__clientID = clientID

    def setGuestList(self, guestList):
        self.__guestList = guestList

    def setCateringCompany(self, cateringCompany):
        self.__cateringCompany = cateringCompany

    def setCleaningCompany(self, cleaningCompany):
        self.__cleaningCompany = cleaningCompany

    def setDecorationsCompany(self, decorationsCompany):
        self.__decorationsCompany = decorationsCompany

    def setEntertainmentCompany(self, entertainmentCompany):
        self.__entertainmentCompany = entertainmentCompany

    def setFurnitureSupplyCompany(self, furnitureSupplyCompany):
        self.__furnitureSupplyCompany = furnitureSupplyCompany

    def setInvoice(self, invoice):
        self.__invoice = invoice

    def getEventID(self):
        return self.__eventID

    def getType(self):
        return self.__type

    def getTheme(self):
        return self.__theme

    def getDate(self):
        return self.__date

    def getTime(self):
        return self.__time

    def getDuration(self):
        return self.__duration

    def getVenueAddress(self):
        return self.__venueAddress

    def getClientID(self):
        return self.__clientID

    def getGuestList(self):
        return self.__guestList

    def getCateringCompany(self):
        return self.__cateringCompany

    def getCleaningCompany(self):
        return self.__cleaningCompany

    def getDecorationsCompany(self):
        return self.__decorationsCompany

    def getEntertainmentCompany(self):
        return self.__entertainmentCompany

    def getFurnitureSupplyCompany(self):
        return self.__furnitureSupplyCompany

    def getInvoice(self):
        return self.__invoice

    def __str__(self):
        return (f"Event ID: {self.__eventID}, Type: {self.__type}, Theme: {self.__theme}, Date: {self.__date}, Time: {self.__time}, Duration: {self.__duration}, Venue Address: {self.__venueAddress}, Client ID: {self.__clientID}, Guest list: {self.__guestList}, Catering Company: {self.__cateringCompany}, Cleaning Company: {self.__cleaningCompany}, Decorations Comapny: {self.__decorationsCompany}, Entertainment Company: {self.__entertainmentCompany}, Furniture Supply Company: {self.__furnitureSupplyCompany}, Invoice: {self.__invoive}")

class DataLayer:
    def __init__(self, filename):
        self.filename = filename

    def read_all_events(self):
            if not os.path.exists(filename):
                return {}
            else:
                with open(filename, 'rb') as file:
                    event = pickle.load(file)
                    return event

    def write_visitors_to_file(self, event):
            with open(filename, 'wb') as f:
                pickle.dump(event, f)

filename = "event.pkl"
dt = DataLayer(filename)
event = dt.read_all_events()
management = EventManagementGUI(dt)
showevent = EventTable(dt)