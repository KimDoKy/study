import os
from celery import Celery

# celery 작동시 기본 django 셋팅 값을 지정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

app = Celery('conf')

# CELERY 접두사 셋팅
app.config_from_object('django.conf:settings', namespace='CELERY')

# settings에 등록된 모든 app의 task를 불러온다.
app.autodiscover_tasks()

@app.task
def add(x, y):
    return x + y
