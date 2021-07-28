from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    """Улучшенное отображение полей в админке, с поиском и активными ссылками"""
    list_display = ('username', 'first_name', 'last_name',)
    list_display_links = ('username',)
    search_fields = ('username',)
    prepopulated_fields = {'slug': ('username',)}


admin.site.register(CustomUser, CustomUserAdmin)
