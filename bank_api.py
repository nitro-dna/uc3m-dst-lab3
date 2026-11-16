from flask import Flask, abort, jsonify
import csv

app = Flask(__name__)

def load_bank_data(filename='bank_operations.csv'):
    operations_list = []
    users_list = []
    seen_users = set()

    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            op_id = int(row['Operation ID'])
            user_id = int(row['User ID'])

            operation = {
             'Operation ID': op_id,
             'User ID': user_id,
             'Amount (Euros)': float(row['Amount (Euros)']),
             'Bank Name': row['Bank Name']
            }
            operations_list.append(operation)

            if user_id not in seen_users:
                user = {
                    'User ID': user_id,
                    'Name': row['Name'],
                    'Family name': row['Family name'],
                    'Bank Name': row['Bank Name']
                }
                users_list.append(user)
                seen_users.add(user_id)

    return operations_list, users_list

operations, users = load_bank_data('bank_operations.csv')

def find_dicts_by_key_value(data, key, value):
    return [item for item in data if item[key] == value]

def delete_element_from_dictionary(data, key, target_id):
    for index, item in enumerate(data):
        if item[key] == target_id:
            del data[index]
            return True
    return False

@app.get('/users/<int:user_id>')
def get_user(user_id):
    user = find_dicts_by_key_value(users, 'User ID', user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'error': 'User not found'}), 404

@app.get('/operations/<int:operation_id>')
def get_operation(operation_id):
    operation = find_dicts_by_key_value(operations, 'Operation ID', operation_id)
    if operation:
        return jsonify(operation), 200
    else:
        return jsonify({'error': 'Operation not found'}), 404

@app.delete('/users/<int:user_id>')
def delete_user(user_id):
    user_deleted = delete_element_from_dictionary(users, 'User ID', user_id)
    if user_deleted:
        return jsonify({}), 204
    else:
        abort(404, description="User not found")

@app.delete('/operations/<int:operation_id>')
def delete_operation(operation_id):
    operation_deleted = delete_element_from_dictionary(operations, 'Operation ID', operation_id)
    if operation_deleted:
        return jsonify({}), 204
    else:
        abort(404, description="Operation not found")

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
