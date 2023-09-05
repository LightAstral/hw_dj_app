from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('toyota/', views.toyota),
    path('honda/', views.honda),
    path('renault/', views.renault),
]
