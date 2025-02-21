from django.contrib import admin
from .models import Subscriber, Newsletter, EmailOpen


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'birthday')
    search_fields = ('email', 'first_name', 'last_name')


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('subject', 'scheduled_time')


@admin.register(EmailOpen)
class EmailOpenAdmin(admin.ModelAdmin):
    list_display = ('opened_at', 'newsletter_id', 'subscriber_id')
