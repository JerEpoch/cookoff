from flask import Flask,jsonify
import time

# venv\Scripts\activate
app = Flask(__name__, static_folder='cookoff-frontend/build')


@app.route('/hello')
def hello():
    return {'success': 'ok'}

@app.route('/time')
def get_current_time():
    print(time.time())
    return jsonify('time', time.time())