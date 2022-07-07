# organize the desktop
# moves images, videos, screenshots, and audio files
# into corresponding folders
import os
import shutil

# Possible extensions
audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

# Functions
def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_image(file):
    return os.path.splitext(file)[1] in img

def is_screenshot(file):
    name, ext = os.path.splitext(file)
    return (ext in img) and "screenshot" in name.lower()

# Set the working directory
os.chdir(r'C:\Users\avelascr\Desktop\Carpeta de prueba')

# List files in the working directory and move them to the correct folder
for file in os.listdir():
    if is_audio(file):
        shutil.move(file, r'C:\Users\avelascr\Music')
    elif is_video(file):
        shutil.move(file, r'C:\Users\avelascr\Videos')
    elif is_image(file):
        if is_screenshot(file):
            shutil.move(file, r"C:\Users\avelascr\Pictures\Screenshots")
        else:
            shutil.move(file, r"C:\Users\avelascr\Pictures")
    else:
        shutil.move(file, r"C:\Users\avelascr\Documents")