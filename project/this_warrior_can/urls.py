from django.urls import path
from . import views

urlpatterns = [
        path('api/dashboard/', views.UserView.as_view()),
        path('api/timesober/', views.TimeSoberEndpoint.as_view()),
]
