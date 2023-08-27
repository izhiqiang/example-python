import time

from queues.celerys.sendTask import celerylistapp

@celerylistapp.task()
def send_list_email(email):
    print('正在{0} 发送...'.format(email))
    time.sleep(3)
    print("发送完成...")