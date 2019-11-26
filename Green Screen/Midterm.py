import matplotlib.pyplot as plt
from scipy import misc
from matplotlib.pyplot import imread
import numpy as np
import cv2

# ' refrences : https://medium.com/fnplus/blue-or-green-screen-effect-with-open-cv-chroma-keying-94d4a6ab2743


#f = imread("C:/Users/Crene/Desktop/UTEP/pictures/GreenScreen.jpg")
f = imread("C:/Users/Crene/Desktop/UTEP/pictures/diego.jpg")
f_copy = np.copy(f)
plt.imshow(f_copy)
plt.show()

#######john travolta
#lower_green = np.array([100, 1, 1])
#upper_green = np.array([200, 255, 10])

#######diego
lower_green = np.array([0, 40, 10])
upper_green = np.array([200, 255, 200])

mask = cv2.inRange(f_copy, lower_green, upper_green)
plt.imshow(mask, cmap='gray')
plt.show()

mask_image = np.copy(f_copy)
mask_image[mask != 0] = [0, 0, 0]
plt.imshow(mask_image)
plt.show()

background_image = imread("C:/Users/Crene/Desktop/UTEP/pictures/Pineapple.jpg")
background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)

#crop_background = background_image[0:698, 0:1092]
crop_background = background_image[0:640, 0:588] #diego
crop_background[mask == 0] = [0, 0, 0]

plt.imshow(crop_background)
plt.show()

final_image = crop_background + mask_image
plt.imshow(final_image)
plt.show()

print(type(f))
print(f.shape)

# This is how we're going to display images
#plt.imshow(f)
#plt.show()
