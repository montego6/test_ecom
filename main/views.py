from django.shortcuts import render
from rest_framework import status
from tinydb import TinyDB, Query
from rest_framework.views import APIView
from rest_framework.response import Response
from .validators import get_data_type
# Create your views here.

db = TinyDB('db.json')


class GetFormView(APIView):
    def post(self, request):
        for schema in db:
            for field, type in schema:
                if not field in request.query_params:
                    break
                if not type == get_data_type(request.query_params[field]):
                    break
            else:
                return Response({'name': schema['name']}, status=status.HTTP_200_OK)
        output = {}
        for field, value in request.query_params:
            output[field] = get_data_type(value)
        return Response(output, status=status.HTTP_200_OK)