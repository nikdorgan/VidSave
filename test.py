import tkinter as tk
from tkinter import filedialog, ttk

window = tk.Tk()
window.title("VidSave")
windowWidth = 500
windowHeight = 300
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
centerX = int(screenWidth/2 - windowWidth / 2)
centerY = int(screenHeight/2 - windowHeight / 2)
window.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')

songLabel = tk.Label(text="Enter YouTube URL")
songLabel.grid(row=0, column=0, columnspan=2, pady=10)

songEntry = tk.Entry()
songEntry.grid(row=1, column=0, padx=5, pady=10, sticky='e')

button = tk.Button(
    text="Download",
    width=25,
    height=5,
    bg="white",
    fg="black",
)

button.grid(row=2, column=0, columnspan=2, pady=10)

style = ttk.Style(window)

destination = ""

def openWinDiag():
    global destination
    destination = filedialog.askdirectory()  

fileButton = ttk.Button(window, text="Open", command=openWinDiag)
fileButton.grid(row=1, column=1, padx = 5, sticky='w')

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

window.mainloop()