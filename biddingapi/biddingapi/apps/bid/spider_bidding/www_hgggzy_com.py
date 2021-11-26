# encoding=utf-8
import random
import re
import sys
import pathlib

sys.path.append(str(pathlib.Path.cwd().parent.parent))  # 解决命令找不到包路径
from bid.spider_bidding.share_spider import *

set_url = set()

# from requests.packages import urllib3
#
# urllib3.disable_warnings()
search_url = 'http://www.hgggzy.com/ceinwz/wxfirst.ashx?newsid=400&zfcg=1111111111&FromUrl=jyxx_cg'


# 抓取的网站信息
# 黄冈市公共资源交易中心
# http://www.hgggzy.com/ceinwz/hgweb/indexhbhg.html?number=A00014A00014

def get_ip():
    # ip_url = 'http://t.ipjldl.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=1&fa=0&fetch_key=&groupid=0&qty=1&time=1&pro=&city=&port=1&format=json&ss=5&css=&ipport=1&dt=1&specialTxt=3&specialJson=&usertype=15'
    ip_url = 'http://www.kingdaili.com:3314/laofu.aspx?action=GetIPAPI&OrderNumber=309bb37e4b0479457008e776de2c8508&poolIndex=1633773042&qty=1'
    page_ip = requests.get(url=ip_url)
    # page_ip = page_ip.json()

    page_ip = page_ip.text
    proxies = page_ip.strip()


    print(page_ip)
    # proxies = page_ip['data'][0]['IP']
    proxies = {'http': 'http://'+proxies}
    print(proxies)
    return proxies


def content(bid_url):
    headers['User-Agent'] = random.choice(ua)
    headers['Connection'] = 'close'
    page_text12 = requests.get(url=bid_url, headers=headers)
    page_text12.encoding = 'utf-8'
    if page_text12.status_code != 200:
        log_write(str(['文章请求失败！--', bid_url]))
        return 0, 0, 0

    page_text1 = page_text12.text
    # print(page_text1)

    # page_text1.replace('\xa0', ' ').replace('\n', ' ')
    soup = BeautifulSoup(page_text1, 'lxml')

    page_text = soup.iframe

    location_url = re.findall(r"location.href='..(.*?)'", page_text1)
    # print(location_url)
    if page_text:
        if 'http' in page_text['src']:
            return [], [], []
        bid_url = 'http://www.hgggzy.com' + page_text['src']


        return content(bid_url)
    elif location_url:
        bid_url = 'http://www.hgggzy.com' + location_url[0]

        return content(bid_url)
    page_text12.encoding = 'utf-16'
    page_text1 = page_text12.text
    soup = BeautifulSoup(page_text1, 'lxml')
    page_text = soup.select('.Section1')
    if not page_text:
        return 0, 0, 0

    page_text = page_text[0].text
    # print(page_text)

    page_text = page_text.replace('\xa0', ' ').replace('\n', ' ')
    # print(page_text)

    # page_text = page_text
    # print(page_text)

    bid_money = re.findall('金额：(.*?) ', page_text)  # 招标金额
    if not bid_money:
        bid_money = re.findall('预算.*?(\d+\.?\d+[万]?)元', page_text)  # 招标金额

        if bid_money:
            bid_money = bid_money[0]
        else:
            bid_money = re.findall('(\d+万)', page_text)  # 招标金额

            if bid_money:
                bid_money = bid_money[0]
    else:
        bid_money = bid_money[0]

    bid_customer = re.findall('招标人：.*?([\u4e00-\u9fa5]+)', page_text)  # 客户名称
    # print(bid_customer)
    if bid_customer:
        bid_customer = bid_customer[0]
    else:
        bid_customer = re.findall('采.*?购.*?人：.*?([\u4e00-\u9fa5]+)', page_text)  # 客户名称
        if bid_customer:
            bid_customer = bid_customer[0]
        else:
            bid_customer = re.findall('联.*?系.*?人.*?：([\u4e00-\u9fa5]+)', page_text)  # 客户名称
            if bid_customer:
                bid_customer = bid_customer[0]

    customer_phone = re.findall('采购人.*?联系方式：.*?(\d+[-]?\d+)', page_text)  # 客户联系方式

    if customer_phone:
        customer_phone = customer_phone[0]
    else:
        customer_phone = re.findall('采购人联系方式.*?话：.*?(\d.*?)传', page_text)  # 客户联系方式
        # print(customer_phone)
        if customer_phone:
            customer_phone = customer_phone[0]
        else:
            customer_phone = re.findall('电.*?话：.*?(.*?)[\u4e00-\u9fa5]', page_text)  # 客户联系方式
            # print(customer_phone)
            if customer_phone:
                customer_phone = customer_phone[0]

    # bid_money = bid_money[:10]
    # customer_phone = customer_phone[:20].split(' ')
    if isinstance(bid_money, str):
        bid_money = bid_money.split()[0]
    # print('***************')
    # print(str(bid_money),'\n', str(bid_customer), '\n',str(customer_phone))
    # print('***************')
    print(str(bid_money), str(bid_customer), str(customer_phone))
    return str(bid_money), str(bid_customer), str(customer_phone)


