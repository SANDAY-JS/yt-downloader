import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    status = False
    finishLabel.configure(text="")

    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
        status=True
    except Exception as e:
        print("🫤 YouTube link is invalid", e)

    if status==True:
        finishLabel.configure(text="Download Complete!")
        print("😙 Download complete!")
    
    else:
        finishLabel.configure(text="Failed to download the video")

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our opp frame
app = customtkinter.CTk()
app.geometry("920x600")
app.title("Youtube Downloader😎")

# Ui Elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var, text_color="#333")
link.pack()

# Finished downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)


# Run the app
app.mainloop()