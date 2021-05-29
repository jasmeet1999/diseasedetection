from keras import models


class BreastCancer:
    def __init__(self, url):
        self.model = models.load_model("models/")
        self.url = url

    def predict(self):
        pass
