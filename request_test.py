import requests

URL = "https://test-fastapi-ik0j.onrender.com"
# URL = "http://127.0.0.1:8000/"

r = requests.get(url=URL)

data = r.json()

nome = data['name']
sobrenome = data['surname']

print(nome)
print(sobrenome)
