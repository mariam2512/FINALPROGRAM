import pickle
import tkinter as tk
from tkinter import ttk
import os

class ClientManagmentGUI: # Generating a class to print the GUI
    def __init__(self, data_layer):
        self.data_layer = data_layer
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("Client Management System")
        # Add labels and fields for entering client id.
        self.client_id_label = tk.Label(self.root, text="Client ID:")
        self.client_id_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        self.client_id_entry = tk.Entry(self.root)
        self.client_id_entry.grid(row=0, column=1)
        # Add labels and fields for entering client name.
        self.name_client_label = tk.Label(self.root, text="Name:")
        self.name_client_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.name_client_entry = tk.Entry(self.root)
        self.name_client_entry.grid(row=1, column=1)
        # Add labels and fields for entering client address.
        self.address_client_label = tk.Label(self.root, text="Address:")
        self.address_client_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.address_client_entry = tk.Entry(self.root)
        self.address_client_entry.grid(row=2, column=1)
        # Add labels and fields for entering client contact details.
        self.contact_details_client_label = tk.Label(self.root, text="Contact Details:")
        self.contact_details_client_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        self.contact_details_client_entry = tk.Entry(self.root)
        self.contact_details_client_entry.grid(row=3, column=1)
        # Add labels and fields for entering client budget.
        self.budget_label = tk.Label(self.root, text="Budget:")
        self.budget_label.grid(row=4, column=0, sticky=tk.W, pady=5)
        self.budget_entry = tk.Entry(self.root)
        self.budget_entry.grid(row=4, column=1)

        # Create buttons adding client to the GUI
        self.add_client_button = tk.Button(self.root, text="Add client", command=self.add_client)
        self.add_client_button.grid(row=5, column=0, pady=5)
        # Create buttons deleting client from the GUI
        self.delete_client_button = tk.Button(self.root, text="Delete client", command=self.delete_client)
        self.delete_client_button.grid(row=5, column=1, pady=5)
        # Create buttons modifying client to the GUI
        self.modify_client_button = tk.Button(self.root, text="Modify client", command=self.modify_client)
        self.modify_client_button.grid(row=6, column=0, pady=5)
        # Create buttons displaying client to the GUI
        self.display_client_details_button = tk.Button(self.root, text="Display client Details",command=self.display_client)
        self.display_client_details_button.grid(row=6, column=1, pady=5)

        self.root.mainloop()

    def add_client(self): # Adding client to the attributes
            self.client_id_entry.add_client(0, tk.END)
            self.name_client_entry.add_client(0, tk.END)
            self.address_client_entry.add_client(0, tk.END)
            self.contact_details_client_entry.add_client(0, tk.END)
            self.budget_entry.add_client(0, tk.END)

    def delete_client(self): # Deleting supplier to the attributes
            self.client_id_entry.delete_client(0, tk.END)
            self.name_client_entry.delete_client(0, tk.END)
            self.address_client_entry.delete_client(0, tk.END)
            self.contact_details_client_entry.delete_client(0, tk.END)
            self.budget_entry.delete_client(0, tk.END)

    def modify_client(self): # Modifying supplier to the attributes
            self.client_id_entry.modify_client(0, tk.END)
            self.name_client_entry.modify_client(0, tk.END)
            self.address_client_entry.modify_client(0, tk.END)
            self.contact_details_client_entry.modify_client(0, tk.END)
            self.budget_entry.modify_client(0, tk.END)

    def display_client(self): # Displaying supplier to the attributes
        client_details = {
            "Client ID": self.client_id_entry.get(),
            "Name": self.name_client_entry.get(),
            "Address": self.address_client_entry.get(),
            "Contact Details": self.contact_details_client_entry.get(),
            "Budget": self.budget_entry.get()
        }
        # Open a new window to show the client details.
        display_window = tk.Toplevel(self.root)
        display_window.title("Client Details")
        # Open a treeview widget to show the client details.
        client_table = ttk.Treeview(display_window)
        client_table['columns'] = tuple(client_details.keys())
        for column in client_table['columns']:
            client_table.heading(column, text=column)
            client_table.column(column, anchor='center')
        client_table.grid(row=0, column=0, sticky='nsew')
        # Fill the table with the values taken from the client_details
        client_table.insert('', 'end', values=tuple(client_details.values()))

        display_window.mainloop()

class Client:
    def __init__(self, clientID, nameClient, addressClient, contactDetailsClient, budget): # Attributes of class client
        self.__clientID = clientID
        self.__nameClient = nameClient
        self.__addressClient = addressClient
        self.__contactDetailsClient = contactDetailsClient
        self.__budget = budget

    # Setter methods
    def setClientID(self, clientID):
        self.__clientID = clientID

    def setNameClient(self, nameClient):
        self.__nameClient = nameClient

    def setAddressClient(self, addressClient):
        self.__addressClient = addressClient

    def setContactDetailsClient(self, contactDetailsClient):
        self.__contactDetailsClient = contactDetailsClient

    def setBudget(self, budget):
        self.__budget = budget

    # Getter methods
    def getClientID(self):
        return self.__clientID

    def getNameClient(self):
        return self.__nameClient

    def getAddressClient(self):
        return self.__addressClient

    def getContactDetailsClient(self):
        return self.__contactDetailsClient

    def getBudget(self):
        return self.__budget

class DataLayer: # Creating a class to input the pickle file
    def __init__(self, filename):
        self.filename = filename
    # Read all clients data from the pickle file
    def read_all_clients(self):
        if not os.path.exists(self.filename):
            return {}
        else:
            with open(self.filename, 'rb') as file:
                clients = pickle.load(file)
            return clients
    # Write client data to the pickle file
    def write_client_to_file(self, client):
        with open(self.filename, 'wb') as f:
            pickle.dump(client, f)

# Define the filename for the pickle file
filename = "client.pkl"
# Create an instance of the DataLayer class
dt = DataLayer(filename)
# Initialize the ClientManagmentGUI using the DataLayer instance
management = ClientManagmentGUI(dt)