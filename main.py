import os
import random
import regression

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
    dict1 = {"name": "monkey", "hge": 23}
    dict2=dict1.copy()
    dict2.update(post)
    aaa=dict2['hge']
    dict2['hge']=int(aaa)+3
    return jsonify(dict2)
@app.route('/cx2',methods=['POST'])
def new_post2():
    post=request.json
    xArr=[[1,1],[1,1.1],[1,1.2],[1,1.3],[1,1.4]]
    yArr=[1,2,3,4,5]
    ws=regression.standRegres(xArr,yArr)
    yuce=[[1,2],[1,3]]
    jieguo=regression.answer(yuce,ws)
    jieguo.update(post)
    return jsonify(jieguo)
@app.route('/play') 
def jsb():
    canshu=random.randint(0,2)
    if canshu==0:
        return '<h1>you give bu!</h1>' 
    elif canshu==1:
        return '<h1>you give jiandao!</h1>' 
    else:
        return '<h1>you give shitou!</h1>'  
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
