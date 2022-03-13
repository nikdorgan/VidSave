from tkinter import filedialog
import tkinter as tk
from pytube import YouTube
import os
import sys 

# This block uses tkinter to make a really simple GUI
window = tk.Tk()
window.title("VidSave")
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
windowWidth = 500
windowHeight = 250
centerX = int(screenWidth / 2 - windowWidth / 2)
centerY = int(screenHeight / 2 - windowHeight / 2)
window.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

# The only inputs on the GUI, the URL and file destination, are initialized here
videoEntry = tk.StringVar()
videoDestination = "."

# This function uses pytube to get the MP3 from the URL and put the resulting file in the destination


def videoDownload():
    videoURL = videoEntry.get()
    global videoDestination

    video = YouTube(str(videoURL))
    audio = video.streams.filter(only_audio=True).first()
    outFile = audio.download(output_path=videoDestination)
    fileName, ext = os.path.splitext(outFile)
    newFile = fileName + '.mp3'
    os.rename(outFile, newFile)
    sys.exit()

# Function that opens file window to choose file destination


def destinationChoice():
    global videoDestination
    videoDestination = filedialog.askdirectory()


# GUI element, just the text on the top
Label = tk.Label(text="Enter YouTube URL", font=('Helvetica', 18, 'bold'))
Label.grid(row=0, column=0, columnspan=2, pady=10)

# GUI element where user pastes URL
URLEntry = tk.Entry(textvariable=videoEntry)
URLEntry.grid(row=1, column=0, padx=5, pady=10, sticky='e')

# GUI button that user can click to start the destination-choosing process
destinationButton = tk.Button(text="Destination", command=destinationChoice)
destinationButton.grid(row=1, column=1, padx=5, sticky='w')

# GUI element where user begins the download process
downloadButton = tk.Button(text="Download", width=25,
                           height=5, command=videoDownload)
downloadButton.grid(row=2, column=0, columnspan=2, pady=10)

# This actually runs the window, keeping it on the screen
window.mainloop()
