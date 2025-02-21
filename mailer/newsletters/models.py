# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone

from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    birthday = models.DateField(null=True, blank=True,
                                verbose_name='Дата рождения')

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    subject = models.CharField(max_length=255, verbose_name='Тема')
    subscribers = models.ManyToManyField(Subscriber,
                                         related_name='newsletters',
                                         verbose_name='Подписчик')
    scheduled_time = models.DateTimeField(null=True, blank=True,
                                          verbose_name='Время отправки')

    def open_count(self):
        return EmailOpen.objects.filter(newsletter=self).count()

    def __str__(self):
        return self.subject


class EmailOpen(models.Model):
    newsletter = models.ForeignKey(Newsletter)
    subscriber = models.ForeignKey(Subscriber)
    opened_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{} opened {} at {}'.format(
            self.subscriber.email, self.newsletter.subject, self.opened_at)
