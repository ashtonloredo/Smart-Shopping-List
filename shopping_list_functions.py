import json

class ShoppingList:
    def __init__(self):
        self.items = {}

    #List functions
    def add_item(self, item, quantity): #Done
        self.items[item] = self.items.get(item, 0) + quantity

    def remove_item(self, item, quantity): #Done
        if item not in self.items:
            return False
        self.items[item] -= quantity
        if self.items[item] <= 0:
            self.items.pop(item)
        return True

    def get_items(self): #Done
       return dict(self.items)

    def save_list(self):
        try:
            with open("grocery_list.json", 'w') as f:
                json.dump(self.items, f, indent=4, sort_keys=True)
            return True

        except OSError:
            return False

    def load_list(self):
        try:
            with open("grocery_list.json", 'r') as f:
                self.items = json.load(f)
            return True
        except FileNotFoundError:
            return False