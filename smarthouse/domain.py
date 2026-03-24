import sys
import sqlite3 as sq
import datetime as dt

class Measurement():
    """
    This class represents a measurement taken from a sensor.
    """

    def __init__(self, timestamp:dt.datetime, 
                 value:float, unit:str):
        self.timestamp = timestamp
        self.value = value
        self.unit = unit


class State():
    def __init__(self, isOn:bool, 
                 targetTemperature:float, dimLevel:int):
        self.isOn = isOn
        self.targetTemperature = targetTemperature
        self.dimLevel = dimLevel

# TODO: Add your own classes here!

class Building:
    def __init__(self, streetName: str, buildingNr: int, ):
        self.building = []

    def add(self, id, name):
        self.id = id
        self.name = name

class Floor:
    def __init__(self, number):
        self.number = number

    def get_area(self):
        pass
        

class Room(Floor):
    def __init__(self, name, area):
        self.name = name
        self.area = area
        

class Device():
    def __init__(self, id, manufacturer, model, 
                 deviceType, nickName):
        self.id = id
        self.manufacturer = manufacturer
        self.model = model
        self.deviceType = deviceType
        self.nickName = nickName

class Sensor(Measurement):
    def __init__(self):
        super().__init__
        self.value = super().value
        self.timestamp = super().timestamp
        self.unit = super().unit
        self.valueHistory = []


    def lastMeasurement(self):
        return [self.timestamp, self.value, self.unit]

    def historicalMeasurement(self):
        pass

class Actuator(State):
    def __init__(self):
        super().__init__
        self.state = super().isOn

    def getState(self,):
        return self.state
    
    def setState(self, state):
        self.state = state








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
    
    
conn = sq.Connection("dbfile.sqlite")
cursor = conn.cursor()

cursor.execute("")
conn.commit()
cursor.close()

def main():
    is_active = True
    
    connection = sq.Connection("smarthouse.sqlite")
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT timestamp, latitude, longitude FROM routes")
        for row in cursor.fetchall():
            timestamp = datetime.fromisoformat(row[0])
            latitude = row[1]
            longitude = row[2]
            route.add(Point(timestamp, latitude, longitude))
    except sqlite3.OperationalError:
        print("No existing route found in route.sqlite")
    finally:
        cursor.close()
        connection.close()

    while is_active:
        print("---- Bike Computer ----\nSelect option:\n1. Track route\n2. Show Route\n3. Save\n4. Quit\n")
        user_input = input(">>> ")
        if not user_input.isdigit() and int(user_input) in {1, 2, 3, 4}:
            print(f"Unrecognized input: '{user_input}'")
        else:
            selected_option = int(user_input)
            if selected_option == 1:
                no_sample = int(input("How many segments do you want to track: "))
                for _ in range(no_sample):
                    route.add(sensor.sample())
                print(f"recorded {no_sample} segments")
            elif selected_option ==2:
                print(route)
            elif selected_option == 3:
                route.save()
            else:
                is_active = False
    print("shutting down")


if __name__ == "__main__":
    main()