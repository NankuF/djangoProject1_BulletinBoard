from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bulletin_board.urls', namespace='bboard')),
    path('users/', include('users.urls', namespace='users')),
]
