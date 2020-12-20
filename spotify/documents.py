from elasticsearch_dsl import analyzer

from django_elasticsearch_dsl import Document, Index, fields

from spotify import models as spotify_models

spotify_index = Index('spotify')
spotify_index.settings(
    number_of_shards=5,
    number_of_replicas=2,
)

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["standard", "lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

@spotify_index.doc_type
class SpotifyDocument(Document):
    """Spotify elasticsearch document"""
    acousticness = fields.FloatField()
    artists = fields.KeywordField(
        multi=True,
        analyzer=html_strip,
        fields={
            'raw': fields.KeywordField(analyzer='keyword'),
        }
    )
    danceability = fields.FloatField()
    duration_ms = fields.IntegerField()
    energy = fields.FloatField()
    explicit = fields.IntegerField()
    id = fields.KeywordField(
        analyzer=html_strip,
        fields={
            'raw': fields.KeywordField(analyzer='keyword'),
        }
    )
    instrumentalness = fields.FloatField()
    key = fields.IntegerField()
    liveness = fields.FloatField()
    loudness = fields.FloatField()
    mode = fields.IntegerField()
    name = fields.KeywordField(
        analyzer=html_strip,
        fields={
            'raw': fields.KeywordField(analyzer='keyword'),
            'suggest': fields.CompletionField(),
        }
    )
    popularity = fields.IntegerField()
    release_date = fields.DateField()
    speechiness = fields.FloatField()
    tempo = fields.FloatField()
    valence = fields.FloatField()
    year = fields.KeywordField(
        analyzer=html_strip,
        fields={
            'raw': fields.KeywordField(analyzer='keyword'),
        }
    )

    class Django:
        model = spotify_models.Spotify