from flask import Flask, render_template
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()
app = Flask(
    __name__,
    static_folder='frontend-build/static',
    template_folder='frontend-build'
)
CORS(app, origins='http://www.coffeeshopcoders.com')


# default route for nows
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')


@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/api')
def hello_world():
    return 'Hello, World!'
