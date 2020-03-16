import os

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    return 'test {}!\n'.format(target)

@app.route('/data',  methods = ['GET', 'POST'])
def testdata():
    if request.method == "GET":
        return 'dit is een test endpoint'

    if request.method == "POST":
        data = request.json
        return data

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))