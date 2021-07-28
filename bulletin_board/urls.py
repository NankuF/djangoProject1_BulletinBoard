from django.urls import path
from .views import bboard_index, contacts, by_rubric, BbCreateView

app_name = 'bboard'

urlpatterns = [
    path('', bboard_index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('<slug:rubric_slug>/', by_rubric, name='by_rubric'),
    path('add/', BbCreateView.as_view(), name='add_ad'),

]
