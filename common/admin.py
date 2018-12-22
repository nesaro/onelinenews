from django.contrib import admin
from .models import HeadLine

class HeadLineAdmin(admin.ModelAdmin):
    list_display = ('url','headline')


admin.site.register(HeadLine, HeadLineAdmin)
