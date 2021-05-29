from keras import models
import numpy as np
from keras.preprocessing import image


class SkinCancer:
    def __init__(self, url):
        self.model = models.load_model("models/model_SC.h5")
        self.url = url

    lesion_classes_dict = {
        0: "Melanocytic nevi",
        1: "Melanoma",
        2: "Benign keratosis-like lesions ",
        3: "Basal cell carcinoma",
        4: "Actinic keratoses",
        5: "Vascular lesions",
        6: "Dermatofibroma",
    }

    def predict(self):
        img = image.load_img(self.url, target_size=(90, 120, 3))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        prediction_value = self.model.predict(x)
        pred_class = prediction_value.argmax(axis=-1)
        pr = self.lesion_classes_dict[pred_class[0]]
        result = str(pr)
        return result
