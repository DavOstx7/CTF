import requests

response = requests.get('https://jupiter.challenges.picoctf.org/problem/26704/flag', {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36!"})
print(response.content.decode('utf-8'))