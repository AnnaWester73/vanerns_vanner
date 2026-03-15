

class Excursion:
    def __init__(self):
        self.members = []
        self.rented_items = {}

    def get_members(self):
        return self.members

    def add_member(self, name):
        self.members.append(name)

    def remove_member(self, name):
        self.members.remove(name)

    def register_item_rented(self, member_name, item_name):
        if member_name not in self.rented_items:
            self.rented_items[member_name] = []
        self.rented_items[member_name].append(item_name)

    def register_item_returned(self, member_name, item_name):
        self.rented_items[member_name].remove(item_name)

    def get_all_who_has_not_returned_items(self):
        result = []

        for member, items in self.rented_items.items():
            if len(items) > 0:
                result.append(member)
        return result