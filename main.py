from flask import render_template, Flask

import os.path

app = Flask(__name__)

@app.route("/components/<comp>")
def component(comp):
    comp = os.path.relpath(os.path.join("/", comp), "/")
    return render_template('components/' + comp)

@app.route("/")
def hello_world():
    return render_template("home.html")
