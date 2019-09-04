import os
import keyboard
import time
import sys
import urllib.request
from PIL import Image
from PIL import ImageDraw 

fileurl = sys.argv[1]
fileurl = fileurl.replace("print:", "")

newfilename = "D:\\image-cmyk-new.jpg"
currentfilename = "D:\\image-rgb.jpg"

urllib.request.urlretrieve(fileurl, currentfilename)

# Function for print file
def print_file(file):
    os.startfile(file, "print")

# Function for check if image is in RGB color format
def fileColorMode(file):
    image = Image.open(file)
    mode = image.mode
    print('File details:')
    print('Color mode: ' + mode)
    return mode  

# Function for translate RGB image to CMYK image
def translateImage(currentfilename, newfilename):
    Image.open(currentfilename).convert('CMYK').save(newfilename)


if fileColorMode(currentfilename) != "CMYK":
    # translate image color to CMYK and print
    translateImage(currentfilename, newfilename)
    print ("File successfully converted")
    fileColorMode(newfilename)
    print_file(newfilename)
else:
    print_file(currentfilename)
    fileColorMode(currentfilename)

input("Press enter to exit")

# Show translated image color format ( was RGB now CMYK )


