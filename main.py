import flask, os
from flask import Flask, request, send_from_directory

app = flask.Flask(__name__)
global status
status = False

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
    status = False
    if status: return 'on'
    else: return 'off'

from flask import Flask, request, send_from_directory
+PHUB
@app.route('/')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])
    

app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
