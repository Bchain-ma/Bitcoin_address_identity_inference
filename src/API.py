import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from numpy.core.defchararray import add
import pandas as pd
from flask_cors import CORS


app = Flask(__name__, static_url_path='', static_folder='../webpage/app/build')
CORS(app)
model = pickle.load(open('src/RandomForest.pkl', 'rb'))
dataset = pd.read_csv("datasets/BitcoinHeistData.csv")


@app.route('/')
# def home():
#     return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    df_copy = dataset.copy()
    address = str(request.get_data())
    address = address[2:-1]
    # print (address)
    chnk = df_copy[df_copy['address'] == address]
    chnk = chnk.drop(['address','year','day','label'], axis=1)
    row = chnk.iloc[0]
    print(chnk)
    row = np.array(row)
    row = row.reshape(1,-1)
    prediction = model.predict(row)

    output = prediction[0]

    return str(output)

if __name__ == "__main__":
    app.run(debug=True)