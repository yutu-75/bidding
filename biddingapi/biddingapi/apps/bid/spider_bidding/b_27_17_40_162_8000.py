# encoding=utf-8
import sys
import pathlib
sys.path.append(str(pathlib.Path.cwd().parent.parent))      # 解决命令找不到包路径
from ..spider_bidding.share_spider import *

set_url = set()

from requests.packages import urllib3
urllib3.disable_warnings()
search_url = 'http://27.17.40.162:8089/quSer/search'



# 抓取的网站信息
# 武汉市政府采购信息发布系统
# http://27.17.40.162:8000/


def content(bid_url):

    page_text1 = requests.get(url=bid_url)
    page_text1.encoding = 'utf-8'
    if page_text1.status_code != 200:
        log_write(str(['文章请求失败！--',bid_url]))
        return 0, 0, 0

    page_text1 = page_text1.text

    # page_text1.replace('\xa0', ' ').replace('\n', ' ')
    soup = BeautifulSoup(page_text1,'lxml')
    # print(page_text1)
    page_text = soup.select('.art_con')

    page_text = page_text[0].text
    # print(page_text)
    page_text = page_text.replace('\xa0', ' ').replace('\n', ' ')
    # page_text = page_text
    # print(page_text)

    bid_money = re.findall('金额：(.*?) ', page_text)                # 招标金额
    if not bid_money:
        bid_money = re.findall('预算.*?：(.*?)（', page_text)  # 招标金额

        if bid_money:
            bid_money = bid_money[0]
        else:
            bid_money = re.findall('预算.*?：(.*?)\n', page_text)  # 招标金额

            if bid_money:
                bid_money = bid_money[0]
    else:
        bid_money=bid_money[0]

    bid_customer = re.findall('采购人信息.*?名.*?称：.*?([\u4e00-\u9fa5]+)', page_text)            # 客户名称
    # print(bid_customer)
    if bid_customer:
        bid_customer = bid_customer[0]
    else:
        bid_customer = re.findall('采购人.*?名.*?称：.*?([\u4e00-\u9fa5]+)', page_text)  # 客户名称
        if bid_customer:
            bid_customer = bid_customer[0]
        else:
            bid_customer = re.findall('联.*?系.*?人.*?：([\u4e00-\u9fa5]+)\n', page_text)  # 客户名称
            if bid_customer:
                bid_customer = bid_customer[0]

    customer_phone = re.findall('采购人信息.*?联系方式：.*?(.*?) ', page_text)          # 客户联系方式

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
    if isinstance(bid_money,str):
        bid_money = bid_money.split()[0]
    # print('***************')
    # print(str(bid_money),'\n', str(bid_customer), '\n',str(customer_phone))
    # print('***************')
    return str(bid_money), str(bid_customer), str(customer_phone)

def r_quests(q, increment=0):
    data = {
        'queryInfo.begin':'',
        'queryInfo.end':'',
        'queryInfo.jhhh':'',
        'queryInfo.key': q,
        'queryInfo.dljgmc':'',
        'queryInfo.type': 'xmgg',
        'queryInfo.gglx': '招标公告',
        'queryInfo.cgfs':'',
        'queryInfo.pageNo': '1',
        'queryInfo.pageSize': '15',
        'queryInfo.pageTotle': '19',
        'queryInfo.c':'',
        'queryInfo.g':'',
        'queryInfo.k':'',
    }
    # get_cookie_u = 'http://www.ccgp-hubei.gov.cn:9040/quSer/initSearch'  # 获取cookie的url地址
    # session = requests.Session()
    # session.get(url=get_cookie_u)
    global set_url
    sign = True
    n = 1
    pageNo = 1
    while sign:
        print('页数pageNo:',pageNo)
        data['queryInfo.pageNo'] = str(pageNo)
        pageNo += 1
        for try_i in range(100):
            try:
                page_text = requests.post(url=search_url, headers=headers, data=data, timeout=2)
                break
            except Exception as e:
                print('search_url_error：',e)
        else:
            log_write(str(['search_url:{}\ndata:{}'.format(search_url,data)]))
            continue

        page_text.encoding = 'utf-8'
        page_text = page_text.text
        tree = etree.HTML(page_text)
        for r_i in range(1,10):
            print('第{}页的第几行r_i:'.format(pageNo),r_i)

            b_title = tree.xpath('/html/body/div[3]/ul/li[{}]/div[1]/div[1]//text()'.format(r_i))      # 招标标题

            if not b_title:
                sign = False
                return

            else:
                b_title = ''.join(b_title).strip()
                # if q not in b_title:
                #     sign = False
                #     return

            b_url = tree.xpath('/html/body/div[3]/ul/li[{}]/div[1]/div[1]/a/@href'.format(r_i))         # 网页链接地址

            if not b_url:
                b_url = ' '
                b_money, customer_name, customer_phone = ' ', ' ', ' '
                continue
            else:

                # 判断路由是否完整
                if "http" not in b_url[0]:
                    b_url[0] = 'http://27.17.40.162:8000'+b_url[0]

                # 判断是否是增量
                if increment:
                    if b_url[0] in set_url:
                        sign = False
                        break
                if b_url[0] in set_url:
                    continue
                else:

                    set_url.add(b_url[0])
                    # set_title.add(bid_title)
                    print('当前行数的url：',b_url[0])
                    b_money, customer_name, customer_phone = content(b_url[0])
                    if b_money == 0:

                        log_write(str(['{}请求了一百次也没有成功！'.format(b_url[0])]))
                        continue
            b_release = tree.xpath('/html/body/div[3]/ul/li[{}]/div[1]/div[2]/text()'.format(r_i))        # 发标日期

            # b_release = b_release[0].strip()
            # ['Wed Sep 29 16:13:00 CST 2021']

            GMT_FORMAT = '%a %b %d %H:%M:%S CST %Y'
            b_release = datetime.strptime(b_release[0], GMT_FORMAT)  # 转换成 指定时间字符串
            # print(b_release)
            # temps = time.strptime(b_release, "%Y-%m-%d %H:%M:%S")         # 转换成 时间元组
            # b_release = int(time.mktime(temps))                                # 转换成 时间戳
            if len(customer_name) > 20:
                customer_name = customer_name[:15]

            db_data = {}
            db_data['collect_time'] = datetime.now()        # 采集日期
            db_data['b_title'] = b_title                    # 招标标题
            db_data['b_url'] = b_url[0]                     # 网页链接地址
            db_data['b_release'] = b_release                # 发标日期
            db_data['b_money'] = b_money                    # 招标金额
            db_data['customer_name'] = customer_name        # 客户名称
            db_data['customer_phone'] = customer_phone      # 客户联系方式
            db_data['b_time'] = b_release                   # 获取招标文件时间
            db_data['collect_id'] = 4                       # 关联id

            print('第{}条数据:'.format(n))
            n += 1
            print('db_data:', db_data)

            try:
                Bidding.objects.create(**db_data)
            except Exception as e:

                log_write(str([e, db_data]))
                print(e, '数据没写进去！！！')
# content('http://27.17.40.162:8000//notice/202008/notice_c4d951fb80ae45ff9dbf12464e3e4173.html')
def main15():
    global set_url
    a = Bidding.objects.filter(collect_id=4).all().values_list('b_url')
    url_list = [i[0] for i in a]

    set_url = set_url | set(url_list)

    # requests.get(url=get_cookie_u, headers=headers,)

    for c_i in crux.split('、'):
        print('关键字:',c_i)
        r_quests(c_i, increment=1)
        # break


# main15()
