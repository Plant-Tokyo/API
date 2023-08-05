import flask, os, csv

app = flask.Flask(__name__)

@app.route('/input/<passw>/<id>/<data>')
def input(passw, id, data):
    if passw == '3645':
        with open(f'{id}.csv', 'w+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([data])
        return 'ddwrite'

@app.route('/data/<id>')
def data(id):
    with open(f"{id}.csv", "r") as file:
        reader = csv.reader(file)
        data_list = list(reader)
        return str(data_list)

@app.route('/')
def main():
    return str(app.url_map)
