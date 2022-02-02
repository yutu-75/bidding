from celery import Celery
from importlib import import_module

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biddingapi.settings')
import django
django.setup()

# print(import_module('config'))

app = Celery('my_celery.main', broker='redis://:123456@127.0.0.1/2')

app.conf.ONCE = {
  'backend': 'celery_once.backends.Redis',
  'settings': {
    'url': 'redis://:123456@127.0.0.1:6379/1',
    'default_timeout': 60 * 60 * 3
  }
}


# app.conf.broker_transport_options = {'visibility_timeout': 86400}
app.config_from_object('my_celery.config')  #

app.autodiscover_tasks(['my_celery.celery_task',])



# python main.py
# 爬虫代码启动命令
# celery -A my_celery.main beat -l info                               
# celery -A my_celery.main worker -l info --pool=solo
#
#
# --loglevel=info --pool=solo
