class Event:
    def __init__(self, eventID, type, theme, date, time, duration, venue, caterer, suppliers=None, clients=None,
                 guests=None):
        self.__eventID = eventID
        self.__type = type
        self.__theme = theme
        self.__date = date
        self.__time = time
        self.__duration = duration
        self.__venue = venue
        self.__caterer = caterer
        self.__suppliers = suppliers if suppliers else []
        self.__clients = clients if clients else []
        self.__guests = guests if guests else []

    def add_supplier(self, supplier):
        self.__suppliers.append(supplier)

    def add_client(self, client):
        self.__clients.append(client)

    def add_guest(self, guest):
        self.__guests.append(guest)

    def __str__(self):
        return f"Event ID: {self.__eventID}\nType: {self.__type}\nTheme: {self.__theme}\nDate: {self.__date}\nTime: {self.__time}\nDuration: {self.__duration}\nVenue: {self.__venue}\nCaterer: {self.__caterer}\n"


class Supplier:
    def __init__(self, supplierID, nameSupplier, addressSupplier, contactSupplier, productsSupplier):
        self.__supplierID = supplierID
        self.__nameSupplier = nameSupplier
        self.__addressSupplier = addressSupplier
        self.__contactSupplier = contactSupplier
        self.__productsSupplier = productsSupplier

    def __str__(self):
        return f"Supplier ID: {self.__supplierID}\nName: {self.__nameSupplier}\nAddress: {self.__addressSupplier}\nContact: {self.__contactSupplier}\nProducts: {self.__productsSupplier}\n"


class Client:
    def __init__(self, clientID, nameClient, addressClient, contactDetailsClient, budget):
        self.__clientID = clientID
        self.__nameClient = nameClient
        self.__addressClient = addressClient
        self.__contactDetailsClient = contactDetailsClient
        self.__budget = budget

    def __str__(self):
        return f"Client ID: {self.__clientID}\nName: {self.__nameClient}\nAddress: {self.__addressClient}\nContact: {self.__contactDetailsClient}\nBudget: {self.__budget}\n"


class Guest:
    def __init__(self, clientIDGuest, nameGuest, addressGuest, contactDetailsGuest):
        self.__clientIDGuest = clientIDGuest
        self.__nameGuest = nameGuest
        self.__addressGuest = addressGuest
        self.__contactDetailsGuest = contactDetailsGuest

    def __str__(self):
        return f"Guest ID: {self.__clientIDGuest}\nName: {self.__nameGuest}\nAddress: {self.__addressGuest}\nContact: {self.__contactDetailsGuest}\n"


supplier1 = Supplier("20247", "Mohammed", "MBZ city", "123456789", "Drinks")
client1 = Client("20247", "Zainab", "Shakhbout city", "123456789", 1000)
guest1 = Guest("20247", "Shahad", "Al Shamkha city", "123456789")
event1 = Event("20247", "Graduation", "Black and white", "03-05-2024", "18:00", 3, "Al Wahda Venue", "Mara Company")

print(supplier1)
print(client1)
print(guest1)
print(event1)
