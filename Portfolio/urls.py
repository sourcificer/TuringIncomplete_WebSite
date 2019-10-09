from django.urls import path, include
from .views import Portfolio,  SendMessageAjaxView

urlpatterns = [
    path('', Portfolio.as_view(), name='index'),
    path('send-message/',  SendMessageAjaxView.as_view(), name="send_message"),

]
