from django.urls import path
from .views import payment_method_view,payment_method_createview

app_name = 'billing'

urlpatterns = [
    path('payment-method/',payment_method_view, name='billing-payment-method'),
    path('payment-method/create/',payment_method_createview, name='billing-payment-method-endpoint')
]
