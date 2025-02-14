from PIL import Image, ImageFilter
import pytesseract

#for debugging
import os

imagefile = "test4.png"
imagepath = "C:/Users/Roland Raga/MyWebsites/Python/screenshots/" + imagefile # "rawscreenshots/Screenshot_20230704-132835.png"

# os.startfile(imagepath)
image = Image.open(imagepath)

# preprocess for better results
image = image.convert("L") # grayscale
# image = image.point(lambda x: x * 1.1) # increase contrast
image = image.filter(ImageFilter.GaussianBlur(radius=.5))

image.save("result.png")
os.startfile("result.png")

# result = pytesseract.image_to_string(image, lang="eng", config=f"--psm 4") 
result = pytesseract.image_to_string(image, lang="eng", config=f"--psm 6")

print("Result:" + result)