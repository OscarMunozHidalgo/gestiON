import customtkinter as ctk
from Item import *

class MainFrame(ctk.CTkFrame):
    def __init__(self, app):
        super().__init__(app)


        # Adding components
        self.button = ctk.CTkButton(self, text="Press me", fg_color="blue", font=("Arial", 30), command=self.button_callbck)
        self.label = ctk.CTkLabel(self, text="Hello world", text_color="green", font=("Arial", 25))
        self.scrollableFrame = ctk.CTkScrollableFrame(self)


        self.button.pack(pady=50)
        self.label.pack()
        self.scrollableFrame.pack()
    

    def button_callbck(self):
        item = Item("test", "this is a test item", 420.69, 100, False, None)

        print(self.controller.addRow("stock",item.queryAttributes()))
