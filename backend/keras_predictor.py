import numpy as np
import keras
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications import MobileNetV2
from keras.applications.mobilenet_v2 import preprocess_input

# load the image
img = load_img("her-er-bildet",target_size=(224, 224))

# convert to numpy array
img_array = img_to_array("her-er-bildet")

def predict():
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return keras.applications.mobilenet_v2.preprocess_input(img_array_expanded_dims)

preprocessed_image = prepare_image('German_Shepherd.jpg')
predictions = mobile.predict(preprocessed_image)
results = imagenet_utils.decode_predictions(predictions)
print(results)

# keras.applications.mobilenet_v2.MobileNetV2(input_shape=None, alpha=1.0, include_top=True, weights='imagenet', input_tensor=None, pooling=None, classes=1000)
