import jsonpath
import requests


def get_json_value(json_data, key):
    values = jsonpath.jsonpath(json_data, f'$..{key}')
    if not values:  # 等价于 if values == False:
        return values

    return values[0] if len(values) == 1 else values


# 登录接口
login_url = 'http://154.12.20.250:5000/user_services/login'
login_data = {
    "password": "password123",
    "username": "user1"
}
res = requests.post(url=login_url, json=login_data)


user_info_url = 'http://154.12.20.250:5000/user_services/user_info'
headers = {
    'Authorization': get_json_value(res.json(), 'token')
}

res2 = requests.get(url=user_info_url, headers=headers)
print(res2.json())

assert 25435 == get_json_value(res2.json(), 'cart_id')

data = {
    "message": "successful",
    "data":
        [
            {'id': 19, 'name': 'iphone 16pm', 'price': 15990.0, 'stock': 1000},
            {'id': 20, 'name': 'xiaomi su7', 'price': 300000.0, 'stock': 1000},
            {'id': 21, 'name': 'xiaomi su7', 'price': 300000.0, 'stock': 1000}
        ]
}
print(type(data))
print(get_json_value(data, 'data[0].name'))


