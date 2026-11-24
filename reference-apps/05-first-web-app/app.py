from flask import Flask, redirect, render_template_string, request, url_for

app = Flask(__name__)
tasks = []
PAGE = """<h1>Task list</h1><form method=post><input name=title required><button>Add</button></form><ul>{% for task in tasks %}<li>{{ task }} <a href='{{ url_for("delete", index=loop.index0) }}'>delete</a></li>{% endfor %}</ul>"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST": tasks.append(request.form["title"].strip())
    return render_template_string(PAGE, tasks=tasks)

@app.get("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(tasks): tasks.pop(index)
    return redirect(url_for("home"))

if __name__ == "__main__": app.run(debug=True)
