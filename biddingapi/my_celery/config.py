# from __future__ import absolute_import # 拒绝隐式引入，因为celery.py的名字和celery的包名冲突，需要使用这条语句让程序正确地运行
from celery.schedules import crontab



broker_url = "redis://:500237@47.108.162.205:6379/2"   # 使用redis存储任务队列
result_backend = "redis://:500237@47.108.162.205:6379/6"  # 使用redis存储结果

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = "Asia/Shanghai"  # 时区设置
worker_hijack_root_logger = True  # celery默认开启自己的日志，可关闭自定义日志，不关闭自定义日志输出为空
CELERY_TASK_ALWAYS_EAGER = True
# CELERY_STORE_ERRORS_EVEN_IF_IGNORED = True
# CELERY_TASK_ALWAYS_EAGER = True
result_expires = 60 * 60 * 24  # 存储结果过期时间（默认1天）
# BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 43200}
# worker_prefetch_multiplier = 1
worker_max_tasks_per_child = 3 #  每个worker最多执行3个任务就会被销毁，可防止内存泄露
# 导入任务所在文件
imports = [
    "my_celery.celery_task.b1_task",  # 导入py文件
    # "celery_task.epp_scripts.test2",
]


# 需要执行任务的配置
beat_schedule = {
    "test1": {
        "task": "my_celery.celery_task.b1_task.celery_run",  #执行的函数
        # "schedule": crontab(minute="*/10"),   # every minute 每分钟执行
        "schedule": crontab(minute=26, hour="9"),  # every minute 每天凌晨十二点执行
        "args": ()  # # 任务函数参数
    },
# celery -A my_celery.main worker -l info -P eventlet
#     "test2": {
#         "task": "my_celery.celery_task.b2_task.celery_run",
#         "schedule": crontab(minute='21', hour="15"),   # every minute 每小时执行
#         "args": ()
#     },

}

# "schedule": crontab（）与crontab的语法基本一致
# "schedule": crontab(minute="*/10",  # 每十分钟执行
# "schedule": crontab(minute="*/1"),   # 每分钟执行
# "schedule": crontab(minute=0, hour="*/1"),    # 每小时执行
