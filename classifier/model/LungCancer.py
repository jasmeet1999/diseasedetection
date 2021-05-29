from keras import models
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np


class LungCancer:
    def __init__(self, url):
        self.model = models.load_model("models/model_LC.h5")
        self.url = url

    def predict(self):
        img = image.load_img(self.url, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        img_data = preprocess_input(x)
        classes = self.model.predict(img_data)
        print(type(classes))
        print(classes)
        if classes[0][0] == 1:
            return "Normal"
        elif classes[0][0] == 0:
            return "Pneumonia"
        return "Hello"
