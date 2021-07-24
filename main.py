import os
import random
import regression

from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
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
    xArr=post['x']
    yArr=post['y']
    yuce=post['yuce']
    lam=0.2
    try:
        lam=post['lam']
    except:
        pass
    ws=regression.standRegres(xArr, yArr)
    jieguo=regression.answer(yuce,ws)
    jieguo.update(post)
    return jsonify(jieguo)
@app.route('/play') 
def jsb():
    canshu=random.randint(0,2)
    if canshu==0:
        image_data = open('1.jpg', "rb").read()
        response = make_response(image_data)
        response.headers['Content-Type'] = 'image/jpg'
        return response
    elif canshu==1:
        image_data = open('2.jpg', "rb").read()
        response = make_response(image_data)
        response.headers['Content-Type'] = 'image/jpg'
        return response
    else:
        image_data = open('3.jpg', "rb").read()
        response = make_response(image_data)
        response.headers['Content-Type'] = 'image/jpg'
        return response
@app.route('/img')
def display_img():
    image_data = open('23.jpg', "rb").read()
    response = make_response(image_data)
    response.headers['Content-Type'] = 'image/jpg'
    return response
  
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
