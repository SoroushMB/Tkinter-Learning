import tkinter as tk

# There are 5 kinds of widgets in the Tkinter
# Their name are mentioned below:Label-Button-Entry-Text-Frame

# Labels: label widgets are used to display text or images
# these text or images can't be edited by user.


# Without customization version
# label = tk.Label(text="Hello, Tkinter")

# Long Version

# label = tk.Label(
#     text="Hello my dear Saba❤️",
#     foreground="#ffffff",
#     background="#00ffff"
# )

# Short Version
#Color link: https://en.wikipedia.org/wiki/Web_colors#Hex_triplet

# label = tk.Label(
#     text="Hello my dear Saba❤️",
#     fg="#800080",
#     bg="#ffffff",
#     width=20,
#     height=5
# )


#The command for executing & showning the window

# label.pack()
# label.mainloop()

# Buttons: Buttons are used to display clickable buttons.
# You can configure them to call a function whenever they're clicked.
# Button is just a label that you can click.

button = tk.Button(
    text = "Click me!",
    width=25,
    height=5,
    bg="#00ffff",
    fg="#008080"
)

button.pack()
button.mainloop()
