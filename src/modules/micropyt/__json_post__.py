from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route('/do_first_analysis', methods=['POST'])
def do_first_analysis():
    # print(request.is_json)
    content = request.get_json()
    # print(type(content))
    print(content)
    response = jsonify({'device ': content['device'], 'value': content['value'], 'timestamp': content['timestamp']})
    return response


app.run(host='0.0.0.0', port='8090')
