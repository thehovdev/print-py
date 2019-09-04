import os
import keyboard
import time

#convert RGB to CMYK
from PIL import Image
Image.open('D:/image.jpg').convert('CMYK').save('D:/image-cmyk.jpg')

#print image
os.startfile("D:/image-cmyk.jpg", "print")

#sleep
time.sleep(0.5)

#input enter for print image
keyboard.press_and_release('enter')
