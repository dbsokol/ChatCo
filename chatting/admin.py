from django.contrib import admin

from chatting import models


@admin.register(models.Sender)
class SenderAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'timestamp', 'content']