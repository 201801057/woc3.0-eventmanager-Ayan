from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .models import EventRegistration, ParticipantRegistration
from twilio.rest import Client
import datetime
import string
import random
import uuid
# Create your views here.


# def signUp(request):
#     if request == 'POST'

def randomPassword():
    characters = string.ascii_letters + string.punctuation + string.digits
    password = ""
    password_length = random.randint(8, 16)
    for x in range(password_length):
        char = random.choice(characters)
        password = password + char

    return password


def indexHandler(request):
    return render(request, 'index.html')


def eventRegistration(request):
    if request.method == "POST":
        eventName = request.POST.get('eventName')
        desc = request.POST.get('desc')
        posterLink = request.POST.get('posterLink')
        eventFrom = request.POST.get('eventFrom')
        eventTo = request.POST.get('eventTo')
        eventDeadline = request.POST.get('eventDeadline')
        hostID = request.POST.get('hostID')
        details = EventRegistration(eventName=eventName, desc=desc, posterLink=posterLink,
                                    eventFrom=eventFrom, eventTo=eventTo, eventDeadline=eventDeadline, hostID=hostID)
        details.save()

        subject = f'Successfull Registration for the event {details.eventName}'
        message = f'Thanks for registering for the {details.eventName} your ID assigned is {details.eventId} and the password for accessing the Event Dashboard is {details.password}'
        email_from = settings.EMAIL_HOST_USER
        receipient_list = [hostID]
        send_mail(subject, message, email_from, receipient_list)
        return redirect('/')

    return render(request, 'eventRegistration.html')


def participantRegistration(request):
    context = EventRegistration.objects.all()
    participants = ParticipantRegistration.objects.all()

    names = []

    for i in context:
        if datetime.date.today() <= i.eventDeadline.date():
            names.append(i.eventName)

    names = {'names': names}

    if request.method == "POST":

        name = request.POST.get('name')
        contact = request.POST.get('contact')
        emailID = request.POST.get('emailID')
        eventList = request.POST.get('eventList')
        registrationType = request.POST.get('registrationType')
        noOfPeople = request.POST.get('noOfPeople')

        again = 0

        for obj in participants:
            if name == obj.name and contact == obj.contact and emailID == obj.emailID and eventList == obj.eventList:
                again = 1
                break

        if again == 0:
            details = ParticipantRegistration(name=name, contact=contact, emailID=emailID,
                                              eventList=eventList, registrationType=registrationType, noOfPeople=noOfPeople)
            details.save()

            imp = {}
            for i in context:
                if i.eventName == eventList:
                    imp = i
                    break

            message_to_broadcast = (
                f"Thanks {name}, for Registering for the event {imp.eventName}.\nThe unique ID alloted to you is {details.pId}.\nYour event starts from {imp.eventFrom}  to {imp.eventTo}.\nHere is the description of the event: {imp.desc} ")

            client = Client(settings.TWILIO_ACCOUNT_SID,
                            settings.TWILIO_AUTH_TOKEN)
            contact = "+91" + contact
            client.messages.create(to=contact,
                                   from_=settings.TWILIO_NUMBER,
                                   body=message_to_broadcast)

            return HttpResponse('Thanks For the Registration, Have a Nice Day!!!!')
        else:
            return HttpResponse('You are already registered for the event')

    return render(request, 'participantRegistration.html', names)


def viewEvents(request):
    # contexts = EventRegistration.objects.all()

    if request.method == "POST":
        name = request.POST.get('eventName')
        secretKey = request.POST.get('password')

        # secretKey = uuid.UUID(secretKey).hex
        # secretKey = secretKey[:len(secretKey)]
        secretKey = secretKey[:36]

        contexts = EventRegistration.objects.filter(
            eventName=name, password=secretKey)

        if len(contexts) == 0:
            return HttpResponse(f'Incorrect Password ')

        members = []

        participants = ParticipantRegistration.objects.all()
        for p in participants:
            if p.eventList == name:
                members.append(p)

        return render(request, 'events.html', {'members': members})

        # return HttpResponse(f'Incorrect Password {name} and {password}')

    return render(request, 'eventDashboard.html')


def dashboard(request):
    return render(request, 'eventDashboard.html')
