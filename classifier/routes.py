from classifier import app
from flask import render_template, redirect, url_for, request
from werkzeug.utils import secure_filename
from keras import models
from classifier.model.SkinCancer import SkinCancer
from classifier.model.LungCancer import LungCancer
from classifier.model.BreastCancer import BreastCancer
import os


@app.route("/")
def to_home():
    return redirect(url_for("home"))


@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/preview", methods=["GET", "POST"])
def preview():
    if request.method == "POST":
        # Deleting old files
        rm_path = "classifier/static/user_file"
        lists = os.listdir(os.path.join(os.getcwd(), rm_path))
        print(lists)
        for img in lists:
            os.remove(os.path.join(rm_path, img))
        file = request.files["file"]
        file_name = secure_filename(file.filename)
        file_path = "classifier/static/user_file/" + file_name
        file.save(file_path)
        return render_template("preview.html", img_url="/user_file/" + file_name)
    else:
        return redirect(url_for("home"))


from keras.preprocessing import image
import numpy as np


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        disease_type = request.form.get("disease-type")
        user_file = "classifier/static/user_file"
        file = os.listdir(os.path.join(os.getcwd(), user_file))
        cancer = object()
        if disease_type == "lung-cancer":
            cancer = LungCancer(url=os.path.join(user_file, file[0]))
        elif disease_type == "breast-cancer":
            cancer = BreastCancer(url=os.path.join(user_file, file[0]))
        elif disease_type == "skin-cancer":
            cancer = SkinCancer(url=os.path.join(user_file, file[0]))
        result = cancer.predict()
        print(result)
        return render_template(
            "predict.html", img_url="/user_file/" + file[0], result=result
        )
    else:
        return redirect(url_for("home"))
