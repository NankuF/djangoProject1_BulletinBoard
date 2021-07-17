from django.urls import path
from .views import bboard_index, contacts

app_name = 'bboard'

urlpatterns = [
    path('', bboard_index, name='index'),
    path('contacts/', contacts, name='contacts'),
]
