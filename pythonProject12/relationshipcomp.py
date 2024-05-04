class Event:
    def __init__(self, eventID, eventName, venue, caterer):
        self.__eventID = eventID
        self.__eventName = eventName
        self.__venue = venue
        self.__caterer = caterer

    def event_details(self):
        return f"Event ID: {self.__eventID}\nEvent Name: {self.__eventName}\nVenue: {self.__venue.get_venue_details()}\nCaterer: {self.__caterer.get_caterer_details()}"
class Venue:
    def __init__(self, venueID, name, address, email, minCapacity, maxCapacity):
        self.__venueID = venueID
        self.__name = name
        self.__address = address
        self.__email = email
        self.__minCapacity = minCapacity
        self.__maxCapacity = maxCapacity

    def get_venue_details(self):
        return f"ID: {self.__venueID}, Name: {self.__name}, Address: {self.__address}, Email: {self.__email}, Min Capacity: {self.__minCapacity}, Max Capacity: {self.__maxCapacity}"

class Caterer:
    def __init__(self, catererID, name, email, menu):
        self.__catererID = catererID
        self.__name = name
        self.__email = email
        self.__menu = menu

    def get_caterer_details(self):
        return f"ID: {self.__catererID}, Name: {self.__name}, Email: {self.__email}, Menu: {', '.join(self.__menu)}"

venue1 = Venue("20247", "Luxury majlis", "DXB", "cg@gmail.com", 20, 100)
caterer1 = Caterer("20247", "Mara Catering", "bhj@gmail.com", ["International"])
event1 = Event("20247", "Come and See", venue1, caterer1)

print(event1.event_details())
