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
    print(df.shape)
    response = jsonify({'shape ': df.shape})
    return jsonify(response)


app.run(host='0.0.0.0', port='8090')
