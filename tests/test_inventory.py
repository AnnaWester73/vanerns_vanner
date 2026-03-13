from src.inventory import Inventory

# Test att items läggs till
def test_set_item():
    inventory = Inventory()

    inventory.set_item("Tält", 100, 5)

    assert inventory.get_amount_left("Tält") == 5

# Test att lagret minskar vid uthyrning
def test_rent():
    inventory = Inventory()
    inventory.set_item("Tält", 100, 5)

    inventory.rent("Tält")

    assert inventory.get_amount_left("Tält") == 4

# Testar att funktionen get_amount_left fungerar
def test_get_amount_left():
    inventory = Inventory()
    inventory.set_item("Tält", 100, 5)

    amount = inventory.get_amount_left("Tält")

    assert amount == 5