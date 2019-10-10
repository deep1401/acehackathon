<<<<<<< HEAD
from flask import Flask, request,jsonify
from flask_cors import CORS,cross_origin
import pandas as pd
import numpy as np
=======
from flask import Flask, request
from flask_cors import CORS,cross_origin
import pandas as pd
>>>>>>> 3b7d4246c80f07c57e908f5c015f1fb8d666e225

app = Flask(__name__)
CORS(app, support_credentials=True)
#load csv files

recom=pd.read_csv('BPM2.csv')
recom.set_index(recom.columns[0], inplace=True)
persuade=pd.read_csv('persuade2.csv')
time=pd.read_csv('Time_hour.csv')
time.set_index('time_hour', inplace=True)
gb = time.groupby(['time_hour'])
result = gb['category_id'].unique()


def recommendation(customer_id):

    return recom.loc[customer_id].to_json()


<<<<<<< HEAD
def timehour(hour):
    return {"hour": hour, "category_id": result.loc[hour].tolist()}


=======
>>>>>>> 3b7d4246c80f07c57e908f5c015f1fb8d666e225
@app.route('/')
def hello():
    return "Welcome: Please put /recom for getting recommendation predictions"


@app.route('/recom',methods=['POST'])
def recommend():
    return recommendation(request.form.get('customer_id', type=int))


@app.route('/hour',methods=['POST'])
def hourtime():
    return jsonify(timehour(request.form.get('hour', type=int)))


if __name__ == '__main__':
    app.run()

