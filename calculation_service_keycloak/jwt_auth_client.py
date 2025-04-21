import requests

url = 'http://127.0.0.1:8000/api/random-expression/'

response = requests.get(url)

print('GUEST')
print(response.status_code)
print(response.json())

print('USER')

get_token_data = {"client_id": "fastapi", "username": "user", "password": "user123", "grant_type": "password"}

url = 'http://localhost:8080/realms/master/protocol/openid-connect/token'

get_token_headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(
    url,
    data=get_token_data,
)

print('GOT TOKEN:', response.status_code)
print('GOT TOKEN:', response.text)

access_token = response.json()['access_token']


auth_headers = {
     'Authorization': f'Bearer {access_token}'
}

url = 'http://127.0.0.1:8000/api/random-expression/'

response = requests.get(url, headers=auth_headers)
#
expression = response.json()['expression']
print('RANDOM EXPRESSION:', expression)

url = 'http://127.0.0.1:8000/api/calculate/'

response = requests.post(
    url,
    json={
        'expression': expression
    },
    headers=auth_headers,
)

print('RESULT:', response.json()['result'])
