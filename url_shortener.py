from flask import Flask, request
from flask.json import jsonify
import requests
import hashlib
from pyshorteners import Shortener
app = Flask(__name__)

hash_to_uri = {}

BASE_URL = 'https://goo.gl/'


@app.route('/', methods=['POST'])
def post_url():
    url = request.form['url']
    short = shortener.short(url).rsplit('/')[-1]
    hash_to_uri[short] = url
    return jsonify({'ID':short, 'URL':BASE_URL + short}), 201


@app.route('/', methods=['DELETE'])
def delete_url():
    global hash_to_uri
    hash_to_uri = {}
    return '', 204


@app.route('/', methods=['GET'])
def all_keys():
    all_keys = [k for k in hash_to_uri.iterkeys()]
    return jsonify({'keys': all_keys}), 200


@app.route('/<id>', methods=['GET'])
def get_value(id):
    if id in hash_to_uri:
        return jsonify(hash_to_uri[id]), 301
    else: return jsonify(''), 404


@app.route('/<id>', methods=['PUT', 'DELETE', 'POST'])
def put_indiv(id):
    if request.method == 'PUT':
        url = request.form['url']
        if id not in hash_to_uri:
            hash_to_uri[id] = url
            return jsonify(''), 200
        else: return jsonify(''), 400
    elif request.method =='POST':
        url = request.form['url']
        if id in hash_to_uri:
            hash_to_uri[id] = url
            return jsonify(''),200
        else: return jsonify(''),404
    else:
        if id in hash_to_uri:
            del hash_to_uri[id]
            return jsonify(''), 204
        else: return jsonify(''), 404


if __name__ == '__main__':
    api_key = 'AIzaSyBducKOMRxPojOCVmby0SeLohxjLnUj2ew'
    shortener = Shortener('Google', api_key=api_key)
    app.run(host='0.0.0.0', debug=True)
