import numpy as np
import json
import pickle

__data_columns = None
__model = None


def get_estimated_oil_type(x1, x2, x3, x4, x5, x6, x7):
    x = np.zeros(len(__data_columns))
    x[0] = x1
    x[1] = x2
    x[2] = x3
    x[3] = x4
    x[4] = x5
    x[5] = x6
    x[6] = x7
    x = x.reshape(1, -1)
    return __model.predict(x)[0]



def get_data_columns():
    return __data_columns

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns

    with open("./artifacts/MA_Steranes_columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']

    global __model
    with open("./artifacts/oil_type_prediction_by_MA_Steranes.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_data_columns())
    print(get_estimated_oil_type(1000, 200, 3, 400, 5, 6, 7))