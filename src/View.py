import customtkinter as ctk
from Controller import *
from Supabase import *
from Item import *
from components import SidebarFrame, MainFrame

class View(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("gestiON")
        
        screenResolution = str(self.winfo_screenwidth()) + "x" + str(self.winfo_screenheight())
        self.geometry(screenResolution)

        # Grid config
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar = SidebarFrame(self)
        self.sidebar.grid(row=0, column=0, rowspan=4, padx=10, pady=(10, 0), sticky="nsew")

        self.checkbox_frame = MainFrame(self)
        self.checkbox_frame.grid(row=0, column=1, rowspan=4, padx=10, pady=(10, 0), sticky="nsew")
