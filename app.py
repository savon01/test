from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://mongodb:27017/')
db = client['mydb']
collection = db['mycollection']


@app.route('/api/data', methods=['GET', 'POST', 'PUT'])
def data():
    if request.method == 'GET':
        key = request.args.get('key')
        data = collection.find_one({'key': key})
        if data:
            return jsonify(data), 200
        else:
            return jsonify({'error': 'Key not found'}), 404

    if request.method == 'POST':
        key = request.json['key']
        value = request.json['value']
        collection.insert_one({'key': key, 'value': value})
        return jsonify({'message': 'Data created'}), 201

    if request.method == 'PUT':
        key = request.json['key']
        value = request.json['value']
        result = collection.update_one({'key': key}, {'$set': {'value': value}})
        if result.modified_count > 0:
            return jsonify({'message': 'Data updated'}), 200
        else:
            return jsonify({'error': 'Key not found'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
