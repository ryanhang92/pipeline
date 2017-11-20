# Start Sentinel Monitoring Server

from flask import Flask
app = Flask('Sentinel') # app = Flask(__name__)

@app.route('/')
def health_check():
    return "Sentinel is alive and well"

@app.route('/reporting/experiment_progress', method='POST')
def report_progress():
    if request.methods == 'POST':
        return True

@app.route('/reporting/experiment_results', method='POST')
def report_results():
    if request.methods == 'POST':
        return True


