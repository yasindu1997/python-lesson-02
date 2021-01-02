from flask import Flask
from flask import request
from nic_parser.parser import Parser

app = Flask(__name__)


@app.route('/')
def hello_world():
    name = f"{request.args['name']}"
    nic = f"{request.args['nic']}"
    nic_pass = Parser(f"{request.args['nic']}")
    bday = nic_pass.birth_date
    gender = nic_pass.gender

    print(f"Name is {name}")
    print(f"NIC is {nic}")

    return f"{name} <br> {nic} <br> {bday} <br> {gender}"


if __name__ == '__main__':
    app.run(port=3232)
