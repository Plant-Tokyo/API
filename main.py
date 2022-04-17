import flask, os

app = flask.Flask(__name__)
global status
status = False

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


app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
