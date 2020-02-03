import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, MobileNetV2, decode_predictions



def pred(img):
    img = image.load_img(img, target_size=(224, 224))
    assert img is not None, 'Image not found'
    #img_array = np.frombuffer(img, dtype=np.uint8)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    predimg = preprocess_input(img_array)
    # define the mobilenetV2 model
    model = MobileNetV2()
    import time
    t=time.time()
    # make predictions on test image using mobilenetV2
    preds = model.predict(predimg)
    print(time.time()-t)
    # convert predictions to readable results
    print('Predicted:', decode_predictions(preds, top=3)[0])
    output = decode_predictions(preds, top=3)[0]
    fmtans = ""
    for o in output:
        fmtans += f"{o[1]}: {o[2]*100:.2f}"
    return fmtans

if __name__=='__main__':
    test_img = "/home/anette/Documents/ML-dash/backend/cat.jpg"
    pred(test_img)
