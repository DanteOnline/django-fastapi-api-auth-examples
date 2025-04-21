import requests


url = 'http://127.0.0.1:8000/api/random-expression/'

response = requests.get(url)

expression = response.json()['expression']
print('RANDOM EXPRESSION:', expression)

url = 'http://127.0.0.1:8000/api/calculate/'

# Интересно, что Django работает с data, а FastAPI только с json
response = requests.post(url, json={
    'expression': expression
})

print('RESULT:', response.json()['result'])
