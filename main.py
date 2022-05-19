import flask, os

app = flask.Flask(__name__)
global status, data
status = True
data = ''

@app.route('/input/<passw>/<data>')
def input(passw, data):
    print(status)
    if passw == '3645':
        with open('data.txt', 'w+') as f: f.write(data)
        return 'dwrite'

@app.route('/data')
def data():
    with open("data.txt", "r") as f:
        return str(f.read() + ' ' + str(status))

@app.route('/')
def main():
    return str(app.url_map)

@app.route('/start')
def start():
    global status
    status = True
    return 'started'

@app.route('/stop')
def stop():
    global status
    status = False
    return 'stopped'

@app.route('/status')
def status():
    global status
    if status: return 'on'
    else: return 'off'

status = True

app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
