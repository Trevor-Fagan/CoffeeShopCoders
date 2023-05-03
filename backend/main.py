from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()
app = Flask(__name__)
CORS(app)


# default route for now
@app.route('/api')
def hello_world():
    return 'Hello, World!'
