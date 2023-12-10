import sys
from models.game import TicTacToe
from models.player import Player
import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = tkinter.Tk()
root.geometry("1400x800")
root.title("TIC-TAC-TOE")

button_coords = [(0.37, 0.75), (0.50, 0.75), (0.63, 0.75), (0.37, 0.523), (0.50, 0.523), (0.63, 0.523),
                 (0.37, 0.296), (0.50, 0.296), (0.63, 0.296)]


def button_function():
    pass


buttons = {}

for i, button_coords in enumerate(button_coords):
    button = customtkinter.CTkButton(master=root, text=" ", border_color="black", border_width=2, width=170, height=170,
                                     corner_radius=1, fg_color="transparent", command=button_function())

    button.place(relx=button_coords[0], rely=button_coords[1], anchor=tkinter.CENTER)
    buttons[f"b{i+1}"] = button


root.mainloop()
