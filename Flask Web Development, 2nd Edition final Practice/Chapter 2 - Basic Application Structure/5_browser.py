from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def user():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)
    
# > set FLASK_APP=5_browser.py
# > set FLASK_DEBUG=1
# > flask run

#open url #open url http://127.0.0.1:5000