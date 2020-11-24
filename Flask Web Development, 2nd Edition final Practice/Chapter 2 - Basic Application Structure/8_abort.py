from flask import Flask
from flask import abort
app = Flask(__name__)

@app.route('/user/<name>')
def user(name):
    #user = load_user(name)
    if not user:
        abort(404)
    return '<h1>Hello, {}</h1>'.format(user.name)
    
# > set FLASK_APP=8_abort.py
# > set FLASK_DEBUG=1
# > flask run

#open url #open url http://127.0.0.1:5000