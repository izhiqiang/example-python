from celery import Celery

# 创建 Celery 实例
celerylistapp = Celery('demo')
# 通过 Celery 实例加载配置模块
celerylistapp.config_from_object('queues.celerys.celeryconf')
