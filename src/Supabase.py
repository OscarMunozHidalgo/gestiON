from SupabaseLoader import *
from supabase import create_client


class Supabase:
    def __init__(self, url, key):
       self.reference = SupabaseLoader.load(url, key)

    def getTable(self, table):
        return self.reference.table(table).select("*").execute()

    def addRow(self, table, element):
        return self.reference.table(table).insert(element).execute()
    
    def updateRow(self, table, rowId, newRow):
        return self.reference.table(table).update(newRow).eq("id", rowId).execute()

    def deleteRow(self, table, rowId):
        return self.reference.table(table).delete().eq("id",rowId).execute()

