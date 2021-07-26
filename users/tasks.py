from celery import shared_task
import time

from bulletin_board.models import Bboard
from djangoProject1.celery import celery_app


# celery_app.task
# def send_mail_task(user_mail):
#     subject = 'Ключ активации',
#     message = f"""
#     {self.username}, для активации аккаунта перейдите по ссылке
#     http://127.0.0.1:8000/{settings.APP_NAME}/activate/{self.activation_key}
#     """,
#     from_email = settings.EMAIL_HOST_USER)


# @celery_app.task
# def sum_value(x, y):
#     return x + y
#
#
# # print(sum_value.delay(2, 4))
# print(sum_value(2, 4))
