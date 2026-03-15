from src.item import Item

class Inventory:
    def __init__(self):
        self.items = {}

    def set_item(self, name, rent_price, amount):
        self.items[name] = Item(name, rent_price, amount)

    def rent(self, item_name):
        if item_name in self.items:
            item = self.items[item_name]
            item.amount -= 1

    def get_amount_left(self, name):
        return self.items[name].amount
