from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('detail/<int:pk>/', Detail.as_view(), name='detail'),
    path('review/<int:pk>', add_review, name='review'),
    path('subscriber/<int:pk>', add_subscriber, name='add_subscriber')
]