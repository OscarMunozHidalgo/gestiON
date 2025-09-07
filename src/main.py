from tkinter import *
import time
# Importing the two libraries
from customtkinter import *

from SupabaseLoader import SupabaseLoader

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

print(SupabaseLoader.load("items"))