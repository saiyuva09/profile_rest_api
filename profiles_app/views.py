from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HellowApiView(APIView):

    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives the most cotrol over application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'hello','an_apiview': an_apiview})
