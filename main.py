from tkinter import filedialog
from pytube import YouTube
import tkinter as tk
import os
import sys

# This code block uses tkinter to make a really basic GUI
window = tk.Tk()
window.title("VidSave")
windowWidth = 500
windowHeight = 250
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
centerX = int(screenWidth / 2 - windowWidth / 2)
centerY = int(screenHeight / 2 - windowHeight / 2)
window.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

# The only inputs on the GUI, the URL and file destination are initialized here
videoEntry = tk.StringVar()
videoDestination = "."

# This function uses pytube to get the MP3 from the URL and put the resulting file in the destination


def videoDownload():
    videoURL = videoEntry.get()
    global videoDestination

    yt = YouTube(str(videoURL))
    video = yt.streams.filter(only_audio=True).first()
    outFile = video.download(output_path=videoDestination)
    base, ext = os.path.splitext(outFile)
    newFile = base + '.mp3'
    os.rename(outFile, newFile)
    sys.exit()

# Function that opens file window to choose file destination


def directoryChoice():
    global videoDestination
    videoDestination = filedialog.askdirectory()


# GUI element, just the text on the top
Label = tk.Label(text="Enter YouTube URL", font=('Helvetica', 18, 'bold'))
Label.grid(row=0, column=0, columnspan=2, pady=10)

# GUI element where user pastes URL
songEntry = tk.Entry(textvariable=videoEntry)
songEntry.grid(row=1, column=0, padx=5, pady=10, sticky='e')

# GUI button that user can click to start the destination-choosing process
destButton = tk.Button(text="Destination", command=directoryChoice)
destButton.grid(row=1, column=1, padx=5, sticky='w')

# GUI element where user begins the download process
downloadButton = tk.Button(text="Download", width=25,
                           height=5, command=videoDownload)
downloadButton.grid(row=2, column=0, columnspan=2, pady=10)

# This actually runs the window, keeping it on the screen
window.mainloop()
