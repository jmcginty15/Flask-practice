from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'welcome'

@app.route('/welcome/<path>')
def welcome_path(path):
    return f'welcome {path}'