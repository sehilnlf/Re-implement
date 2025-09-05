from PIL import Image
import numpy as np

image = Image.open("D:/Empty/Re-implement/Dataset/val/cat/Abyssinian_155_jpg.rf.fdd90a163673ab77ec9690317a69b94e.jpg")
img_arr = np.array(image)
print(img_arr.shape) # (height, width, channels - RGB) 
print(img_arr)