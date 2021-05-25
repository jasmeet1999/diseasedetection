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
        file = request.files["file"]
        file_name = secure_filename(file.filename)
        file_path = "classifier/static/user_file/" + file_name
        file.save(file_path)
        return render_template("preview.html", img_url="/user_file/" + file_name)
    else:
        return redirect(url_for("home"))
