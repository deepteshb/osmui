from flask import Flask, render_template,session,url_for,g

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def index():
    return render_template('index.html')

@app.route("/firstrun", methods = ['GET','POST'])
def firstrun():
    return render_template('firstrun.html')