from my_celery.main import app
from pathlib import Path
from celery_once import QueueOnce

from biddingapi.apps.bid.spider_bidding.xianning_gov_cn import main1
from biddingapi.apps.bid.spider_bidding.xgxz_xiaogan_gov_cn import main2
from biddingapi.apps.bid.spider_bidding.www_suizhou_gov_cn import main3
from biddingapi.apps.bid.spider_bidding.www_snj_gov_cn import main4
from biddingapi.apps.bid.spider_bidding.www_jzggzy_comwww_jzggzy_com import main5
from biddingapi.apps.bid.spider_bidding.www_hsztbzx_com import main6
from biddingapi.apps.bid.spider_bidding.www_hgggzy_com import main7
from biddingapi.apps.bid.spider_bidding.www_hbggzyfwpt_cn import main8
from biddingapi.apps.bid.spider_bidding.www_ezhou_gov_cn import main9
from biddingapi.apps.bid.spider_bidding.www_es_gov_cn import main10
from biddingapi.apps.bid.spider_bidding.www_ccgp_hubei_gov_cn import main11
from biddingapi.apps.bid.spider_bidding.ggzyjy_yichang_gov_cn import main12
from biddingapi.apps.bid.spider_bidding.ggzyjy_shiyan_gov_cn import main13
from biddingapi.apps.bid.spider_bidding.b_121_61_253_44 import main14
from biddingapi.apps.bid.spider_bidding.b_27_17_40_162_8000 import main15


def test33():
    print('_________________________start_____________________________')
    try:
        print('_________________________main1_____________________________')
        main1()
        print('_________________________main2_____________________________')
        main2()
        print('_________________________main3_____________________________')
        main3()
        print('_________________________main4_____________________________')
        main4()
        print('_________________________main5_____________________________')
        main5()
        print('_________________________main6_____________________________')
        main6()
        print('_________________________main7_____________________________')
        main7()
        print('_________________________main8_____________________________')
        main8()
        print('_________________________main9_____________________________')
        main9()
        print('_________________________main10_____________________________')
        main10()
        print('_________________________main11_____________________________')
        main11()
        print('_________________________main12_____________________________')
        main12()
        print('_________________________main13_____________________________')
        main13()
        print('_________________________main14_____________________________')
        main14()
        print('_________________________main15_____________________________')
        main15()
    except Exception as e:
        with open('celery_error_log.txt','w',encoding='utf-8') as c_f:
            c_f.write(str(e)+'\n')
        print(str(e)+'\n')


def test44():
    with open('qqq.txt','a+',encoding='utf-8') as f1:
        f1.write('qwq\n')
    print("test44--------------")
    # print("------" * 50)

@app.task(base=QueueOnce, once={'graceful': True})
def celery_run():
    print('______________celery_run__________________')
    test33()
    return 'ok'
    # test44()
# if __name__ == '__main__':

    # celery_run()