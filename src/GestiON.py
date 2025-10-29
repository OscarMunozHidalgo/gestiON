import os
import customtkinter as ctk

from Supabase import *
from dotenv import load_dotenv

from Controller import *
from Item import *
from View import *

load_dotenv()

url= os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
database = Supabase(url, key)

#item = Item("test", "this is a test item", 420.69, 100, False, None)
#print(database.addRow("stock",item.queryAttributes()))

controller = Controller(database)

ctk.set_appearance_mode("system")

app = View(controller)
app.mainloop()
