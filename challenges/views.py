from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    challeng_text = None
    if month == "january":
        challeng_text = "eat no meat for the entire month"

    elif month == "february":
        challeng_text = "Walk for at least 20 min every day"

    elif month == "march":
        challeng_text = "Learn Django for 20 min every day"

    else:
        return HttpResponseNotFound("This month is invalid!")

    return HttpResponse(challeng_text)
