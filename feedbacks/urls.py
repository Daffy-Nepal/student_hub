from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedbacks, name='feedback'),
    path('create/', views.create_feedback, name='create_feedback'),
    path('delete/', views.delete_feedback, name='delete_feedback'),
    path('update/', views.update_feedback, name='update_feedback'),
]
