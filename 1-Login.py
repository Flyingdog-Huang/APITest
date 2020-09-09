import requests, json

# 接口路径
login_url = 'http://10.254.24.36/auth/login'
# body
body = json.dumps({"username": "it@dtsjy.com", "password": "dtsjy2586", "auth_token": True})
# json.dumps()将字典形式的数据转化为字符串
# json.loads()用于将字符串形式的数据转化为字典
# headers
head = {"Content-Type":"application/json", "user-agent":"Koala Admin", "Authorization": "e3f14076-571e-4243-b315-bbc4d34547d4"}
result = requests.post(login_url, data=body, headers=head)
print(result.json())