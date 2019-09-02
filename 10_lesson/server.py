from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def home():
    # time.sleep(20)
    return '<b>Hello World!</b>'

@app.route('/test/')
def test():
    # time.sleep(20)
    return '<b>Hello User!</b>'

if __name__ == '__main__':
    app.run()