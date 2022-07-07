
from PIL import Image
import cv2
import sys


args =  sys.argv)
image = Image.open(args[1])
mask = Image.open(args[2])
image.putalpha(mask)
image.save("cutout.png")
