import tkinter as tk

window = tk.Tk()
window.title("VidSave")
window.geometry('600x400+50+50')

windowWidth = 500
windowHeight = 300

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

centerX = int(screenWidth/2 - windowWidth / 2)
centerY = int(screenHeight/2 - windowHeight / 2)

window.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')

label = tk.Label(text="Enter the URL of the video you want to convert")
entry = tk.Entry()
label.pack()
entry.pack()

button = tk.Button(
    text="Download",
    width=25,
    height=5,
    bg="white",
    fg="black",
)

button.pack()

window.mainloop()