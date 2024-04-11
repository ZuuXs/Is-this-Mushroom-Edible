import sys
from joblib import load
import numpy as np
import pandas as pd

FEATURE_NAMES = ['Polypore', 'Convex', 'Bellshaped', 'Flat', 'Depressed', 'CupFungi', 'CoralFungi',
                  'Knobbed', 'Conical', 'JellyFungi', 'Stinkhorns', 'Earthstars', 'Bolete', 
                  'ToothFungi', 'Shellshaped', 'Funnelshaped', 'Puffballs', 'Corticioid',
                    'Chanterelles', 'Cylindrical', 'Truffles', 'FalseMorels', 'TrueMorels', 
                    'Cauliflower', 'Smooth', 'Fibrous', 'FlatScales', 'Patches', 'Silky', 
                    'RaisedScales', 'Hairy', 'Powder', 'Velvety', 'R', 'G', 'B']



def prepare_input(R, G, B, shapes, surfaces):

    shape_order = ["Polypore", "Convex", "Bellshaped", "Flat", "Depressed", "CupFungi",
                   "CoralFungi", "Knobbed", "Conical", "JellyFungi", "Stinkhorns", "Earthstars",
                   "Bolete", "ToothFungi", "Shellshaped", "Funnelshaped", "Puffballs", "Corticioid",
                   "Chanterelles", "Cylindrical", "Truffles", "FalseMorels", "TrueMorels", "Cauliflower"]
    surface_order = ["Smooth", "Fibrous", "FlatScales", "Patches", "Silky", "RaisedScales",
                     "Hairy", "Powder", "Velvety"]

    
    shape_features = [1 if shape in shapes else 0 for shape in shape_order]
    surface_features = [1 if surface in surfaces else 0 for surface in surface_order]
    rgb_features = [R, G, B]

    
    features = shape_features + surface_features + rgb_features 
    return np.array(features).reshape(1, -1)


def make_prediction(features, modelPath):
    model = load(modelPath)
    features_df = pd.DataFrame(features, columns=FEATURE_NAMES)
    return model.predict(features_df)

if __name__ == '__main__':

    # Arguments passed from node.js
    R = sys.argv[1]
    G = sys.argv[2]
    B = sys.argv[3]
    shapes = sys.argv[4].split(',')  
    surfaces = sys.argv[5].split(',')  
    modelPath = sys.argv[6]

   
    features = prepare_input(R, G, B, shapes, surfaces)
    prediction = make_prediction(features, modelPath)

    # Output the prediction
    if prediction[0] == 0:
        print("Edible")
    elif prediction[0] == 1:
        print("Inedible")
    elif prediction[0] == 2:
        print("Poisonous")
    else:
        print("Something went wrong...")
 