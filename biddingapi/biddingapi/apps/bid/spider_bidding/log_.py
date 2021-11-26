import re
import time
from datetime import datetime,timedelta
from pathlib import Path
import os
from bid.spider_bidding.config import log_day, log_file_size


def log_write(content: str) -> None:
    """
      content: # 日志文本
    """

    dir_path = Path(Path.cwd()) / 'error_log'
    if not Path.is_dir(dir_path):  # 判断是否有这个文件目录 没有则创建
        os.mkdir(dir_path)
    f_list = list(dir_path.iterdir())  # 文件路径列表
    before_time = datetime.now() - timedelta(days=log_day)  # 半年前的时间

    time_stamp = time.mktime(time.strptime(str(before_time), '%Y-%m-%d %H:%M:%S.%f'))  # 半年前的时间戳
    # print(time_stamp)
    if not f_list:
        with open('./error_log/log_1.txt', 'a+', encoding='utf_8') as f:
            print(content)
            f.write(str(datetime.now()) + ": " + str(content) + '\n')
        return
    re_number_max = 0
    for i in f_list:

        re_number = re.findall(r'_(\d+).txt', str(i))
        if int(re_number[0]) > int(re_number_max):
            re_number_max = re_number[0]
        i_s = i.stat()
        if i_s.st_mtime < time_stamp:
            os.remove(i)
            print('有六个月之前的日志！')

        if i_s.st_size > log_file_size:

            if i == f_list[-1]:
                with open(str(i).replace(re_number[0], str(int(re_number_max) + 1)), 'a+', encoding='utf-8') as b_f:
                    b_f.write(str(datetime.now()) + ": " + content + '\n')
            continue
        else:
            with open(i, 'a+', encoding='utf-8') as b_f:
                b_f.write(str(datetime.now()) + ": " + content + '\n')