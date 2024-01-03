from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


monthly_challenges = {"january": "eat no meat for the entire month",
                      "february": "Walk for at least 20 min every day",
                      "march": "Learn Django for 20 min every day",
                      "april": "Gym workout for 2 hours daily",
                      "may": "Travel and tour",
                      "june": "Focus on business",
                      "july": "Learn Django for 20 min every day",
                      "august": "Travel and tour",
                      "september": "Walk for at least 20 min every day",
                      "october": "eat no meat for the entire month",
                      "November": "Learn Django for 20 min every day",
                      "December": "Walk for at least 20 min every day",
                      }
# Create your views here.


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    try:
        challeng_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("Invalid month")

    return HttpResponse(challeng_text)
