from tkinter import*
import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
root=customtkinter.CTk() #first button
root1=customtkinter.CTk() 
root.geometry("300x400")
root1.geometry("300x400")
button=customtkinter.CTkButton(master=root, text="Select by Keyword")
button1=customtkinter.CTkButton(master=root1,text="Select by Country")
button.place(relx=0.45,rely=0.45, anchor=CENTER)
button.place(relx=7,rely=7,anchor=CENTER)
root.mainloop()
root1.mainloop()