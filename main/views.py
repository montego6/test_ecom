from rest_framework import status
from tinydb import TinyDB, Query
from rest_framework.views import APIView
from rest_framework.response import Response
from .validators import get_data_type


db = TinyDB('db.json', cache_size=0)


class GetFormView(APIView):
    def post(self, request):
        db.clear_cache()
        for field, value in request.query_params.items():
            fragment = {}
            fragment[field] = get_data_type(value)
            queryset = db.search(Query().fragment(fragment))
            for schema in queryset:
                name = schema.pop('name')            
                for schema_field, schema_value in schema.items():
                    if (not schema_field in request.query_params) or (schema_value != get_data_type(request.query_params.get(schema_field))):
                        break
                else: 
                    return Response({'name': name}, status=status.HTTP_200_OK)

        # for schema in db:
        #     name = schema.pop('name')
        #     for field, type in schema.items():
        #         if not field in request.query_params:
        #             print(field, ' is not in params')
        #             break
        #         if not type == get_data_type(request.query_params[field]):
        #             break
        #     else:
        #         return Response({'name': name}, status=status.HTTP_200_OK)
        output = {}
        for field, value in request.query_params.items():
            output[field] = get_data_type(value)
        return Response(output, status=status.HTTP_200_OK)