from flask import Flask, render_template
# ...
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


#run cmd > set FLASK_APP=1.py
# > set FLASK_DEBUG=1
# > flask run 
 
#open url http://127.0.0.1:5000
#open url http://127.0.0.1:5000/user/Mustafa Ali