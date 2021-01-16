from django.contrib import admin
from myApp.models import EventRegistration, ParticipantRegistration
# Register your models here.
admin.site.register(EventRegistration)
admin.site.register(ParticipantRegistration)
