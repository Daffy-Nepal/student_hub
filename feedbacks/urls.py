from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedbacks, name='feedback'),
    path('create/', views.create_feedback, name='create_feedback'),
]
