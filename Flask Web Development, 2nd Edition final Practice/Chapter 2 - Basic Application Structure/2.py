from flask import Flask
app = Flask(__name__)

@app.route('/')

def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

#run cmd >set FLASK_APP=2.py
# > flask run 
# open http://127.0.0.1:5000/
# open http://127.0.0.1:5000/user/Mustafa Ali