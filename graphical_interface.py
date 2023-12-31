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


def open_game_window():
    # Hide the welcome window
    welcome_frame.pack_forget()
    # Show the main game window
    root.deiconify()


welcome_frame = tk.Frame(root, width=1280, height=720)
welcome_frame.pack()
welcome_frame.pack_propagate(False)

welcome_label = tk.Label(welcome_frame, text="WELCOME to TIC-TAC-TOE", font=("Arial", 40))
welcome_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

play_button = tk.Button(welcome_frame, text="PLAY", font=("Arial", 40), command=open_game_window)
play_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# Create frame for board
board_frame = tk.Frame()
board_frame.pack(pady=100)

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
            check_draw(buttons)
            check_win_conditions(buttons)
            current_player = "O"
        else:
            buttons[button].config(text="O")
            check_draw(buttons)
            check_win_conditions(buttons)
            current_player = "X"
    else:
        pass


# Function to disable all the buttons if there was a win.
def disable_buttons(button_dict):
    for button in button_dict:
        button_dict[button].config(state="disabled")


# Create function to check for horizontal / vertical / diagonal button occupancy.
def check_win_conditions(button_dict):
    avail_buttons = ["b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9"]
    avail_signs = ["X", "O"]
    win_comb = [
        [0, 1, 2],  # Row 1
        [3, 4, 5],  # Row 2
        [6, 7, 8],  # Row 3
        [0, 3, 6],  # Column 1
        [1, 4, 7],  # Column 2
        [2, 5, 8],  # Column 3
        [0, 4, 8],  # Diagonal 1
        [6, 4, 2]  # Diagonal 2
    ]
    # BLACK MAGIC
    for combination in win_comb:
        if all(buttons[avail_buttons[i]].cget("text") == current_player for i in combination):
            disable_buttons(button_dict)
            create_win_message()
            play_again()
            break


def check_draw(button_dict):
    counter = 0
    for item in button_dict:
        if button_dict[item].cget("text") in ["X", "O"]:
            counter += 1
    if counter == 9:
        disable_buttons(button_dict)
        create_draw_message()
        play_again()
        return True
    else:
        pass


def create_draw_message():
    win_label = tk.Label(root, text="IT'S A DRAW", font=("Arial", 20))
    win_label.place(relx=0.43, rely=0.7)


# Creates a win message at the bottom of the screen if someone's won.
def create_win_message():
    win_label = tk.Label(root, text="WE HAVE A WINNER!", font=("Arial", 20), background="white")
    win_label.place(relx=0.39, rely=0.7)


def play_again():
    again_button = tk.Button(root, text="Play Again?", font=("Arial", 20), command=clear_board)
    again_button.place(relx=0.43, rely=0.8)


def clear_board():
    buttons.clear()
    create_buttons()



root.mainloop()
