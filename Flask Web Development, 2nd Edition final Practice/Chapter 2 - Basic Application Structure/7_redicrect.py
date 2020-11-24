from flask import redirect
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('http://www.facebook.com/Mustafa.Ali.Mir.96')

# > set FLASK_APP=7_redicrect.py
# > set FLASK_DEBUG=1
# > flask run

#open url #open url http://127.0.0.1:5000