import requests


url = 'http://127.0.0.1:8000/api/random-expression/'

response = requests.get(url)

expression = response.json()['expression']
print('RANDOM EXPRESSION:', expression)

url = 'http://127.0.0.1:8000/api/calculate/'

response = requests.post(url, data={
    'expression': expression
})

print('RESULT:', response.json()['result'])
