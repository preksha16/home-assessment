from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
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
        print(tickets["tickets"])
        return JsonResponse({"ok":"ok"})


