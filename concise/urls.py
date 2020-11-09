from django.urls import path
from .views import *

urlpatterns = [
    path('stripped-URL/', StripURLCreateAPIView.as_view(), name='api-post-list'),
    path('stripped-URL/<int:pk>/', StripURLDetailsAPIView.as_view(), name='api-post-details'),
]