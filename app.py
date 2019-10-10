from flask import Flask, request, jsonify
from flask_cors import CORS,cross_origin
import pandas as pd
import json
import numpy as np


app = Flask(__name__)
CORS(app, support_credentials=True)
#load csv files
recom=pd.read_csv('BPM2.csv')
recom.set_index(recom.columns[0],inplace=True)
persuade=pd.read_csv('persuade2.csv')


def recommendation(customer_id):
    x=recom.loc[customer_id].to_json()
    return x


@app.route('/recom',methods=['POST'])
def recommend():
    return recommendation(request.form.get('customer_id', type=int))


if __name__ == '__main__':
    app.run()

