# encoding=utf-8
import sys
import pathlib
sys.path.append(str(pathlib.Path.cwd().parent.parent))      # 解决命令找不到包路径
from bid.spider_bidding.share_spider import *

set_url = set()

from requests.packages import urllib3
urllib3.disable_warnings()
search_url = 'http://xgxz.xiaogan.gov.cn/zfcg/index.jhtml'


# 抓取的网站信息
# 孝感政务服务和大数据管理局
# http://xgxz.xiaogan.gov.cn/zfcg/index.jhtml


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
    page_text = soup.select('#content_txt')

    page_text = page_text[0].text
    # print(page_text)
    page_text = page_text.replace('\xa0', ' ').replace('\n', ' ')
    # page_text = page_text
    # print(page_text)

    bid_money = re.findall('金额：(.*?) ', page_text)                # 招标金额
    if not bid_money:
        bid_money = re.findall('预算.*?(\d+\.?\d+[万]?)元', page_text)  # 招标金额

        if bid_money:
            bid_money = bid_money[0]
        else:
            bid_money = re.findall('(\d+万)', page_text)  # 招标金额

            if bid_money:
                bid_money = bid_money[0]
    else:
        bid_money=bid_money[0]

    bid_customer = re.findall('招标人：.*?([\u4e00-\u9fa5]+)', page_text)            # 客户名称
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
    print(str(bid_money), str(bid_customer), str(customer_phone))
    return str(bid_money), str(bid_customer), str(customer_phone)


def r_quests(crux_list, increment=0):

    """
    mainUrl: http://ggzyjy.yichang.gov.cn/
    :param crux_list:
    :param increment:
    :return:
    """
    global set_url
    main_url = 'http://ggzyjy.yichang.gov.cn'

    # 采购公告
    cg_url_one = 'http://xgxz.xiaogan.gov.cn/cggg/index.jhtml'
    cg_url = 'http://xgxz.xiaogan.gov.cn/cggg/index_{}.jhtml'

    def get_etree(c_url):
        for try_i in range(10):
            try:
                page_text = requests.get(url=c_url, headers=headers)
                page_text.encoding = 'utf-8'
                tree_ = etree.HTML(page_text.text)
                return tree_

            except Exception as e:
                print('value_id_error：', e)
        else:
            log_write(str([c_url, '--请求了十次也没有反回数据！', ]))
            return 0

    sign = True
    n = 0
    while sign:

        n += 1
        print(f'第{n}页')
        c_ul = cg_url.format(n)
        if n == 1:
            c_ul = cg_url_one

        tree = get_etree(c_ul)
        if tree == 0:
            return

        for r_i in range(1, 16):
            # print(f'第{pageNo1}页 第{r_i}行:')
            b_title = tree.xpath(f'/html/body/div/div/div[2]/div[2]/ul/li[{r_i}]/a/text()')  # 招标标题
            if not b_title:
                sign = False
                return

            else:
                b_title[0] = b_title[0].strip()
                # print(b_title)
                for crux_i in crux_list:
                    # print(crux_i)
                    if crux_i in b_title[0]:
                        print('关键字:', crux_i)
                        break
                else:
                    # print(b_title)
                    continue

            b_url = tree.xpath(f'/html/body/div/div/div[2]/div[2]/ul/li[{r_i}]/a/@href')  # 网页链接地址

            if not b_url:
                b_url = ' '
                b_money, customer_name, customer_phone = ' ', ' ', ' '
                continue
            else:
                # 判断路由是否完整
                if "http" not in b_url[0]:
                    b_url[0] = main_url + b_url[0]

                # 判断是否是增量
                if increment:
                    if b_url[0] in set_url:
                        sign = False
                        break
                if b_url[0] in set_url:
                    continue
                else:
                    set_url.add(b_url[0])

                    print('当前行数的url：', b_url[0])
                    b_money, customer_name, customer_phone = content(b_url[0])
                    if b_money == 0:
                        log_write(str(['{}请求了一百次也没有成功！'.format(b_url[0])]))
                        continue
            b_release = tree.xpath(f'/html/body/div/div/div[2]/div[2]/ul/li[{r_i}]/span/text()')  # 发标日期
            db_data = {}
            db_data['collect_time'] = datetime.now()  # 采集日期
            db_data['b_title'] = b_title[0]  # 招标标题
            db_data['b_url'] = b_url[0]  # 网页链接地址
            db_data['b_release'] = b_release[0]  # 发标日期
            db_data['b_money'] = b_money  # 招标金额
            db_data['customer_name'] = customer_name  # 客户名称
            db_data['customer_phone'] = customer_phone  # 客户联系方式
            db_data['b_time'] = b_release[0]  # 获取招标文件时间
            db_data['collect_id'] = 5  # 关联id

            print('第{}条数据:'.format(n))
            n += 1
            print()
            print('db_data:', db_data)
        # return
            try:
                Bidding.objects.create(**db_data)
            except Exception as e:

                log_write(str([e, db_data]))
                print(e, '数据没写进去！！！')


def main2():
    global set_url
    a = Bidding.objects.filter(collect_id=5).all().values_list('b_url')
    url_list = [i[0] for i in a]

    set_url = set_url |   set(url_list)

    # requests.get(url=get_cookie_u, headers=headers,)

    crux_list = crux.split('、')
    r_quests(crux_list, increment=1)
        # break


