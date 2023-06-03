#Import the required Libraries
from tkinter import *
from tkinter import ttk
import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

#Create an instance of Tkinter frame
win = customtkinter.CTk()
lbl=Label(window,text="Hello")
lbl.grid(column=0,row=0)
#Set the geometry of Tkinter frame
win.geometry("750x250")


#Create Buttons with proper position
button1= customtkinter.CTkButton(win, text= "Serch By Keyword")
button1.pack(side=TOP,padx=0.65,pady=0.65)
button2= customtkinter.CTkButton(win, text= "Serch By Country")
button2.pack(side=TOP,padx=7,pady=7)


win.mainloop()