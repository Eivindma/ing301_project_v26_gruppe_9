import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from smarthouse.domain import SmartHouse

DEMO_HOUSE = SmartHouse()

# Building house structure
ground_floor = DEMO_HOUSE.register_floor(1)
first_floor = DEMO_HOUSE.register_floor(2)
guest_room_1 = DEMO_HOUSE.register_room(ground_floor, 6.3, "bathroom")
guest_room_1 = DEMO_HOUSE.register_room(ground_floor, 8, "guest room 1")
living_room_kitchen = DEMO_HOUSE.register_room(ground_floor, 39.75, "living room kitchen")
entrance = DEMO_HOUSE.register_room(ground_floor, 13.5, "entrance")
garage = DEMO_HOUSE.register_room(ground_floor, 19, "garage")
guest_room_2 = DEMO_HOUSE.register_room(first_floor, 8, "guest_room 2")
bathroom_2 = DEMO_HOUSE.register_room(first_floor, 9.25, "bathroom 2")
office = DEMO_HOUSE.register_room(first_floor, 11.75, "office")
guest_room_3 = DEMO_HOUSE.register_room(first_floor, 10, "guest room_3")
dressing_room = DEMO_HOUSE.register_room(first_floor, 4, "dresing room")
master_bedroom = DEMO_HOUSE.register_room(first_floor, 17, "master bedroom")
hallway = DEMO_HOUSE.register_room(first_floor, 10, "hallway")


#panelovn_registered = DEMO_HOUSE.register_device(entrance, Device(test,test,test,test))
# TODO: continue registering the remaining floor, rooms and devices

print(DEMO_HOUSE.get_floors())

print(DEMO_HOUSE.get_rooms())

print(DEMO_HOUSE.get_area())
