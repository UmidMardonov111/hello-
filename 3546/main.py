from flask import Flask
from flask import render_template
from flaskwebgui import FlaskUI 

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    FlaskUI(app=app, server="flask").run()