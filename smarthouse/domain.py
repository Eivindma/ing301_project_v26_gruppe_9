import sys
import sqlite3


class Measurement:
    """
    This class represents a measurement taken from a sensor.
    """

    def __init__(self, timestamp, value, unit):
        self.timestamp = timestamp
        self.value = value
        self.unit = unit



# TODO: Add your own classes here!

class Building:
    def __init__(self, streetName: str, buildingNr: int, ):
        self.building = []

    def add(self, streetName, buildingNr):
        self.building.append([streetName, buildingNr])




class Floor(Building):
    def __init__(self, floorNr):
        self.floorNr = floorNr

    def floorAreal(self):
        

class Room(Floor):
    def __init__(self, roomName, areal):
        self.roomName = roomName
        self.areal = areal
        

class Units():
    def __init__(self, unitName):
        self.unitName = unitName

class Sensor():
    pass

class TemperatureSensor():
    pass

class AirQualitySensor():
    pass

class Co2Sensor():
    pass

class MovementSensor():
    pass

class Actuator():
    pass



class SmartHouse:
    """
    This class serves as the main entity and entry point for the SmartHouse system app.
    Do not delete this class nor its predefined methods since other parts of the
    application may depend on it (you are free to add as many new methods as you like, though).

    The SmartHouse class provides functionality to register rooms and floors (i.e. changing the 
    house's physical layout) as well as register and modify smart devices and their state.
    """

    def register_floor(self, level):
        """
        This method registers a new floor at the given level in the house
        and returns the respective floor object.
        """


    def register_room(self, floor, room_size, room_name = None):
        """
        This methods registers a new room with the given room areal size 
        at the given floor. Optionally the room may be assigned a mnemonic name.
        """
        pass


    def get_floors(self):
        """
        This method returns the list of registered floors in the house.
        The list is ordered by the floor levels, e.g. if the house has 
        registered a basement (level=0), a ground floor (level=1) and a first floor 
        (leve=1), then the resulting list contains these three flors in the above order.
        """
        pass


    def get_rooms(self):
        """
        This methods returns the list of all registered rooms in the house.
        The resulting list has no particular order.
        """
        pass


    def get_area(self):
        """
        This methods return the total area size of the house, i.e. the sum of the area sizes of each room in the house.
        """


    def register_device(self, room, device):
        """
        This methods registers a given device in a given room.
        """
        pass

    
    def get_device(self, device_id):
        """
        This method retrieves a device object via its id.
        """
        pass



class startMenu:
    def __init__(self):
        pass



    def quit(self):
        sys.exit()




print("Choose what you want to do \n1. Open existing project\n2. Create new project 3. Quit")
input1 = input()

if input == 1:
    print("Write name of new project")
    input2 = input()
    #sqlite3.
elif input == 3:
    startMenu().quit()