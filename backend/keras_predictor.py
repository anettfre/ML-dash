import keras
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

# load the image
img = load_img("her-er-bildet")

# convert to numpy array
img_array = img_to_array("her-er-bildet")