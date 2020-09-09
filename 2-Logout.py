import requests, json

# 接口路径
logout_url = 'http://10.254.24.36/api/v2/auth'

# headers
head = {"Content-Type":"application/x-www-form-urlencoded"}

result = requests.delete(logout_url, headers=head)
print(result.json())