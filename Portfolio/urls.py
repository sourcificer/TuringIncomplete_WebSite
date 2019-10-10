from django.urls import path, include
from .views import (
    Portfolio, CartView,
    SendMessageAjaxView,

)

urlpatterns = [
    path('', Portfolio.as_view(), name='index'),
    path('view-cart/', CartView.as_view(), name="cart_view"),
    path('send-message/',  SendMessageAjaxView.as_view(), name="send_message"),

]
