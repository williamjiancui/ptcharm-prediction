from flask import Flask, request, render_template
import pickle
import numpy as np
import json

app = Flask(__name__)
model = pickle.load(open('./artifacts/oil_type_prediction_by_MA_Steranes.pickle', 'rb'))
__data_columns = json.load(open("./artifacts/MA_Steranes_columns.json", 'r'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def get_estimated_oil_type(x1, x2, x3, x4, x5, x6, x7):
    x = np.zeros(len(__data_columns))
    x[0] = float(request.form['x1'])
    x[1] = float(request.form['x2'])
    x[2] = float(request.form['x3'])
    x[3] = float(request.form['x4'])
    x[4] = float(request.form['x5'])
    x[5] = float(request.form['x6'])
    x[6] = float(request.form['x7'])
    x = x.reshape(1, -1)
    output = __model.predict(x)[0]
    return render_template('index.html', prediction_test='oil type is $ {}'.format(output))




if __name__ == "__main__":
    app.run(debug=True)

