import os
import sqlite3
from flask import Flask, g, redirect, render_template_string, request, url_for

app = Flask(__name__); app.config["DATABASE"] = os.getenv("DATABASE", "tasks.db")
PAGE = """<h1>Database tasks</h1><form method=post><input name=title required><button>Add</button></form><ul>{% for task in tasks %}<li>{{ task['title'] }}</li>{% endfor %}</ul>"""

def db():
    if "db" not in g: g.db = sqlite3.connect(app.config["DATABASE"]); g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(_error):
    connection = g.pop("db", None)
    if connection: connection.close()

@app.route("/", methods=["GET", "POST"])
def home():
    connection = db(); connection.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT NOT NULL)")
    if request.method == "POST": connection.execute("INSERT INTO tasks (title) VALUES (?)", (request.form["title"].strip(),)); connection.commit(); return redirect(url_for("home"))
    return render_template_string(PAGE, tasks=connection.execute("SELECT title FROM tasks ORDER BY id DESC"))

if __name__ == "__main__": app.run()
