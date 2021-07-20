from django.contrib import admin
from .models import Bboard, Rubric


class BboardAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'updated_at', 'rubric')
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(Bboard, BboardAdmin)
admin.site.register(Rubric)
