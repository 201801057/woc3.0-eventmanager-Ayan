from django import forms
from models import *


class EventRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = EventRegistration
        fields = ('eventId', 'eventName', 'password', 'desc', 'posterLink', 'eventFrom',
                  'eventTo', 'eventDeadline', 'hostID')
