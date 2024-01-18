import requests


url = 'http://127.0.0.1:8000/api/category/'

response = requests.head(url)
# print(response.json())
assert response.status_code == 200
print(response.headers)

response = requests.get(url)
# print(response.json())
assert response.status_code == 200

response = requests.options(url)
# print(response.json())
assert response.status_code == 200

data = {
    'name': 'New category'
}

response = requests.post(url, data=data)
assert response.status_code == 201
#print(response.json())

id = response.json()['id']

url = f'http://127.0.0.1:8000/api/category/{id}/'

data = {
    'name': 'New new category'
}

response = requests.put(url, data)
assert response.status_code == 200
print(response.json())

data = {
    'name': 'New new category'
}

response = requests.patch(url, data)
assert response.status_code == 200
print(response.json())

response = requests.delete(url)
assert response.status_code == 204 # 204 No Content

