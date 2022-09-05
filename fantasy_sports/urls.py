from django.urls import path
from . import views

urlpatterns = [
    path('api/EPLPlayers/', views.ListPlayers.as_view()),
]