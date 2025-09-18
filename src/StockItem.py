import Item


class StockItem(Item):
    def __init__(self, id, created_at, item):
        super().__init__(item.name, item.description, item.price, item.stock, item.available, item.image)
        self.id = id
        self.created_at = created_at


    def queryAttributes(self):
        return {"id":self.id, "name":self.name, "description":self.description, "price":self.price, "stock":self.stock, "available":self.available, "image_url":self.image, "created_at":self.created_at}