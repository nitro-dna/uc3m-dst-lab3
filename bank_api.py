#Mateo Gomez, Artun Gonen, Andrey Bozev
from flask import Flask, abort, jsonify
from utilsAPI import (
    load_bank_data,
    find_dicts_by_key_value,
    delete_element_from_dictionary
)

app = Flask(__name__)
# load csv data into memory at startup using utilsAPI.py
operations, users = load_bank_data('bank_operations.csv')

@app.get('/users/<int:user_id>')
def get_user(user_id):
    user = find_dicts_by_key_value(users, 'User ID', user_id)
    if user:
        return jsonify(user[0]), 200
    else:
        return jsonify({'error': 'User not found'}), 404

@app.get('/operations/<int:operation_id>')
def get_operation(operation_id):
    operation = find_dicts_by_key_value(operations, 'Operation ID', operation_id)
    if operation:
        return jsonify(operation[0]), 200
    else:
        return jsonify({'error': 'Operation not found'}), 404

@app.delete('/users/<int:user_id>')
def delete_user(user_id):
    user_deleted = delete_element_from_dictionary(users, 'User ID', user_id)
    if user_deleted:
        return jsonify({}), 204
    else:
        return jsonify({'error': 'User not found'}), 404

@app.delete('/operations/<int:operation_id>')
def delete_operation(operation_id):
    operation_deleted = delete_element_from_dictionary(operations, 'Operation ID', operation_id)
    if operation_deleted:
        return jsonify({}), 204
    else:
        return jsonify({'error': 'Operation not found'}), 404

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
