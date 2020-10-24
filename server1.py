from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/predict_oil_type', methods=['POST'])
def predict_oil_type():
    x1 = float(request.form['x1'])
    x2 = float(request.form['x2'])
    x3 = float(request.form['x3'])
    x4 = float(request.form['x4'])
    x5 = float(request.form['x5'])
    x6 = float(request.form['x6'])
    x7 = float(request.form['x7'])

    response = jsonify({
        'estimated_oil_type': util.get_estimated_oil_type(x1, x2, x3, x4, x5, x6, x7)
    })
    response.header.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Oil Type Prediction")
    util.load_saved_artifacts()
    app.run(debug=True
            )