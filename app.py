from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/login')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

app.run(debug=True, host='0.0.0.0', port=8080)