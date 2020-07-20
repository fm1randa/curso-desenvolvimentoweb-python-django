import requests

url = 'https://django.pro.br'
req = requests.get(url)

print(req.url)

print(req.status_code)

print(req.text)