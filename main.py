import flask, os

app = flask.Flask(__name__)

@app.route('/start')
def start():
    return 'started'

@app.route('/stop')
def stop():
    return 'stopped'

app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
