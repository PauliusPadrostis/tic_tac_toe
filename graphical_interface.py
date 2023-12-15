import tkinter as tk
from tkinter import *
from PIL import Image, ImageFilter, ImageTk

root = tk.Tk()  # Create main window
root.geometry("1280x720")  # Set main window size to "1280x720"
root.title("TIC-TAC-TOE")  # Set the title of the main window
root.resizable(False, False)  # Lock the window size

# Using PIL to blur out the background image
image = Image.open("background.png")
blurred_image = image.filter(ImageFilter.GaussianBlur(radius=7))

# Converting the blurred photo to a format usable by tkinter
blurred_photo = ImageTk.PhotoImage(blurred_image)

# Setting the background image
lbl_background = tk.Label(root, image=blurred_photo)
lbl_background.place(x=0, y=0, relwidth=1, relheight=1)

# Create frame for board
board_frame = tk.Frame()
board_frame.pack(pady=150)

# Change button creation
buttons = {}
current_player = "X"


def create_buttons():
    row = 0
    button_id = 1
    for x in range(0, 3):
        col = 0
        row += 1
        for xx in range(0, 3):
            col += 1
            b = tk.Button(master=board_frame, text="", width=16, height=8, relief="ridge",
                          command=lambda button_id=button_id: update_board(f"b{button_id}"))
            buttons[f"b{button_id}"] = b
            buttons[f"b{button_id}"].grid(row=row, column=col)
            button_id += 1


create_buttons()


# Create function to place 'x' or 'o' on buttons and check for current player and if square is empty.
def update_board(button):
    global current_player
    if buttons[button].cget("text") == "":
        if current_player == "X":
            buttons[button].config(text="X")
            current_player = "O"
        else:
            buttons[button].config(text="O")
            current_player = "X"
    else:
        pass


# Create function to check for horizontal / vertical / diagonal button occupancy
def check_win_condition(button_dict):
    pass


root.mainloop()
