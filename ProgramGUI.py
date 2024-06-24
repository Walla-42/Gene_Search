import tkinter as tk
from PIL import ImageTk
import sqlite3

bg_color = "#000000"

def fetch_db():
    connection = sqlite3.connect("")
    cursor = connection.cursor()
    cursor.execute()
    all_tables = cursor.fetchall()
    print(all_tables[0])
    connection.close()

def load_frame1():
    frame1.pack_propagate(False)
    logo_img = ImageTk.PhotoImage(file="Images/Gene_Search_Logo.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack()

    #Entry message
    tk.Label(
        frame1,
        text="Welcome to the Gene Search Application",
        bg=bg_color,
        fg="white",
        font=("TkMenuFont", 14)
    ).pack()

    #Main Menu Button
    tk.Button(
        frame1,
        text="Get Started",
        font=("TkHeadingFont", 20),
        bg="#0350b4",
        fg="#000000",
        cursor="hand2",
        activebackground="#227ff8",
        activeforeground="#000000",
        command=lambda:load_frame2()
        ).pack(pady=20)

def load_frame2():
    fetch_db()


#initalize app  
root = tk.Tk()
root.title("Gene Search Application")

root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, width=500, height=400, bg=bg_color)
frame2 = tk.Frame(root, bg=bg_color)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0)

load_frame1()


root.mainloop()