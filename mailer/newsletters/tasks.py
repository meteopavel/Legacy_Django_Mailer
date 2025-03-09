# -*- coding: utf-8 -*-
from __future__ import absolute_import

import logging
import time

from datetime import datetime
from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Newsletter


logger = logging.getLogger(__name__)


@shared_task
def send_newsletter(newsletter_id):
    newsletter = Newsletter.objects.get(id=newsletter_id)
    subscribers = newsletter.subscribers.all()

    for subscriber in subscribers:
        html_content = render_to_string(
            'my_email.html',
            context={
                'first_name': subscriber.first_name,
                'last_name': subscriber.last_name,
                'birthday': subscriber.birthday.strftime('%d %B %Y') + ' года',
                'current_year': datetime.now().year,
                'newsletter': newsletter,
                'subscriber': subscriber,
                'timestamp': int(time.mktime(datetime.now().timetuple())),
                'base_url': settings.BASE_URL
            },
        )

        msg = EmailMultiAlternatives(
            newsletter.subject,
            '',
            'mail@meteopavel.space',
            [subscriber.email],
            headers={},
        )

        msg.attach_alternative(html_content, 'text/html')

        try:
            msg.send()
            logger.info(
                u'Письмо успешно отправлено '
                u'подписчику: {}'.format(subscriber.email)
            )
        except Exception as e:
            logger.error(
                u'Ошибка при отправке письма '
                u'подписчику {}: {}'.format(subscriber.email, str(e))
            )
