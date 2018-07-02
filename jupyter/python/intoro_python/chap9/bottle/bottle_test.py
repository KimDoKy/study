import requests

resp = requests.get('http://localhost:9999/echo/Doky')

if resp.status_code == 200 and \
        resp.text == 'Say hello to my little friend: Doky!':
    print('It worked! That almost never happends!')
else:
    print('Arhg, got this:', resp.text)
