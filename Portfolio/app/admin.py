from email import message
from django.contrib import admin
from .models import Info

class InfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date', 'subject', 'message', ]

admin.site.register(Info, InfoAdmin)
# Register your models here.
