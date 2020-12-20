from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
)
from django_elasticsearch_dsl_drf.constants import SUGGESTER_COMPLETION
from django_elasticsearch_dsl_drf.pagination import LimitOffsetPagination
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
    SuggesterFilterBackend
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from spotify import documents as spotify_documents
from spotify import serializers as spotify_serializers
import logging



class SpotifyViewSet(DocumentViewSet):
    logger = logging.getLogger(__name__)
    document = spotify_documents.SpotifyDocument
    serializer_class = spotify_serializers.SpotifyDocumentSerializer
    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
        SuggesterFilterBackend,
    ]

    # Define search fields
    search_fields = (
        'name',
        'release_date',
        'artists'
    )
    suggester_fields = {
        'name_suggest': {
            'field': 'name.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
            'options': {
                'size': 20,  # Override default number of suggestions
                'skip_duplicates': True,  # Whether duplicate suggestions should be filtered out.
            },
        }
    }

    # Filter fields
    filter_fields = {
        'acousticness':'acousticness',
        'artists':'artists' ,
        'danceability': 'danceability',
        'duration_ms':'duration_ms',
        'energy':'energy',
        'explicit': 'explicit',
        'id': 'id.raw',
        'instrumentalness': 'instrumentalness',
        'key': 'key',
        'liveness': 'liveness',
        'loudness': 'loudness',
        'mode': 'mode',
        'name': 'name',
        'popularity': 'popularity',
        'release_date':'release_date',
        'speechiness':'speechiness',
        'tempo': 'tempo',
        'valence': 'valence',
        'year' :'year',
    }

    # Define ordering fields
    ordering_fields = {
        'year': 'year.raw'
    }
    pagination_class = LimitOffsetPagination
    # Specify default ordering

    logger.info('Query{}'.format(DocumentViewSet.get_queryset))

