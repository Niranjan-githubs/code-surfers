from flask_sqlalchemy import SQLAlchemy
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable = False)

    def set_pw(self,pw):
        self.password_hash = generate_password_hash(pw)

    def check_pw(self,pw):
        return check_password_hash(self.password_hash,pw)

    