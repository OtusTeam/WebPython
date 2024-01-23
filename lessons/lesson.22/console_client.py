import requests
from requests.auth import HTTPBasicAuth
import base64


url = 'http://127.0.0.1:8000/api/viewsets/category/'

# response = requests.head(url)
# # print(response.json())
# assert response.status_code == 200, response.status_code
# print(response.headers)


username = 'user'
password = 'user123456'

# response = requests.get(url, auth=HTTPBasicAuth(username, password))
response = requests.get(url, auth=(username, password))
assert response.status_code == 200, response.status_code
print(response.json())

# 88170d4bb8f0e284d06ec7e2c7da1a36241a8dfa
pare = f"{username}:{password}"
pare_coded = pare.encode("ascii")
print('PARE_CODED', pare_coded)

base64_bytes = base64.b64encode(pare_coded)
base64_string = base64_bytes.decode("ascii")
print(base64_string)

headers = {
    'Authorization': f'Basic {base64_string}'
}

print('HEADER:', headers)

response = requests.get(url, headers=headers)
assert response.status_code == 200, response.status_code
print(response.json())

token = '88170d4bb8f0e284d06ec7e2c7da1a36241a8dfa'

headers = {
    'Authorization': f'Token {token}'
}
#
response = requests.get(url, headers=headers)
assert response.status_code == 200, response.status_code
print(response.json())

# assert response.status_code == 200
#
# data = {
#     'name': 'New category'
# }
#
# response = requests.post(url, data=data)
# assert response.status_code == 201
# #print(response.json())
#
# id = response.json()['id']
#
# url = f'http://127.0.0.1:8000/api/viewsets/category/{id}/'
#
# data = {
#     'name': 'New new category'
# }
#
# response = requests.put(url, data)
# assert response.status_code == 200
# print(response.json())
#
# data = {
#     'name': 'New new category'
# }
#
# response = requests.patch(url, data)
# assert response.status_code == 200
# print(response.json())
#
# response = requests.delete(url)
# assert response.status_code == 204 # 204 No Content

