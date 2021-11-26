# encoding=utf-8
import sys
import pathlib
sys.path.append(str(pathlib.Path.cwd().parent.parent))      # 解决命令找不到包路径
from biddingapi.apps.bid.spider_bidding.share_spider import *

# 抓取的网站信息
# 中国政府采购公告
# 'http://www.ccgp-hubei.gov.cn/notice/cggg/pzbgg/index_1.html'


search_url = 'http://www.ccgp-hubei.gov.cn:9040/quSer/search'


def content(session, bid_url):
    page_text = session.get(url=bid_url)
    page_text.encoding = 'utf-8'
    page_text = page_text.text
    # print(page_text)
    bid_money = re.findall('中标（成交）金额：.*?1px solid #666;">(.*?)</span>', page_text)                # 招标金额
    if not bid_money:
        bid_money = re.findall('预算金额：.*?1px solid #666;">(.*?)</span>', page_text)  # 招标金额
        if bid_money:
            bid_money = bid_money[0]+'(万元)'

    bid_customer = re.findall('采购人信息.*?名.*?称.*?1px solid #666;">(.*?)</span>', page_text)            # 客户名称
    if bid_customer:
        bid_customer = bid_customer[0]
    customer_phone = re.findall('采购人信息.*?联系方式.*?1px solid #666;">(.*?)</span>', page_text)          # 客户联系方式
    if customer_phone:
        customer_phone = customer_phone[0]
    return str(bid_money), str(bid_customer), str(customer_phone)


set_url = set()


def r_quests(q, increment=0):
    data = {
        'queryInfo.type': 'xmgg',
        'queryInfo.key': q,
        'queryInfo.jhhh': '',
        'queryInfo.fbr': '',
        'queryInfo.gglx': '',
        'queryInfo.cglx': '',
        'queryInfo.cgfs': '',
        'queryInfo.city': '--请选择--',
        'queryInfo.qybm': '',
        'queryInfo.district': '全省',
        'queryInfo.cgr': '',
        'queryInfo.begin': '',
        'queryInfo.end': '',
        'queryInfo.pageNo': '1',
        'queryInfo.pageSize': '15',
        'queryInfo.pageTotle': '11484',
    }
    get_cookie_u = 'http://www.ccgp-hubei.gov.cn:9040/quSer/initSearch'  # 获取cookie的url地址
    session = requests.Session()
    session.get(url=get_cookie_u)
    global set_url
    data['queryInfo.key'] = q
    sign = True
    n = 1
    pageNo = 1
    while sign:

        data['queryInfo.pageNo'] = str(pageNo)
        pageNo += 1
        page_text = session.post(url=search_url, headers=headers, data=data)

        page_text.encoding = 'utf-8'
        page_text = page_text.text
        # print(page_text)
        tree = etree.HTML(page_text)
        for r_i in range(1,16):
            b_title = tree.xpath('/html/body/div[3]/div/ul/li[{}]/div[1]/div[1]//text()'.format(r_i))      # 招标标题
            if not b_title:
                sign = False
                return
            else:
                # bid_title = ''.join([bt for bt in bid_title if '' not in bt or '\t' not in bt or '\r' not in bt or '\n' not in bt])
                b_title = ''.join(
                    [bt for bt in b_title if '' not in bt or '\t' not in bt or '\r' not in bt or '\n' not in bt])
            b_url = tree.xpath('/html/body/div[3]/div/ul/li[{}]/div[1]/div[1]//@href'.format(r_i))         # 网页链接地址

            if not b_url:
                b_url = ' '
                b_money, customer_name, customer_phone = ' ', ' ', ' '
                sign = False
                return
            else:
                if increment:
                    if b_url[0] in set_url:
                        sign = False
                        break

                if b_url[0] in set_url:
                    continue
                else:
                    set_url.add(b_url[0])
                    # set_title.add(bid_title)
                    b_money, customer_name, customer_phone = content(session, b_url[0])
            b_release = tree.xpath('/html/body/div[3]/div/ul/li[{}]/div[1]/div[2]/text()'.format(r_i))        # 发标日期
            GMT_FORMAT = '%a %b %d %H:%M:%S GMT+08:00 %Y'
            b_release = datetime.strptime(b_release[0], GMT_FORMAT)  # 转换成 指定时间字符串
            # temps = time.strptime(b_release, "%Y-%m-%d %H:%M:%S")         # 转换成 时间元组
            # b_release = int(time.mktime(temps))                                # 转换成 时间戳

            db_data = {}
            db_data['collect_time'] = datetime.now()        # 采集日期
            db_data['b_title'] = b_title                    # 招标标题
            db_data['b_url'] = b_url[0]                     # 网页链接地址
            db_data['b_release'] = b_release                # 发标日期
            db_data['b_money'] = b_money                    # 招标金额
            db_data['customer_name'] = customer_name        # 客户名称
            db_data['customer_phone'] = customer_phone      # 客户联系方式
            db_data['b_time'] = b_release                   # 获取招标文件时间
            db_data['collect_id'] = 1                       # 关联id

            print('第{}条数据:'.format(n))
            n += 1
            print('db_data:', db_data)
            try:
                Bidding.objects.create(**db_data)
            except Exception as e:

                log_write(str([e, db_data]))
                print(e, '数据没写进去！！！')


def main11():
    global set_url
    a = Bidding.objects.filter(collect_id=1).all().values_list('b_url')
    url_list = [i[0] for i in a]

    set_url = set_url | set(url_list)

    for c_i in crux.split('、'):
        r_quests(c_i, increment=1)


# main11()