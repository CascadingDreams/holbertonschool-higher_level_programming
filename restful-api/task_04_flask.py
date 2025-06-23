#!/usr/bin/python3

'''Basic flask API module'''

from flask import Flask, jsonify, request


app = Flask(__name__)

users = {}


@app.route('/')
def home():
    '''Root endpoint that returns welcome message'''
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    '''Retunrs a list of all usernames stored in the API'''
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/status')
def get_status():
    '''Returns status OK'''
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    '''returns the full obj corredponding to the provided username'''
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    '''Handles POST requests to add new users'''
    user_data = request.get_json()
    if not user_data or 'username' not in user_data:
        return jsonify({"error": "Username is required"}), 400
    username = user_data['username']
    users[username] = user_data

    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)
