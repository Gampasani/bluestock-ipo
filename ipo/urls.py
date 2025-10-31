from django.urls import path
from .views import IPOListAPIView, IPODetailAPIView

urlpatterns = [
    path('ipo/', IPOListAPIView.as_view(), name='ipo-list'),
    path('ipo/<int:pk>/', IPODetailAPIView.as_view(), name='ipo-detail'),
]
