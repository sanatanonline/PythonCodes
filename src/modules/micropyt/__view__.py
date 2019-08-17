from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd
from io import StringIO

app = Flask(__name__)


@app.route('/do_first_analysis', methods=['POST'])
def do_first_analysis():
    # print(request.is_json)
    content = request.get_json()
    # print(type(content))
    # print(content['file_content'])
    df = pd.read_csv(StringIO(content['file_content']), sep=",")
    number_of_samples = len(df)
    features = list(df)
    number_of_features = len(features)

    response = jsonify(
        {'file_name': content['file_name'],
         'file_size': content['file_size'],
         'file_type': content['file_type'],
         'shape': str(df.shape),
         'number_of_samples': number_of_samples,
         'number_of_features': number_of_features,
         'features': features})
    return response


app.run(host='0.0.0.0', port='8090')
