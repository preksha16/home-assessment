from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
import json
# Create your views here.

class ListTicket(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        tickets = json.loads(open('ticket.json').read())
        return JsonResponse({"tickets":tickets["tickets"]})


class ListUniqueTags(APIView):


    def post(self, request, *args, **kwargs):
        tickets = json.loads(open('ticket.json').read())
        tags=[]
        for ticket in tickets["tickets"]:
            tags.extend(ticket["tags"])

        return JsonResponse({"tags":list(set(tags))})
