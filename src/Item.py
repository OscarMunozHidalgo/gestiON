class Item:
    def __init__(self, name, description, price, stock, available, image_url):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.available = available
        self.image_url = image_url

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

    def setImage(self, image_url):
        self.image_url = image_url

    def setId(self, id):
        self.id = id

    def queryAttributes(self):
        return {"name":self.name, "description":self.description, "price":self.price, "stock":self.stock, "available":self.available, "image_url":self.image_url}