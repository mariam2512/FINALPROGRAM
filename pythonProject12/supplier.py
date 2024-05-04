import pickle
import tkinter as tk
from tkinter import ttk
import os

class SupplierManagmentGUI: # Generating a class to print the GUI
    def __init__(self, data_layer):
        self.data_layer = data_layer
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("Supplier Management System")
        # Add labels and fields for entering supplier id.
        self.supplier_id_label = tk.Label(self.root, text="Supplier ID:")
        self.supplier_id_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        self.supplier_id_entry = tk.Entry(self.root)
        self.supplier_id_entry.grid(row=0, column=1)
        # Add labels and fields for entering supplier name.
        self.name_supplier_label = tk.Label(self.root, text="Name:")
        self.name_supplier_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.name_supplier_entry = tk.Entry(self.root)
        self.name_supplier_entry.grid(row=1, column=1)
        # Add labels and fields for entering supplier address.
        self.address_supplier_label = tk.Label(self.root, text="Address:")
        self.address_supplier_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.address_supplier_entry = tk.Entry(self.root)
        self.address_supplier_entry.grid(row=2, column=1)
        # Add labels and fields for entering supplier contact.
        self.contact_supplier_label = tk.Label(self.root, text="Contact:")
        self.contact_supplier_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        self.contact_supplier_entry = tk.Entry(self.root)
        self.contact_supplier_entry.grid(row=3, column=1)
        # Add labels and fields for entering supplier products.
        self.products_supplier_label = tk.Label(self.root, text="Products:")
        self.products_supplier_label.grid(row=4, column=0, sticky=tk.W, pady=5)
        self.products_supplier_entry = tk.Entry(self.root)
        self.products_supplier_entry.grid(row=4, column=1)

        # Create buttons adding supplier to the GUI
        self.add_supplier_button = tk.Button(self.root, text="Add Supplier", command=self.add_supplier)
        self.add_supplier_button.grid(row=5, column=0, pady=5)
        # Create buttons deleting supplier from the GUI
        self.delete_supplier_button = tk.Button(self.root, text="Delete Supplier", command=self.delete_supplier)
        self.delete_supplier_button.grid(row=5, column=1, pady=5)
        # Create buttons to modify the supplier to the GUI
        self.modify_supplier_button = tk.Button(self.root, text="Modify Supplier", command=self.modify_supplier)
        self.modify_supplier_button.grid(row=6, column=0, pady=5)
        # Create buttons to display the supplier to the GUI
        self.display_supplier_details_button = tk.Button(self.root, text="Display Supplier Details",command=self.display_supplier)

        self.display_supplier_details_button.grid(row=6, column=1, pady=5)

        self.root.mainloop()

    def add_supplier(self): # Adding supplier to the attributes
            self.supplierID.add_supplier(0, tk.END)
            self.nameSupplier.add_supplier(0, tk.END)
            self.addressSupplier.add_supplier(0, tk.END)
            self.contactSupplier.add_supplier(0, tk.END)
            self.productsSupplier.add_supplier(0, tk.END)

    def delete_supplier(self): # Deleting supplier from the attributes
            self.supplierID.delete_supplier(0, tk.END)
            self.nameSupplier.delete_supplier(0, tk.END)
            self.addressSupplier.delete_supplier(0, tk.END)
            self.contactSupplier.delete_supplier(0, tk.END)
            self.productsSupplier.delete_supplier(0, tk.END)

    def modify_supplier(self): # Modifying supplier to the attributes
            self.supplierID.modify_supplier(0, tk.END)
            self.nameSupplier.modify_supplier(0, tk.END)
            self.addressSupplier.modify_supplier(0, tk.END)
            self.contactSupplier.modify_supplier(0, tk.END)
            self.productsSupplier.modify_supplier(0, tk.END)

    def display_supplier(self): # Displaying supplier using getter methods
        supplier_details = {
            "Supplier ID": self.supplier_id_entry.get(),
            "Name": self.name_supplier_entry.get(),
            "Address": self.address_supplier_entry.get(),
            "Contact": self.contact_supplier_entry.get(),
            "Products": self.products_supplier_entry.get()
        }

        # Open a new window to show the supplier details.
        display_window = tk.Toplevel(self.root)
        display_window.title("Supplier Details")

        # Open a treeview widget to show the supplier details.
        supplier_table = ttk.Treeview(display_window)
        # Determine which table columns to include depending on the supplier_details dictionary's keys.
        supplier_table['columns'] = tuple(supplier_details.keys())
        for column in supplier_table['columns']:
            supplier_table.heading(column, text=column)
            supplier_table.column(column, anchor='center')
        supplier_table.grid(row=0, column=0, sticky='nsew')
        # Fill the table with the values taken from the supplier_details
        supplier_table.insert('', 'end', values=tuple(supplier_details.values()))

        display_window.mainloop()

class Supplier:
    def __init__(self, supplierID, nameSupplier, addressSupplier, contactSupplier, productsSupplier): # Attributes of class supplier
        self.__supplierID = supplierID
        self.__nameSupplier = nameSupplier
        self.__addressSupplier = addressSupplier
        self.__contactSupplier = contactSupplier
        self.__productsSupplier = productsSupplier

    # Setter methods
    def setSupplierID(self, supplierID):
        self.__supplierID = supplierID

    def setNameSupplier(self, nameSupplier):
        self.__nameSupplier = nameSupplier

    def setAddressSupplier(self, addressSupplier):
        self.__addressSupplier = addressSupplier

    def setContactSupplier(self, contactSupplier):
        self.__contactSupplier = contactSupplier

    def setProductsSupplier(self, productsSupplier):
        self.__productsSupplier = productsSupplier

    # Getter methods
    def getSupplierID(self):
        return self.__supplierID

    def getNameSupplier(self):
        return self.__nameSupplier

    def getAddressSupplier(self):
        return self.__addressSupplier

    def getContactSupplier(self):
        return self.__contactSupplier

    def getProductsSupplier(self):
        return self.__productsSupplier

class DataLayer: # Creating a class to input the pickle file
    def __init__(self, filename):
        self.filename = filename

    # Read all supplier data from the pickle file
    def read_all_supplier(self):
        if not os.path.exists(self.filename):
            return {}
        else:
            with open(self.filename, 'rb') as file:
                supplier = pickle.load(file)
            return supplier

    # Write supplier data to the pickle file
    def write_supplier_to_file(self, supplier):
        with open(self.filename, 'wb') as f:
            pickle.dump(supplier, f)

# Define the filename for the pickle file
filename = "supplier.pkl"
# Create an instance of the DataLayer class
dt = DataLayer(filename)
# Initialize the SupplierManagmentGUI using the DataLayer instance
management = SupplierManagmentGUI(dt)