import pymysql
from flask import Flask, request, jsonify
import db_connector

app = Flask(__name__)


@app.route('/users/<user_id>', methods=['GET'])
def get_user_data(user_id):
    if request.method == 'GET':
        try:
            user_data = db_connector.get_user_data(user_id)
            if user_data:
                return jsonify({
                    "status": "ok",
                    "user_name": user_data[0][1]
                }), 200
            else:
                return jsonify({
                    "status": "error",
                    "reason": "no such id"
                }), 500
        except pymysql.Error as error:
            print(error)


@app.route('/users/<user_id>', methods=['POST'])
def create_user(user_id):
    if request.method == 'POST':
        request_data = request.json
        user_name = request_data.get('user_name')
        try:
            db_connector.create_user(user_id=user_id, user_name=user_name)
            return jsonify({
                "status": "ok",
                "user_name": user_name
            }), 200
        except pymysql.IntegrityError:
            return jsonify({
                "status": "error",
                "reason": "id already exists"
            }), 500


@app.route('/users/<user_id>', methods=['PUT'])
def modify_user(user_id):
    pass


@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    pass


app.run(host='127.0.0.1', port=5600)
