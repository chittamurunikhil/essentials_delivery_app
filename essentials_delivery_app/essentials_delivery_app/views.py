from django.http import HttpResponse


def index(request):
    return HttpResponse("You are at your step to all your essentials")