from django.urls import path
from . import views

urlpatterns = [
        path('api/dashboard/', views.UserViewEndpoint.as_view()),
        path('api/timesober/', views.TimeSoberEndpoint.as_view()),
        path('api/createuser/', views.CreateUserEndpoint.as_view()),
]
