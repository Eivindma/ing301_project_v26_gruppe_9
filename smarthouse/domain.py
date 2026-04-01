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
    def __init__(self):
        self.floors : list[Floor] = []
        
    def add(self, floor: Floor):
        self.floors.append(floor)
        self.floors.sort(key=lambda f: f.level) #Sorting list after adding
        
    
    def get_floors(self):
        return self.floors
        
    

class Floor:
    def __init__(self, level : int):
        self.rooms : list[Room] = []
        self.level = level

    def get_area(self):
        return sum(room.area for room in self.rooms)
    
    def add(self, room: Room):
        
        self.rooms.append(room)
        return room
    
    def get_rooms(self):
        all_rooms = []
        for floor in self.get_floors():
            all_rooms.extend(floor.get_rooms())
        return self.rooms
    
    def __repr__(self):
        area = self.get_area()
        return f"Floor(level={self.level}, rooms={len(self.rooms)}, area={area:.1f}m²)"
        
        

class Room:
    def __init__(self, floor, area, name):
        self.floor = floor
        self.name = name
        self.area = area
        self.devices = []
        
    def add(self, device:Device):
        self.devices.append(device)
        
    def __repr__(self):
        return (f"Room(name='{self.name}', "
            f"area={self.area:.1f}m², "
            f"floor_level={self.floor.level})")
        
        

class Device():
    def __init__(self, id, supplier, model_name, 
                 deviceType, nickName, sensors: Sensor, actuators: Actuator):
        self.id = id
        self.supplier = supplier
        self.model_name = model_name
        self.deviceType = deviceType
        self.nickName = nickName
        self.Sensors = []
        self.actuators = []
        
    def is_sensor(self):
        pass
    
    def get_device_type(self):
        pass
    
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

class Motion_sensor:
    pass

class Temperature_sensor:
    pass

class Humidity_sensor:
    pass

class Current_sensor:
    pass
    
class Co2_sensor:
    pass

class Actuator(State):
    def __init__(self):
        super().__init__
        self.state = super().isOn

    def getState(self,):
        return self.state
    
    def setState(self, state):
        self.state = state


    
class Panel_heater:
    pass

class Air_condition:
    pass

class Humidifyer:
    pass

class Socket:
    pass

class Light:
    pass

class SmartHouse:
    def __init__(self):
        self.building = Building()
        
        

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
        
        floor = Floor(level)
        self.building.add(floor)
        return floor
        


    def register_room(self, floor, room_size, room_name = None):
        """
        This methods registers a new room with the given room areal size 
        at the given floor. Optionally the room may be assigned a mnemonic name.
        """
        if not isinstance(floor, Floor):
            raise TypeError(f"Expected Floor object, got {type(floor)}")
    
        room = Room(floor, room_size, room_name)   # Create the room correctly
        floor.add(room)                            # Add it to the actual floor
        return room


    def get_floors(self):
        """
        This method returns the list of registered floors in the house.
        The list is ordered by the floor levels, e.g. if the house has 
        registered a basement (level=0), a ground floor (level=1) and a first floor 
        (leve=1), then the resulting list contains these three flors in the above order.
        """
        return self.building.get_floors()


    def get_rooms(self):
        """
        This methods returns the list of all registered rooms in the house.
        The resulting list has no particular order.
        """
        rooms = []
        floors = self.building.get_floors()
        for floor in floors:
            rooms.extend(floor.get_rooms)
        return rooms



    def get_area(self):
        """
        This methods return the total area size of the house, i.e. the sum of the area sizes of each room in the house.
        """
        for room in all_rooms:
            area = 0
            area += room.area


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

