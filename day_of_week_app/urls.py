from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_day_of_week)
]
