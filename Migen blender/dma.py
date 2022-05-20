import numpy as np
from PIL import Image


#matrix with 8bit RGBA values
image_1 = np.zeros([100, 200, 4], dtype=np.uint8)
image_1[:, :100] = [255, 128, 0, 255]
image_1[:, 100:] = [0, 0, 255, 255]

image_2 = np.zeros([100, 200, 4], dtype=np.uint8)
image_2[:, :100] = [255, 255, 255, 255]
image_2[:, 100:] = [0, 255, 0, 255]

image_3 = np.zeros([100, 200, 4], dtype=np.uint8)

#matrix with 32bit word which consist of 8bit RGBA values for a single pixel
image_32bit_1 =  np.zeros([100, 200, 1], dtype=np.uint32)
image_32bit_1 [:, :100] = [0b11111111100000000000000011111111]
image_32bit_1 [:, 100:] = [0b00000000000000001111111111111111]

image_32bit_2 =  np.zeros([100, 200, 1], dtype=np.uint32)
image_32bit_2 [:, :100] = [0b11111111111111111111111111111111]
image_32bit_2 [:, 100:] = [0b00000000111111110000000011111111]

image_32bit_3 = np.zeros([100, 200, 1], dtype=np.uint32)

def save_image():
    img = Image.fromarray(image_1)
    img.save('first_image.png')

    img = Image.fromarray(image_2)
    img.save('second_image.png')

    img = Image.fromarray(image_3)
    img.save('alpha_blending.png')