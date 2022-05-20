from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
import json
# Create your views here.

class ListTicket(APIView):

    def get(self, request, format=None): #To receive tickets with get method

        tickets = json.loads(open('ticket.json').read())
        return JsonResponse({"tickets":tickets["tickets"]})

    def post(self, request, format=None): #To receive tickets with post method
        # To use pagination first we need to load json data into databse table
        # Then we can create serializers for pagination.
        
        tickets = json.loads(open('ticket.json').read())
        return JsonResponse({"tickets":tickets["tickets"]})


class ListUniqueTags(APIView): # It will return list of unique tags


    def post(self, request, *args, **kwargs):
        tickets = json.loads(open('ticket.json').read())
        tags=[]
        for ticket in tickets["tickets"]:
            tags.extend(ticket["tags"])

        return JsonResponse({"tags":list(set(tags))})
