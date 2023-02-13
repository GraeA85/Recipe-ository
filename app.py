import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        task = {
            "category_name": request.form.get("category_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("recipe_category", 1)
    return render_template("add_recipe.html", recipe_categories=recipe_categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        is_vegetarian = "on" if request.form.get("is_vegetarian") else "off"
        submit = {
            "recipe_category": request.form.get("recipe_category"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "is_vegetarian": is_vegetarian,
            "date_created": request.form.get("date_created"),
            "created_by": session["user"]
        }
        mongo.db.recipes.replace_one({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")

    task = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("recipe_category", 1)
    return render_template("edit_recipe.html", recipe=recipe, recipe_categories=recipe_categories)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


@app.route("/get_recipes_categories")
def get_recipe_categories():
    categories = list(mongo.db.recipe_categories.find().sort("recipe_category", 1))
    return render_template("recipe_categories.html", recipe_categories=recipe_categories)


@app.route("/add_recipe_category", methods=["GET", "POST"])
def add_recipe_category():
    if request.method == "POST":
        recipe_category = {
            "recipe_category": request.form.get("recipe_category")
        }
        mongo.db.recipe_categories.insert_one(recipe_category)
        flash("New Recipe Category Added")
        return redirect(url_for("get_recipe_categories"))

    return render_template("add_recipe_category.html")


@app.route("/edit_recipe_category/<category_id>", methods=["GET", "POST"])
def edit_recipe_category(category_id):
    if request.method == "POST":
        submit = {"$set": {
            "recipe_category": request.form.get("recipe_category")
        }}
        mongo.db.recipe_categories.update_one({"_id": ObjectId(recipe_category_id)}, submit)
        flash("Recipe Category Successfully Updated")
        return redirect(url_for("get_recipe_categories"))

    recipe_category = mongo.db.recipe_categories.find_one({"_id": ObjectId(recipe_category_id)})
    return render_template("edit_recipe_category.html", recipe_category=recipe_category)


@app.route("/delete_recipe_category/<recipe_category_id>")
def delete_recipe_category(recipe_category_id):
    mongo.db.recipe_categories.delete_one({"_id": ObjectId(recipe_category_id)})
    flash("Recipe Category Successfully Deleted")
    return redirect(url_for("get_recipe_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
