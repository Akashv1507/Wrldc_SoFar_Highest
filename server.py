from src.appConfig import getAppConfigDict
from flask import Flask, jsonify, render_template
from waitress import serve
from datetime import datetime as dt, timedelta
import warnings
from src.apiResponse.soFarHighestApiResp import SoFarHighestApiResp

warnings.filterwarnings("ignore")

app = Flask(__name__)

# get application config
appConfig = getAppConfigDict(sheetName='appConfig')
app.config['SECRET_KEY'] = appConfig['flaskSecret']

obj_soFarHighest = SoFarHighestApiResp(appConfig['con_string_mis_warehouse'])

@app.route('/')
def home():
    return render_template('index.html.j2')

@app.route('/api/soFarHighest/<dataSource>/<metricName>')
def soFarHighestApi(dataSource:str, metricName:str):

    respData = obj_soFarHighest.fetchSoFarHighest(dataSource, metricName)
    return jsonify(respData)


if __name__ == '__main__':
    serverMode: str = appConfig['mode']
    if serverMode.lower() == 'd':
        app.run(host="localhost", port=int(appConfig['flaskPort']), debug=True)
    else:
        serve(app, host='0.0.0.0', port=int(
            appConfig['flaskPort']),  threads=1)