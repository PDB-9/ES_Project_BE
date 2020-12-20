from django.shortcuts import render
import json
from collections import Counter
from rest_framework import viewsets
from .serializers import LogSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.conf import settings as conf_settings
# Create your views here.
class LogViewSet(viewsets.ViewSet):
    pagination_class = None
    serializer_class= LogSerializers

    @action(detail=False)
    def get(self, request):
        infile = r"{}\app.log".format(conf_settings.STATIC_ROOT)
        data_searched = []
        with open(infile) as f:
            f = f.readlines()
            for line in f:
                result = json.loads(line)
                if 'INFO' in line:
                    json_data = result['INFO']
                    for data in json_data:
                        search_data = result['INFO'][data]["request"]["data"]
                        if search_data != {}:
                            data_searched.append(search_data['search'])
        queryset= Counter(data_searched)
        list_query = {"search": []}
        for k, v in sorted(queryset.items(), key=lambda pair: pair[1], reverse=True):
            list_query["search"].append({"term": k, "count": v})
        return Response(list_query)

