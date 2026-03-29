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
# TODO: continue registering the remaining floor, rooms and devices

print(ground_floor)

