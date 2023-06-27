from rest_framework import serializers
from .models import Party, Member

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    Party = PartySerializer(many=True, read_only=True)

    class Meta:
        model = Member
        fields = '__all__'