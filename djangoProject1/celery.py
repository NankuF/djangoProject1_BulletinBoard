import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject1.settings')
app = Celery('djangoProject1')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_email_when_add_bboard': {
        'task': 'bulletin_board.tasks.send_email_task',
        'schedule': 150.0
    }
}
