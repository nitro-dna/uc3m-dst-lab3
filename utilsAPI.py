# Authors: Mateo Gomez, Artun Gonen, Andrey Bozev
# Utility functions for Exercise 2: Bank API REST

import csv

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
                    'Family name': row['Family Name'],
                    'Bank Name': row['Bank Name']
                }
                users_list.append(user)
                seen_users.add(user_id)

    return operations_list, users_list

def find_dicts_by_key_value(data, key, value):
    return [item for item in data if item[key] == value]

def delete_element_from_dictionary(data, key, target_id):
    for index, item in enumerate(data):
        if item[key] == target_id:
            del data[index]
            return True
    return False