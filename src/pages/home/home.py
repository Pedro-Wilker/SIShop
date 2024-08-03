import customtkinter as ctk
from tkinter import PhotoImage

window = ctk.CTk()

frame_config = ctk.CTkFrame(
    master=window, 
    width=1100, 
    height=790
) 

frame_config.pack(side=RIGHT)
frame_login = frame_config

class Home():
    
    def __init__(self):
        self.window = window
        self.theme()
        self.screen()
        window.mainloop()
    
    def theme(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def screen(self):
        window.geometry("1280x800")
        window.title("Tela de Login")
        window.iconbitmap("../../img/icon.ico")
        window.resizable(False, False)
               



Home()