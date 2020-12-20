
from rest_framework import serializers


class LogSerializers(serializers.BaseSerializer):
    def to_representation(self, obj):
        return obj