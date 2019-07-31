import requests
import json
a = json.dumps({"organizationID":"-1","useruid":"29d6a026-f774-4c9d-904c-e492a4246e10"})
header = {"Content-Type": "application/octet-stream","userinfo":a}
url = 'http://192.168.1.18:8150/api/Login/userlogin'
print("开始登陆集成平台")
def login(account,password,organizationID):
    data = {"account":account,"password":password,"organizationID":organizationID}
    response = requests.post(url,data,headers = header)
    print(response.text)
    if response.status_code ==200:
        print("登录成功")
    else:
        print("登录失败")
if __name__ == "__main__":
    login("admin","123456","-1")