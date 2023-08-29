from rest_framework import serializers
from users.models import User
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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name',  'email', 'phone']

class MemberlistSerializer(serializers.ModelSerializer):
    Party = PartySerializer(many=True, read_only=True)
    userID = UserSerializer()
    party = PartySerializer()

    class Meta:
        model = Member
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    Party = PartySerializer(many=True, read_only=True)
    party = PartySerializer()

    class Meta:
        model = Member
        fields = '__all__'