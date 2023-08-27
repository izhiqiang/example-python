from queues.celerys.celery_task_email import send_email
from celery.result import AsyncResult
from queues.celerys.celery_task_list import send_list_email



def taskIdFuncStatus(task_id,task_name):
    res = AsyncResult(id=task_id, task_name=task_name)
    if res.successful() or res.status == "SUCCESS":
        print("任务执行成功")
    elif res.failed() or res.status == "FAILURE":
        print("任务失败")
    elif res.status == 'STARTED':
        print("任务已开始")
    elif res.status == 'PENDING':
        print("任务等待中")
    elif res.status == 'REVOKED':
        print("任务取消")
    elif res.status == 'RETRY':
        print("任务将被重试")

def celery_run(type =None):
    if type is  None:
        task_id = send_email.delay("admin222@domain.com")
        print("单任务运行task_id:" + str(task_id))
    else:
        task_ids = send_list_email.delay("admin222@domain.com")
        print("多任务运行task_id:" + str(task_ids))



if __name__ == '__main__':
    celery_run(None)
    # taskIdFuncStatus("dfcded47-6a49-448f-9306-40f933b2dbae", send_email)