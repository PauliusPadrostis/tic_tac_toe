import tkinter as tk
from tkinter import *
from PIL import Image, ImageFilter, ImageTk


current_player = "X"


# Create function to place 'x' or 'o' on buttons and check for current player and if square is empty.
def update_board(button):
    global current_player
    if button["text"] == "":
        if current_player == "X":
            button.config(text="X")
            current_player = "O"
        else:
            button.config(text="O")
            current_player = "X"
    else:
        pass


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

# First (bottom) row
b1 = tk.Button(master=board_frame, text="", width=16, height=8, relief="ridge", command=lambda: update_board(b1))
b1.grid(row=2, column=0, padx=2, pady=2)
b2 = tk.Button(master=board_frame, text="", width=16, height=8, relief="ridge", command=lambda: update_board(b2))
b2.grid(row=2, column=1, padx=2, pady=2)
b3 = tk.Button(master=board_frame, text="", width=16, height=8, relief="ridge", command=lambda: update_board(b3))
b3.grid(row=2, column=2, padx=2, pady=2)

# Second (middle) row
b4 = tk.Button(master=board_frame, text="", width=16, height=8, relief="ridge", command=lambda: update_board(b4))
b4.grid(row=1, column=0, padx=2, pady=2)
b5 = tk.Button(master=board_frame, text="", width=16, height=8, relief="ridge", command=lambda: update_board(b5))
b5.grid(row=1, column=1, padx=2, pady=2)
b6 = tk.Button(master=board_frame, text="", width=16, height=8, relief="ridge", command=lambda: update_board(b6))
b6.grid(row=1, column=2, padx=2, pady=2)

# Third (top) row
b7 = tk.Button(master=board_frame, text="", width=16, height=8, relief="ridge", command=lambda: update_board(b7))
b7.grid(row=0, column=0, padx=2, pady=2)
b8 = tk.Button(master=board_frame, text="", width=16, height=8, relief="ridge", command=lambda: update_board(b8))
b8.grid(row=0, column=1, padx=2, pady=2)
b9 = tk.Button(master=board_frame, text="", width=16, height=8, relief="ridge", command=lambda: update_board(b9))
b9.grid(row=0, column=2, padx=2, pady=2)

root.mainloop()
