"""
This program takes in multiple youtube links and will run yt-dlp.exe on those files. I only made this so I don't have to run "yt-dlp.exe -f bestaudio -x --audio-format mp3 [ytlink]" every time
"""

import os

songlist = []
completed = False
print(r"""\)

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

print("Keep inserting Youtube links. When you want to stop, press enter without inputting a link. \n")   

while completed == False:

    music = input("Youtube link: ")
    if music == "":
        completed = True
        break
    songlist.append(music)

#You need to change this to wherever your yt-dlp exe is.
os.chdir('C:\ytdl')

for items in songlist:
    command = "yt-dlp.exe -f bestaudio -x --audio-format mp3 " + items
    os.system(command)

os.system('"start ."')