import os
import random


from flask import Flask
from flask import request
from flask import jsonify
def get_bus_info(station):
    info = []
    for random_bus in range(10):
        bus_name = f"W{random.randint(1, 100)}"
        bus_arrival_time = random.randint(1, 30)
        bus_info = f"{bus_name} has {bus_arrival_time} minutes to {station}"
        info.append({bus_name: bus_info})
    return info
def get_jieguo(shu):
    t=int(shu)*int(shu)
    return t
app = Flask(__name__)
@app.route('/bus/<station>')
def bus_info(station):
    info = get_bus_info(station)
    return {
        "msg": "success",
        "data": info
    }
@app.route('/cx',methods=['POST'])
def new_post():
    post = request.json
    dict1 = {"name": "monkey", "age": 23}
    try:
        for i,e in post.items():
            dict1[i]=e
        ta=int(dict1['a'])+int(dict1['b'])
        c={'jieguo':ta}
    except: pass
    return jsonify(c)
 
    
@app.route('/')
def hello_world():
    user_agent = request.headers.get('User-Agent') 
    return '<p>Your browser is %s</p>' % user_agent
@app.route('/js/<int:shu>')
def pingfang(shu):
    jieguo= get_jieguo(shu)
    return '<h1>welcome %s</h1>' %jieguo


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
