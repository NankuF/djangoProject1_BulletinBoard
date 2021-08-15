from celery import shared_task
import time

from django.conf import settings

from bulletin_board.models import Bboard
from django.core.mail import send_mail


@shared_task
def send_email_task():
    start = time.time()
    time.sleep(10)
    send_mail(
        'Оповещение',
        'Объявление создано',
        settings.EMAIL_HOST_USER,
        ['fireloki@mail.ru', ]
    )
    stop = time.time()
    print('EMAIL SEND', stop - start)
    return None
