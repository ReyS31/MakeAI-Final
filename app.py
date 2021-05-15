from flask import Flask
from flask import render_template, url_for, request, jsonify
# from predictor_api import make_prediction, visualHari, visualJumlahKecelakaan
import predictor_api as pa
from flask import jsonify

app = Flask(__name__)


@app.route('/hari/<int:hari>', methods=['GET'])
def hari(hari):
    return pa.visualHari(hari)

@app.route('/map/<time>', methods=['GET'])
def waktu(time):
    return pa.mapVisualization(time)


@app.route('/category', methods=['POST'])
def kategori():
    req = request.get_json()
    kategori = req['kat1']
    kondisi = req['kondisi1']
    kategori2 = req['kat2']
    kondisi2 = req['kondisi2']
    if kondisi is None and kategori is not None:
        return pa.visualCategory(kategori)
    elif kondisi2 is None or kategori2 is None:
        return pa.visualOneCategory(kategori, kondisi)
    else:
        return pa.visualTwoCategory(kategori,kondisi,kategori2,kondisi2)

@app.route('/predict', methods=["POST"])
def predict():
    req = request.get_json()
    day = req['day']
    time = req['time']
    road = req['road']
    speed = req['limit']
    wheater = req['weather']
    light = req['light']
    x = [[day, time, road, speed, wheater, light]]
    # x = [[3, 4, 5, 1, 2, 4]]
    prediction = pa.make_prediction(x)
    return {
        "prediction":prediction
    }

if __name__ == "__main__":
    # For local development:
    app.run(debug=True)
    # For public web serving:
    # app.run(host='0.0.0.0')
    app.run()
