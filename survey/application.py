import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    name = request.form.get("name")
    school = request.form.get("school")
    state_origin = request.form.get("state")
    graduation_year = request.form.get("graduation")
    email = request.form.get("email")
    flat_no = request.form.get("flat")
    gender = request.form.get("gender")
    info_tup = (name, school, state_origin, graduation_year, email, flat_no, gender)
    for info in info_tup:
        if info == 'undefined':
            return render_template("error.html", message="One or two fields missing")

    file = open("survey.csv", "a")
    writer = csv.writer(file)
    writer.writerow(info_tup)
    file.close()
    return redirect("/sheet")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    file = open("survey.csv", "r")
    reader = csv.reader(file)
    info_tup = list(reader)
    file.close()
    if not info_tup:
        return render_template("error.html", message="No registered information")
    return render_template("sheet.html", info_tup = info_tup)

