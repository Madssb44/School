from flask import Flask, render_template, url_for, request, redirect  
from hashlib import sha256
app = Flask(__name__, static_url_path="/static")
#name = "Mads"
thing_list = ["And","Need","A","Life"]
genres = {"rock":["rock","metal","deathcore"], "pop": ["pop","j-pop","k-pop"], "folk": ["irish","celtic","danish"]}
name = ""
age = ""
#user = ""
#passwd = ""
aduser = sha256("admin".encode()).hexdigest()
adpass = sha256("admin".encode()).hexdigest()
accounts = {"username":[aduser], "password":[adpass], "id":[0]}

def encrypt(user, passwd):
#    user = user.decode()
#    passwd = passwd.decode()
    username = sha256(user.encode()).hexdigest()
    password = sha256(passwd.encode()).hexdigest()
    return username, password 



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
    if request.method == 'POST':        
        user = request.form.get('username')        
        if sha256(user.encode()).hexdigest() in accounts['username']:
            index = accounts["username"].index(sha256(user.encode()).hexdigest())
            passwd = request.form.get('password')
            if sha256(passwd.encode()).hexdigest() == accounts['password'][index]:
                return render_template('dashboard.html', user=user)
            else:
                return render_template("login.html")
        else:
            return render_template("login.html")
    return render_template("login.html")


@app.route("/create", methods=['POST','GET'])
def create_account_page():
    if request.method == 'POST':
        user = request.form.get('username')
        passwd = request.form.get('password')
        if user in accounts["username"]:
            pass 
        else:
            encuser, encpasswd = encrypt(user, passwd)
            accounts['username'].append(encuser)
            accounts['password'].append(encpasswd)
            return render_template("/dashboard", user=user)
    return render_template("create_account.html")


@app.route("/dashboard", methods=["POST","GET"])
def dashboard():
    return render_template("dashboard.html", user="not logged in yet")


app.run(port=5000)
