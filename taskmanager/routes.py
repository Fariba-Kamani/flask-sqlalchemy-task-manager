<<<<<<< HEAD
from flask import render_template, request, redirect, url_for
=======
from flask import render_template
>>>>>>> 3e4e25ce3051093a154542d1dd38896ce4167780
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
<<<<<<< HEAD
    return render_template("tasks.html")

@app.route("/categories")
def categories():
    return render_template("categories.html")

@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")
=======
    return render_template("tasks.html")
>>>>>>> 3e4e25ce3051093a154542d1dd38896ce4167780
