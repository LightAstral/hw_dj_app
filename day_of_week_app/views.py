import base64
from django.shortcuts import render
import os
from django.conf import settings
import datetime


def show_day_of_week(request):
    current_day = datetime.datetime.now().strftime('%A')

    image_filename = f'day_of_week_app/img/background_{current_day.lower()}.jpg'
    image_path = os.path.join(settings.BASE_DIR, image_filename)

    with open(image_path, 'rb') as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')

    context = {
        'current_day': current_day,
        'base64_image': base64_image,
    }

    return render(request, 'day_of_week_app/days_of_week.html', context)
