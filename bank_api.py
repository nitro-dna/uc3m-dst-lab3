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

#get function to retrieve user and operation data by ID, returning 404 if not found
@app.get('/users/<int:user_id>')
def get_user(user_id):
    user = find_dicts_by_key_value(users, 'User ID', user_id)
    if user:
        #return the first matching user as a JSON response with a 200 status code 
        return jsonify(user[0]), 200
    else:
        #return a JSON response with an error message and a 404 status code if the user is not found
        return jsonify({'error': 'User not found'}), 404
    
#get function to retrieve operation data by ID, returning 404 if not found
@app.get('/operations/<int:operation_id>')
def get_operation(operation_id):
    operation = find_dicts_by_key_value(operations, 'Operation ID', operation_id)
    if operation:
        #return the first matching operation as a JSON response with a 200 status code
        return jsonify(operation[0]), 200
    else:
        #return a JSON response with an error message and a 404 status code if the operation is not found
        return jsonify({'error': 'Operation not found'}), 404

#delete function to remove user and operation data by ID, returning 404 if not found
@app.delete('/users/<int:user_id>')
def delete_user(user_id):
    user_deleted = delete_element_from_dictionary(users, 'User ID', user_id)
    if user_deleted:
        #return a JSON response with an empty object and a 204 (No Content)status code if the user is successfully deleted
        return jsonify({}), 204
    else:
        #return a JSON response with an error message and a 404 status code if the user is not found
        return jsonify({'error': 'User not found'}), 404

#delete function to remove operation data by ID, returning 404 if not found
@app.delete('/operations/<int:operation_id>')
def delete_operation(operation_id):
    operation_deleted = delete_element_from_dictionary(operations, 'Operation ID', operation_id)
    if operation_deleted:
        #return a JSON response with an empty object and a 204 (No Content)status code if the operation is successfully deleted
        return jsonify({}), 204
    else:
        #return a JSON response with an error message and a 404 status code if the operation is not found
        return jsonify({'error': 'Operation not found'}), 404

if __name__ == '__main__':
    #run the Flask application on localhost at port 5000 with debug mode enabled
    app.run(host='localhost', port=5000, debug=True)
