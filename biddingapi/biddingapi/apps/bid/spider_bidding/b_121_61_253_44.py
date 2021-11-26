# encoding=utf-8
import random
import re
import sys
import pathlib

import requests

sys.path.append(str(pathlib.Path.cwd().parent.parent))  # 解决命令找不到包路径
from bid.spider_bidding.share_spider import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
set_url = set()

# from requests.packages import urllib3
#
# urllib3.disable_warnings()
search_url = 'http://121.61.253.44:9127/EpointWebBuilder/rest/frontAppCustomAction/getPageInfoListNew'


# 抓取的网站信息
# 荆门市公共资源交易中心
# http://121.61.253.44:9127/xxfb/003002/level-two.html


def content(bid_url):







    page_text = requests.get(url=bid_url)
    if page_text.status_code != 200:
        return '[]','[]','[]'
    print(page_text.status_code)
    page_text = page_text.text
    # print(page_text.text)


    soup = BeautifulSoup(page_text, 'lxml')
    page_text = soup.select('.ewb-article-info')
    page_text = page_text[0].text
    # print(page_text)

    bid_money = re.findall('金额：(\d+,?\d+\.?\d+[万]?)', page_text)                # 招标金额
    if not bid_money:
        bid_money = re.findall('预算.*?(\d+,?\d+\.?\d+[万]?)元', page_text)  # 招标金额

        if bid_money:
            bid_money = bid_money[0]
        else:
            bid_money = re.findall('预算价.*?(\d+\.?\d+)', page_text)  # 招标金额

            if bid_money:
                bid_money = bid_money[0]
            else:
                bid_money = re.findall('(\d+\.?\d+[万]?)元', page_text)  # 招标金额

                if bid_money:
                    bid_money = bid_money[0]
    else:
        bid_money=bid_money[0]

    bid_customer = re.findall('招标人：([\u4e00-\u9fa5]+)', page_text)            # 客户名称
    # print(bid_customer)
    if bid_customer:
        bid_customer = bid_customer[0]
    else:
        bid_customer = re.findall('采.*?购.*?人：.*?([\u4e00-\u9fa5]+)', page_text)  # 客户名称
        if bid_customer:
            bid_customer = bid_customer[0]
        else:
            bid_customer = re.findall('联.*?系.*?人.*?：([\u4e00-\u9fa5]+)\n', page_text)  # 客户名称
            if bid_customer:
                bid_customer = bid_customer[0]

    customer_phone = re.findall('采购人.*?联系方式：.*?(\d+-?\d+)', page_text)          # 客户联系方式

    if customer_phone:
        customer_phone = customer_phone[0]
    else:
        customer_phone = re.findall('电话（传真）：.*?(\d+-?\d+)', page_text)  # 客户联系方式
        # print(customer_phone)
        if customer_phone:
            customer_phone = customer_phone[0]
        else:
            customer_phone = re.findall('电.*?话：(\d+-?\d+)', page_text)  # 客户联系方式
            # print(customer_phone)
            if customer_phone:
                customer_phone = customer_phone[0]

    # bid_money = bid_money[:10]
    # customer_phone = customer_phone[:20].split(' ')
    if isinstance(bid_money,str):
        bid_money = bid_money.split()[0]
    # print('***************')
    # print(str(bid_money),'\n', str(bid_customer), '\n',str(customer_phone))
    # print('***************')
    print(str(bid_money), str(bid_customer), str(customer_phone))
    return str(bid_money), str(bid_customer), str(customer_phone)



def r_quests(q, increment=0):
    data = {
        'params':
            '{"siteGuid":"7eb5f7f1-9041-43ad-8e13-8fcb82ea831a","categoryNum":"","startDate":"","endDate":"","kw":"第三方","pageIndex":1,"pageSize":15}'
    }
    # get_cookie_u = 'http://www.ccgp-hubei.gov.cn:9040/quSer/initSearch'  # 获取cookie的url地址
    # session = requests.Session()
    # session.get(url=get_cookie_u)
    global set_url
    sign = True
    n = 1
    pageNo = 0
    proxies = None
    while sign:

        print('页数pageNo:', pageNo)
        c = eval(data['params'])
        c['pageIndex'] = pageNo
        c['kw'] = q

        data['params'] = str(c)


        data['params'] = data['params']
        pageNo += 1
        for try_i in range(10):
            try:

                page_text = requests.post(
                    url=search_url,
                    headers=headers,
                    params=data,
                )


                page_text = page_text.json()

                # print(page_text)
                # return
                break
            except Exception as e:

                print('search_url_error：', e)
        else:
            log_write(str(['search_url:{}\ndata:{}'.format(search_url, data)]))
            continue

        # page_text.encoding = 'utf-8'

        # print(page_text)


        page_data = page_text['custom']['infodata']
        if not page_data:
            return

        for r_i in page_data:
            print('第{}页的数据:'.format(pageNo))

            b_title = r_i['title']  # 招标标题

            b_url = r_i['infourl']  # 网页链接地址

            b_release = r_i['infodate']  # 发标日期
            # 判断路由是否完整
            if "http" not in b_url:
                b_url = 'http://121.61.253.44:9127' + b_url  # 网页链接地址

            # 判断是否是增量
            if increment:
                if b_url in set_url:
                    sign = False
                    break
            if b_url in set_url:
                continue
            else:

                set_url.add(b_url)
                # set_title.add(bid_title)
                print('当前行数的url：', b_url)
                # print(b_title,b_url)

                b_money, customer_name, customer_phone = content(b_url)

                if b_money == 0:
                    log_write(str(['{}请求了一百次也没有成功！或者没有网页没有内容！'.format(b_url)]))
                    continue



            # GMT_FORMAT = '%a %b %d %H:%M:%S GMT+08:00 %Y'
            # b_release = datetime.strptime(b_release[0], GMT_FORMAT)  # 转换成 指定时间字符串
            # temps = time.strptime(b_release, "%Y-%m-%d %H:%M:%S")         # 转换成 时间元组
            # b_release = int(time.mktime(temps))                                # 转换成 时间戳
            if len(b_title) > 50:
                b_title = b_title[:51]
            db_data = {}
            db_data['collect_time'] = datetime.now()  # 采集日期
            db_data['b_title'] = b_title  # 招标标题
            db_data['b_url'] = b_url  # 网页链接地址
            db_data['b_release'] = b_release  # 发标日期
            db_data['b_money'] = b_money  # 招标金额
            db_data['customer_name'] = customer_name  # 客户名称
            db_data['customer_phone'] = customer_phone  # 客户联系方式
            db_data['b_time'] = b_release  # 获取招标文件时间
            db_data['collect_id'] = 11  # 关联id

            print('第{}条数据:'.format(n))
            n += 1
            print('db_data:', db_data)
            # return
            try:
                Bidding.objects.create(**db_data)
            except Exception as e:

                log_write(str([e, db_data]))
                print(e, '数据没写进去！！！')
                return
            #

def main14():
    global set_url
    a = Bidding.objects.filter(collect_id=11).all().values_list('b_url')
    url_list = [i[0] for i in a]

    set_url = set_url | set(url_list)

    # requests.get(url=get_cookie_u, headers=headers,)

    for c_i in crux.split('、'):
        print('关键字:', c_i)
        r_quests(c_i, increment=1)
        # break


# main14()
