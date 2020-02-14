from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.parsers import FormParser
from django.contrib import messages
from django.db import IntegrityError

from this_warrior_can.models import User
from this_warrior_can.serializers import UserSerializerSerializer

@login_required(login_url='/account/login/')
def index(request):
    return render(request, 'frontend/index.html')


def create_user(request):
    if request.method == 'GET':
        serializer = UserSerializerSerializer()

        return render(request, 'registration/create_user.html',{'serializer': serializer})

    elif request.method == 'POST':
        data = FormParser().parse(request)
        serializer = UserSerializerSerializer(data=data)
        if serializer.is_valid():
            try:
                serializer.save()
                messages.success(request, 'User created successfully, please log in')
                return redirect('/account/login/')
            except IntegrityError as e:
                return render(request, 'registration/create_user.html', {'serializer': serializer, 'error': ['Username already taken. Please try again']})
        else:
            return render(request, 'registration/create_user.html',{'serializer': serializer, 'error': serializer.errors})



