from tkinter import filedialog
from pytube import YouTube
import tkinter as tk
import os

window = tk.Tk()
window.title("VidSave")
windowWidth = 500
windowHeight = 250
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
centerX = int(screenWidth/2 - windowWidth / 2)
centerY = int(screenHeight/2 - windowHeight / 2)
window.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

vidEntry = tk.StringVar()
destination = "."


def vidDownload():
    vid = vidEntry.get()
    yt = YouTube(str(vid))

    video = yt.streams.filter(only_audio=True).first()

    global destination

    out_file = video.download(output_path=destination)

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print(yt.title + " has been successfully downloaded.")


songLabel = tk.Label(text="Enter YouTube URL", font=('Helvetica', 18, 'bold'))
songLabel.grid(row=0, column=0, columnspan=2, pady=10)

songEntry = tk.Entry(textvariable=vidEntry)
songEntry.grid(row=1, column=0, padx=5, pady=10, sticky='e')

downButton = tk.Button(
    text="Download",
    width=25,
    height=5,
    command=vidDownload
)

downButton.grid(row=2, column=0, columnspan=2, pady=10)


def openWinDiag():
    global destination
    destination = filedialog.askdirectory()


fileButton = tk.Button(
    text="Destination",
    command=openWinDiag
)

fileButton.grid(row=1, column=1, padx=5, sticky='w')

window.mainloop()
