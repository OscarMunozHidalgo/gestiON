class Item:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def format(self):
        return {"name":self.name, "description":self.description, "price":self.price}