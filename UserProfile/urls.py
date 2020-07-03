from django.urls import path
from .views import *

urlpatterns = [
    path('activity/',activity.as_view(),name='activity')
]