from django.urls import path, include
from .views import Portfolio, send_message

urlpatterns = [
    path('', Portfolio.as_view(), name='index'),
    path('send-message/', send_message, name="send_message"),

]
