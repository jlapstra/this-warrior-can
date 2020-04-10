from django.shortcuts import render
from this_warrior_can.models import User, TimeSober
from this_warrior_can.serializers import UserSerializer, UserSerializerSerializer, TimeSoberSerializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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


class DeleteTimeSoberEndpoint(generics.DestroyAPIView):
    serializer_class = TimeSoberSerializer

    def get_object(self, pk):
        queryset = TimeSober.objects.filter(
                        id=pk,
                        user=self.request.user.id
                    )
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object(self.kwargs['pk'])
        if instance:
            instance.delete()
            return Response(status=status.HTTP_200_OK)
        return Response("Could not find habit to delete", status=status.HTTP_404_NOT_FOUND)



class CreateUserEndpoint(generics.CreateAPIView):
    serializer_class = UserSerializerSerializer