def r_quests(q, increment=0):
    data = {
        'k': 'getnewsList',
        'pageIndex': '0',
        'pageCount': '10',
        'KW': q,
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
        data['pageIndex'] = str(pageNo)
        pageNo += 1
        for try_i in range(10):
            try:
                headers = {
                    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
                }
                headers['Connection'] = 'close'
                headers['User-Agent'] = random.choice(ua)
                page_text = requests.post(
                    url='http://www.hgggzy.com/ceinwz/wxfirst.ashx?newsid=400&zfcg=1111111111&FromUrl=jyxx_cg',
                    headers=headers,
                    data=data,
                    proxies=proxies,
                )
                # print(page_text.text)
                # print(headers)
                # print(data)
                if '防火墙' in page_text.text:
                    proxies = get_ip()
                    continue

                page_text = page_text.json()
                break
            except Exception as e:
                proxies = get_ip()
                print('search_url_error：', e)
        else:
            log_write(str(['search_url:{}\ndata:{}'.format(search_url, data)]))
            continue

        # page_text.encoding = 'utf-8'

        # print(page_text)

        # return
        page_data = page_text['newslist']
        if not page_data:
            return
        for r_i in page_data:
            print('第{}页的数据:'.format(pageNo))

            b_title = r_i['title']  # 招标标题

            b_url = r_i['url']  # 网页链接地址

            # 判断路由是否完整
            if "http" not in b_url:
                b_url = 'http://www.hgggzy.com/ceinwz' + r_i['url'].replace('..', '')  # 网页链接地址

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
                b_money, customer_name, customer_phone = content(b_url)

                if b_money == 0:
                    log_write(str(['{}请求了一百次也没有成功！或者没有网页没有内容！'.format(b_url)]))
                    continue
            b_release = r_i['pubdate']  # 发标日期

            # GMT_FORMAT = '%a %b %d %H:%M:%S GMT+08:00 %Y'
            # b_release = datetime.strptime(b_release[0], GMT_FORMAT)  # 转换成 指定时间字符串
            # temps = time.strptime(b_release, "%Y-%m-%d %H:%M:%S")         # 转换成 时间元组
            # b_release = int(time.mktime(temps))                                # 转换成 时间戳
            if len(customer_name) > 20:
                customer_name = customer_name[:15]
            db_data = {}
            db_data['collect_time'] = datetime.now()  # 采集日期
            db_data['b_title'] = b_title  # 招标标题
            db_data['b_url'] = b_url  # 网页链接地址
            db_data['b_release'] = b_release  # 发标日期
            db_data['b_money'] = b_money  # 招标金额
            db_data['customer_name'] = customer_name  # 客户名称
            db_data['customer_phone'] = customer_phone  # 客户联系方式
            db_data['b_time'] = b_release  # 获取招标文件时间
            db_data['collect_id'] = 6  # 关联id

            print('第{}条数据:'.format(n))
            n += 1
            print('db_data:', db_data)

            try:
                Bidding.objects.create(**db_data)
            except Exception as e:

                log_write(str([e, db_data]))
                print(e, '数据没写进去！！！')


def main7():
    global set_url
    a = Bidding.objects.filter(collect_id=6).all().values_list('b_url')
    url_list = [i[0] for i in a]

    set_url = set_url | set(url_list)

    # requests.get(url=get_cookie_u, headers=headers,)

    for c_i in crux.split('、'):
        print('关键字:', c_i)
        r_quests(c_i, increment=1)
        # break


# main7()
# get_ip()
# content('http://www.hgggzy.com/ceinwz/hyzq/hyzbjggszfcg.aspx?sgzbbm=HGJY(2017)F002')
