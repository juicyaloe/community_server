#backend/post/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('all/', views.WritingAll.as_view()),
    path('airplane/', views.WritingAIRPLANE.as_view()),
    path('car/', views.WritingCAR.as_view()),
    path('<int:pk>/', views.WritingDetail.as_view()),
]