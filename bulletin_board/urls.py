from django.urls import path
from .views import bboard_index, contacts, by_rubric, BbCreateView, see_user_info

app_name = 'bboard'

urlpatterns = [
    path('', bboard_index, name='index'),
    path('hi/', see_user_info, name='hi'),
    path('contacts/', contacts, name='contacts'),
    path('add/', BbCreateView.as_view(), name='add_ad'),
    path('<slug:rubric_slug>/', by_rubric, name='by_rubric'),



]
