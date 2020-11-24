from flask import make_response
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


# > set FLASK_APP=6_cookie.py
# > set FLASK_DEBUG=1
# > flask run
# open url #open url http://127.0.0.1:5000