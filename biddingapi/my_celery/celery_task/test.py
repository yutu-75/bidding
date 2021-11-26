import requests


url = 'http://xnztb--xianning--gov--cn--e5016.proxy.xianning.gov.cn/'
page = requests.get(url=url)
print(page)
print(page.status_code)
print(page.text)