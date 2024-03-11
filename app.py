
from flask import Flask, render_template,request,redirect,url_for
from models import db,User
from werkzeug.security import generate_password_hash, check_password_hash

import hashlib


app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('login.html')

def hash_password(pw):
    pw_bytes = pw.encode('utf-8')
    hash_obj = hashlib.sha256(pw_bytes)
    return hash_obj.hexdigest()



@app.route('/signup', methods=['POST'])
def signup():
    
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']


    if password!=confirm_password:
        return "Passwords do not match. Try Again!"
    
    print(f"Attempting to add user!:{username}")

    try:
        with app.app_context():
            hashed_pw = hash_password(password)
            new = User(username=username,password_hash=hashed_pw)
            db.session.add(new)
            db.session.commit()
    except Exception as e:
        print(f"Error: {str(e)}")
    
    print(f"Successful in adding {username}")
    return f"User {username} successfully registered!"
    
def check_creds(username,pw):
    user = User.query.filter_by(username=username).first()
    if user and user.password_hash == hash_password(pw):
        return True
    else:
        return False


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if check_creds(username,password):
            return "Login successful"
        else:
            return "Invalid credentials"
    return render_template('login.html')



with app.app_context():
    
    db.create_all()



if __name__ == '__main__':
    app.run(debug=True)