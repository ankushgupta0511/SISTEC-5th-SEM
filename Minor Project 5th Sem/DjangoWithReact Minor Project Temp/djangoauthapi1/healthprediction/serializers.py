from rest_framework import serializers
from healthprediction.models import Symtoms


class DiseasePredictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symtoms
        fields=['id','symtoms_name']
        