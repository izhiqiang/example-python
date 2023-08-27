## 需要扩展库
~~~
pip install celery
pip install redis
pip install eventlet
~~~

## cmd命令启动
~~~
前台启动命令
celery worker -A 项目目录 -l info
后台启动命令
celery multi start w1 -A 项目目录 -l info 
后台重启命令
elery multi restart w1 -A 项目目录 -l info
后台停止命令
celery multi stop w1 -A 项目目录 -l info
~~~



## 单个DEMO任务运行
~~~
使用协程的方式启动。当然首先需要安装eventlet。
celery -A queues.celerys.celery_task_email  worker --loglevel=info -P eventlet 
~~~


## 多个DEMO任务运行
~~~
celery -A queues.celerys.sendTask  worker --loglevel=info -P eventlet 
~~~
