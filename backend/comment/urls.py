from django.urls import path

from . import views

urlpatterns = [
    path('all/', views.CommentAll.as_view()),
    path('<int:pk>/', views.CommentDetail.as_view()),
]