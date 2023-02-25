from django.contrib import admin
from contact.models import Message

# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'message', 'updated_date', 'created_date']
    search_fields = ['name', 'email', 'subject', 'message', ]

    class Meta:
        model = Message
