import flask, os

app = flask.Flask(__name__)
global data
data = ''

@app.route('/input/<passw>/<data>', methods = ['POST','GET'])
def input(passw, data):r
    if passw == '3645':
        with open('data.txt', 'w+') as f: f.write(data)
        return 'ddwrite'

@app.route('/data', methods = ['POST','GET'])
def data():
    with open("data.txt", "r") as f:
        return str(f.read())

@app.route('/', methods = ['POST','GET'])
def main():
    return str(app.url_map)

app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
