from my_celery.main import app
from pathlib import Path
from celery_once import QueueOnce





def main_send():
    print('这里被执行了！')
    pass



@app.task(base=QueueOnce, once={'graceful': True})
def celery_run():
    print('______________celery_run__________________')
    main_send()
    return 'ok'