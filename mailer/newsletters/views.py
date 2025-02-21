# -*- coding: utf-8 -*-
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .forms import NewsletterForm
from .models import Newsletter, Subscriber, EmailOpen
from .tasks import send_newsletter


def create_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            newsletter = form.save()
            scheduled_time = newsletter.scheduled_time
            current_time = timezone.localtime(timezone.now())
            if scheduled_time and scheduled_time > current_time:
                send_newsletter.apply_async(
                    (newsletter.id,), eta=scheduled_time)
                return JsonResponse(
                    {'status':
                     'Рассылка запланирована на {}'.format(scheduled_time)}
                )
            else:
                send_newsletter.delay(newsletter.id)
                return JsonResponse({'status': 'Рассылка отправлена сразу'})
        else:
            return JsonResponse({'status': 'errors', 'errors': form.errors})
    else:
        form = NewsletterForm()
    return render(request, 'create_newsletter.html', {'form': form})


def track_open(request, newsletter_id, subscriber_id):
    try:
        newsletter = Newsletter.objects.get(id=newsletter_id)
        subscriber = Subscriber.objects.get(id=subscriber_id)
        EmailOpen.objects.get_or_create(newsletter=newsletter,
                                        subscriber=subscriber)
        return HttpResponse(status=204)
    except (Newsletter.DoesNotExist, Subscriber.DoesNotExist):
        return HttpResponse(status=404)
