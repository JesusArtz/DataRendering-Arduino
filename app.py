from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

import functions

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('graficas.html')

 
@app.route('/postTemp/<temp>', methods=["GET"])
def insert_temp(temp):
    #data = request.get_data(as_text=True)
    #humedad = data
    result = functions.insert_temp(temp)
    return jsonify(result)


@app.route('/postHum/<hum>', methods=["GET"])
def insert_hum(hum):
    #data = request.get_data(as_text=True)
    #humedad = data
    result = functions.insert_humedad(hum)
    return jsonify(result)


@app.route('/getData', methods=["GET"])
def getData():
    dataHum = *map(lambda x: x[1], functions.get_humedad()),
    dataTemp = *map(lambda x: x[1], functions.get_temp()),

    return jsonify({"temperatura":dataTemp, "humedad":dataHum})


app.run(host='0.0.0.0', port=8000, debug=False) 