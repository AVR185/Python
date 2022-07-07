# file handling: navigate, rename, move, copy, remove
# how to keep your desktop organized

import os
import shutil
from pathlib import Path

# Check current working directory
print(os.getcwd())

# Change directory
os.chdir(r'C:\Users\avelascr\Desktop\Carpeta de prueba') # r escape special characters

# Check current working directory
print(os.getcwd())

# List files in this directory
print(os.listdir())

"""
# Rename files
for file in os.listdir():
    name, ext = os.path.splitext(file)
    splitted = name.split(" ")
    new_name = "_".join(splitted) + ext
    os.rename(file, new_name)
    print(new_name)
""" 

# Another option to get name and extension
for file in os.listdir():
    f = Path(file)
    name, ext = f.stem, f.suffix
    splitted = name.split(" ")
    new_name = "_".join(splitted) + ext
    os.rename(file, new_name)
    print(new_name)

# Create Directory
Path("data_copy").mkdir(exist_ok=True) # Create a new directory - parameter => not throw an exception if exists

# Another option to create a directory
if not os.path.exists("data_move"):
    os.mkdir("data_move")

# Move and remove files
for file in os.listdir():
    f = Path(file)
    if f.is_dir(): # check is directory
        continue
    
    if "delete" in f.stem:
        os.remove(file) # remove file
        continue
    
    shutil.copy(file, "data_copy") # copy and paste with new timestamp
    # shutil.copy2(file, "data_copy") # copy and paste with the same timestamp
    
    shutil.move(file, "data_move") # move
    
# Delete directories
# os.remove("filename") # remove files
try:
    os.rmdir("data_copy") # remove empty directories
except OSError:
    print("The 'data_copy' directory is not empty. Lets remove it!")
    shutil.rmtree("data_copy") # remove NOT empty directories
except Exception as e:
    print(f"What happend?? -> {e}")


# List files in the current directory
print(os.listdir())

# Then End