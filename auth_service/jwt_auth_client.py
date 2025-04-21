import requests

url = 'http://127.0.0.1:8000/api/random-expression/'

response = requests.get(url)

print('GUEST')
print(response.status_code)
print(response.json())

print('USER')

get_token_data = {"username": "user", "password": "user123"}

url = 'http://127.0.0.1:8000/api/token/'

response = requests.post(
    url,
    json=get_token_data,
)

print('GOT TOKEN:', response.json())

access_token = response.json()['access']


auth_headers = {
    'Authorization': f'Bearer {access_token}'
}

url = 'http://127.0.0.1:8000/api/random-expression/'


response = requests.get(url, headers=auth_headers)

expression = response.json()['expression']
print('RANDOM EXPRESSION:', expression)

url = 'http://127.0.0.1:8000/api/calculate/'

response = requests.post(
    url,
    data={
        'expression': expression
    },
    headers=auth_headers,
)

print('RESULT:', response.json()['result'])
