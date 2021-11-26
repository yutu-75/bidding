from gevent import monkey
import gevent
import requests

monkey.patch_socket()  # 实现高并发，这个猴子补丁是必须的

from requests.packages import urllib3

urllib3.disable_warnings()
from gevent import monkey
import gevent
import requests

monkey.patch_socket()  # 实现高并发，这个猴子补丁是必须的

s = """建设地点；恩施市第三高级中学.
预算价： 159776.48 元.
计划工期：45天."""

import re
bid_money = re.findall('预算.*?(\d+\.?\d+\(?（?万?元?）?\)?)', s)  # 招标金额
print(bid_money)