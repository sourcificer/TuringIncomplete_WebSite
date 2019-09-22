from django.urls import path,include
from .views import Portfolio

urlpatterns = [
    path('',Portfolio.as_view(),name='home_page'),
]