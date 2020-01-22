import numpy as np
from keras.preprocessing import image
from keras.applications.mobilenet_v2 import preprocess_input, MobileNetV2, decode_predictions


test_img = "/home/anette/Documents/ML-dash/backend/cat.jpg"

def pred(test_img):
    img = image.load_img(test_img, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    pImg = preprocess_input(img_array)
    # define the mobilenetV2 model
    model = MobileNetV2()
    import time
    t=time.time()
    # make predictions on test image using mobilenetV2
    preds = model.predict(pImg)
    print(time.time()-t)
    # convert predictions to readable results
    print('Predicted:', decode_predictions(preds, top=3)[0])
    return preds
