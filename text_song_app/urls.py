from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_text_song),
    path('<str:language>/', views.text_song_language),
]