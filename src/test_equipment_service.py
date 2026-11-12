from equipment_service import (
    Equipment,
    EquipmentService,
    EquipmentStatus,
)

def test_get_equipment_returns_matching_equipment():
    equipment = Equipment(
        1, "equipment_name", "location", EquipmentStatus.AVAILABLE
    )
    service = EquipmentService({1: equipment})

    assert service.get_equipment(1) is equipment

def test_get_equipment_returns_none_for_unknown_id():
    service = EquipmentService({})

    assert service.get_equipment(99) is None


def test_get_equipment_returns_equipment_for_another_id():
    equipment = Equipment(
        2, "equipment_name", "location", EquipmentStatus.AVAILABLE
    )
    service = EquipmentService({2: equipment})

    assert service.get_equipment(2) is equipment