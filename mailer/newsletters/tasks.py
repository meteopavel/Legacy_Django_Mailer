# -*- coding: utf-8 -*-
from __future__ import absolute_import

import logging
import requests
import time

from datetime import datetime
from celery import shared_task
from django.conf import settings
from django.template.loader import render_to_string

from .models import Newsletter


logger = logging.getLogger(__name__)


API_URL = settings.SMTP_BZ_API_URL 
API_KEY = settings.SMTP_BZ_API_KEY


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

        payload = {
            'name': 'Pavel Naidenov',
            'from': 'mail@meteopavel.space',
            'subject': newsletter.subject,
            'to': subscriber.email,
            'html': html_content,
        }

        headers = {
            'Authorization': '{}'.format(API_KEY),
            'Content-Type': 'application/json',
        }

        try:
            response = requests.post(API_URL, json=payload, headers=headers)

            if response.status_code == 200:
                logger.info(
                    u'Письмо успешно отправлено '
                    u'подписчику: {}'.format(subscriber.email)
                )
            else:
                logger.error(
                    u'Ошибка при отправке письма '
                    u'подписчику {}: Статус {}, Ответ: {}'.format(
                        subscriber.email, response.status_code, response.text
                    )
                )
        except Exception as e:
            logger.error(
                u'Ошибка при отправке письма '
                u'подписчику {}: {}'.format(subscriber.email, str(e))
            )
