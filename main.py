from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    name = f"{request.args['name']}"
    nic = f"{request.args['nic']}"

    print(f"Name is {name}")
    print(f"NIC is {nic}")

    return f"{name} <br> {nic}"


if __name__ == '__main__':
    app.run(port=3232)
