from django.shortcuts import render
import json
from collections import Counter
from rest_framework import viewsets
from .serializers import LogSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search, Q, A
from django.conf import settings as conf_settings

# Create your views here.
class LogViewSet(viewsets.ViewSet):
    pagination_class = None
    serializer_class= LogSerializers

    @action(detail=False)
    def get(self, request):
        # Define a default Elasticsearch client
        # client = connections.create_connection(hosts=['http://localhost:9200'])
        client = connections.create_connection(hosts=[conf_settings.ELASTICSEARCH_HOST])
        s = Search(using=client, index="log-app")
        a = A('terms', field='message.request.data.search.keyword')
        s.aggs.bucket('search', a)
        t=s.execute()
        aggr_dict={}
        for item in t.aggregations.search:
            item.key=item.key.split(":")[-1]
        for item in t.aggregations.search:
            if item.key in aggr_dict.keys():
                aggr_dict[item.key] += item.doc_count
            else:
                aggr_dict[item.key]=item.doc_count
        list_query = {"search": []}
        for k, v in sorted(aggr_dict.items(), key=lambda pair: pair[1], reverse=True):
            list_query["search"].append({"term": k, "count": v})
        return Response(list_query)

        #WITHOUT ES

        # infile = r"{}\logs\app.log".format(conf_settings.STATIC_ROOT)
        # data_searched = []
        # with open(infile) as f:
        #     f = f.readlines()
        #     for line in f:
        #         result = json.loads(line)
        #         if 'INFO' in line:
        #             json_data = result['INFO']
        #             for data in json_data:
        #                 search_data = result['INFO'][data]["request"]["data"]
        #                 if search_data != {}:
        #                     data_searched.append(search_data['search'])
        # queryset= Counter(data_searched)
        # list_query = {"search": []}
        # for k, v in sorted(queryset.items(), key=lambda pair: pair[1], reverse=True):
        #     list_query["search"].append({"term": k, "count": v})
        # return Response(list_query)

