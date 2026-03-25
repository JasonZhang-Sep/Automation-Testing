import json
import requests

login_url = 'http://154.12.20.250:5000/user_services/login'
login_data = {
    "password": "password123",
    "username": "user1"
}

res = requests.post(url=login_url, json=login_data)
# print(res)
# print(type(res))
# print(res.json())
# print(type(res.json()))
# print(res.headers)
# print(res.text)
# print(res.content)
# print(res.request.url)

user_info_url = 'http://154.12.20.250:5000/user_services/user_info'
headers = {
    'Authorization': res.json()['token']
}
res2 = requests.get(url=user_info_url, headers=headers)
print(res2.json())

# a = 1
# b = 'asdfgh'
# c = [1, 2, 3]
# d = {'a': 1, 'b': '张杰'}
#
# print(json.dumps(a))
# print(type(json.dumps(a)))
# print(json.dumps(b))
# print(type(json.dumps(b)))
# print(json.dumps(c))
# print(type(json.dumps(c)))
# print(json.dumps(d, ensure_ascii=False))
# print(type(json.dumps(d)))

e = '{"name": "hcc","age": "18"}'
print(e)
print(type(e))
e = json.loads(e)
print(e)
print(type(e))



