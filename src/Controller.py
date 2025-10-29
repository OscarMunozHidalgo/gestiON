import Item

class Controller:
    def __init__(self, data):
        self.data = data

    def setCurrentData(self, newData):
        self.data = newData

    def addRow(self, table, newrow):
        return self.data.addRow(table, newrow)