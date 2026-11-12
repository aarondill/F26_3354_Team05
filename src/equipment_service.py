from enum import Enum

class EquipmentStatus(Enum):
    LOCKED_OUT = "LOCKED_OUT"
    AVAILABLE = "AVAILABLE"

class Equipment:
    def __init__(self, equipment_id, name, location, status):
        self.equipment_id = equipment_id
        self.name = name
        self.location = location
        self.status = status

    def get_status(self):
        return self.status

class EquipmentService:
    def __init__(self, equipment_map):
        self.equipment_map = equipment_map

    def get_equipment(self, equipment_id):
        return self.equipment_map.get(equipment_id)

    def get_status(self, equipment_id):
        equipment = self.get_equipment(equipment_id)
        if equipment is not None:
            return equipment.get_status()
        return None