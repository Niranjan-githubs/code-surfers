from flask import Flask, render_template

index_app = Flask(__name__)

@index_app.route('/')
def index():
    return render_template('index.html')
