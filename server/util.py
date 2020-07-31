import json
import pickle
import numpy as np

__locations = None
__emelet = None
__lift = None
__butor = None
__data_columns = None
__model = None
# kerület, m2, szoba, félszoba, bútorozott, emelet, lift
def get_estimated_price(district,m2,room_f,room_hf,butor,emelet,lift):
    try:
        loc_index = __data_columns.index(district.lower())
    except:
        loc_index = -1
    try:
        butor_index = __data_columns.index(butor.lower())
    except:
        butor_index = -1
    try:
        emelet_index = __data_columns.index(emelet.lower())
    except:
        emelet_index = -1
    try:
        lift_index = __data_columns.index(lift.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = room_f
    x[1] = room_hf
    x[2] = m2
    if loc_index >= 0:
        x[loc_index] = 1
    if butor_index >= 0:
        x[butor_index] = 1
    if emelet_index >= 0:
        x[emelet_index] = 1
    if lift_index >= 0:
        x[lift_index] = 1

    return round(__model.predict([x])[0], 2)

def get_location_names():
    return __locations

def get_butor_names():
    return __butor

def get_emelet_names():
    return __emelet

def get_lift_names():
    return __lift

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __emelet
    global __lift
    global __butor
    global __model
    with open("./artifacts/columns.json","r") as f:
        __data_columns = json.load(f)['data_columns']
        __butor = __data_columns[3:7]
        __emelet = __data_columns[7:21]
        __lift = __data_columns[21:23]
        __locations = __data_columns[23:]

    with open("./artifacts/budapest_kiado_lakasok","rb") as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")


if __name__ == "util":
    load_saved_artifacts()
    # kerület, m2, szoba, félszoba, bútorozott, emelet, lift
    print(get_location_names())
    print(get_butor_names())
    print(get_emelet_names())
    print(get_lift_names())
    print(get_estimated_price('1. kerület', 80, 3, 0, 'igen', '8', 'van'))
    print(get_estimated_price('8. kerület', 80, 3, 0, 'igen', '2', 'nincs'))
    print(get_estimated_price('13. kerület', 80, 3, 0, 'igen', '8', 'van'))