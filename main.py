from flask import render_template, Flask, request, make_response
from surrealdb import Surreal
import os.path

app = Flask(__name__)



@app.route("/pages/<page>")
def render_page(page):
    page = os.path.relpath(os.path.join("/", page), "/")
    return render_template('pages/' + page)

@app.route("/components/<comp>")
def component(comp):
    comp = os.path.relpath(os.path.join("/", comp), "/")
    return render_template('components/' + comp)


@app.route("/signup", methods=["post"])
def signup():
    with Surreal("ws://localhost:8000/rpc") as db:
        db.signin({"username": 'root', "password": 'root'})
        db.use("tmi", "hcse")
        resp = make_response(render_template("pages/home.html"))
        uname = request.form['username']
        passw = request.form['password']
        db.signup({
            "namespace": 'tmi',"database": 'hcse',"access": 'user',
            "variables": {
                "name": uname,
                "password": passw,
            }
        })
        x = db.signin({
            "namespace": 'tmi',"database": 'hcse',"access": 'user',
            "variables": {
                "name": uname,
                "password": passw,
            }
        })
        print(x)
        resp.set_cookie('jwt', x)
        return resp

@app.route("/login", methods=["post"])
def login():
    with Surreal("ws://localhost:8000/rpc") as db:
        db.signin({"username": 'root', "password": 'root'})
        db.use("tmi", "hcse")
        resp = make_response(render_template("pages/home.html"))
        uname = request.form['username']
        passw = request.form['password']
        x = db.signin({
            "namespace": 'tmi',"database": 'hcse',"access": 'user',
            "variables": {
                "name": uname,
                "password": passw,
            }
        })
        resp.set_cookie('jwt', x)
        return resp

@app.route("/")
def hello_world():
    return render_template("index.html")
