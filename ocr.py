import pytesseract
from PIL import Image

#for debugging
import os
import random
import keyboard
import threading

def key_monitor():
    global continue_loop
    while continue_loop:
        # press esc to terminate the loop
        if keyboard.is_pressed('esc'):
            continue_loop = False
            break

# Flag to indicate if loop should continue
continue_loop = True

folderpath = "rawscreenshots"

# list directory content to use in random choice
files = os.listdir(folderpath)

# Start key monitoring thread
monitor_thread = threading.Thread(target=key_monitor)
monitor_thread.start()

# Wait for monitor thread to finish
monitor_thread.join()

while continue_loop:
    # get a random file just for debugging
    randomfile = random.choice(files)

    imagefile = folderpath + "/" + randomfile # "rawscreenshots/Screenshot_20230704-132835.png"

    # open the image in default image viewer for debugging
    os.startfile("C:/Users/Roland Raga/MyWebsites/Python/screenshots/" + imagefile)

    image = Image.open(imagefile)

    # preprocess for better results
    image = image.convert("L") # grayscale
    image = image.point(lambda x: x * 1.2) # increase contrast

    result = pytesseract.image_to_string(image, lang="eng", config=f"--psm 4") 
    # result = MangaOcr(image)

    print(result)

    # space to continue
    keyboard.wait("space")