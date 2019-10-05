from django.shortcuts import render
from this_warrior_can.models import User
from this_warrior_can.serializers import UserSerializer
from rest_framework import generics


class UserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
