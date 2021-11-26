import requests

session = requests.Session()
session.get(url="http://www.xiladaili.com")
# 去代理商获取url
response = session.get(
    url='http://www.xiladaili.com/api/?uuid=9e2ed14b846a4d28ad3afb8442916f54&num=3&place=中国&protocol=2&port=80&sortby=0&repeat=1&format=3&position=1')
a = response.text
ip_list = a.split(' ')  # 代理ip列表
print(ip_list)
# page_text = resume = requests.get(url=url, headers=headers, proxies={"https": random.choice(ip_list)})