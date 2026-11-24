import os
import sqlite3
from functools import wraps
from flask import Flask, g, redirect, render_template_string, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__); app.secret_key = os.getenv("SECRET_KEY", "change-this-before-deploying")
DB = "accounts.db"
PAGE = """<h1>{{ title }}</h1>{% if error %}<p>{{ error }}</p>{% endif %}<form method=post><input name=email type=email placeholder=email required><input name=password type=password placeholder=password required><button>Continue</button></form>"""

def db():
    if "db" not in g: g.db = sqlite3.connect(DB); g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(_error):
    connection = g.pop("db", None)
    if connection: connection.close()

def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "user_id" not in session: return redirect(url_for("login"))
        return view(*args, **kwargs)
    return wrapped

@app.route("/register", methods=["GET", "POST"])
def register():
    connection = db(); connection.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT UNIQUE, password_hash TEXT)")
    if request.method == "POST":
        try:
            connection.execute("INSERT INTO users (email, password_hash) VALUES (?, ?)", (request.form["email"].lower(), generate_password_hash(request.form["password"]))); connection.commit()
            return redirect(url_for("login"))
        except sqlite3.IntegrityError: return render_template_string(PAGE, title="Register", error="That email is already registered.")
    return render_template_string(PAGE, title="Register", error=None)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = db().execute("SELECT * FROM users WHERE email = ?", (request.form["email"].lower(),)).fetchone()
        if user and check_password_hash(user["password_hash"], request.form["password"]): session["user_id"] = user["id"]; return redirect(url_for("dashboard"))
        return render_template_string(PAGE, title="Login", error="Email or password was incorrect.")
    return render_template_string(PAGE, title="Login", error=None)

@app.get("/")
@login_required
def dashboard(): return f"<h1>Private dashboard</h1><p>You are user {session['user_id']}.</p><a href='/logout'>Log out</a>"

@app.get("/logout")
def logout(): session.clear(); return redirect(url_for("login"))

if __name__ == "__main__": app.run()
