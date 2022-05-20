from django.contrib import admin
from django.urls import path
from .views import ListTicket
urlpatterns = [
    path('list', ListTicket.as_view()),
]

