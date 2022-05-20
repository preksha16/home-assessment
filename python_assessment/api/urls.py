from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('list_tickets', ListTicket.as_view()),
    path('list_unique_tags', ListUniqueTags.as_view())
]

