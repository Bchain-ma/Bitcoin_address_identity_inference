import numpy as np
from flask import Flask, request
import pickle
import pandas as pd
from flask_cors import CORS


app = Flask(__name__)
# CORS(app)
model = pickle.load(open('model.pkl', 'rb'))
dataset = pd.read_csv("BitcoinHeistData.csv")


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
    app.run(debug=True, host='0.0.0.0')