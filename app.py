import sqlite3
import mysql.connector
from flask import Flask, render_template, request
app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host='sql7.freesqldatabase.com',
        user='	sql7820090',
        password='QG1bsZdiYX',
        database=' sql7820090'

    )
    
def create_table():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    db.commit()
    db.close()



@app.route('/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        username = username = request.form['username']
        password = request.form['password']
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        account = cursor.fetchone()
        if account:
            msg ='logged in successfully!'
            name = account[1]
            return render_template('welcome.html', name=name)
        else: 
            msg = 'Incorrect username/password!'
        db.close()
    return render_template('login.html', msg=msg)

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists!'
        else:
            cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
            db.commit()
            msg = 'You have successfully registered!'
            return render_template('welcome.html', name=username)
        
        db.close()
    return render_template('register.html', msg=msg)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')




app.run(debug=True, host='0.0.0.0', port=8080)