from django.shortcuts import render
from this_warrior_can.models import User, TimeSober
from this_warrior_can.serializers import UserSerializer, TimeSoberSerializer
from rest_framework import generics
from rest_framework.response import Response


class UserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        queryset = User.objects.get(pk=request.user.id)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)


class TimeSoberEndpoint(generics.RetrieveAPIView):
    queryset = TimeSober.objects.all()
    serializer_class = TimeSoberSerializer

    def get(self, request):
        queryset = TimeSober.objects.get(user_id=request.user.id)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
