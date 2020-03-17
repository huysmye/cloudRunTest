import os

from flask import Flask
from flask import request
from google.cloud import bigquery

app = Flask(__name__)

client = bigquery.Client()
table_id = "cardealership-256711:arduino_raspberry.apiData"

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
@app.route('/db', methods = ['POST', 'GET', 'DELETE'])
def db():
    if request.method == "GET":
        return 'getting all the data from the db'

    if request.method == "POST":
        data = request.json
        table = client.get_table(table_id)
        rows_to_insert= data
        errors = client.insert_rows(table, rows_to_insert)
        if errors == []:
            print('succesfull added the data to bigquery')
        return 'Posting this {} to the db'.format(data)

    if request.method == "DELETE":
        data = request.json
        return 'Deleting this {} from the db'.format(data)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))