from rest_framework import status
from tinydb import TinyDB, Query
from rest_framework.views import APIView
from rest_framework.response import Response
from .validators import get_data_type


db = TinyDB('db.json')


class GetFormView(APIView):
    def post(self, request):
        db.clear_cache()
        for field, value in request.data.items():
            fragment = {}
            fragment[field] = get_data_type(value)
            queryset = db.search(Query().fragment(fragment))
            for schema in queryset:
                name = schema.pop('name')            
                for schema_field, schema_value in schema.items():
                    if (not schema_field in request.data) or (schema_value != get_data_type(request.data.get(schema_field))):
                        break
                else: 
                    return Response({'name': name}, status=status.HTTP_200_OK)

        output = {}
        for field, value in request.data.items():
            output[field] = get_data_type(value)
        return Response(output, status=status.HTTP_200_OK)