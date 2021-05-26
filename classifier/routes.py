from classifier import app
from flask import render_template, redirect, url_for, request
from werkzeug.utils import secure_filename
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


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        disease_type = request.form.get("disease-type")
        print(disease_type)
        user_file = "classifier/static/user_file"
        file = os.listdir(os.path.join(os.getcwd(), user_file))
        return render_template("predict.html", img_url="/user_file/" + file[0])
