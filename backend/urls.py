from django.urls import path, include
from . import views

urlpatterns = [
    path('api/wiki/', views.WikiListView.as_view()),
]