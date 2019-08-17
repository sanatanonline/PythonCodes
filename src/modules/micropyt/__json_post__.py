from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
from io import BytesIO
import base64

x1 = ["red", "blue", "green", "orange", "yellow"]
y1 = [5, 2, 7, 8, 2]

x2 = ["red", "blue", "green", "orange", "yellow"]
y2 = [8, 6, 2, 5, 6]

plt.bar(x1, y1, label="Bar1")
plt.bar(x2, y2, label="Bar2", color="g")

plt.title("Bar Graph")
plt.xlabel("X-axis data")
plt.ylabel("Y-axis data")

plt.legend()

# plt.show()
fig = plt.figure()
figdata = BytesIO()
fig.savefig(figdata, format='png')
d = figdata.getvalue()
print(type(d))
d = base64.b64encode(d)
#print(d)

app = Flask(__name__)


@app.route('/do_first_analysis', methods=['POST'])
def do_first_analysis():
    # print(request.is_json)
    content = request.get_json()
    # print(type(content))
    # print(content['file_content'])
    df = pd.read_csv(StringIO(content['file_content']), sep=",")
    number_of_samples = len(df)
    number_of_features = 12
    features = list(df)
    response = jsonify(
        {'shape': str(df.shape), 'number_of_samples': number_of_samples, 'number_of_features': number_of_features,
         'features': features, 'image_content': str(d)})
    return response


app.run(host='0.0.0.0', port='8090')
