from flask import Flask
from flask import request
app = Flask(__name__)

import py2json

@app.route("/api/py", methods=['POST'])
def py():
    return py2json.get_st(request.form['code'])

if __name__ == "__main__":
    app.run()
