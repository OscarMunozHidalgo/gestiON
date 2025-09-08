from tkinter import *
import time
from customtkinter import *

from Supabase import *
from Item import *
from dotenv import load_dotenv

load_dotenv()
# Creating the window and making it fullscreen with tkinter
""" root = Tk()
root.attributes('-fullscreen', True)

# Adding modern-looking widgets with customtkinter
button = CTkButton(root, text="Press me", fg_color="blue", font=("Arial", 30))
label = CTkLabel(root, text="Hello world", text_color="green", font=("Arial", 25))

button.pack(pady=50)
label.pack()

# Calling the mainloop
root.mainloop()
 """
url= os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
database = Supabase(url, key)

print(database.getTable("items"))

item = Item("name", "description", 12.50)

print(database.addRow("items",item.format()))

print(database.getTable("items"))
