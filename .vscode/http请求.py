import requests

# 发送GET请求获取特定用户信息
response = requests.get('http://127.0.0.1:5000/api/user/1')

# 打印响应内容
print(response.json())