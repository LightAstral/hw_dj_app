from django.shortcuts import render
import datetime


# Create your views here.

def show_time_of_day(request):
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if 5 <= hour < 12:
        greeting = "Доброе утро!"
    elif 12 <= hour < 18:
        greeting = "Добрый день!"
    else:
        greeting = "Добрый вечер!"

    context = {
        "current_time": current_time,
        "greeting": greeting
    }

    return render(request, "time_of_day_app/time_of_day.html", context)