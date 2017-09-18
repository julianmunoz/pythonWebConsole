import os
import subprocess
from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)


@app.route('/login')
def render_login():
    return render_template('index.html')

@app.route('/python')
def render_python():
    return render_template('python.html')

def render_python_with_data(lines, code):
    return render_template('python.html', lines=lines, code=code)

def render_sandbox_catched():
    return render_template("sandbox_catched.html")

@app.route("/python", methods=['POST'])
def process_python():
    code_file = open('code_file.py', 'w')
    code = request.form.get('note')
    for elem in ['import os', 'subprocess', 'import file', 'import sys']:
        if elem in code:
            return render_sandbox_catched()
    code_file.write(code)
    code_file.close()
    with open("result_file.txt", "w+") as output:
        subprocess.call(["python", "code_file.py"], stdout=output)
    result_file = open("result_file.txt", "r+")
    lines = result_file.readlines()
    result_file.close()
    return render_python_with_data(lines, code)


if __name__ == '__main__':
    app.run(host="0.0.0.0")

