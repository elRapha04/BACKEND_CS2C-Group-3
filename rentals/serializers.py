from rest_framework import serializers
from .models import BoardingHouse

class BoardingHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardingHouse
        fields = '__all__'
