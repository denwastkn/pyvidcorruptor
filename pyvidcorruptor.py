import os
import time

print ("Before running, make sure to have ffmpeg installed via your package manager, or is in the same folder as the script.")
time.sleep(2)
file = input("Path to file (Drag and drop works, depending on Terminal App) = ").strip()
output = input("Output Video Name (mp4 is put at the end of the video)= ").strip()
size1 = input("Scale of video corruption (the lower the higher) = ").strip()
size2 = input("Scale of audio corruption (the lower the higher) = ").strip()

os.system(f"ffmpeg -i '{file}' -c:a ac3 -ac 1 -ar 48000 -bsf:a noise={size2} -bsf:v noise={size1} -c:v libx264 -af 'volume=20dB' -r 60 -vf 'scale=800:600' tmp.avi && ffmpeg -i tmp.avi '{output}.mp4' && rm 'tmp.avi'")

if os.path.exists("tmp.avi"):
 os.remove("tmp.avi")