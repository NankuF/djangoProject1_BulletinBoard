from django.contrib import admin
from .models import Bboard, Rubric


class BboardAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'updated_at', 'rubric','slug')
    list_display_links = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class RubricAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Bboard, BboardAdmin)
admin.site.register(Rubric,RubricAdmin)
