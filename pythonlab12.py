# # https://docs.google.com/document/d/1kr_pn9wtBC9CEivOP525sreC1Tl74oFlwcVg_CJuZBY/edit

# I. Write a Python GUI program to import Tkinter package and create a window and set its
# title.

# II. Write a Python GUI program to import Tkinter package and create a window. Set its title
# and add a label to the window.

# III. Write a Python GUI program to create a label and change the label font style (font name,
# bold, size) using tkinter module.

# IV. Write a Python GUI program to create a window and set the default window size using
# tkinter module.

# V. Write a Python GUI program to create a window and disable to resize the window using
# tkinter module.

#1
def window_with_title():
    import tkinter as tk

    # Create a new window
    window = tk.Tk()

    # Set the window title
    window.title("My GUI Program")

    # Run the window main loop
    window.mainloop()

#2
def set_title_level():
    import tkinter as tk

    # Create a new window
    window = tk.Tk()

    # Set the window title
    window.title("My GUI Program")

    # Create a label widget and add it to the window
    label = tk.Label(window, text="Hello, world!")
    label.pack()

    # Run the window main loop
    window.mainloop()

#3
import tkinter as tk
from tkinter.font import Font

class FontChanger(tk.Tk):
    def __init__(self):
        super().__init__()

        # set the window title
        self.title("Font Changer")

        # create the label
        self.label = tk.Label(text="Hello, world!", font=("Arial", 12))
        self.label.pack(pady=20)

        # create the font selection widgets
        self.font_family_var = tk.StringVar(value="Arial")
        self.font_family_label = tk.Label(text="Font Family:")
        self.font_family_label.pack()
        self.font_family_entry = tk.Entry(textvariable=self.font_family_var)
        self.font_family_entry.pack()

        self.font_size_var = tk.IntVar(value=12)
        self.font_size_label = tk.Label(text="Font Size:")
        self.font_size_label.pack()
        self.font_size_entry = tk.Entry(textvariable=self.font_size_var)
        self.font_size_entry.pack()

        self.bold_var = tk.BooleanVar(value=False)
        self.bold_checkbox = tk.Checkbutton(text="Bold", variable=self.bold_var)
        self.bold_checkbox.pack()

        # create the button to change the font
        self.change_button = tk.Button(text="Change Font", command=self.change_font)
        self.change_button.pack(pady=20)

    def change_font(self):
        # get the current font properties
        current_font = Font(font=self.label["font"])

        # update the font family if the user entered a new value
        new_family = self.font_family_var.get()
        if new_family != "":
            current_font.configure(family=new_family)

        # update the font size if the user entered a new value
        new_size = self.font_size_var.get()
        if new_size != current_font.actual()["size"]:
            current_font.configure(size=new_size)

        # update the bold setting
        current_bold = "bold" in current_font.actual()["weight"]
        new_bold = self.bold_var.get()
        if new_bold != current_bold:
            if new_bold:
                current_font.configure(weight="bold")
            else:
                current_font.configure(weight="normal")

        # update the label's font
        self.label.configure(font=current_font.actual())

# create and run the application
app = FontChanger()
app.mainloop()

#4
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        # set the window title
        self.title("My Window")

        # set the default window size
        self.geometry("400x300")

# create and run the application
app = Window()
app.mainloop()

#5
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        # set the window title
        self.title("My Window")

        # disable resizing the window
        self.resizable(False, False)

# create and run the application
app = Window()
app.mainloop()
