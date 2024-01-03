from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    forward_month = months[month - 1]

    redirect_path = reverse(
        "month-challenge", args=[forward_month])  # /challenge/january

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challeng_text = monthly_challenges[month.lower()]
    except:
        return HttpResponseNotFound("This is not supported")

    return HttpResponse(challeng_text)
