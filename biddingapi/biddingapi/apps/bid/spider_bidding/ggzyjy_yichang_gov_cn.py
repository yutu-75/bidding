# encoding=utf-8
import sys
import pathlib
sys.path.append(str(pathlib.Path.cwd().parent.parent))      # 解决命令找不到包路径
from ..spider_bidding.share_spider import *

# 抓取的网站信息
# 宜昌市公共资源交易中心
# http://ggzyjy.yichang.gov.cn/TPFront/


set_url = set()

from requests.packages import urllib3
urllib3.disable_warnings()



def content(bid_url):

    page_text1 = requests.get(url=bid_url)
    page_text1.encoding = 'utf-8'
    page_text1 = page_text1.text

    soup = BeautifulSoup(page_text1,'lxml')
    # print(page_text1)
    page_text = soup.select('#mainContent')
    page_text = page_text[0].text
    page_text = page_text.replace('\xa0',' ')
    # print(page_text)

    bid_money = re.findall('金额：(.*?) ', page_text)                # 招标金额
    if not bid_money:
        bid_money = re.findall('预算.*?：(.*?) ', page_text)  # 招标金额

        if bid_money:
            bid_money = bid_money[0]
        else:
            bid_money = re.findall('预算.*?：(.*?)\n', page_text)  # 招标金额

            if bid_money:
                bid_money = bid_money[0]
    else:
        bid_money=bid_money[0]

    bid_customer = re.findall('采购人信息.*?名.*?称：.*?([\u4e00-\u9fa5]+) ', page_text)            # 客户名称

    if bid_customer:
        bid_customer = bid_customer[0]
    else:
        bid_customer = re.findall('联.*?系.*?人.*?：.*?([\u4e00-\u9fa5]+) ', page_text)  # 客户名称
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
        customer_phone = re.findall('电.*?话：.*?(.*?) ', page_text)  # 客户联系方式
        if customer_phone:
            customer_phone = customer_phone[0]
        else:
            customer_phone = re.findall('电.*?话：.*?(.*?) \n', page_text)  # 客户联系方式
            if customer_phone:
                customer_phone = customer_phone[0]

    # bid_money = bid_money[:10]
    # customer_phone = customer_phone[:20].split(' ')
    # print(str(bid_money),'\n', str(bid_customer), '\n',str(customer_phone))
    return str(bid_money), str(bid_customer), str(customer_phone)


def r_quests(crux_list, increment=0):

    """
    mainUrl: http://ggzyjy.yichang.gov.cn/
    :param crux_list:
    :param q:
    :param increment:
    :return:
    """
    global set_url
    main_url = 'http://ggzyjy.yichang.gov.cn'
    # 采购公告

    # 货物
    cg_hw_url = 'http://ggzyjy.yichang.gov.cn/TPFront/jyxx/003002/003002001/003002001001/?pageing='

    # 服务
    cg_fw_url = 'http://ggzyjy.yichang.gov.cn/TPFront/jyxx/003002/003002001/003002001002/?pageing='

    # 工程
    cg_gc_url = 'http://ggzyjy.yichang.gov.cn/TPFront/jyxx/003002/003002001/003002001003/?pageing='


    # 更正公告
    gzgg_url = 'http://ggzyjy.yichang.gov.cn/TPFront/jyxx/003002/003002002/'

    # 货物
    gz_hw_url = 'http://ggzyjy.yichang.gov.cn/TPFront/jyxx/003002/003002002/003002002001/?pageing='

    # 服务
    gz_fw_url = 'http://ggzyjy.yichang.gov.cn/TPFront/jyxx/003002/003002002/003002002002/?pageing='

    # 工程
    gz_gc_url = 'http://ggzyjy.yichang.gov.cn/TPFront/jyxx/003002/003002002/003002002003/?pageing='


    # 中标/成交公告
    zbgg_url = 'http://ggzyjy.yichang.gov.cn/TPFront/jyxx/003002/003002003/'

    # 货物
    zb_hw_url = 'http://ggzyjy.yichang.gov.cn/TPFront/jyxx/003002/003002003/003002003001/?pageing='

    # 服务
    zb_fw_url = 'http://ggzyjy.yichang.gov.cn/TPFront/jyxx/003002/003002003/003002003002/?pageing='

    # 工程
    zb_gc_url = 'http://ggzyjy.yichang.gov.cn/TPFront/jyxx/003002/003002003/003002003003/?pageing='

    def f_url(f_url_i):
        sign = True
        n = 1
        pageNo1 = 0
        while sign:
            pageNo1 += 1
            print('页数pageNo1:',pageNo1)
            c_url = f_url_i+str(pageNo1)
            print('c_url:',c_url)

            for try_i in range(10):
                try:
                    page_text = requests.get(url=c_url, headers=headers)
                    break
                except Exception as e:

                    print('value_id_error：', e)

            else:
                log_write(str([c_url, '--请求了十次也没有反回数据！',]))
                continue

            page_text.encoding = 'utf-8'
            page_text = page_text.text
            # print(page_text)
            tree = etree.HTML(page_text)
            # tree = etree.HTML(page_text,'lxml')

            for r_i in range(1, 13):
                # print(f'第{pageNo1}页 第{r_i}行:')
                b_title = tree.xpath('//ul//li[{}]/div/a//text()'.format(r_i))  # 招标标题
                if not b_title:
                    sign = False
                    return
                else:
                    for crux_i in crux_list:
                        if crux_i in b_title[0]:
                            print('关键字:',crux_i)
                            break
                    else:
                        continue

                b_url = tree.xpath('//ul//li[{}]/div/a/@href'.format(r_i))  # 网页链接地址

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
                b_release = tree.xpath('//ul//li[{}]/span/text()'.format(r_i))  # 发标日期
                db_data = {}
                db_data['collect_time'] = datetime.now()        # 采集日期
                db_data['b_title'] = b_title[0]                 # 招标标题
                db_data['b_url'] = b_url[0]                     # 网页链接地址
                db_data['b_release'] = b_release[0]             # 发标日期
                db_data['b_money'] = b_money                    # 招标金额
                db_data['customer_name'] = customer_name        # 客户名称
                db_data['customer_phone'] = customer_phone      # 客户联系方式
                db_data['b_time'] = b_release[0]                # 获取招标文件时间
                db_data['collect_id'] = 3                       # 关联id

                print('第{}条数据:'.format(n))
                n += 1
                print()
                print('db_data:', db_data)

                try:
                    Bidding.objects.create(**db_data)
                except Exception as e:

                    log_write(str([e, db_data]))
                    print(e, '数据没写进去！！！')


    u_list = [
        cg_hw_url, cg_fw_url, cg_gc_url,
        gz_hw_url, gz_fw_url, gz_gc_url,
        zb_hw_url, zb_fw_url, zb_gc_url,
    ]
    for i in u_list:
        f_url(i)
        # break

# content('http://ggzyjy.yichang.gov.cn/TPFront/InfoDetail/?InfoID=1ffc00c4-20ab-4dce-9c96-fa01b18e5d52&CategoryNum=003002003002')

def main12():
    global set_url
    a = Bidding.objects.filter(collect_id=3).all().values_list('b_url')
    url_list = [i[0] for i in a]

    set_url = set_url | set(url_list)

    # requests.get(url=get_cookie_u, headers=headers,)
    crux_list = crux.split('、')


    r_quests(crux_list,increment=1)
        # break


# main12()

