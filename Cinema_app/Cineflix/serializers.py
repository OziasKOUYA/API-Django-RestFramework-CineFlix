from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

class UserProfilesSerializers(serializers.ModelSerializer):
    class Meta:
        model=UserProfiles
        fields='__all__'
class TicketSerializers(serializers.ModelSerializer):
    class Meta:
        model=Ticket
        fields='__all__'

class SalleSerializers(serializers.ModelSerializer):
    class Meta:
        model=Salle
        fields='__all__'

class FilmSerializers(serializers.ModelSerializer):
    class Meta:
        model=Film
        fields='__all__'

    def get_affiche(self, obj):
        request = self.context.get('request')
        if obj.affiche and hasattr(obj.affiche, 'url'):
            return request.build_absolute_uri(obj.affiche.url)
        return None

class ProjectionSerializers(serializers.ModelSerializer):
    class Meta:
        model=Projection
        fields='__all__'


