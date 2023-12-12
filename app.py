from flask import Flask, request, render_template
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'
debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    
    return render_template("index.html")


# @app.route("/greet-2")
# def get_greeting_2():
#     username = request.args["username"]
#     wants_compliments = request.args.get("wants_compliments")
#     nice_things = sample(COMPLIMENTS, 3)
#     return render_template("greet-2.html", username=username, wants_compliments=wants_compliments,
#     compliments=nice_things)


@app.route("/story.html")
def make_sotry():
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adj = request.args["adjective"]
    pr = request.args["plural_noun"]
    return render_template("story.html", place=place, noun=noun, verb=verb, adj=adj, pr=pr)

