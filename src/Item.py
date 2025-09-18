class Item:
    def __init__(self, name, description, price, stock, available, image):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.available = available
        self.image = image

    def setName(self, name):
        self.name = name

    def setDescription(self, description):
        self.description = description
    
    def setPrice(self, price):
        self.price = price
    
    def setStock(self, stock):
        self.stock = stock

    def setAvailable(self, availability):
        self.available = availability

    def setImage(self, image):
        self.image = image

    def setId(self, id):
        self.id = id

    def queryAttributes(self):
        return {"name":self.name, "description":self.description, "price":self.price, "stock":self.stock, "available":self.available, "image_url":self.image}