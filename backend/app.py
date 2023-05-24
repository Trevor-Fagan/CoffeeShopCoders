from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()
app = Flask(__name__)
CORS(app, origins='http://www.coffee-shop-coders.com')


# default route for nows
@app.route('/api')
def hello_world():
    return 'Hello, World!'
