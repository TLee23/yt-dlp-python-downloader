"""
This program takes in multiple youtube links and will run yt-dlp.exe on those files. I only made this so I don't have to run "yt-dlp.exe -f bestaudio -x --audio-format mp3 [ytlink]" every time
"""

# Importing OS so the program can navigate through the file system
import os

# Creating an empty list for the songs to be held in
songlist = []

# Setting completed to false for the while loop
completed = False

# The command for downloading the videos
command = "yt-dlp.exe -f bestaudio -x --audio-format mp3 "

# Giant text that will display when opened in the terminal
print(r"""
██╗░░░██╗████████╗░░░░░░██████╗░██╗░░░░░██████╗░
╚██╗░██╔╝╚══██╔══╝░░░░░░██╔══██╗██║░░░░░██╔══██╗
░╚████╔╝░░░░██║░░░█████╗██║░░██║██║░░░░░██████╔╝
░░╚██╔╝░░░░░██║░░░╚════╝██║░░██║██║░░░░░██╔═══╝░
░░░██║░░░░░░██║░░░░░░░░░██████╔╝███████╗██║░░░░░
░░░╚═╝░░░░░░╚═╝░░░░░░░░░╚═════╝░╚══════╝╚═╝░░░░░
██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗██╗░░░░░░█████╗░░█████╗░██████╗░███████╗██████╗░  ░░███╗░░░░░░█████╗░
██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗  ░████║░░░░░██╔══██╗
██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║██║░░░░░██║░░██║███████║██║░░██║█████╗░░██████╔╝  ██╔██║░░░░░██║░░██║
██║░░██║██║░░██║░░████╔═████║░██║╚████║██║░░░░░██║░░██║██╔══██║██║░░██║██╔══╝░░██╔══██╗  ╚═╝██║░░░░░██║░░██║
██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║███████╗╚█████╔╝██║░░██║██████╔╝███████╗██║░░██║  ███████╗██╗╚█████╔╝
╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝  ╚══════╝╚═╝░╚════╝░
  """)      

# Lets the user know how to use this
print("Keep inserting Youtube links. When you want to stop, press enter without inputting a link. \n")   

# Loops until user inputs nothing. Every link gets appended to a list
while completed == False:

    music = input("Youtube link: ")
    if music == "":
        break
    songlist.append(music)

# !!!You need to change this to wherever your yt-dlp exe is.!!!
os.chdir(r'C:\ytdl')

# For every link in the list, add it to the end of the command
for item in songlist:
    command += " " + item

# Run the command that'll download
os.system(command)

# Once the downloads are done, open the folder with the songs
os.system('"start ."')
