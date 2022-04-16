import flask

app = flask.Flask(__name__)

@app.route('/start')
def start():
    return 'started'

@app.route('/stop')
def stop():
    return 'stopped'

app.run()
