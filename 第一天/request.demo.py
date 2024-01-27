#第一天

#pip install requests 安装requests库
import requests
from requests import utils

url = 'http://127.0.0.1:8787/dar/user/login'

header = {'Content-Type':'application/x-www-formurlencoded;charset=UTF-8'}

data = {
   "user_name": "test01",
   "passwd": "admin123"
}


# ---------------Post---------------
res=requests.post(url=url,data=data)

#默认返回状态码
print(res)
#返回文本类型的数据 如出现中文显示不出 可加上res.text.encode().decode("unicode_escape") 双引号
print(res.text,type(res.text))

#返回二进制内容
#print(res.content)

#返回json格式 单引号
print(res.json(),type(res.json()))

#----get
#----put
#----delete
url_2="http://127.0.0.1:8787//coupApply/cms/goodsList"
header_2={
   'Content-Type':'application/x-www-formurlencoded;charset=UTF-8'
}
json_data={
"msgType": "getHandsetListOfCust",
"page": 1,
"size": 20
}




# ---------------PUT---------------
#requests.put()


# ---------------DELETE---------------
#requests.delete()


#-------------------------requests.session() 会话------------------------------------
#在多个请求之间共享的  会话管理-持久性会话  比如说登录一个页面进行身份验证，然后才能访问受保护的页面，才session中创建一个登录状态以便在其它地方访问就不需要再次登录了

session = requests.session()

res_3 =session.request(method='get',url=url_2,params=json_data,headers=header_2)
#其中有个verify=None参数，但为https时需要将verify的值设置为false否则无法通过


print(res_3.json())


#4.获取接口的cookie-存储在浏览器里的一个消息 一个状态
#也就是说在访问其它接口的时候，不需要重新登录，登录一次即可
# （存储一系列登录信息 拿到cookie之后会校验的你的身份对不对，
# 如果对的话访问相应接口，不对返回报错信息）

result = session.request(method='post',url=url,data=data)
cookie = requests.utils.dict_from_cookiejar(result.cookies) #这样就拿到cookie
#{'error_code': None, 'msg': '登录成功', 'msg_code': 200, 'orgId': '6140913758128971280', 'token': '46fc2BCDEd3eAD405A02BE4b59EfE', 'userId': '5201911959691425856'} <class 'dict'>
#{'access_token_cookie': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwMDgyMTQxOSwianRpIjoiYzVhZjYwNzItNWNjZC00NzIyLThiZjEtYjA2YTEzODA2ZjkwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImV4YW1wbGVfdXNlciIsIm5iZiI6MTcwMDgyMTQxOSwiZXhwIjoxNzAwODIyMzE5fQ.Bydpgt7Wdd2CAaRPAqOUJ8RkMIu60eUKo71UbEJpzz8'}


#服务器生成的cookie
print(cookie)

if __name__ == '__main__':
   res = requests.post(url=url, data=data)
   print(res.text,type(res.text))#text是字符串str形式
   print(res.json(), type(res.json())) # <class 'dict'>
   result = session.request(method='post', url=url, data=data)
   cookie = requests.utils.dict_from_cookiejar(result.cookies)
   print(cookie)





