import os
import random
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    f=random.randint(0,9)
    return f

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
