from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
todos = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("item", "").strip()
        if text:
            todos.append({"text": text, "done": False})
        return redirect(url_for("index"))
    return render_template("index.html", todos=todos)

@app.route("/toggle/<int:idx>")
def toggle(idx):
    if 0 <= idx < len(todos):
        todos[idx]["done"] = not todos[idx]["done"]
    return redirect(url_for("index"))

@app.route("/delete/<int:idx>")
def delete(idx):
    if 0 <= idx < len(todos):
        todos.pop(idx)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
