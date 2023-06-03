from tkinter import *
import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

window = customtkinter.CTk()

window.title("Newsify!!")

window.geometry('350x200')

lbl = Label(window, text="Welcome to Newsify!")

lbl.grid(column=0, row=0)

def clicked():

    lbl.configure(text="LOL !!")

btn = customtkinter.CTkButton(window, text="Click Me", command=clicked)

btn.grid(column=1, row=0)

window.mainloop()