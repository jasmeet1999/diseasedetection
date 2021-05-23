from classifier import app
from flask import render_template, redirect, url_for, request


@app.route("/")
def to_home():
    return redirect(url_for("home"))


@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/preview", methods=["GET", "POST"])
def preview():
    if request.method == "POST":
        return render_template("preview.html")
    else:
        return redirect(url_for("home"))
