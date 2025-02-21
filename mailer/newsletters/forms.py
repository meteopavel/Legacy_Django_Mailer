# -*- coding: utf-8 -*-
from django import forms

from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    scheduled_time = forms.DateTimeField(
        label='Время отправки (если не заполнить - отправим сразу)',
        required=False,
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control'},
            format='%Y-%m-%dT%H:%M')
    )

    class Meta:
        model = Newsletter
        fields = ('subject', 'subscribers', 'scheduled_time')
        labels = {
            'subject': 'Тема (обязательно)',
            'subscribers': 'Получатели (хотя бы один)',
            'scheduled_time': 'Время отправки'
        }
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'col-12'}),
            'subscribers': forms.SelectMultiple(attrs={'class': 'col-12'}),
        }
