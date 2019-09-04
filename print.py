import os
import sys
import loadconfig
from PIL import Image
from urllib.request import urlretrieve
from urllib.parse import urlparse


def get_filename(url_address):
    filename = urlparse(url_address)
    return os.path.basename(filename.path)


# Function for print file
def print_file(file):
    os.startfile(file, "print")


# Function for check if image is in RGB color format
def file_color_mode(file):
    image = Image.open(file)
    mode = image.mode
    print('File details:%s\nColor mode: %s' % file, mode)
    return mode


# Function for translate RGB image to CMYK image
def translate_image(image, output_filename):
    Image.open(image).convert('CMYK').save(output_filename)


os.chdir(loadconfig.directory)
url = sys.argv[1].replace(loadconfig.proto, "")
current_filename = get_filename(url)
new_filename = "cmyk-%s" % current_filename
urlretrieve(url, current_filename)

if file_color_mode(current_filename) != "CMYK":
    # translate image color to CMYK and print
    translate_image(current_filename, new_filename)
    print ("File successfully converted")
    file_color_mode(new_filename)
    print_file(new_filename)
else:
    print_file(current_filename)
    file_color_mode(current_filename)

input("Press enter to exit")

