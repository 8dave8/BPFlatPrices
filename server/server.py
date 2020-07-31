from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_butor_names', methods=['GET'])
def get_butor_names():
    response = jsonify({
        'butorozott': util.get_butor_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_emelet_names', methods=['GET'])
def get_emelet_names():
    response = jsonify({
        'emeletek': util.get_emelet_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_lift_names', methods=['GET'])
def get_lift_names():
    response = jsonify({
        'lift': util.get_lift_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_m2 = float(request.form['m2'])
    location = request.form['location']
    room_f = int(request.form['room_f'])
    room_hf = int(request.form['room_hf'])
    butor = request.form['butor']
    emelet = request.form['emelet']
    lift = request.form['lift']
    # kerület, m2, szoba, félszoba, bútorozott, emelet, lift
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_m2, room_f, room_hf, butor, emelet, lift)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()