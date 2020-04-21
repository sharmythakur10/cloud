
from pprint import pprint
from flask import Flask, request, jsonify
from cassandra.cluster import Cluster
import json
import requests

cluster = Cluster(contact_points=['172.17.0.2'],port=9042)
session = cluster.connect()
app = Flask(__name__)

@app.route('/')
def hello():
    var =  "<h1>Hello {x}!</h1>".format(x="India")
    return var

@app.route('/cities', methods=['GET'])
def profile():
    rows = session.execute( """Select * From cities.result""")
    result=[]
    for r in rows:
            result.append({"city":r.city,"state":r.state,"district":r.district})
    return jsonify(result)


@app.route('/cities/<state>', methods=['GET'])
def list(state):
    rows2 = session.execute( """Select city from cities.result where state = '{}' ALLOW FILTERING""".format(state))
    #rows = session.execute( """Select count(city) from cities.result where state = '{}'""".format(state))
    result=[]
    for r in rows2:
            result.append(r.city)
         
    return jsonify(result)     

@app.route('/cities/integrate', methods=['GET'])
def intensity():
    url = "https://indian-cities-api-nocbegfhqg.now.sh/cities"
    headers = {}
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.ok:
            r = response.json()
            return jsonify(r)
    else:
            print(response.reason)


@app.route('/cities', methods=['POST'])
def create():
    #url = """INSERT INTO cities.result(city,state,district) VALUES( '{}','{}','{}')""".format(request.json['city'],request.json['state'],request.json['district']
    session.execute( """INSERT INTO cities.result(city,state,district) VALUES( '{}','{}','{}')""".format(request.json['city'],request.json['state'],request.json['district']))
    #print(url)
    return jsonify({'message': 'created: /records/{}'.format(request.json['city'])}), 201

@app.route('/cities', methods=['PUT'])
def update():
    session.execute( """UPDATE cities.result SET state= '{}', district= '{}' WHERE city='{}'""".format(request.json['state'],request.json['district'],request.json['city']))
    return jsonify({'message':'updated: /records/{}'.format(request.json['city'])}), 200


@app.route('/cities/<city>', methods=['DELETE'])
def delete(city):
    session.execute( """DELETE FROM cities.result WHERE city='{}'""".format(city))
    return jsonify({'message': 'deleted: /records/{}'.format(city)}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context=('cert.pem', 'key.pem'))

