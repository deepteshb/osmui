from flask import Flask, render_template,session,url_for,g

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def index():
    return render_template('index.html')

@app.route("/firstrun", methods = ['GET','POST'])
def firstrun():
    return render_template('firstrun.html')

@app.route("/setup", methods = ['GET','POST'])
def setup():
    return render_template('setup.html')

if __name__ == '__main__':
    app.run_server(debug=True)