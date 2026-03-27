from flask import Flask, render_template, url_for, request, redirect  

app = Flask(__name__, static_url_path="/static")
#name = "Mads"
thing_list = ["And","Need","A","Life"]
genres = {"rock":["rock","metal","deathcore"], "pop": ["pop","j-pop","k-pop"], "folk": ["irish","celtic","danish"]}
name = ""
age = ""
@app.route("/", methods=['POST','GET'])
def hello_world():
    global name, age 
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        return render_template("index.html", name=name, age=age, len=len(thing_list), thing_list=thing_list)
    return """<form method='POST' action=''>
    What is your name? <input types='text' name='name'><br>
    How old are you? <input types='text' name='age'><br>
    <input type='submit'>
    </form>"""

@app.route("/old")
def old():
    return render_template("are_you_old.html", old=int(age))

@app.route("/music")
def music():
    return render_template("music.html", genres=genres)

@app.route("/login", methods=['POST','GET'])
def login_page():
    return render_template("login.html")

@app.route("/create", methods=['POST','GET'])
def create_account_page():
    return render_template("create_account.html")

app.run(port=5000)
