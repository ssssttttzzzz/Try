import os
import random


from flask import Flask
def get_bus_info(station):
    info = []
    for random_bus in range(10):
        bus_name = f"W{random.randint(1, 100)}"
        bus_arrival_time = random.randint(1, 30)
        bus_info = f"{bus_name} has {bus_arrival_time} minutes to {station}"
        info.append({bus_name: bus_info})
    return info

app = Flask(__name__)
@app.route('/bus/<station>')
def bus_info(station):
    info = get_bus_info(station)
    return {
        "msg": "success",
        "data": info
    }
@app.route('/')
def hello_world():
    print('first try!\n')
    return 'oh lalala'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
