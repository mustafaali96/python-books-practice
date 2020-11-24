
from flask import make_response
from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Bad Request</h1>', 400


# > set FLASK_APP=4_bad_req.py
# > set FLASK_DEBUG=1
# > flask run

#open url #open url http://127.0.0.1:5000