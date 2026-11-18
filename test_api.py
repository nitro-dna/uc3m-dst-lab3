#Mateo Gomez, Artun Gonen, Andrey Bozev
import requests

url_operation_10 = 'http://localhost:5000/operations/10'
url_user_5 = 'http://localhost:5000/users/5'

print("1. FETCH OPERATION #10 (GET)")
response = requests.get(url_operation_10)
print("Status Code:", response.status_code)
if response.status_code == 200:
    print("Response:", response.json())

print("\n=== 2. DELETE OPERATION #10 (DELETE) ===")
response = requests.delete(url_operation_10)
print("Status Code:", response.status_code)
print("Response:", response.json() if response.text else {})

print("\n=== 3. VERIFY OPERATION #10 IS DELETED (GET -> 404) ===")
response = requests.get(url_operation_10)
print("Status Code:", response.status_code)

print("\n" + "-" * 50 + "\n")

print("=== 4. FETCH USER #5 (GET) ===")
response = requests.get(url_user_5)
print("Status Code:", response.status_code)
if response.status_code == 200:
    print("Response:", response.json())

print("\n=== 5. DELETE USER #5 (DELETE) ===")
response = requests.delete(url_user_5)
print("Status Code:", response.status_code)
print("Response:", response.json() if response.text else {})

print("\n=== 6. VERIFY USER #5 IS DELETED (GET -> 404) ===")
response = requests.get(url_user_5)
print("Status Code:", response.status_code)