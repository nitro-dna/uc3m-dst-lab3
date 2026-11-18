#Mateo Gomez, Artun Gonen, Andrey Bozev
import requests

#url for the operation and user endpoints
url_operation_10 = 'http://localhost:5000/operations/10'
url_user_5 = 'http://localhost:5000/users/5'

print("1. FETCH OPERATION #10 (GET)")
#make a GET request to the operation endpoint for operation ID 10
response = requests.get(url_operation_10)

#print the status code and response content if the request was successful
print("Status Code:", response.status_code)
if response.status_code == 200:
    print("Response:", response.json())

print("\n=== 2. DELETE OPERATION #10 (DELETE) ===")
#make a DELETE request to the operation endpoint for operation ID 10
response = requests.delete(url_operation_10)
#print the status code and response content if the request was successful
print("Status Code:", response.status_code)
print("Response:", response.json() if response.text else {})

print("\n=== 3. VERIFY OPERATION #10 IS DELETED (GET -> 404) ===")
#make a GET request to the operation endpoint for operation ID 10 to verify deletion
response = requests.get(url_operation_10)
#print the status code to confirm that the operation has been deleted (should return 404)
print("Status Code:", response.status_code)
print("\n" + "-" * 50 + "\n")

print("=== 4. FETCH USER #5 (GET) ===")
#make a GET request to the user endpoint for user ID 5
response = requests.get(url_user_5)
#print the status code and response content if the request was successful
print("Status Code:", response.status_code)
if response.status_code == 200:
    print("Response:", response.json())

print("\n=== 5. DELETE USER #5 (DELETE) ===")
#make a DELETE request to the user endpoint for user ID 5
response = requests.delete(url_user_5)
#print the status code and response content if the request was successful
print("Status Code:", response.status_code)
print("Response:", response.json() if response.text else {})

print("\n=== 6. VERIFY USER #5 IS DELETED (GET -> 404) ===")
#make a GET request to the user endpoint for user ID 5 to verify deletion
response = requests.get(url_user_5)
#print the status code to confirm that the user has been deleted (should return 404)
print("Status Code:", response.status_code)