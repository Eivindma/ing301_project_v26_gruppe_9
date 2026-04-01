import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from smarthouse.domain import SmartHouse

DEMO_HOUSE = SmartHouse()

# Building house structure
ground_floor = DEMO_HOUSE.register_floor(1)
entrance = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance")
bedroom1 = DEMO_HOUSE.register_room(ground_floor, 13.5, "Bedroom1")
entrance2 = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance2")
bedroom2 = DEMO_HOUSE.register_room(ground_floor, 13.5, "Bedroom2")
livingroom1 = DEMO_HOUSE.register_room(ground_floor, 13.5, "livingroom1")
livingroom2 = DEMO_HOUSE.register_room(ground_floor, 13.5, "livingroom2")
livingroom3 = DEMO_HOUSE.register_room(ground_floor, 13.5, "livingroom3")
bedroom3 = DEMO_HOUSE.register_room(ground_floor, 13.5, "Bedroom3")
bedroom4 = DEMO_HOUSE.register_room(ground_floor, 13.5, "bedroom4")

#panelovn_registered = DEMO_HOUSE.register_device(entrance, Device(test,test,test,test))
# TODO: continue registering the remaining floor, rooms and devices

print(DEMO_HOUSE.get_floors())

print(DEMO_HOUSE.get_rooms())

print(DEMO_HOUSE.get_area())
