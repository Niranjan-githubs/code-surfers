from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    password = db.Column(db.String(60), nullable=False)


@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    new = User(username=username,password=password)
    db.session.add(new)
    db.session.commit()

    if password!=confirm_password:
        return "Passwords do not match. Try Again!"
    
    return f"User {username} successfully registered!"
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)