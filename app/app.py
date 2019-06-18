from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index_page():
    hostname = os.uname()[1]
    return "<h1>This hostname {}</h1".format(hostname)

if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug = True)
