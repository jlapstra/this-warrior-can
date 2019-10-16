from django.urls import path
from . import views

urlpatterns = [
        path('api/dashboard/<int:pk>/', views.UserView.as_view()),
]
