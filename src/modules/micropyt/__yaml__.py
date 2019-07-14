from flask import Flask
import yaml

app = Flask(__name__)


def yamlify(data, status=200, headers=None):
    _headers = {'Content-Type': 'application/x-yaml'}
    if headers is not None:
        _headers.update(headers)
    return yaml.safe_dump(data), status, _headers


@app.route('/api')
def yaml_micro():
    return yamlify(['Hello', 'YAML', 'World!'])


if __name__ == '__main__':
    app.run()
