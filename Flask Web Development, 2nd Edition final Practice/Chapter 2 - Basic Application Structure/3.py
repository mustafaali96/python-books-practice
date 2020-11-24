from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello First Flask!</h1>'

@app.route('/div/<num1>/<num2>')
def div(num1, num2):
    #res = =int(num1)/int(num2)
    res = int(num1)/int(num2)
    return '<h1>Dividing {} by {} is equals to {}!</h1>'.format(num1, num2, res)

@app.route('/add/<num1>/<num2>')
def add(num1, num2):
    #res = =int(num1)/int(num2)
    res = int(num1) + int(num2)
    return '<h1>Adding {} by {} is equals to {}!</h1>'.format(num1, num2, res)

@app.route('/sub/<num1>/<num2>')
def sub(num1, num2):
    #res = =int(num1)/int(num2)
    res = int(num1) - int(num2)
    return '<h1>subtracting {} by {} is equals to {}!</h1>'.format(num1, num2, res)

@app.route('/mul/<num1>/<num2>')
def mul(num1, num2):
    #res = =int(num1)/int(num2)
    res = int(num1)*int(num2)
    return '<h1>Multiplying {} by {} is equals to {}!</h1>'.format(num1, num2, res)
# uncomment line 9, You'll get SyntaxError in line 9




#run cmd > set FLASK_APP=3_calculator.py
# > set FLASK_DEBUG=1
# > flask run 
 
#open url http://127.0.0.1:5000
#open url http://127.0.0.1:5000/div/10/4
#open url http://127.0.0.1:5000/div/10/0