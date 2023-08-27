import time

from celery import Celery

"""
创建了一个 Celery 实例 app，名称为 task_work
指定消息中间件用 redis，URL 为 redis://127.0.0.1:6379/0；
指定存储用 redis，URL 为 redis://127.0.0.1:6379/1；
创建了一个 Celery 任务 send_email，当函数被 @app.task 装饰后，就成为可被 Celery 调度的任务；
"""

appcelery = Celery('task_work',
                   broker='redis://127.0.0.1:6379/0',
                   backend='redis://127.0.0.1:6379/1')


@appcelery.task()
def send_email(email):
    print('正在{0} 发送...'.format(email))
    time.sleep(3)
    print("发送完成...")