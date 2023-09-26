import tkinter
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("600x440")
app.title("Login")

img1 = ImageTk.PhotoImage(Image.open("background.jpg"))
li = customtkinter.CTkLabel(master=app, image=img1)
li.pack()
frame = customtkinter.CTkFrame(master=li, width=320, height=360)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
l2 = customtkinter.CTkLabel(
    master=frame, text="Log into Your Account", font=('Century Gothic', 20))
l2.place(x=50, y=45)

entry1 = customtkinter.CTkEntry(
    master=frame, width=220, placeholder_text="Username")
entry1.place(x=50, y=110)

entry2 = customtkinter.CTkEntry(
    master=frame, width=220, placeholder_text="Password")
entry2.place(x=50, y=165)

l2 = customtkinter.CTkLabel(
    master=frame, text="Forgot Password", font=('Century Gothic', 12))
l2.place(x=165, y=195)

button1 = customtkinter.CTkButton(
    master=frame, width=220, text="Login", corner_radius=6)
button1.place(x=50, y=240)


img2 = ImageTk.PhotoImage(Image.open(
    "Google.png").resize(20, 20), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(Image.open(
    "Facebook.png").resize(20, 20), Image.ANTIALIAS)

button2 = customtkinter.CTkButton(master=frame, width=220, image=img2, text="Google",
                                  height=20, corner_radius=6, compound="left", text_color="Black")
button2.place(x=50, y=290)

button3 = customtkinter.CTkButton(master=frame, width=220, image=img3, text="Facebook",
                                  height=20, corner_radius=6, compound="left", text_color="Black")
button3.place(x=50, y=290)


app.mainloop()
