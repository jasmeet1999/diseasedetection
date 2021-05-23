from classifier import app
from flask import render_template, redirect, url_for


@app.route("/")
def to_home():
    return redirect(url_for("home"))


@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/preview")
def preview():
    return render_template("preview.html")
