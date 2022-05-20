from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
import json
from django.core.paginator import Paginator

# Create your views here.

class ListTicket(APIView):
    def get(self, request, format=None): #To receive tickets with get method

        tickets = json.loads(open('ticket.json').read())
        data = tickets['tickets']
        #print("data",data)
        try:
            page_number=request.META.get('HTTP_PAGE')
        except:
            
            page_number=1
        
        p = Paginator(data,2)
        try:
            page = p.page(page_number)
            page_number = page_number
        except Exception as e:
            page = p.page(1)
            page_number = 1
        total_pages = p.num_pages
        print("total_pages",total_pages)


        return JsonResponse({'current_page':page_number,'total_pages':total_pages,"tickets":list(page)})


    def post(self, request, format=None): #To receive tickets with post method
        tickets = json.loads(open('ticket.json').read())
        data = tickets['tickets']
        #print("data",data)
        try:
            page_number=request.META.get('HTTP_PAGE')
        except:
            
            page_number=1
        
        p = Paginator(data,2)
        try:
            page = p.page(page_number)
            page_number = page_number
        except Exception as e:
            page = p.page(1)
            page_number = 1
        total_pages = p.num_pages
        print("total_pages",total_pages)


        return JsonResponse({'current_page':page_number,'total_pages':total_pages,"tickets":list(page)})



class ListUniqueTags(APIView): # It will return list of unique tags


    def post(self, request, *args, **kwargs):
        tickets = json.loads(open('ticket.json').read())
        tags=[]
        for ticket in tickets["tickets"]:
            tags.extend(ticket["tags"])

        return JsonResponse({"tags":list(set(tags))})
