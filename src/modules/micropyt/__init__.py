from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd
import ml.data as dt

app = Flask(__name__)


@app.route('/first_look', methods=['POST'])
def do_first_look():
    content = request.get_json()
    df, df1 = dt.load_titanic_data()
    number_of_samples = len(df)
    features = list(df)
    number_of_features = len(features)
    datadict = pd.DataFrame(df.dtypes)

    response = jsonify(
        {'shape': str(df.shape),
         'number_of_samples': number_of_samples,
         'number_of_features': number_of_features,
         'meta_data': datadict.to_dict(),
         'features': features})
    return response


app.run(host='0.0.0.0', port='8090')
