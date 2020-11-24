from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello First Flask!</h1>'

#set FLASK_APP=1.py
#flask run
#open url  http://127.0.0.1:5000/