import os
import random


from flask import Flask
def get_bus_info(station):
    info = []
    for random_bus in range(10):
        bus_name = f"W{random.randint(1, 100)}"
        bus_arrival_time = random.randint(1, 30)
        bus_info = f"{bus_name} 还有 {bus_arrival_time} 分钟到达 {station}"
        info.append({bus_name: bus_info})
    return info
sd='a'
app = Flask(__name__)
@app.route('/bus/<station>')
def bus_info(station):
    info = bus.get_bus_info(station)
    return {
        "msg": "success",
        "data": info
    }
@app.route('/')
def hello_world():
    return get_bus_info(sd)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
