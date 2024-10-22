from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import *
from .serializers import *
# Create your views here.

class UserProfilesViewSet(viewsets.ModelViewSet):
    queryset=UserProfiles.objects.all()
    serializer_class=UserProfilesSerializers

    def get_queryset(self):
        """
        Optionally filter queryset based on request user.
        """
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Automatically set the user of the profile to the requesting user.
        """
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['post'])
    def get_user_info(self, request):
        """
        Retrieve the information of the user using the provided token.
        """
        token_key = request.data.get('token')

        if not token_key:
            return Response({"error": "Token is required"}, status=400)

        try:
            token = Token.objects.get(key=token_key)
            user = token.user
        except Token.DoesNotExist:
            return Response({"error": "Invalid token"}, status=401)

        try:
            user_profile = UserProfiles.objects.get(user=user)
            serializer = UserProfilesSerializers(user_profile)
        except UserProfiles.DoesNotExist:
            return Response({"error": "User profile not found"}, status=404)

        return Response(serializer.data)




class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializers

class SalleViewSet(viewsets.ModelViewSet):
    queryset = Salle.objects.all()
    serializer_class = SalleSerializers

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializers

class ProjectionViewSet(viewsets.ModelViewSet):
    queryset = Projection.objects.all()
    serializer_class = ProjectionSerializers
 