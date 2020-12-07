from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from spotify import documents as spotify_documents


class SpotifyDocumentSerializer(DocumentSerializer):
    class Meta:
        document = spotify_documents.SpotifyDocument
        fields = (
            'acousticness',
            'artists',
            'danceability',
            'duration_ms',
            'energy',
            'explicit',
            'id',
            'instrumentalness',
            'key',
            'liveness',
            'loudness',
            'mode',
            'name',
            'popularity',
            'release_date',
            'speechiness',
            'tempo',
            'valence',
            'year'
        )