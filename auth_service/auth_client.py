import requests


url = 'http://127.0.0.1:8000/api/random-expression/'

response = requests.get(url)

print('GUEST')
print(response.status_code)
print(response.json())

print('USER')

auth = ('user', 'user123')
response = requests.get(url, auth=auth)

expression = response.json()['expression']
print('RANDOM EXPRESSION:', expression)

url = 'http://127.0.0.1:8000/api/calculate/'

response = requests.post(
    url,
    data={
        'expression': expression
    },
    auth=auth,
)

print('RESULT:', response.json()['result'])
