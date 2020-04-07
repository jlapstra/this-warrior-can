from django.shortcuts import render
from this_warrior_can.models import User, TimeSober
from this_warrior_can.serializers import UserSerializer, UserSerializerSerializer, TimeSoberSerializer
from rest_framework import generics, status
from rest_framework.response import Response


class UserViewEndpoint(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        queryset = User.objects.get(pk=request.user.id)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)


class TimeSoberEndpoint(generics.ListCreateAPIView):
    queryset = TimeSober.objects.all()
    serializer_class = TimeSoberSerializer

    def get_serializer_context(self):
        return {'request': self.request}

    def get(self, request):
        try:
            queryset = TimeSober.objects.filter(user_id=request.user.id)
        except TimeSober.DoesNotExist:
            return Response({})
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateUserEndpoint(generics.CreateAPIView):
    serializer_class = UserSerializerSerializer
