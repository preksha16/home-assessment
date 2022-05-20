from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('list_tickets', ListTicket.as_view()), #To receive tickets with get and post method
    path('list_unique_tags', ListUniqueTags.as_view()) # It will return list of unique tags
]

